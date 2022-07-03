PASSWORD = '12345'

def password(func):
    def wraper():
        passw = input('What is your password?')
        if passw == PASSWORD:
            return func()
            print('Incorrect Password')
    return wraper

@password
def need_password():
    print("Tu contraseña es correcta")

if __name__ == '__main__':
    need_password()