import pytest
from jeu import *


def test_is_word_present():
        reset_game()
        set_mot("python")
        assert get_mot() == "python"

def test_proposer_lettre():
    reset_game()
    set_mot("python")
    assert proposer_lettre("p") == True
    assert proposer_lettre("x") == False
    assert proposer_lettre("x") == None


def test_get_life():
    reset_game()
    set_mot("python")
    initial_life = get_life()
    assert initial_life == 10
    proposer_lettre("x")  # incorrect letter


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