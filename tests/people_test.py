import unittest
import sys
sys.path.insert(0, '../src')
from People import People
from test_data import TestData


class PeopleTestCases(unittest.TestCase):
    def setUp(self):
        test_data = TestData()
        self.people=People(test_data.get_names, test_data.get_ages)

    def test_getfunction(self):
        self.assertEqual(self.people.get(18), ['Cathy', 'Dan'])

    def test_bonus_reverse(self):
        self.assertEqual(self.people.get_reverse('Larry'), 
        [19, 20])
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(PeopleTestCases('test_getfunction'))
    suite.addTest(PeopleTestCases('test_bonus_reverse'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())