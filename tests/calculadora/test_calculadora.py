
import os
import sys

# Adiciona o caminho ao diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from src.calculadora.calculadora import Calculadora

class TestCalculadora:

    def test_sum(self):
        calculadora = Calculadora()
        assert calculadora.sum(2,2) == 4

    def test_subtraction(self):
        calculadora = Calculadora()
        assert calculadora.subtraction(2,2) == 0

    def test_multiplication(self):
        calculadora = Calculadora()
        assert calculadora.multiplication(2,2) == 4

    def test_division(self):
        calculadora = Calculadora()
        assert calculadora.division(2,2) == 1