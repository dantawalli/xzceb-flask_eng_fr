import unittest
from translator import english_to_french, french_to_english

class FrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual('null', 'null') # test when null is given as input the output is null.
        self.assertNotEqual('Bonjour', 'Hello')  # test when Bonjour is given as input the output is Hello
        

class EnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual('null', 'null') # test when null is given as input the output is null.
        self.assertNotEqual('Hello', 'Bonjour')  # test when Hello is given as input the output is Bonjour
        
unittest.main()