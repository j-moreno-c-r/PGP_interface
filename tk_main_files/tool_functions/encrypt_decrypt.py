from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt(message):
    with open('keys/public_key.txt', 'r') as file:
        public_key = file.read()

    public_key_bytes = public_key.encode('utf-8')
    public_key = serialization.load_pem_public_key(public_key_bytes)

    encrypted = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted


def decrypt(encrypted):
    with open('keys/private_key.txt', 'r') as file:
        private_key = file.read()
    private_key_bytes = private_key.encode('utf-8')

    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)
    
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message

