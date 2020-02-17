import getopt, sys
import numpy as np
import pandas as pd 
import clean

parametri = sys.argv
listaParametri = parametri[1:]

opzioni = "c:n:s:b:e:h"
opzioni_parola = ["help", "output=", "verbose"]

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
    elif argomento in ("-n", "--nets"):
    	nets = valore
    elif argomento in ("-s", "--shape"):
    	righe, colonne = valore,valore
    elif argomento in ("-n", "--nets"):
    	nets = valore
    elif argomento in ("-b", "--batch"):
    	batch = valore
    elif argomento in ("-e", "--epochs"):
    	epochs = valore

print("=======================================================================================")
print("-------------------------WELCOME TO THE BABYEYE TRAINER SCRIPT-------------------------")
print("=======================================================================================")
try:
    n_classi
    print (("----------| Selected number of classes: (%s)") % (n_classi))
except NameError:
    n_classi = 10
    print (("----------| Number of nets not defined, using the default one: (%s)") % (n_classi))
try:
    nets
    print (("----------| Selected number of nets: (%s)") % (nets))
except NameError:
    nets = 1
    print (("----------| Number of nets not defined, using the default one: (%s)") % (nets))
try:
    righe
    print (("----------| Selected number of pixels: (%s)") % ([righe,colonne]))
except NameError:
    righe, colonne = 28,28
    print (("----------| Number of pixels not defined, using the default one: (%s)") % ([righe,colonne]))
try:
    batch
    print (("----------| Selected batch size: (%s)") % (batch))
except NameError:
    batch = 30
    print (("----------| Batch size not defined, using the default one: (%s)") % (batch))
try:
    epochs
    print (("----------| Selected number of epochs: (%s)") % (epochs))
except NameError:
    epochs = 20
    print (("----------| Number of epochs not defined, using the default one: (%s)") % (epochs))
print("=======================================================================================")


### PULIZIA DEL FILE ###
clean.preelab_csv_data(n_classi,righe,colonne,nets,batch,epochs)
