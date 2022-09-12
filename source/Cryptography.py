def numberify(letter):
    integer = ord(letter)

    if 65 <= integer <= 90:
        integer -= 65

    if 97 <= integer <= 122:
        integer -= 97

    return integer

def letterify(integer):
    integer += 97

    letter = chr(integer)

    return letter


class Caesar():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify((numberify(char) + key) % 26)

        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify((numberify(char) - key) % 26)

        return plaintext

class Atbash():
    def __init__(self):
        pass

    def encrypt(plaintext):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify(25-numberify(char))

        return ciphertext

    def decrypt(ciphertext):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify(25-numberify(char))

        return plaintext

class Rot13():
    def __init__(self):
        pass

    def encrypt(plaintext):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify((numberify(char) + 13) % 26)

        return ciphertext

    def decrypt(ciphertext):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify((numberify(char) + 13) % 26)

        return plaintext

class Vigenere():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + numberify(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) - numberify(key[i % len(key)])) % 26)
        
        return plaintext

class Trithemius():
    def __init__(self):
        pass

    def encrypt(plaintext):
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + i % 26) % 26)
        
        return ciphertext

    def decrypt(ciphertext):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) - i % 26) % 26)
        
        return plaintext

class VariantBeaufort():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) - numberify(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) + numberify(key[i % len(key)])) % 26)
        
        return plaintext

class Beaufort():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify(25 - ((numberify(char) + numberify(key[i % len(key)])) % 26))
        
        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify(25 - ((numberify(char) - numberify(key[i % len(key)])) % 26))
        
        return plaintext

class Gronsfeld():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        key = str(key)
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + int(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(ciphertext, key):
        key = str(key)
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) - int(key[i % len(key)])) % 26)
        
        return plaintext

class Autokey():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        key = key + plaintext
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + numberify(key[i])) % 26)
        
        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plain_letter = letterify((numberify(char) - numberify(key[i])) % 26)
            plaintext += plain_letter
            key += plain_letter
        
        return plaintext

class RunningKey():
    def __init__(self):
        pass

    def encrypt(plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + numberify(key[i])) % 26)
        
        return ciphertext

    def decrypt(ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) - numberify(key[i])) % 26)
        
        return plaintext
