import pytest
from Principal import somar
from principal import multiplicar


def teste_somar():
    assert somar(2,4)==6

def teste_multiplicar():
    assert multiplicar(6,12)==72