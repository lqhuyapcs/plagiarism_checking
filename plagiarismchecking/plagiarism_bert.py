from sentence_transformers import SentenceTransformer
from scipy import spatial


def BertTextSimilarity(sentence1, sentence2):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence1 = [sentence1]
    sentence2 = [sentence2]
    sentence1_embeddings = model.encode(sentence1)
    sentence2_embeddings = model.encode(sentence2)
    distances = spatial.distance.cosine(sentence1_embeddings[0], sentence2_embeddings[0])
    if 1 - distances > 0.6:
        return True
    return False