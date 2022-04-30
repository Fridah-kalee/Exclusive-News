import unittest
from models import Sources

class SourcesTest(unittest.TestCase):
    def setUp(self):
        '''
        Test method that runs before
        '''
        self.new_source =Sources('bbc-news','BBC News','Your trusted source for breaking news','http://www.bbc.co.uk/news/world-61281895','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == "__main__":
    unittest.main()