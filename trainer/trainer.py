from keras.callbacks import LearningRateScheduler
from sklearn.model_selection import train_test_split
import warnings 
warnings.filterwarnings('ignore')

def train_1(X_train,y_train,model,nets,datagen):

	batch = input("-------| BATCH SIZE -------> ")
	batch = int(batch)
	epochs = input("-------| EPOCHS -------> ")
	epochs = int(epochs)

	learning_rate = LearningRateScheduler(lambda x: 1e-3 * 0.95 ** x)
	
	H = [0] * nets

	for j in range(nets):
	    X_train2, X_val2, y_train2, y_val2 = train_test_split(X_train, y_train, test_size = 0.1)
	    H[j] = model[j].fit_generator(datagen.flow(X_train2,y_train2, batch_size=batch),
	                              epochs = epochs, validation_data = (X_val2,y_val2),
	                              verbose = 1, steps_per_epoch=X_train2.shape[0] // batch
	                              ,callbacks=[learning_rate])
