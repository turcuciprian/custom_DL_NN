import random

#  IMPORTANT !!!!!!!!!!!!!!
# the last layer has 1 neuron because it is the output layer. so the last layer has the predicted value

# I still will need to calculate the cost function and then backpropagation


#  START

# house prices data (suared meters, nr of bathrooms, price)
data = [[50, 2, 200000], [43, 1, 150000], [40, 1, 143000], [60, 2, 220000]]
input_layer_length = len(data)
# list of number of neurons for each layer
neuron_layers_length = [input_layer_length, 3, 4, 1]

# list of all the weights for each neuron (will be randomly generated)
neuron_layers_weights = []
# list of all the resulting values for each neuron
neuron_layers_values = [[x[0] for x in data]]  # the first layer is the data itself


def get_relu(current_neuron, prev_layer, weights, cur_neuron_index):
    relu = 0
    for prev_neuron_index, prev_neuron in enumerate(prev_layer):
        for weight in weights:
            relu = value * weight
    return relu


def set_neuron_layer_values(layer_length, input_layer):
    new_layer = []
    for neuron_index in range(layer_length):
        new_layer.append(get_relu(input_layer, neuron_layers_weights[neuron_index]))
        print("")


# .0
def init_weights():
    for index, neurons_count in enumerate(neuron_layers_length):
        if index == 0:
            continue

        columns = len(data[0]) - 1
        previous_column_length = neuron_layers_length[index - 1]

        # istantiate current layer total number of weights
        total_weights_for_current_layer = (
            neurons_count * previous_column_length * columns
        )
        # random list of numbers from -1 to 1 (3 decimals)
        neuron_layers_weights.append(
            [
                round(random.uniform(-1.00, 1.00) * 1000) / 1000
                for y in range(total_weights_for_current_layer)
            ]
        )


# 1.
def forward_pass():
    for cur_layer_index, current_layer_length in enumerate(neuron_layers_length):
        prev_layer_index = cur_layer_index - 1
        weight_index = 0
        if cur_layer_index == 0:
            # jumping the first layer because it is the input layer and it has no previous layer to calculate the relu and work with
            continue
        else:
            # calculate relu for the current layer with the weights and neuron values from the previous layers
            # do this neuron by neuron
            layer_neuron_pass(cur_layer_index)
            print("processing each layer")


# 2.
def layer_neuron_pass(cur_layer_index):
    prev_layer_index = cur_layer_index - 1
    print("processing each neuron")
    for neuron_index in range(neuron_layers_length[cur_layer_index]):
        print(
            "processing neuron index: "
            + str(neuron_index)
            + " for layer index: "
            + str(cur_layer_index)
        )
        neuron_layers_values[cur_layer_index] = get_relu(
            neuron_layers_values[prev_layer_index],
            neuron_layers_weights[neuron_index],
        )


def main():
    # initializing the script
    print("Starting...")
    # initializing the weights
    init_weights()
    #  forwad propagation
    forward_pass()

    # # looping trough each neuron layer length list value
    # for _, number_of_leyers in enumerate(neuron_layers_length):
    #     # setting the total number of weights for the current layer
    #     total_weights_for_current_layer = number_of_leyers * len(data)

    #     # generatuig random weights for the current layer and appending them to the neuron_layers_weights list
    #     neuron_layers_weights.append([round(random.uniform(-1.00,1.00) * 1000)/1000 for y in range(total_weights_for_current_layer)])

    #     # looping trough each neuron layer
    #     layers_loop()


# looping trough each neuron layer
def layers_loop():
    for neuron_index, neuron_count in enumerate(neuron_layers_length):
        # instantiate current layer list values
        current_layer_values = []


main()
print("done")


"""
# PREVIOUS CODE:

# initialize weights
def init_weights():
#  map neur_layers_length to neuron_layers_weights
    for _, number_of_leyers in enumerate(neuron_layers_length):
        
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
                weight_index = neuron_count+data_index-1 #formula to identify the index of each weight based on the 2 enclosed for loops
                
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
"""
