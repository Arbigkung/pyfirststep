import unittest
from city_function import city_info

class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        info = city_info('BKK', 'Thailand')
        self.assertEqual(info, 'BKK, Thailand')
    
    def test_city_country_population(self):
        info = city_info('Taipei', 'Taiwan', '7000000')
        self.assertEqual(info, 'Taipei, Taiwan Pop: 7000000')
unittest.main()
