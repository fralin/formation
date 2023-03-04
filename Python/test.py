from puissance import calc_puissance
import unittest

class TestPuissance(unittest.TestCase):
    def test_puissance(self):
        self.assertEqual(calc_puissance(2,2), 4)
        
if __name__ == "__main__":        
    unittest.main()