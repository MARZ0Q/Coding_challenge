

def max(*arg):
    infinitely_flat_array = []
    def recursion(item1):
        for item1 in item1:
            if(type(item1)== type([])):
                recursion(item1)
            else:
                infinitely_flat_array.append(item1)
    recursion(arg)
    infinitely_flat_array.sort(reverse=True)
    return infinitely_flat_array[0]

