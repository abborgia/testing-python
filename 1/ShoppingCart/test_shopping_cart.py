import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("pan", 10)
        self.jugo = Item("Jugo", 20)

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self):
        print("Metodo tearDown despues de la prueba")

    def test_cinco_mas_cinco_igual_diez(self): 
        assert 5 + 5 == 10

    def test_nombre_product_igual_pan(self):
        self.assertEqual(self.pan.name, "pan")    # Compara valores (==)
    
    def test_nombre_product_distinto_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_item())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_item())
    
    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)     # compara objeto (Is)
        self.assertIsNot(item, self.jugo)

    def test_exeption_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total,0)
        self.assertLess(total, self.pan.price + 1.0)
        self.assertEqual(total, self.pan.price)

    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(), self.pan.name)

    def test_fail(self):
        if 2>3:
            self.fail("Dos no es mayor a tres")
    

if __name__ == '__main__':
    unittest.main()

