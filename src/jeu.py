

mot_secret = input ("Choisis ton mot ptit pd")
life=10
lettreProposees = []

def set_mot(mot):
    global mot_secret
    mot_secret = mot

def get_mot():
    return mot_secret

def proposer_lettre(lettre):
    global life
    global lettreProposees
    lettreProposees.append(lettre)

    if lettre in mot_secret:
        return True
    else:
        life -= 1
        return False

def get_life():
    return life

def proposer_mot(mot):
    global life
    if mot == mot_secret:
        return True
    else:
        life -= 1
        return False

