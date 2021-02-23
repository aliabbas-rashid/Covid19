from cryptography.fernet import Fernet

def checkpass(pwd):
    file = open("key.key", 'rb')
    key = file.read()
    file.close()

    file = open("passkey.key", 'rb')
    passkey = file.read()
    file.close()

    f = Fernet(key)
    decrypted = decrypted = f.decrypt(passkey)
    passwrd = decrypted.decode()

    return pwd == passwrd