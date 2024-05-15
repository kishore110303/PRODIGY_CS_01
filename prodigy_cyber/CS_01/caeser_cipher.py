alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5

def encrypt(text, shift):

  
  encrypt_text = ""

  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      encrypt_text += alphabet[(index + shift) % 26]
    else:
      encrypt_text += char

  print(encrypt_text)
      
def decrypt(text, shift):
  
  decrypt_text = ""

  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      decrypt_text += alphabet[(index - shift) % 26]
    else:
      decrypt_text += char
  
  print(decrypt_text)  

if direction == "encode":
  encrypt(text, shift)

elif direction == "decode":
  decrypt(text, shift)

else:
  print("Invalid input, please enter encode to decrypt or decode to decrypt.")
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.