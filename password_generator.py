import random

print ('Password Generator')

passwordChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890!@#$%^&*()+' # All the characters that can be used in the passwords

numberOfPasswords = int(input('\nHow many passwords would you like? ')) # How many passwords the user wants

lengthOfPasswords = int(input('\nHow long do the passwords need to be? ')) # How long the passwords need to be

print ('\nYour passwords are:')

for pwds in range(numberOfPasswords):
    passwords = ''
    for i in range(lengthOfPasswords):
        passwords += random.choice(passwordChars)
    print (passwords)

    # Created by @ckitchens1997