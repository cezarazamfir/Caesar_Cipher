import string


def encrypt(message, key):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]


    table = str.maketrans(alphabet,shifted_alphabet)
    print(message.translate(table))



def decrypt(message, key):
    shifted_alphabet = string.ascii_lowercase
    alphabet = shifted_alphabet[key:] + shifted_alphabet[:key]


    table = str.maketrans(alphabet, shifted_alphabet)
    print(message.translate(table))


print('This is a Caesar Cipher Program\n Would you like to encrypt or decrypt a message?')
print()
mode = input('e/d: ').lower()


while mode != 'e' and mode!='d':
    mode = input('Please select either e or d:')


if mode == 'e':
    print('\nYou have chosen the ENCRYPTION mode!')
    key = int(input('Please input the key:'))%26
    message = input('Please input the message you want to encrypt:\n')
    encrypt(message,key)
else: 
    print('\nYou have chosen the DECRYPTION mode!')
    key = int(input('Please input the key:'))%26
    message = input('Please input the message you want to decrypt:\n')
    decrypt(message,key)
