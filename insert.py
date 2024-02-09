

def insert(array,where_to_insert,*what_to_insert):
    place_holder_array = [None]*(len(what_to_insert)+len(array))
    sliced_array = array[where_to_insert:len(array)]
    not_moved_number_count = 0

    for index in range(where_to_insert,len(what_to_insert)+where_to_insert):
        place_holder_array[index] = what_to_insert[where_to_insert-index]

    for index in range(0,where_to_insert):
        place_holder_array[index] = array[index]
        not_moved_number_count += 1

    for index in range(1,not_moved_number_count+len(sliced_array)-where_to_insert+1):
        place_holder_array[-(index)] = sliced_array[-(index)]
        

    print(place_holder_array)



insert([2,2,3,4,5,5,1],7,[1,2,3],[1,2,4])