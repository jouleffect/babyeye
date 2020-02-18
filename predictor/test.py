import os, os.path
import sys
from keras.models import load_model
import warnings 
warnings.filterwarnings('ignore')

PATH = 'model/'

nets = len([name for name in os.listdir(PATH)])

model = [0] *nets

for i in range(nets):
	nome_file = PATH + str(i+1)+".h5"
	model[i] = load_model(nome_file)

print("Model succesfully loaded.")

t = raw_input("Do you want to test the data? (Make sure you put the test.csv file into the data path)")
if t == 'Y' or t == 'y':
	n_classi = raw_input("--------| NUMBER OF CLASSES: ")
	shape = raw_input("--------| NUMBER OF PIXELS: ")
	righe, colonne = int(shape), int(shape)
	import clean
	test = clean.preelab_csv_data_test(n_classi,righe,colonne)
	import show
	show.show_data_test(test,model)
print("=====================GOODBYE===================")