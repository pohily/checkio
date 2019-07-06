def from_camel_case(name):
    result = name[0].lower()
    name = name[1:]
    for letter in name:
        if letter.isupper():
            result += '_' + letter.lower()
        else:
            result += letter
    return result
print(from_camel_case("MyFunctionName"))    


"""


    """


