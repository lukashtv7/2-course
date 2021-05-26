class Encryptor:

    def encrypt(self, data, key):
        enc_data = ''

        for symb in data:
            enc_data += chr(abs(ord(symb) + key))

        return enc_data

    def decrypt(self, data, key):
        enc_data = ''

        for symb in data:
            enc_data += chr(abs(ord(symb) - key))

        return enc_data