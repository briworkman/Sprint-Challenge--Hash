def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for i in a:
        # * initialize cache
        cache[i] = None
    # TODO: if the number is greater than 0, check if there is also the same number multiplied by -1 in the same dict. If there is, append the number to the end of the result array
    for i in a:
        if i > 0:
            if i * -1 in cache:
                result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
