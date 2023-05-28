def get_sublist(list_input, start_index, end_index):
    sublist = list_input[start_index:end_index+1:2]
    return sublist


list_input = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

sublist = get_sublist(list_input, start_index, end_index)
print(sublist)
