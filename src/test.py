import pytest
from jeu import *


def test_is_word_present():
        set_mot("python")
        assert get_mot() == "python"

def proposer_lettre_tests():
    set_mot("python")
    assert proposer_lettre("p") == True
    assert proposer_lettre("x") == False
    assert proposer_lettre("p") == None

def test_get_life():
    set_mot("python")
    initial_life = get_life()
    proposer_lettre("x")  # incorrect letter
    assert get_life() == initial_life - 1
    proposer_lettre("p")  # correct letter
    assert get_life() == initial_life - 1  # life should not decrease

def test_proposer_mot():
    set_mot("python")
    assert proposer_mot("python") == True
    assert proposer_mot("java") == False

def count_lettresProposees_tests():
    set_mot("python")
    proposer_lettre("x")
    proposer_lettre("y")
    assert count_lettres_error() == 2

def get_lettreProposees_tests():
    set_mot("python")
    proposer_lettre("x")
    proposer_lettre("y")
    assert get_lettreProposees() == ["x", "y"]