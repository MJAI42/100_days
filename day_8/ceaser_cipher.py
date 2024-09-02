from encode import encode_text, decode_text 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
     encoded_text = encode_text(text, shift)
elif direction == "decode":
     encoded_text = decode_text(text, shift)
"""
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
"""
"""
if direction == "decode":
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
                alpha_shift = (position - shift - 1) % len(alphabet)
                print(position)
                encoded_text += alphabet[alpha_shift]
""""

print(f"Your encoded text is: {encoded_text}")