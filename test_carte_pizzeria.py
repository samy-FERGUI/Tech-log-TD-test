import unittest
from carte_pizzeria import CartePizzeria
class TestCartePizzeria(unittest.TestCase): 

    #tester une carte vide
    def test_empty_carte_pizzeria(self):
        carte_pizz = CartePizzeria()
        self.assertTrue(carte_pizz.is_empty)



if __name__ == "__main__":
    unittest.main()
