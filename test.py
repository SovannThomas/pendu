import pytest
from jeu import set_mot,get_mot

class TestPendu():

    def test_is_word_present():
        set_mot("python")
        assert get_mot() == "python"

