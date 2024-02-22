import matplotlib.pyplot as plt

# Read data from the text file
with open('test.txt', 'r') as file:
    data = file.readlines()

# Extract x and y values from the data
x = []
y = []
for line in data:
    parts = line.strip().split('.')
    x.append(float(parts[0]))
    y.append(float(parts[1]))

# Plot the line
plt.plot(x, y)

# Add labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Title of the Plot')

# Display the plot
plt.show()
