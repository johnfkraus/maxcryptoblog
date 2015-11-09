# page 13,  https://media.readthedocs.org/pdf/cryptography/latest/cryptography.pdf

import base64
#  import os ## required to generate salt
import sys
import inspect
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# password = b'password'
# print('password = ', password, 'password.__class__ = ', password.__class__)
db = False  # debugging? > verbose output

"""In this scheme, the salt has to be stored in a
retrievable location in order to derive the same key
from the password in the future."""
# salt = os.urandom(16)
salt = b'AJ\xf6\x12\x970B\x82\x15\xd6\xea\x01\x81k0S'


def lineno():
    """ Returns the current line number in the program.
    Danny Yoo (dyoo@hkn.eecs.berkeley.edu).
    Requires import inspect.
    """
    return inspect.currentframe().f_back.f_lineno


def encrypt(password, plaintext):
    if db:
        print(lineno(), 'salt =', salt, 'type(salt) =', type(salt), 'len(salt) =', len(salt))
    salt_list = list(salt)
    if db:
        print(lineno(), 'salt_list =', salt_list, 'len(salt_list) =', len(salt_list))

    """Key derivation function.
    The iteration count used should be adjusted to be as
    high as your server can tolerate. A good default is
    at least 100,000 iterations which is what Django
    recommends in 2014."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )

    # convert password to bytes
    bytestring_password = bytes(password, 'utf-8')
    # convert plaintext to bytes
    plaintext_bytes = bytes(plaintext, 'utf-8')
    key = base64.urlsafe_b64encode(kdf.derive(bytestring_password))
    f = Fernet(key)
    token = f.encrypt(plaintext_bytes)
    if db:
        print(lineno(), 'token = ', token)
    if db:
        print(lineno(), 'f.decrypt(token)=', f.decrypt(token))
    return token  # ciphertext


def decrypt(password, ciphertext):
    if db:
        print(lineno(), 'salt =', salt, 'type(salt) =', type(salt), 'len(salt) =', len(salt))
    salt_list = list(salt)
    if db:
        print(lineno(), 'salt_list =', salt_list, 'len(salt_list) =', len(salt_list))

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )

    # convert password to bytes
    bytestring_password = bytes(password, 'utf-8')
    key = base64.urlsafe_b64encode(kdf.derive(bytestring_password))
    f = Fernet(key)
    plaintext = ''
    # try:
    if type(ciphertext) != 'bytes':
        ciphertext = bytes(ciphertext, 'utf-8')
    print(ciphertext.__class__)
    plaintext_bytes = f.decrypt(ciphertext)
    plaintext = plaintext_bytes.decode('utf-8')
    # except:
    # print(ciphertext.__class__)

    if db:
        print(lineno(), 'plaintext =', plaintext)
    return plaintext


def main():
    """ Define a main() function that parses parameters and runs a test."""
    args = sys.argv[1:]
    if db:
        print(lineno(), 'args =', args)
    args = sys.argv[1:]
    if not args or len(args) > 2 or (len(args) == 1 and args[0] != '--test'):
        print('usage: [--test | password plaintext]')
        sys.exit(1)
    if args[0] == '--test':
        print('testing!')
        password = 'swordfish'
        plaintext = 'Triple secret message!'
    else:
        password = sys.argv[1]
        plaintext = sys.argv[2]

    print(lineno(), 'password =', password, 'plaintext =', plaintext)
    ciphertext = encrypt(password, plaintext)
    print(lineno(), 'ciphertext =', ciphertext)
    plaintext = decrypt(password, ciphertext)
    print(lineno(), 'recovered plaintext =', plaintext)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
