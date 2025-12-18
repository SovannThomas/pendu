

_mot_secret = None
_life=10

def set_mot(mot):
    global mot_secret
    mot_secret = mot

def get_mot():
    return mot_secret

def mot_existe(mot):
    return True
