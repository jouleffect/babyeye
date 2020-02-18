import pandas as pd 
from keras.utils.np_utils import to_categorical 

def preelab_csv_data(n_classi,righe,colonne):

    train = pd.read_csv("../data/train.csv")

    y_train = train["label"]
    X_train = train.drop(labels = ["label"],axis = 1)
    X_train = X_train / 255.0
    X_train = X_train.values.reshape(-1,righe,colonne,1)
    y_train = to_categorical(y_train, num_classes = n_classi)

    return X_train, y_train


def preelab_csv_data_test(n_classi,righe,colonne):

    test = pd.read_csv("data/test.csv")
    test = test / 255.0
    test = test.values.reshape(-1,righe,colonne,1)
    
    return test

# DA MODIFICARE
def preelab_img_data():
    test = pd.read_csv("test.csv")
    train = pd.read_csv("train.csv")

    y_train = train["label"]
    X_train = train.drop(labels = ["label"],axis = 1)
    X_train = X_train / 255.0
    test = test / 255.0
    X_train = X_train.values.reshape(-1,righe,colonne,1)
    test = test.values.reshape(-1,righe,colonne,1)
    y_train = to_categorical(y_train, num_classes = n_classi)


    datagen = ImageDataGenerator(
            rotation_range=10,  
            zoom_range = 0.10,  
            width_shift_range=0.1, 
            height_shift_range=0.1)


