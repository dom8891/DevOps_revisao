import pytest
from Principal import somar
from principal import multiplicar
from principal import subtrair
from principal import divisao


def teste_somar():
    assert somar(2,4)==6

def teste_multiplicar():
    assert multiplicar(6,12)==72

def teste_subtrair():
    assert subtrair(290-800)==610

def teste_divisao():
    assert divisao(6,2)== 3