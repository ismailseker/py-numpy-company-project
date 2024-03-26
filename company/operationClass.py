import numpy as np

class IntArray:

    def __init__(self, int_array):
        if not isinstance(int_array,np.ndarray) or int_array.dtype != int:
            raise ValueError("Input must be Numpy array of integers !")
        
        self.int_array = int_array

    def display(self):
        print(self.int_array)
    
    def salary(self):
        arrayShape = self.int_array.shape
        moneyPerProduct = np.full(arrayShape, 7)
        salaries = self.int_array * moneyPerProduct

        print(f"People made {self.int_array} products and this is their salaries {salaries}")
        
