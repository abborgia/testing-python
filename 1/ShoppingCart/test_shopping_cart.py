import unittest
from shopping_cart import Item, ShoppingCart

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
        self.assertEqual(self.pan.name, "pan")
    
    def test_nombre_product_distinto_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_item())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_item())
    
    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)

    
    

if __name__ == '__main__':
    unittest.main()

