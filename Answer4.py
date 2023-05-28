def switch_dict_keys_values(dictionary):
    return dict(zip(dictionary.values(), dictionary.keys()))


input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result = switch_dict_keys_values(input_dict)
print(result)
