#raw code for reference 
import string

lower_case = list(string.ascii_lowercase) #creates a list of all lowercase letters from a to z 
upper_case = list(string.ascii_uppercase) #creates a list of all upperrcase letters from A to Z

def encryption(plain_text, shift_key): 
    cipher_text = "" #initializes empty string to store encrypted string
    for char in plain_text:
        if char in lower_case:
            position = lower_case.index(char) #finds the index position of char in lowercase list 
            new_position = (position + shift_key) % 26 #modulo ensures that the index wrap around if it goes past the end of the alphabet.
            cipher_text += lower_case[new_position]
        elif char in upper_case:
            position = upper_case.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += upper_case[new_position]
        else:
            cipher_text += char  # Keep non-alphabet characters unchanged
    print(f"Here is the text after encryption: {cipher_text}\n")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in lower_case:
            position = lower_case.index(char)
            new_position = (position - shift_key) % 26
            plain_text += lower_case[new_position]
        elif char in upper_case:
            position = upper_case.index(char)
            new_position = (position - shift_key) % 26
            plain_text += upper_case[new_position]
        else:
            plain_text += char  # Keep non-alphabet characters unchanged
    print(f"Here is the text after decryption: {plain_text}\n")

end = False
while not end:
    what = input("Type 'encrypt' for encryption, \nType 'decrypt' for decryption:\n").lower()  #lower() -> converts the input to lowercase to make the comparison case-insensitive. 
    text = input("Type your message:\n")
    shift = int(input("Enter shift key: \n"))
    if what == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    else:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")
    play_again = input("Type 'yes' to continue, \ntype 'no' to exit \n").lower()
    if play_again == 'no':
        end = True
        print("THE END...")
