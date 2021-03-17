import unittest 
from apis import cat_fact_api


class TestCatFact(unittest.TestCase):

    def test_get_cat_fact(self):
        fact = cat_fact_api.get_random_fact()
        self.assertIsNotNone(fact)

        # TODO more meaningful tests