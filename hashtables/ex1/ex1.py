def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """

    weight_dict = {}
    # do a for loop through range equal to length
    # do a weight_dict.get call for limit subtracted by weights list item at the specified indice
    # if number exists in dict then return i and get_dict
    # if not then add weights item by the indice as the key and the indice as the value
    for i in range(length):
        get_dict = weight_dict.get(limit - weights[i])
        if get_dict is None:
            weight_dict[weights[i]] = i
        else:
            return (i, get_dict)
