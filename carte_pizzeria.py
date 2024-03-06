class CartePizzeria:
    def __init__(self) -> None:
        self.liste_pizzas = []

    def is_empty(self):
        return len(self.liste_pizzas) == 0
    def nb_pizzas(self):
        return len(self.nb_pizzas)

    def add_pizza(self,pizza):
        self.liste_pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizz in self.liste_pizzas:
            if (isinstance(name, pizz) and pizz == name):
                self.liste_pizzas.remove(name)
                return
        raise CartePizzeria("la pizza n'existe pas sur le menu")
        