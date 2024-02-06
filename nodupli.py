
def nodupli(array):
    new_array = []
    for item in array:
        if(not item in new_array):
            new_array.append(item)
    return new_array

# It even works with string!!!