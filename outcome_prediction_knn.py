import sqlite3
import numpy as np
from sklearn import neighbors
from sklearn.externals import joblib
import os
from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split

dataset_tier1 = []
labels_tier1 = []

dataset_tier2 = []
labels_tier2 = []

dataset_tier3 = []
labels_tier3 = []

dataset_tier4 = []
labels_tier4 = []




conn = sqlite3.connect('dota.db')
c = conn.cursor()
print "Opened database successfully"

cursor = c.execute("SELECT dire_team, radiant_team, radiant_win from data WHERE game_mode == 22 AND lobby_type == 7 AND avg_rank_tier > 20 AND avg_rank_tier < 30 LIMIT 100000")
for row in cursor:
	data_tuple = np.zeros((130))
	dire_team = row[0].split(",")
	radiant_team = row[1].split(",")
	for dire in dire_team:
		data_tuple[int(dire)] = 1
	for radiant in radiant_team:
		data_tuple[int(radiant)] = -1
	dataset_tier1.append(data_tuple)
	labels_tier1.append(int(row[2]))

cursor = c.execute("SELECT dire_team, radiant_team, radiant_win from data WHERE game_mode == 22 AND lobby_type == 7 AND avg_rank_tier >= 30 AND avg_rank_tier < 40 LIMIT 100000")
for row in cursor:
	data_tuple = np.zeros((130))
	dire_team = row[0].split(",")
	radiant_team = row[1].split(",")
	for dire in dire_team:
		data_tuple[int(dire)] = 1
	for radiant in radiant_team:
		data_tuple[int(radiant)] = -1
	dataset_tier2.append(data_tuple)
	labels_tier2.append(int(row[2]))

cursor = c.execute("SELECT dire_team, radiant_team, radiant_win from data WHERE game_mode == 22 AND lobby_type == 7 AND avg_rank_tier >= 40 AND avg_rank_tier < 60 LIMIT 10000")
for row in cursor:
	data_tuple = np.zeros((130))
	dire_team = row[0].split(",")
	radiant_team = row[1].split(",")
	for dire in dire_team:
		data_tuple[int(dire)] = 1
	for radiant in radiant_team:
		data_tuple[int(radiant)] = -1
	dataset_tier3.append(data_tuple)
	labels_tier3.append(int(row[2]))

cursor = c.execute("SELECT dire_team, radiant_team, radiant_win from data WHERE game_mode == 22 AND lobby_type == 7 AND avg_rank_tier >= 60 AND avg_rank_tier < 80 LIMIT 10000")
for row in cursor:
	data_tuple = np.zeros((130))
	dire_team = row[0].split(",")
	radiant_team = row[1].split(",")
	for dire in dire_team:
		data_tuple[int(dire)] = 1
	for radiant in radiant_team:
		data_tuple[int(radiant)] = -1
	dataset_tier4.append(data_tuple)
	labels_tier4.append(int(row[2]))

dataset_tier1 = np.asarray(dataset_tier1)
labels_tier1 = np.asarray(labels_tier1)
dataset_tier2 = np.asarray(dataset_tier2)
labels_tier2 = np.asarray(labels_tier2)
dataset_tier3 = np.asarray(dataset_tier3)
labels_tier3 = np.asarray(labels_tier3)
dataset_tier4 = np.asarray(dataset_tier4)
labels_tier4 = np.asarray(labels_tier4)

print dataset_tier1.shape

# split_point = int(len(labels)*0.7)

# train_X = dataset[:split_point]
# train_y = labels[:split_point]
# test_X = dataset[split_point:]
# test_y = labels[split_point:]

random_state = 100

#train_X, test_X, train_y, test_y = train_test_split(dataset, labels, test_size = 0.3, random_state = random_state)

k = 13

knn_tier1 = neighbors.KNeighborsClassifier(n_neighbors = k)
knn_tier1.fit(dataset_tier1, labels_tier1)
joblib.dump(knn_tier1, "models/knn_tier1_model.m")

knn_tier2 = neighbors.KNeighborsClassifier(n_neighbors = k)
knn_tier2.fit(dataset_tier2, labels_tier2)
joblib.dump(knn_tier2, "models/knn_tier2_model.m")


knn_tier3 = neighbors.KNeighborsClassifier(n_neighbors = k)
knn_tier3.fit(dataset_tier3, labels_tier3)
joblib.dump(knn_tier3, "models/knn_tier3_model.m")

knn_tier4 = neighbors.KNeighborsClassifier(n_neighbors = k)
knn_tier4.fit(dataset_tier4, labels_tier4)
joblib.dump(knn_tier4, "models/knn_tier4_model.m")

# parameters = {'n_neighbors':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}
# clf = GridSearchCV(knn, parameters, cv=10)
# clf.fit(test_X, test_y)
# print(clf.best_score_)
# print(clf.best_params_)




conn.close()

