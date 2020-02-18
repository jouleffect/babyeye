import getopt, sys
import numpy as np
import pandas as pd 
import warnings 
warnings.filterwarnings('ignore')

parametri = sys.argv
listaParametri = parametri[1:]

opzioni = "c:s:h"
opzioni_parola = ["help", "class=", "shape="]

try:
    arguments, values = getopt.getopt(listaParametri, opzioni, opzioni_parola)
except getopt.error as err:
	helpfile = open("help.txt", "r")
	for line in helpfile:
		print(line)
	sys.exit()

for argomento, valore in arguments:
    if argomento in ("-h", "--help"):
    	helpfile = open("help.txt", "r")
    	for line in helpfile:
    		print(line)
    	sys.exit()
    elif argomento in ("-c", "--class"):
    	n_classi = valore
    elif argomento in ("-s", "--shape"):
    	righe, colonne = valore,valore

print("=======================================================================================")
print("-------------------------WELCOME TO THE BABYEYE TRAINER SCRIPT-------------------------")
print("=======================================================================================")
try:
    n_classi
    print (("----------| Selected number of classes: (%s)") % (n_classi))
except NameError:
    n_classi = 10
    print (("----------| Number of classes not defined, using the default one: (%s)") % (n_classi))
try:
    righe
    print (("----------| Selected number of pixels: (%s)") % ([righe,colonne]))
except NameError:
    righe, colonne = 28,28
    print (("----------| Number of pixels not defined, using the default one: (%s)") % ([righe,colonne]))

print("=======================================================================================")

print("=======================================================================================")
print("I'm cleaning the data...")

import clean
X_train, y_train = clean.preelab_csv_data(n_classi,righe,colonne)

print("Data Augmentation..")
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
            rotation_range=10,  
            zoom_range = 0.10,  
            width_shift_range=0.1, 
            height_shift_range=0.1)

s = raw_input("Data succesfully cleaned. Do you want to visualize them?")
if s == 'Y' or s == 'y':
    import show
    show.show_data(X_train,y_train,datagen)
mod = raw_input("Do you want to create the model?")
if mod =='Y' or mod == 'y':
    import modello
    m, nets = modello.crea_modello(righe,colonne,n_classi)

    tr = raw_input("Model created! Do you want to train it?")
    if tr =='Y' or tr == 'y':
        import trainer
        trainer.train_1(X_train,y_train,m,nets,datagen)

        salva = raw_input("Do you want to save the trained model?")
        if salva =='Y' or salva == 'y':
            import save
            save.save_model(m,nets)
            print("Model succesfully saved!")

print("==================================GOODBYE========================================")   
