

_mot_secret = input ("Choisis ton mot ptit pd")
_life=10

def set_mot(mot):
    global mot_secret
    mot_secret = mot

def get_mot():
    return mot_secret

def proposer_lettre(lettre):
    global life
    if lettre in mot_secret:
        return True
    else:
        life -= 1
        return False

def get_life():
    return life

