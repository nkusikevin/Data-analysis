# import Numpy (data manipulation) and Matplotlib (trending)
import numpy as np
import matplotlib.pyplot as plt

# load the data file
data_file = np.genfromtxt('data_file.txt', delimiter=',')

# create time vector from imported data (starts from index 0)
time = data_file[:,][:,0]
# parse good sensor data from imported data
sensors = data_file[:,][:,1:5]

# display the first 6 sensor rows
print(sensors[0:6])

# adjust time to start at zero by subtracting the
#  first element in the time vector (index = 0)
time = time - time[0]

# calculate the average of the sensor readings
avg = np.mean(sensors,1) # over the 2nd dimension

# export data
# reshape time and avg as column vectors
time_col = time.reshape(-1,1)
avg_col = avg.reshape(-1,1)
my_data = np.concatenate((time_col,sensors,avg_col), axis=1)
np.savetxt('export_from_python.txt',my_data,delimiter=',')

# generate a figure
plt.figure(1)
plt.plot(time,sensors[:,][:,1],'r-')
plt.plot(time,avg,'b.')
# add text labels to the plot
plt.legend(['Sensor 2','Average'])
plt.xlabel('Time (sec)')
plt.ylabel('Sensor Values')
# save the figure as a PNG file
plt.savefig('my_Python_plot.png')
# show the figure on the screen (pauses execution until closed)
plt.show()

