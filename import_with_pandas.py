# import Pandas (data manipulation) and Matplotlib (trending)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the data file
data_file = pd.read_csv('data_with_headers.csv')

# create time vector from imported data
time = data_file['time']
# parse good sensor data from imported data
sensors = data_file.loc[:,'s1':'s4']

# display the first 6 sensor rows
print(sensors[0:6])

# adjust time to start at zero by subtracting the
#  first element in the time vector (index = 0)
time = time - time[0]

# calculate the average of the sensor readings
avg = np.mean(sensors,1) # over the 2nd dimension

# export data
my_data = [time, sensors, avg]
result = pd.concat(my_data,axis=1)
#or use:  result = pd.DataFrame(time,sensors,avg)

result.to_csv('result.csv')
result.to_excel('result.xlsx')
result.to_html('result.htm')
result.to_clipboard()

# generate a figure
plt.figure(1)
plt.plot(time,sensors['s1'],'r-')
plt.plot(time,avg,'b.')
# add text labels to the plot
plt.legend(['Sensor 2','Average'])
plt.xlabel('Time (sec)')
plt.ylabel('Sensor Values')
# save the figure as a PNG file
plt.savefig('my_Python_plot.png')
# show the figure on the screen (pauses execution until closed)
#plt.show()

