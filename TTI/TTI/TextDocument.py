import requests
import spacy
from collections import Counter
from .doc2vec import encode_article


BASE_URL = "https://en.wikipedia.org/w/api.php"


def clean_document(document):
    words = document.split()

    character_blocklist = ["}", "{", "^", "*", "\\", "(", ")", "|", "=", "\""]

    cleaned_words = []
    for word in words:
        if len(word) > 1 and not any(ext in word for ext in character_blocklist):
            cleaned_words.append(word)

    return " ".join(cleaned_words)


def get_article_content(title):
    response = requests.get(
        url=BASE_URL,
        params={
            "action": "query",
            "titles": title,
            "prop": "extracts",  # get only the article content
            "format": "json",
            "explaintext": ""  # no html tags
        }
    )
    if not (response.status_code < 400):
        raise "Couldn't download article"

    json = response.json()
    content = list(json["query"]["pages"].values())[0]["extract"]
    return clean_document(content)


def get_document_representation(document, words_count=50):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(document)

    # Extract nouns
    words = [token.lemma_ for token in doc if token.pos_ == "NOUN"]

    counter = Counter(words)
    most_common_words = [w[0] for w in counter.most_common(words_count)]

    word_representation = most_common_words

    article_description = " ".join(most_common_words)
    vector_representation = encode_article(article_description)

    return {"vector": vector_representation, "words": word_representation}
