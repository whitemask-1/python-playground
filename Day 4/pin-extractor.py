#Pin Extractor project from freeCodeCamp to help build understanding and muscle memory

def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')

        for line_index, line in enumerate(lines):
            words = line.split(' ')
            if line_index < len(words): #Handle edge case for when the line index num is greater than the num of words in the line
                secret_code += (str(len(words[line_index])))
            else:
                secret_code += '0' #If line index num is greater then the line value will evaluate to 0 to ensure every line gets a value

        secret_codes.append(secret_code)
    return secret_codes
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))