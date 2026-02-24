def manhattan_distance(vector1: list, vector2: list):
    """
    Calculates the Manhattan distance between two vectors using standard Python.
    Args:
        vector1 (list): The first vector.
        vector2 (list): The second vector.
    Returns:
        int: The Manhattan distance between the two vectors.
    Raises:
        ValueError: If the vectors are not of the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length.")

    return sum(abs(a - b) for a, b in zip(vector1, vector2))
