import sqlite3
import numpy as np
from sklearn import neighbors
from sklearn.externals import joblib
import os

dataset = []
labels = []

conn = sqlite3.connect('dota.db')
c = conn.cursor()
print "Opened database successfully"

cursor = c.execute("SELECT dire_team, radiant_team, radiant_win from data WHERE game_mode == 22 AND lobby_type == 7 LIMIT 10000")
for row in cursor:
	data_tuple = np.zeros((130))
	dire_team = row[0].split(",")
	radiant_team = row[1].split(",")
	for dire in dire_team:
		data_tuple[int(dire)] = 1
	for radiant in radiant_team:
		data_tuple[int(radiant)] = -1
	dataset.append(data_tuple)
	labels.append(int(row[2]))

dataset = np.asarray(dataset)
labels = np.asarray(labels)
print dataset.shape
print labels

split_point = int(len(labels)*0.7)

train_X = dataset[:split_point]
train_y = labels[:split_point]
test_X = dataset[split_point:]
test_y = labels[split_point:]

k = 5

knn = neighbors.KNeighborsClassifier(n_neighbors = k)
knn.fit(train_X, train_y)
joblib.dump(knn, "models/knn_model.m")


conn.close()

