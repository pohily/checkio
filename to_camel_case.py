def to_camel_case(name):
    return ''.join([word[0].upper() + word[1:] for word in name.split('_')])
        

print(to_camel_case('my_function_name'))
"""

"""               



