
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text, shift_amount, cipher_direction):
    text_crypt = ""
    if cipher_direction == "encode":
        for i in start_text:
            if ord(i) + shift_amount > 122:
                text_crypt += chr((ord(i) + shift_amount) - 122  + ord("a"))
            else:
                text_crypt += chr(ord(i) + shift_amount)
    elif cipher_direction == "decode":
        for i in start_text:
                if ord(i) - shift_amount < ord("a"):
                    text_crypt += chr((ord(i) - shift_amount) + 122)
                else:
                    text_crypt += chr(ord(i) - shift_amount)
    else:
        print("wrong input")
    print(text_crypt)

ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)

