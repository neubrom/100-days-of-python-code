#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_f, shift_f):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' 
    # forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    text_encrypt = ""
    for i in text_f:
        if ord(i) + shift_f > 122:
            text_encrypt += chr((ord(i) + shift_f) - 122  + ord("a"))
        else:
            text_encrypt += chr(ord(i) + shift_f)
    print(text_encrypt)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able 
# to test the code and encrypt a message.

def decrypt(text_f, shift_f):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' 
    # forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    
    text_decrypt = ""
    for i in text_f:
        if ord(i) - shift_f < ord("a"):
            text_decrypt += chr((ord(i) - shift_f) + 122)
        else:
            text_decrypt += chr(ord(i) - shift_f)
    print(text_decrypt)

if direction == "encode":
    encrypt(text_f=text, shift_f=shift)
elif direction == 'decode':
    decrypt(text_f=text, shift_f=shift)
