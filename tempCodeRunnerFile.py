    def test_remove_pizza_not_found(self):
        carte = CartePizzeria()
        with self.assertRaises(PizzeriaException):
            carte.remove_pizza("samy")