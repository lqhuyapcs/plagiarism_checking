def LevenshteinTextSimilarity(sentence1, sentence2):
    distances = seqratio(sentence1, sentence2)
    if distances > 0.8:
        return True
    return False