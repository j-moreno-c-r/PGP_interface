import os
def private_key():
    return os.path.join(os.path.expanduser('~'), 'PGP_interface/pgpinterface/src/pgpinterface/resources/keys/private_key.asc')

def public_key():
    return os.path.join(os.path.expanduser('~'), 'PGP_interface/pgpinterface/src/pgpinterface/resources/keys/public_key.asc')

def figerprint_pubkey():
    return os.path.join(os.path.expanduser('~'), 'PGP_interface/pgpinterface/src/pgpinterface/resources/keys/fingerprint_pubkey.asc')

def main_bg():
    return os.path.join(os.path.expanduser('~'), 'PGP_interface/pgpinterface/src/pgpinterface/resources/images/main_bg.jpeg')