import itertools

def try_passwords(password):
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for password_length in range(1, 9): # try password lengths from 1 to 8
        for guess in itertools.product(charset, repeat=password_length):
            guess = ''.join(guess)
            if guess == password:
                return guess
    return None

# usage
password = 'abc'
print('Password found:', try_passwords(password))
