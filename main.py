from encrypt_decrypt import encrypt, decrypt
import base64

if __name__ == "__main__":
    message = input("Enter the message you want to encrypt: ")

    encrypted_message = encrypt(message)
    encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')

    pgp_message = f"-----BEGIN PGP MESSAGE-----\n\n{encrypted_message_base64}\n-----END PGP MESSAGE-----"
    print(pgp_message)

    # The PGP-like message to decrypt
    message_to_decrypt = pgp_message.replace("-----BEGIN PGP MESSAGE-----\n\n", "").replace("\n-----END PGP MESSAGE-----", "")
    message_to_decrypt = base64.b64decode(message_to_decrypt)

    original_message = decrypt(message_to_decrypt)
    print(original_message.decode('utf-8'))