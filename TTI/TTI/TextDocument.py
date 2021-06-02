import requests

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


def extract_key_words(document):
    pass
