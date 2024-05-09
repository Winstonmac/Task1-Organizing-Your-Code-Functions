import pandas as pd
import matplotlib.pyplot as plt

def get_file(file_path):
    with open(file_path, 'r') as file:
        return file

def plot_data(file):
    # Read the data from the file into a pandas DataFrame
    data = pd.read_csv(file)

    # Extract the x and y columns from the DataFrame
    x = data['x']
    y = data['y']

    # Create a scatter plot of the data
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')
    plt.show()

# Example usage:
file = get_file('data.csv')
plot_data(file)
