import random
import string


# noinspection PyPep8Naming
def password(characters_no):
    lowercase = [random.choice(string.ascii_lowercase) for L in range(characters_no)]
    uppercase = [random.choice(string.ascii_uppercase) for U in range(characters_no)]
    numbers = [random.choice(string.digits) for number in range(characters_no)]
    symbols = ['_', '.']

    generatedPassword = ''.join(lowercase + uppercase + numbers + symbols)
    generatedPassword = ''.join(random.choice(generatedPassword) for i in range(characters_no))
    return generatedPassword


c = int(input('Please enter the password length you wish to generate '))
print(password(c))
