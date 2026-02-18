import jwt
import bcrypt
from datetime import datetime, timedelta

class AuthUtils:
    def __init__(self, secret_key, algorithm='HS256'):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_token(self, user_id, expires_in=3600):
        expiration = datetime.utcnow() + timedelta(seconds=expires_in)
        token = jwt.encode({'user_id': user_id, 'exp': expiration}, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
