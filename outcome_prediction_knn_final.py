import sqlite3
import numpy as np
from sklearn import neighbors
from sklearn.externals import joblib
import os

# HOW TO USE THIS FUNCTION
# from outcome_prediction_knn_final import predict_knn
# radiant_team = [3,5,12,25,64]
# dire_team = [87,24,34,42,14]

# outcome = predict_knn(dire_team, radiant_team)
# print outcome

def predict_knn(radiant_team, dire_team):
	dataset = []

	# test data
	# radiant_team = [3,5,12,25,64]
	# dire_team = [87,24,34,42,14]

	data_tuple = np.zeros((130))
	for i in radiant_team:
		data_tuple[i] = -1
	for j in dire_team:
		data_tuple[j] = 1

	dataset.append(data_tuple)

	knn = joblib.load("models/knn_model.m")
	win_prob = knn.predict_proba(dataset)[0][0]
	return str(win_prob * 100)+ '%'
	# return "51.42%"




