The pgp in this project its descarted only for tests, the interface will only works if you import this keys or register a key imported and logged on your system.
If you forget how follow the instructions(Linux OS):
```bash
python -m venv .pgp_interface
source .pgp_interface/bin/activate
```
The result will be something like:
```bash
(..pgp_interface) username:~/directory name$ 
```
clone the repo and run a:
```bash
python -r instal requirements.txt
```
you can run with 
```bash 
python main.py
```
or with     
```bash 
chmod +x ./run.sh
```
and next 
```bash 
./run.sh
```

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
!["..."](./images/registerkeys.jpeg "Cypherpunks write code ")
