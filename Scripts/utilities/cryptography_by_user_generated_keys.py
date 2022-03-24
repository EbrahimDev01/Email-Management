from Scripts.utilities import hash_sha512


def generate_key(got_key: str):
    """
    generate key based string

    :param got_key: string for generate key
    :return: key code for encrypt and decrypt data
    """
    got_key = hash_sha512.hash_sha512(got_key)
    key_code = ord(got_key[0])
    for character in got_key:
        key_code += ord(character)
    return int(key_code)


def encrypt(got_text, got_key):
    """
    encrypt text based self key generated

    :param got_text: string for encrypt
    :param got_key: key code for encrypting string
    :return: encrypted input string
    """
    encrypted = ''
    if isinstance(got_key, str):
        got_key = generate_key(got_key)
    for chars in got_text:
        encrypted += str(got_key * ord(chars)) + '.'
    return encrypted[:-1]


def decrypt(got_text, got_key):
    """
    decrypting text encrypted based self key code

    :param got_text: text encrypted
    :param got_key: key code generated for decrypting text
    :return: decrypted text
    """
    encrypted = ''
    if isinstance(got_key, str):
        got_key = generate_key(got_key)
    for chars in got_text.split('.'):
        encrypted += chr(int(chars) // got_key)
    return encrypted


if __name__ == '__main__':
    key = generate_key('Ebrahim')
    text = 'EbrahimDev01@gmail.com'

    enc_text = encrypt(text, key)
    dec_text = decrypt(enc_text, key)

    print('key:', key)
    print('encrypt text:', enc_text)
    print('decrypt text:', dec_text)
