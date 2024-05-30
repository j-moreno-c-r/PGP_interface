import gnupg

# Initialize the gnupg object
gpg = gnupg.GPG()

def encrypt_message(message, public_key_file):
    # Import the public key
    with open(public_key_file) as f:
        public_key = f.read()
    import_result = gpg.import_keys(public_key)

    # Get the key fingerprint
    key_fingerprint = import_result.fingerprints[0]

    # Encrypt the message
    encrypted_data = gpg.encrypt(message, key_fingerprint)
    return encrypted_data

def decrypt_message(encrypted_data, private_key_file):
    # Import the private key
    with open(private_key_file) as f:
        private_key = f.read()
    gpg.import_keys(private_key)

    # Decrypt the message
    decrypted_data = gpg.decrypt(str(encrypted_data))
    return decrypted_data



