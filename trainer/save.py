def save_model(model,nets):
	for i in range(nets):
		nome_file = str(i+1)+".h5"
		model[i].save("../model/"+nome_file)
