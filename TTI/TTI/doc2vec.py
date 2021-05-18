import gensim.models as gsm

doc2vec = gsm.Doc2Vec.load("../models/doc2vec.bin")


def encode_article(content):
    """ Encodes the content as a numeric vector """

    start_alpha = 0.01
    infer_epoch = 1000

    formatted_content = content.strip().split()
    vector_representation = doc2vec.infer_vector(
        formatted_content, alpha=start_alpha, steps=infer_epoch)

    return [float(i) for i in vector_representation]
