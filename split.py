
def split(string,tosplit):
    index = 0
    new_array = []
    start = 0
    if tosplit != '':
        for item in string:
            if item == tosplit:
                new_array.append([string[start:index]])
                start = index+1
            elif index==len(string)-1:
                new_array.append([string[start:len(string)]])
            index+=1
    else:
        for item in string:
            new_array.append([item])

    return new_array

