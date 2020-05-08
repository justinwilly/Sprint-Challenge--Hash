def intersection(arrays):

    """
    YOUR CODE HERE
    """
    inter_dict = {}
    result = []

    # first we break the array of arrays into seperate arrays
    # then go through each item in an array
    # if that item exists in the dict then add 1 to the value
    # if that item doesnt exist yet then add that item as a key with a 1 as the value
    # then go through the inter_dict and add any dict keys that have a value equal to the number of inner arrays to the result list
    # this represents that this particular item appears in all the arrays
    for a in arrays:
        for b in a:
            if inter_dict.get(b):
                inter_dict[b] += 1
            else:
                inter_dict[b] = 1
    for key, value in inter_dict.items():
        if value > len(arrays) - 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
