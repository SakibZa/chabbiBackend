def get_file_type(extension_type_list, filenames):
    extension_type_pairs = extension_type_list.split(";")
    extension_type_dict = {}
    
    for pair in extension_type_pairs:
        extension, file_type = pair.split(",")
        extension_type_dict[extension] = file_type
    
    result_dict = {}
    for filename in filenames:
        file_extension = filename.split(".")[-1]
        file_type = extension_type_dict.get(file_extension, "unknown")
        result_dict[filename] = file_type
    
    return result_dict


extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_type(extension_type_list, filenames)
print(result)

