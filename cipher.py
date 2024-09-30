from afd import AFD

class CesarCipherAFD(AFD):
    def encrypt(self, input_string, shift=3):
        encrypted = []
        for char in input_string:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
                encrypted.append(encrypted_char)
            else:
                encrypted.append(char)
        return '|' + ''.join(encrypted) + '|'

    def decrypt(self, input_string, shift=3):
        decrypted = []
        if input_string.startswith('|') and input_string.endswith('|'):
            input_string = input_string[1:-1]

        for char in input_string:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted.append(decrypted_char)
            else:
                decrypted.append(char)
        return ''.join(decrypted)
