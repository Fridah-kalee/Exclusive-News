import unittest
from models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles("Barron's","Al Root","Elon Musk Is Likely Getting a Tax Deduction From His Stock Sales","The Tesla CEO paid about $11 billion in taxes in 2021. He's likely due to get some of that back when he files his 2022 taxes.","https://www.barrons.com/articles/elon-musk-sales-tesla-stock-tax-deduction-51651267518","https://images.barrons.com/im-534978/social","2022-04-30T08:54:17Z","Elon Musk paid about $11 billion in taxes in 2021. The Tesla CEO might get some of that back when he files his 2022 taxes because he likely has a loss on the stock he just sold to fund his purchase o… [+2091 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == "__main__":
    unittest.main()           
