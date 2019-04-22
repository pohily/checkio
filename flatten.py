def flatten(dictionary):
    result = ''
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            if result:
                result += '/'
            result += key
            a = list(dictionary[key].keys())
            b = list(dictionary[key].values())
            dictionary[a[0]] = b[0]
            del dictionary[key]
        else:
            if result:
                result += '/'
            result += key
            print('res', result)
            print('key', key)
            dictionary[result] = dictionary[key]
            del dictionary[key]
            break
    return dictionary
print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))

"""

"""               



