import matplotlib.pyplot as plt
import numpy as np

def calculate(numbers=None):
    if numbers is None:
        # Get user input for a list of 9 numbers
        numbers = input("Enter a list of 9 numbers separated by spaces: ")
        numbers = list(map(float, numbers.split()))

    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3x3 Numpy array
    matrix = np.array(numbers).reshape(3, 3)

    # Calculate mean, variance, standard deviation, max, min, and sum along rows, columns, and flattened matrix
    result = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    }

    return result

# To test the function with user input
print(calculate())