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
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify((numberify(char) + key) % 26)

        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify((numberify(char) - key) % 26)

        return plaintext

class Atbash():
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify(25-numberify(char))

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify(25-numberify(char))

        return plaintext

class Rot13():
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            ciphertext += letterify((numberify(char) + 13) % 26)

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            plaintext += letterify((numberify(char) + 13) % 26)

        return plaintext

class Vigenere():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext):
            ciphertext += letterify((numberify(char) + numberify(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            plaintext += letterify((numberify(char) - numberify(key[i % len(key)])) % 26)
        
        return plaintext

class Trithemius():
    def encrypt(self, plaintext):
        ciphertext = ""
        for i, char in enumerate(plaintext):
            ciphertext += letterify((numberify(char) + i % 26) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            plaintext += letterify((numberify(char) - i % 26) % 26)
        
        return plaintext

class VariantBeaufort():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext):
            ciphertext += letterify((numberify(char) - numberify(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            plaintext += letterify((numberify(char) + numberify(key[i % len(key)])) % 26)
        
        return plaintext

class Beaufort():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext):
            ciphertext += letterify(25 - ((numberify(char) + numberify(key[i % len(key)])) % 26))
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            plaintext += letterify(25 - ((numberify(char) - numberify(key[i % len(key)])) % 26))
        
        return plaintext

class Gronsfeld():
    def encrypt(self, plaintext, key):
        key = str(key)
        ciphertext = ""
        for i, char in enumerate(plaintext): 
            ciphertext += letterify((numberify(char) + int(key[i % len(key)])) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        key = str(key)
        plaintext = ""
        for i, char in enumerate(ciphertext): 
            plaintext += letterify((numberify(char) - int(key[i % len(key)])) % 26)
        
        return plaintext

class Autokey():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        key = key + plaintext
        for i, char in enumerate(plaintext):
            ciphertext += letterify((numberify(char) + numberify(key[i])) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext):
            plain_letter = letterify((numberify(char) - numberify(key[i])) % 26)
            plaintext += plain_letter
            key += plain_letter
        
        return plaintext

class RunningKey():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for i, char in enumerate(plaintext):
            ciphertext += letterify((numberify(char) + numberify(key[i])) % 26)
        
        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ""
        for i, char in enumerate(ciphertext):
                plaintext += letterify((numberify(char) - numberify(key[i])) % 26)
        
        return plaintext