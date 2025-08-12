# ANN

- simulate the human brain's information processing -> like the brain uses neurons to process data and make decisions
- use artificial neurons to analyze data, identify patterns and make predictions

## architecture: layers working together

- input layer: receives raw data, each neuron in this layer represents one piece of input information
- hidden layers: perform the actual computation and pattern recognition -> like feature detectors that learn to recognize increasingly complex patterns -> the first hidden layer might detect simple edges in an image, while deeper layers combine these to recognize shapes, and eventually whole objects
- output layer: produces the final result

## artificial neuron: basic building block

a simple decision-maker that receives multiple inputs, weights their importance, and produces an output:

1. inputs: the neuron receives several numerical values (like pixel intensities in an image or features of data)
2. weights: each input has an associated weight that determines its importance
3. summation: the neuron multiples each input by its weight and adds them all together
4. bias: a bias value is added to adjust the neuron's sensitivity
5. activation function: this sum passes through a function that determines the final outputs

## how: training process

- **forward propagation**: data flows from input to output, with each layer transforming the information based on current weights and biases
- **error calculation**: the network's output is compared to the correct answer, measuring how far off the prediction was
- **backpropagation**: the learning mechanism -> the error is propagated backwards through the network, and the weights are adjusted to reduce this error
- **iteration**: this process repeats many times with different examples until the network learns the underlying patterns in the data

## key concepts

- patter recognition: excels at finding complex patterns in data that would be nearly impossible to program explicitly
- non-linearity: the activation functions introduce non-linear transformations, allowing the network to model complex, curved relationships in data
- distributed representation: information is stored across many connections rather in specific locations

# CNN

## problem

- regular neural networks treat each input as an independent feature, but images have **spatial relationships** -> it would treat a pixel in the top-left corner the same way as a pixel in the bottom-right corner, losing all that spatial context that makes images interpretable
- it connects every neuron in one layer to every neuron in the next layer -> a typical image might have hundreds of thousands of pixels, and connecting each pixel to every neuron in the next layer would create an enormous number of connections

-> CNNs were primarily designed to extract features from grid-like matrix datasets, mimicking the natural way of processing visual information

## core innovation: local connectivity

instead of every neuron connecting to every neuron in the previous layer, CNNs use **local receptive fields**

picture a small window sliding across an image, examining just a small patch at a time -> this window is called a filter or kernel - a small neural network that specializes in detecting specific patterns like edges, corners, or textures within that local region

as this window slides across the entire image -> look for its particular pattern everywhere

## overview of convolution

- convolution layers consist of a set of learnable filters having small widths, heights and the same depth of that of input volume (3 if the input layer is image input)
- during forward pass, it slides each filter across the whole input volume step by step where each is called stride and compute the dot product between the filter weights and patch from input volume
- it slides filters -> get a 2D output for each filter and stack them together as a result

## layers used to build CNNs

example by running a convnets on of image of dimension 32 x 32 x 3
- input layers: the input will be an image or s sequence of images, this layer holds the raw input of the image with width 32, height 32, and depth 3
- convolutional layers: extract the feature from the input dataset. it applies a set of learnable filters known as the kernels (may be 2x2, 3x3, etc) to the input images -> the output of this layer is referred as feature maps. suppose we use a total of 12 filters for this layer, we'll get an output volume of dimension 32x32x12
- activation layer: apply activation function to feature maps (the volume remains unchanged)
- pooling layer: periodically inserted in the convnets and used to reduce the size of volume which makes the computation faster, reduce memory and also preventing overfitting
- batch normalization & dropout layers: to stabilize training and prevent overfitting
- flattening: the resulting feature maps are flattened into an 1D vector so they can be passed into a completely linked layer for classification or regression
- full connected layers: takes the input from the previous layer and computes the final classification or regression task

# basic concepts

## kernels

- structure: a small matrix (3x3, 5x5, etc) of learnable weights. during training, these weights adjust to detect specific visual patters -> a 3x3 kernel has 9 parameters regardless of input size -> parameter-efficient
- multiple kernels per layer: each convolution layer uses many different kernels. if have 32 kernels in a layer -> 64 different feature maps as output - each detecting different types of patterns

## padding

- boundary problem: when sliding a kernel across an image, the output is smaller than the input -> deep networks would rapidly shrink the spatial dimensions to unusable sizes
- used to manage spatial dimensions

## stride: control information sampling

- defines how many pixels the kernel move
- larger strides reduce computation by examining fewer positions, but at the cost of spatial resolution -> trade-off between detail preservation and processing speed
