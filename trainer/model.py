from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Dropout, MaxPool2D

nets = 7
model = [0] *nets

for i in range(nets):
    model[i] = Sequential()
    model[i].add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu', input_shape = (righe,colonne,1)))
    model[i].add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu'))
    model[i].add(MaxPool2D(pool_size=(2,2)))
    model[i].add(Dropout(0.25))
    model[i].add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                 activation ='relu'))
    model[i].add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                 activation ='relu'))
    model[i].add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model[i].add(Dropout(0.25))
    model[i].add(Flatten())
    model[i].add(Dense(256, activation = "relu"))
    model[i].add(Dropout(0.5))
    model[i].add(Dense(n_classi, activation = "softmax"))

    model[i].compile(loss="categorical_crossentropy",
              optimizer='adam',
              metrics=['accuracy'])
