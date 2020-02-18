import os, os.path
import sys
from tensorflow.keras.models import load_model
import warnings 
warnings.filterwarnings('ignore')

PATH = 'model/'

nets = len([name for name in os.listdir(PATH)])

model = [0] *nets

for i in range(nets):
	nome_file = PATH + str(i+1)+".h5"
	model[i] = load_model(nome_file)

print("Model succesfully loaded.")

t = input("Do you want to test the data? (Make sure you put the test.csv file into the data path)")
