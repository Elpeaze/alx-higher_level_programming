def best_score(a_dictionary):

    max_value = -1

    max_key = None

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

