def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for i in range(length):
        # TODO: Check if the hash table already contains an entry for 'limit - weight' i.e  - the sum we're looking for
        sum = cache.get(limit - weights[i])
        # * if there is a value there, we've found the two items whose weights sum up to the limit and we need to return a tuple
        if sum is not None:
            return (i, sum)
        # * if there is not a value there, set the key as the current value and the value as the index
        else:
            cache[weights[i]] = i

    return None
