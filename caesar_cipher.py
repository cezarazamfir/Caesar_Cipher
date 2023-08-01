import string


def encrypt(message, key):
    alphabets = [string.ascii_lowercase, string.ascii_uppercase]
    final_alphabet=''.join(alphabets)
    
    final_shifted_alphabet = ''
    for alphabet in alphabets:
        final_shifted_alphabet= final_shifted_alphabet + alphabet[key:] + alphabet[:key]


    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    print(message.translate(table))



def decrypt(message, key):
    alphabets = [string.ascii_lowercase, string.ascii_uppercase]
    final_shifted_alphabet=''.join(alphabets)
    
    final_alphabet = ''
    for alphabet in alphabets:
        final_alphabet= final_alphabet + alphabet[key:] + alphabet[:key]
    
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
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
