import unittest
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import PizzeriaException
from unittest.mock import Mock

class TestCartePizzeria(unittest.TestCase): 

    #tester une carte vide
    def test_empty_carte_pizzeria(self):
        carte_pizz = CartePizzeria()
        self.assertTrue(carte_pizz.is_empty)

    def test_pizza_number(self):
        carte_pazz = CartePizzeria()
        pizza = Mock()  
        carte_pazz.add_pizza(pizza)
        self.assertEqual(carte_pazz.nb_pizzas(), 1)

    def test_remove_number(self): 
        carte_pazz = CartePizzeria()
        pizza = Mock()  
        pizza.name = "jemmy"
        carte_pazz.add_pizza(pizza)
        carte_pazz.remove_pizza("jemmy")
        self.assertEqual(carte_pazz.nb_pizzas(), 0)

    def test_remove_pizza_by_name(self):
        carte_pazz = CartePizzeria()
        pizza = Mock()  
        pizza2 = Mock()
        pizza.name = "margarita"
        pizza2.name = "vvegii"
        carte_pazz.add_pizza(pizza)
        carte_pazz.add_pizza(pizza2)
        self.assertEqual(carte_pazz.nb_pizzas(), 2)
        carte_pazz.remove_pizza("margarita")
        self.assertEqual(carte_pazz.nb_pizzas(), 1)
        

    # def test_remove_pizza_not_found(self):
    #     carte = CartePizzeria()
    #     with self.assertRaises(PizzeriaException):
    #         carte.remove_pizza("samy")



if __name__ == "__main__":
    unittest.main()
