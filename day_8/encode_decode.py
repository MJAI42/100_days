alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_text (text, shift):   
    encoded_text = ""
    for char in text:
        #check if it is a letter
        count = 0
        position = 0
        is_letter = False
        while count < len(alphabet):
            if char == alphabet[count]:
                is_letter = True
                count += 1
                position = count
            else:
                count += 1
        #if it is not a letter add it directly
        if is_letter == False:
            encoded_text += char
        #if it is a letter do the shift
        elif is_letter == True:
            alpha_shift = (position + shift - 1) % len(alphabet)
            print(position)
            encoded_text += alphabet[alpha_shift]
    return (encoded_text)

def decode_text (text, shift):   
    decoded_text = ""
    for char in text:
        #check if it is a letter
        count = 0
        position = 0
        is_letter = False
        while count < len(alphabet):
            if char == alphabet[count]:
                is_letter = True
                count += 1
                position = count
            else:
                count += 1
        #if it is not a letter add it directly
        if is_letter == False:
            decoded_text += char
        #if it is a letter do the shift
        elif is_letter == True:
            alpha_shift = (position - shift - 1) % len(alphabet)
            print(position)
            decoded_text += alphabet[alpha_shift]
    return (decoded_text)