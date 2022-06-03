import pandas as pd

file = pd.read_csv(r'/Users/hwwwa/Algorithm-python/pn.txt', names=['value'])

val1 = []
val2 = []
val3 = []

for values in file.iloc[:, 0]:
    [v1, v2, v3] = values.split()
    val1.append(v1)
    val2.append(v2)
    val3.append(v3)

file['value1'] = pd.Series(val1)
file['value2'] = pd.Series(val2)
file['value3'] = pd.Series(val3)

file = file.iloc[:, 1:]

new_csv_file = file.to_csv(r'/Users/hwwwa/Algorithm-python/pn.csv')