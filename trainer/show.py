import matplotlib.pyplot as plt
#-------Immagini di esempio---------------#

def show_data(X_train,Y_train,datagen):
	plt.figure(figsize=(15,6))
	for i in range(40):  
	    plt.subplot(4, 10, i+1)
	    X_train2, Y_train2 = datagen.flow(X_train,Y_train).next()
	    plt.imshow(X_train2[0].reshape((28,28)),cmap=plt.cm.binary)
	    plt.axis('off')
	plt.subplots_adjust(wspace=-0.1, hspace=-0.1)
	plt.show()
