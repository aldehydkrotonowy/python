import math
import pandas_datareader as pdr
import numpy as np
import pandas as pd
from pprint import pprint
from sklearn.preprocessing import MinMaxScaler
# Future versions of pandas will require you to explicitly register matplotlib converters
from pandas.plotting import register_matplotlib_converters
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
register_matplotlib_converters()
df = pdr.DataReader('AAPL', data_source='yahoo',
                    start="2012-01-01", end="2019-12-17")


plt.figure(figsize=(16, 8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel("Date", fontsize=18)
plt.ylabel("Close Price USD ($)", fontsize=18)
# plt.show()


# filter close prices and conver to numpy array
onlyClosePriceData = df.filter(['Close'])
closePriceArray = onlyClosePriceData.values
# take 80% of data for training
training_data_len = math.ceil(len(closePriceArray) * .8)

pprint(training_data_len)  # 1603

# rescale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(closePriceArray)
# pprint(scaled_data)
# take first training_data_len points
scaled_train_data = scaled_data[0:training_data_len]

# create training data set;
# x set will containd data points for training
# y set will contain target data point wich we want to predict

x_train = []
y_train = []

for i in range(60, len(scaled_train_data)):
    x_train.append(scaled_train_data[i-60:i, 0])
    y_train.append(scaled_train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# reshape sample data from 2D to 3D
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# pprint(x_train.shape)

# build LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mean_squared_error")


# Time to train our model
# model.fit(x_train,y_train,batch_size=1, epochs=1)
pprint('finished')


# create testing data set
test_data = scaled_data[training_data_len - 60:, :]
x_test = []
y_test = closePriceArray[training_data_len:, :]
