def find_common_keys(dict1, dict2):
    common_keys = []
    for key in dict1:
        if key in dict2:
            common_keys.append(key)
        
    return common_keys

dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = find_common_keys(dict1, dict2)

print(f"The common keys are : {common_keys}")