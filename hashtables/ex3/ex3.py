def intersection(arrays):
    """
    YOUR CODE HERE
    """
    integers = {}
    result = []

    for i, nums in enumerate(arrays):
        for j in nums:
            # TODO: if the there is already a number pesent in the dict we want to increase the count by  1
            if integers.get(j) is not None:
                integers[j] = integers[j] + 1
            # TODO: if that number is not present in the dict, we want to set the initial count to 1
            elif integers.get(j) is None:
                integers[j] = 1
            else:
                continue

    for i in integers:
        # TODO: if the number count is equal to the array length, append it to the result
        if integers[i] == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
