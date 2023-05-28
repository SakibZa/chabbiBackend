def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x.get(sort_key))
    return sorted_list



list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sort_key = "fruit"
sorted_result = sort_list_of_dicts(list_of_dicts, sort_key)
print(sorted_result)
