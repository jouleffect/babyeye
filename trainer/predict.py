results = np.zeros( (test.shape[0],10) ) 

for j in range(nets):
    results = results + model[j].predict(test)
    
results = np.argmax(results,axis = 1)
results = pd.Series(results,name="Label")

sub = pd.concat([pd.Series(range(1,28001),name = "ImageId"),ris],axis = 1)
sub.to_csv("prediction.csv",index=False)
