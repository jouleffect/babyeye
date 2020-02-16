# BaByEyE

This mini software, written in python with the tensorflow libraries, is divided in 2 parts.
The first one is the trainer. It is the core of the script, because it allows the baby eye to learn the types of image.
Furthermore, depending on the established parameters, this part takes a long time once executed.
The second part of the mini script is the predictor, the user tool of the script.
By loading the model trained in the first part and saved in a specific file, the predictor will predict the input image.

To run the training of some data set, you can type this command in your shell:

#### sh trainer.sh [params]

the set of params of the command is:

-h help

-i the img files path

-p pixels of the images (rows and columns)

-c classes of predictions

-b batch_size

-e epochs

-n number of nets

## Example:

#### $ sh trainer -i /home/user/img -p [28,28] -c 10 -b 64 -e 10 -n 20

Instead, to test an image, type this command in your shell:

#### $ sh test.sh [params]

the set of params of the command is:

-h help

-i the img files path
