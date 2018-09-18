import csv
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

# Initialize the Linear Regression
reg = LinearRegression()
# lable = pd.DataFrame(sf['maxPrice'])

# Read the data from the csv file
gapminder_csv ='data_housePrice.csv'
gapminder = pd.read_csv(gapminder_csv)

#Extract the required field for the prediction
train1 = gapminder['arrivals']
label = gapminder['maxPrice'] # which part you

# location = label._get_index_resolvers(0)
null_location = []

# Find the locations of Null Values in the data
for i in range(len(label)):
    if (np.isnan(label[i]) or np.isnan(train1[i])):
        null_location.append(i)

# Remove the Null value data from the data
filter_data_train = []
filter_data_label = []
for i in range(len(label)):
    if (i not in null_location):
        filter_data_train.append(train1[i])
        filter_data_label.append(label[i])


print (len(filter_data_label))
print (len(filter_data_train))
filter_data_train = pd.DataFrame(filter_data_train)
filter_data_label = pd.DataFrame(filter_data_label)
reg.fit(filter_data_label,filter_data_train)

# xfit = np.linspace(0, 200, 200)
# yfit = reg.predict(xfit[:, np.newaxis])

yfit = reg.predict(filter_data_train)
# plt.xlim(filter_data_train.min, filter_data_train.max)
# plt.ylim(filter_data_label.min(), filter_data_label.max())
plt.scatter(filter_data_label, filter_data_train)
plt.plot(filter_data_train, yfit,color = 'red');
plt.show()


























# predicted response vector

#print (reg.intercept_)
#print (reg.s)

#x = range(len(lable))
#y_pred = reg.intercept_ + reg.coef_ * x

# plotting the regression line

#plt.plot(x, y_pred, color="g")
# plt.plot()
#reg.scrop(x_test,y_test)

#reg.plot()
#plt._show()

