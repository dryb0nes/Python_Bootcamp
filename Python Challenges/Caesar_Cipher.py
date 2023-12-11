alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def caesar_cipher(text, shift, direction):
    if direction == "decode":
        shift = -shift
    return ''.join([alphabet[(alphabet.index(letter) + shift) % len(alphabet)] for letter in text])

print(caesar_cipher(text, shift, direction))






# def decrypt(text, shift):
#     decrypted_text = [alphabet[((alphabet.index(letter) - shift) + len(alphabet)) % len(alphabet)] for letter in text]
#     # for letter in text:
#     #     text_indexs = alphabet.index(letter) - shift
#     #     decoded_indexs = (text_indexs + len(alphabet)) % len(alphabet)
#     #     decrypted_letter = alphabet[decoded_indexs]
#     #     decrypted_text.append(decrypted_letter)
#     print(''.join(decrypted_text))