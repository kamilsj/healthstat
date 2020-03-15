import os
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encryption:
    
    def GenerateKeyFromPassword(self, password):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend,
        )
        
        key = base64.urlsafe_b64decode(kdf.derive(password))
        return key
    
        
    
    def GenerateKey(self):
        key = Fernet.generate_key()
        return key