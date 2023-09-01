import random

# house prices data (m2, price)
data = [
    [50,200000],
    [43,150000],
    [40,143000],
    [60,220000]
    ]
# list of number of neurons for each layer
neuron_layers_length =[3,4,4,3]
# list of all the weights for each neuron
neuron_layers_weights = []
# list of all the resulting values for each neuron
neuron_layers_numbers = []


# initialize weights
def init_weights():
#  map neur_layers_length to neuron_layers_weights
    for layerIndex, number_of_leyers in enumerate(neuron_layers_length):
        
        # istantiate current layer total number of weights
        total_weights_for_current_layer = number_of_leyers * len(data)
        
        # random list of numbers from -1 to 1 (3 decimals)
        neuron_layers_weights.append([round(random.uniform(-1.00,1.00) * 1000)/1000 for y in range(total_weights_for_current_layer)])
        
def calculate_neuron_layer_numbers():
    # cycle trough each neuron layer group
    for neuron_index,neuron_count in enumerate(neuron_layers_length):
        # instantiate current layer list values
        current_layer_values = []
        
        # neuron count range
        neuron_count_range = range(neuron_count)
        
        # cyclre trought each neuron
        for neuron in neuron_count_range:
        
        # initialise relu
            current_relu = 0
            
            # cycle trough each data item
            for data_index, current_data_value in enumerate(data):
                # current data value
                data_value = current_data_value[0] # 0 is for x1 (the actual data value and 1 is for y (the resulting price)
                
                # change the weight index (to get the weight for the current data value)
                weight_index = len(data)+data_index #formula to identify the index of each weight based on the 2 enclosed for loops
                
                # current weight value
                current_weight = neuron_layers_weights[neuron_index][weight_index]
                
                #  value with weights
                value_with_weight = data_value * current_weight
                
                # calculate relu
                current_relu= current_relu + value_with_weight
                
            # append current relu to current layer values
            current_layer_values.append(current_relu)
            
        # append current layer values to neuron layers numbers
        neuron_layers_numbers.append(current_layer_values)
        
    print(neuron_layers_numbers)
    
    
# mean normalization
def normalize(data,x):
    # formula (x - avg) / max - min
    iterable = [row[0] for row in data]
    average = sum(iterable) / len(data)
    maximum = max(iterable)
    minimum = min(iterable)
    return (x-average) / (maximum-minimum)

# print(normalize(data,50))
# initialise the weights
init_weights()
# forward propagation
calculate_neuron_layer_numbers()
print('DONE')