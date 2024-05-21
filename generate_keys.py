from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


def generate_keys():
    privkey = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )

    pubkey = privkey.public_key()

    private_key = privkey.private_bytes(
            encoding=crypto_serialization.Encoding.PEM,
            format=crypto_serialization.PrivateFormat.PKCS8,
            encryption_algorithm=crypto_serialization.NoEncryption()
        )
    public_key = pubkey.public_bytes(
            encoding=crypto_serialization.Encoding.PEM,
            format=crypto_serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    return private_key, public_key

private_key, public_key = generate_keys()

print("-----BEGIN PRIVATE KEY-----")
print(private_key.decode()[27:-25])  # remove the first and last line
print("-----END PRIVATE KEY-----\n")

print("-----BEGIN PUBLIC KEY-----")
print(public_key.decode()[26:-24])  # remove the first and last line
print("-----END PUBLIC KEY-----")