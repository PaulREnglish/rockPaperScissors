import unittest
from rockPaperScissors import rockCalculator

class MyTest(unittest.TestCase):
    def test_aiCountersRepeatRockChoices(self):
        rockCalculatorInstance = rockCalculator()
        rockCalculatorInstance.fight('rock')
        rockCalculatorInstance.fight('rock')
        rockCalculatorInstance.fight('rock')
        for i in range(0,100):
            self.assertEqual(rockCalculatorInstance.fight('rock')[2],'You lose!')

    def test_aiDoesNotChooseSameChoiceEveryTime(self):
        rockCalculatorInstance = rockCalculator()
        aiItemChoiceArray = []
        for i in range(0,100):
            aiItemChoiceArray.append(rockCalculatorInstance.fight(rockCalculatorInstance.randomItemChoice())[1])

        def isPaper(aiItem): 
            return aiItem == 'paper'

        self.assertEqual(all(map(isPaper, aiItemChoiceArray)), False)
 

if __name__ == '__main__':
    unittest.main()
