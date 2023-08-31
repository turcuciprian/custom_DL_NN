# house prices data (m2, price)
data = [
    [50,200000],
    [43,150000],
    [40,143000],
    [60,220000]
    ]
layer1_weights =  [0.1, 0.1, 0.1] # initial weights, random values, 3 neurons

# mean normalization
def normalize(data,x):
    # formula (x - avg) / max - min
    iterable = [row[0] for row in data]
    average = sum(iterable) / len(data)
    maximum = max(iterable)
    minimum = min(iterable)
    return (x-average) / (maximum-minimum)
# print(normalize(data,50))