mot_secret = ""
life=10
lettreProposees = []

def reset_game():
    global mot_secret
    global life
    global lettreProposees

    mot_secret = ""
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
    if lettre in lettreProposees[:]:
        return None
    elif lettre in mot_secret:
        return True
    else:
        life -= 1
        lettreProposees.append(lettre)
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

def count_lettres_error():
    return len(lettreProposees)

def get_lettreProposees():
    return lettreProposees