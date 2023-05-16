import os

class Config:
    # gera uma chave secreta aleatória
    SECRET_KEY = os.urandom(32)
