from pizza import Pizza
from carte_pizzeria_exception import PizzeriaException
class CartePizzeria:
    def __init__(self) -> None:
        self.liste_pizzas = []

    def is_empty(self):
        return len(self.liste_pizzas) == 0
    def nb_pizzas(self):
        return len([item for item in self.liste_pizzas])

    def add_pizza(self,pizza):
        self.liste_pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizz in self.liste_pizzas:
            if (pizz.name == name):
                self.liste_pizzas.remove(pizz)
                return
        raise PizzeriaException(f"error {name}")
        