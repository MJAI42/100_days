from encode_decode import encode_text, decode_text 
from ascii_caeser_cipher import caeser, cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caeser)
print(cipher)
repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encoded_text = encode_text(text, shift)
    elif direction == "decode":
        encoded_text = decode_text(text, shift)
    print(f"Your encoded text is: {encoded_text}")

    repeat = input("Would you like to encode or decode another message?")