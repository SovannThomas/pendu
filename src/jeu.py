

_mot_secret = input ("Choisis ton mot ptit pd")
_life=10

def set_mot(mot):
    global mot_secret
    mot_secret = mot

def get_mot():
    return mot_secret


print(_mot_secret)