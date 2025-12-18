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
    reset_game()
    set_mot("python")
    assert proposer_mot("python") == True
    assert proposer_mot("java") == False

def test_count_lettresProposees():
    reset_game()
    set_mot("python")
    proposer_lettre('x')
    proposer_lettre('y')
    assert count_lettres_error() == 1

def test_get_lettreProposees():
    reset_game()
    set_mot("python")
    proposer_lettre('x')
    assert get_lettreProposees() == ['x']
    proposer_lettre('y')
    assert get_lettreProposees() == ['x']
    proposer_lettre('u')
    assert get_lettreProposees() == ['x','u']

def test_definir_life():
    reset_game()
    assert get_life() == 10
    set_life(5)
    assert get_life() == 5
    set_mot("python")
    proposer_lettre('z')
    assert get_life() == 4
    proposer_lettre('p')
    assert get_life() == 4
    reset_game()
    assert get_life() == 10