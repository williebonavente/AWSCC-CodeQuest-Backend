"""Author: Willie M. Bonavente
   Date: 12/03/2023

STD programming - polymorphism
"""

import math

class Basic_Arithmetic:
    
    @staticmethod
    def addition(dataset: list):
        total = 0 
        for i in dataset:
            total += i
        return total
    
    @staticmethod
    def subtraction(dataset: list):
        difference = sum([-i for i in dataset])
        return difference
        
    @staticmethod
    def multiplication(dataset: list):
        product = 1  # Initialize product to 1 instead of 0
        for i in dataset:
            product *= i
        return product
    
    @staticmethod
    def division(dataset: list):
        quotient = dataset[0]  # Initialize quotient with the first element of the dataset
        for i in dataset[1:]:
            quotient /= i
        return quotient
    
    # Applying Polymorphism
    @staticmethod
    def get_mean(dataset: list):
        average = Basic_Arithmetic.addition(dataset) / len(dataset)
        num_of_decimal = str(average)[::-1].find('.') 
        if num_of_decimal > 2:
            raise ValueError("Basic Arithmetic Class can only handle 2 floating point.")
        else:
            return f"{average:.2f}" 
    
class AdditionalComputation(Basic_Arithmetic):
    
    # Formula for standard deviation 
    # \sqrt{sum(each value - the population mean) / N}
    # Applying Polymorphism
    @staticmethod
    def get_mean(dataset: list): 
        average = Basic_Arithmetic.addition(dataset) / len(dataset) 
        return average
        
    @staticmethod
    def get_variance(dataset: list):
        get_average = AdditionalComputation.get_mean(dataset)
        # Find each score's deviation from the mean
        sum_squared = 0  # Initialize sum_squared to 0
        for scores in dataset:
            diff_scores = scores - get_average
            # squared each deviation
            squared = (diff_scores) ** 2
            sum_squared += squared  # Accumulate the squared deviations

        # get the variance 
        variance = sum_squared/(len(dataset) - 1)
        return variance
 
    @staticmethod
    def standard_deviation(dataset: list):
        input_variance = AdditionalComputation.get_variance(dataset)
        std = math.sqrt(input_variance)
        # Note we will only round of the answer if the variance was already complete
        return f"Std: {std:.2f}"
    
    

# Testing 

dataset_input_1 = [46, 69, 32, 60, 52, 41] 
dataset_input_2 = [46.32, 69.53, 32.13532, 60.2321, 52.3142, 41.5126] 
get_std = AdditionalComputation.standard_deviation(dataset_input_1)
print(get_std)


# Mean
dataset_mean = AdditionalComputation.get_mean(dataset_input_2) # Additional_Computation Class

print(dataset_mean)