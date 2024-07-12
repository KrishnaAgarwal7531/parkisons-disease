import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to read the CSV file and return the last 30 points
def get_last_30_points():
    data = pd.read_csv('live.csv')
    # Take the last 30 points from each column
    return data.iloc[-30:]

# Initialize the plot
fig, ax = plt.subplots()

# Initialize an empty list of lines (one for each column)
lines = []
for i in range(1, len(get_last_30_points().columns)):
    line, = ax.plot([], [], label=get_last_30_points().columns[i])
    lines.append(line)

# Set the labels and legend
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.legend()

# Function to update the plot
def update(frame):
    # Get the latest data
    data = get_last_30_points()
    x = data.index
    for i, line in enumerate(lines):
        y = data.iloc[:, i + 1]
        line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return lines

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=1000, blit=True)

# Show the plot
plt.show()