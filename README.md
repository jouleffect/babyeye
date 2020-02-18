# BaByEyE

This mini software, written in python with tensorflow and keras libraries, is divided in 2 parts.

The first one is the trainer. It is the core of the script, because it allows the baby eye to learn the types of image.
Furthermore, depending on the established parameters, this part takes a long time once executed.
In this part, you can specify by input command line, the number of prediction classes and the shape of the input image.
You also need to put yor data train file into the Data path, (there's an example one by default).
First of all, the script will load and parse the data file Data/train.csv, cleaning it. Then you can choose if visualize or not the ploto of the data. You can create and train the model, by choosing the number of nets and the batch size and the number of epochs. Finally, you can save the trained model in a file, to use it in the test part.


The second part of the mini script is the predictor, the user tool of the script.
By loading the model trained in the first part and saved in a specific file, the predictor will predict the input image.

To run the training of some data set, you can type this command in your shell:

#### $ python run.py [params]

the set of params of the command is:

-h help

-i the img files path

-s pixels of the images (rows and columns)

-c classes of predictions

-b batch_size

-e epochs

-n number of nets

## Example:

#### $ python run.py -c 10 -b 64 -e 10 -n 20

Instead, to test an image, type this command in your shell:

#### $ python test.py [params]

the set of params of the command is:

-h help

-c classes of predictions
