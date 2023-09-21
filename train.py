import random

#  IMPORTANT !!!!!!!!!!!!!!
# the last layer has 1 neuron because it is the output layer. so the last layer has the predicted value

# I still will need to calculate the cost function and then backpropagation


#  START
# current weight index
weight_index = 0
# house prices data (suared meters, nr of bathrooms, price)
data = [[50, 2, 200000], [43, 1, 150000], [40, 1, 143000], [60, 2, 220000]]
input_layer_length = len(data)
# list of number of neurons for each layer
neuron_layers_length = [input_layer_length, 3, 4, 1]

# list of all the weights for each neuron (will be randomly generated)
neuron_layers_weights = []
# list of all the resulting values for each neuron
neuron_layers_values = [
    [[x[0], x[1]] for x in data]
]  # the first layer is the data itself


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


# 1. Starting forward pass
def forward_pass():
    # go trough each layer
    for index, current_layer_length in enumerate(neuron_layers_length):
        # jump the first layer (the data layer)
        if index == 0:
            continue
        # set the previous layer index
        prev_layer_index = index - 1

        # go trought each neuron in the current layer
        current_layer_neuron_loop(current_layer_length, prev_layer_index)


# 2. looping trough each layer of neurons
def process_previous_layer_neurons(index):
    global weight_index
    # previous layer index
    prev_layer_index = index - 1
    print("processing layer: " + str(index))
    for neuron_index in range(neuron_layers_length[index]):
        current_layer_length = neuron_layers_length[index]
        print("weight index: {}".format(weight_index))
        weight_index = weight_index + 1


# 3. looping trough each neuron in the current layer
def current_layer_neuron_loop(current_layer_length, prev_layer_index):
    global weight_index
    # loop trough each neuron in the current layer
    weight_index = 0
    for neuron_index in range(current_layer_length):
        # loop trough each neuron in the previous layer
        neuron_value = 0
        for prev_neuron_index, prev_neuron_value in enumerate(
            neuron_layers_values[prev_layer_index]
        ):
            weight = neuron_layers_weights[prev_layer_index][weight_index]
            # neuron_value = neuron_value + (float(prev_neuron_value[0]) * weight)
            # neuron_layers_values[prev_layer_index + 1] = [[50, 1]]
            print(
                "neuron index: {}, prev neuron index:{}, values:{} weight:{}".format(
                    neuron_index, prev_neuron_index, prev_neuron_value, weight
                )
            )
            weight_index += 1
        neuron_layers_values.append([[1, 2], [1, 2], [1, 2]])


def main():
    # initializing the script
    print("Starting...")
    # initializing the weights
    init_weights()
    #  forwad propagation
    forward_pass()
    print('done!')


# looping trough each neuron layer
def layers_loop():
    for neuron_index, neuron_count in enumerate(neuron_layers_length):
        # instantiate current layer list values
        current_layer_values = []


main()
print("done")
