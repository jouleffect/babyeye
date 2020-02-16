import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

righe, colonne = 28,28
n_classi = 10

test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

y_train = train["label"]
X_train = train.drop(labels = ["label"],axis = 1)

#------Normalizzazione-----#
X_train = X_train / 255.0
test = test / 255.0

#-----Ridimensionamento----#
X_train = X_train.values.reshape(-1,righe,colonne,1)
test = test.values.reshape(-1,righe,colonne,1)
#-------Label encoding-------#
y_train = to_categorical(y_train, num_classes = n_classi)


#-------Immagini di esempio---------------#
plt.figure(figsize=(15,4.5))
for i in range(30):  
    plt.subplot(3, 10, i+1)
    plt.imshow(X_train[i].reshape((righe,colonne)),cmap=plt.cm.binary)
    plt.axis('off')
plt.subplots_adjust(wspace=-0.1, hspace=-0.1)
plt.show()
