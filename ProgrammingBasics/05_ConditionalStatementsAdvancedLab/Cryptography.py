from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

private_data = b"IBAN 1000 4017 2364 3333 pass 12345677"

encrypt_data = cipher_suite.encrypt((private_data))
print(encrypt_data)

decrypt_data = cipher_suite.decrypt(encrypt_data)
print(decrypt_data)