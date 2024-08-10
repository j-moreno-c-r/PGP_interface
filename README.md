I use briefcase to admin and build this project,if you want to contribute to use this you will need to install the briefcase admin:
```bash
pip install briefcase
```
in the root of the code: /PGP_interface/pgpinterface/src/pgpinterface/resources, run:
```bash
pip install -r requirements.txt
```
in the:/PGP_interface/pgpinterface run:
```bash 
briefcase create
```
later
```bash 
briefcase dev
```
Now having fun... and RTFM the briefcase docs:https://docs.beeware.org/en/latest/

For now the interface has a liltle problem, burocracy of the lib, you need to trust a pubkey before write for this contact, and for now you will need to do this for terminal, i will fix this in future updates, you can trust a pubkey with:

you can see the fingerprints with
```bash
gpg --list-keys 
```
with the fingerprint of a pubkey:
```bash
gpg --edit-key The fingerprint of the key

gpg> trust

Your decision? 5

Do you really want to set this key to ultimate trust? (y/N) y

gpg> save

```
please if you want to up a PR dont up your keys is hard to me to verify and maybe you will expose this...
If you dont have keys, use this execelent workshop: https://github.com/CasaVinteUm/workshop-pgp 
!["..."](./images/registerkeys.jpeg "Cypherpunks write code ")
