while True:
    age = input('Enter you age: ')
    if age.isdigit():
        break
    print('Your age must be a number')

while True:
    password= input('Please Enter your password (letters and Numbers only): ')


    if  password.isalnum():
        break
    print('Password can have only numbers and letters')