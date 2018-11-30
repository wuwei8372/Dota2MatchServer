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

def predict_knn(radiant_team, dire_team, player_tier):
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

	if (player_tier<30):
		knn = joblib.load("models/knn_tier1_model.m")
	elif (player_tier>=30 and player_tier<40):
		knn = joblib.load("models/knn_tier2_model.m")
	elif (player_tier>=40 and player_tier<60):
		knn = joblib.load("models/knn_tier3_model.m")
	elif (player_tier>=60):
		knn = joblib.load("models/knn_tier4_model.m")
	win_prob = knn.predict_proba(dataset)[0][0]
	return str(win_prob * 100)+ '%'

radiant_team = [73, 102, 2, 38, 56]
dire_team = [68, 1, 113, 65, 66]
outcome = predict_knn(radiant_team,dire_team, 12)
print(outcome)





