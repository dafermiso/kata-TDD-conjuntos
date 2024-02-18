import unittest
from kataTDD.conjunto import Conjunto


class TestConjunto(unittest.TestCase):
  def test_conjunto_vacio(self):
    conjunto = Conjunto([])
    self.assertIsNone(conjunto.promedio())
