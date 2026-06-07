def calculate_confidence(
    num_docs,
    top_k
):

    if num_docs >= top_k:
        return 95

    if num_docs >= 4:
        return 90

    if num_docs >= 3:
        return 85

    if num_docs >= 2:
        return 75

    return 60