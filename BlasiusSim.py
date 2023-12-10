import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    # Generating sample data
    x = np.linspace(0, 10, 100)  # Creating an array of 100 points from 0 to 10
    y = np.sin(x)                # Example function (sine wave)

    # Plotting the data
    plt.figure(figsize=(8, 6))   # Creating a figure object
    plt.plot(x, y, label='Sine Wave')  # Plotting x vs y with label
    plt.xlabel('X-axis Label')   # Setting the label for the x-axis
    plt.ylabel('Y-axis Label')   # Setting the label for the y-axis
    plt.title('Example Plot')    # Setting the title of the plot
    plt.legend()                 # Displaying the legend

    # Displaying the plot
    plt.grid(True)               # Adding a grid
    plt.tight_layout()           # Adjusting layout for better appearance
    plt.show()                   # Displaying the plot

def main():
    plot_graph()

if __name__ == "__main__":
    main()
