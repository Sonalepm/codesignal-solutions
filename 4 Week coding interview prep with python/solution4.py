def replace_character(input_string, c1, c2):

    return ''.join(c2 if i == c1 else i for i in input_string)