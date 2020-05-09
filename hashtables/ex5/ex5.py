def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for i in queries:
        cache[i] = []

    for file in files:
        # TODO: split the path at the last forward slash
        path = file.split('/')[-1]
        # TODO: if the path is already present in the cache from queries, append them to the end of the result array
        if path in cache:
            result.append(file)
        else:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
