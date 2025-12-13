def levenshtein(word1: str, word2: str) -> int:
    """Calculate Levenshtein distance between two words."""
    matrix: list[list[int]] = [[] for _ in range(len(word1) + 1)]

    for num in range(len(word2) + 1):
        matrix[0].append(num)

    for num in range(1, len(word1) + 1):
        matrix[num].append(num)

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            levens = min(
                matrix[i - 1][j] + 1,  # deletion
                matrix[i][j - 1] + 1,  # insertion
                matrix[i - 1][j - 1] + cost,  # substitution
            )
            matrix[i].append(levens)

    return matrix[len(word1)][len(word2)]
