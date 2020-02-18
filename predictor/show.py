import matplotlib.pyplot as plt
from keras.models import Model
#-------Immagini di esempio---------------#

def show_data_test(test,model):
	plt.figure(figsize=(15,6))
	for i in range(40):  
	    plt.subplot(4, 10, i+1)
	    plt.imshow(test[0].reshape((28,28)),cmap=plt.cm.binary)
	    plt.title("Predict: %d" % model[i].predict(test))
	    plt.axis('off')
	plt.subplots_adjust(wspace=-0.1, hspace=-0.1)
	plt.show()