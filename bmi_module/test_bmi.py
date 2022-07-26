import unittest
import assesment
import table1

#Test cases with different height and weight
l = [[171, 52], [180, 77], [167, 82], [170, 85], [171, 96], [155, 90], [155, 96]]

#Class for testing
class TestBmi(unittest.TestCase):

    #intialises the count of overweight person
    count_overweight = 0

    #Method for checking test cases fall under right BMI category
    def check(self, bmi_value):        

        #Checking the test cases for Underweight
        if bmi_value<= 18.4:
            self.assertEqual(table1.df['BMI Category'][0], 'Underweight')

        #Checking the test cases for Normal weight
        elif 18.5<= bmi_value <= 24.9:
            self.assertEqual(table1.df['BMI Category'][1], 'Normal weight')
            
        #Checking the test cases for Overweight
        elif 25 <= bmi_value <= 29.9:
            self.assertEqual(table1.df['BMI Category'][2], 'Overweight')            

        #Checking the test cases for Moderately obese
        elif 30 <=bmi_value<= 34.9:
            self.assertEqual(table1.df['BMI Category'][3], 'Moderately obese')

        #Checking the test cases for Severely obese
        elif 35<= bmi_value <= 39.9:
            self.assertEqual(table1.df['BMI Category'][4], 'Severely obese')

        #Checking the test cases for Very severely obese
        elif bmi_value >= 40:
            self.assertEqual(table1.df['BMI Category'][5], 'Very severely obese')

    #Counting overweight person
    def overweight_count(self, bmi_value):
        if 25<= bmi_value <= 29.9:
            self.count_overweight = self.count_overweight+1           
            
    #Test method for BMI category
    def test_bmi(self):
        
        for height, weight in l:
            bmi_value = assesment.calc_bmi(height, weight)
            self.check(bmi_value)

    #Test method for counting overweight person
    def test_countOverweight(self):

        for height, weight in l:
            bmi = assesment.calc_bmi(height, weight)
            self.overweight_count(bmi)
        
        self.assertEqual(self.count_overweight, 2)         

#Running for same module  
if __name__ == '__main__':
    unittest.main()