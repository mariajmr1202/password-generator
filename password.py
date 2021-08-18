import random

def password_generator():
    CAPITAL = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
    SYMBOLS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#',"'"]

    characters = CAPITAL + LOWER + NUMBERS + SYMBOLS
    new_password = []

    for i in range(15):
        random_char = random.choice(characters)
        new_password.append(random_char)
    
    new_password = ''.join(new_password) #convert list to string
    return new_password

def run():
    password = password_generator()
    print(f'Your new password is: {password}')

if __name__ == '__main__':
    run()