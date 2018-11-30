import numpy as np
from numpy import  genfromtxt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import csv

rank_tier=input("player rank tier:")
id=input("hero id(the frequest played):")
rank_tier=int(rank_tier)
id=int(id)
tier1 = genfromtxt('tier1_att_final.csv', delimiter=',',skip_header=1)
tier2 = genfromtxt('tier2_att_final.csv', delimiter=',',skip_header=1)
tier3 = genfromtxt('tier3_att_final.csv', delimiter=',',skip_header=1)
tier4 = genfromtxt('tier4_att_final.csv', delimiter=',',skip_header=1)


#print(tier1.view(type=np.matrix))
Y_1=[i[0] for i in tier1]
X_1=[i[1:]for i in tier1]

Y_2=[i[0] for i in tier2]
X_2=[i[1:]for i in tier2]

Y_3=[i[0] for i in tier3]
X_3=[i[1:]for i in tier3]

Y_4=[i[0] for i in tier4]
X_4=[i[1:]for i in tier4]




#print(type(tier1))
Y_1=np.array(Y_1)
X_1=np.array(X_1)

Y_2=np.array(Y_2)
X_2=np.array(X_2)

Y_3=np.array(Y_3)
X_3=np.array(X_3)


Y_4=np.array(Y_4)
X_4=np.array(X_4)
# #######################################building model######################################################################
rank=int()
goal_label=int()
def recommend(rank_tier,id):
    def cluster_label_making(rank_tier):
        if rank_tier>=60:
            rank==1
            kmeans= KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=500,random_state=0).fit(X_1)###change########################################################33
            cluster_label = np.vstack((Y_1, kmeans.labels_)).T
            #centroids=kmeans.cluster_centers_
            return cluster_label
        if 60>rank_tier>=40:
            rank==2
            kmeans= KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=500,random_state=0).fit(X_2)###change########################################################33
            cluster_label = np.vstack((Y_2, kmeans.labels_)).T#################change################################################################
            #centroids=kmeans.cluster_centers_
            return cluster_label
        if 40>=rank_tier>=30:
            rank==3
            kmeans= KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=500,random_state=0).fit(X_3)###change########################################################33
            cluster_label = np.vstack((Y_3, kmeans.labels_)).T
            #centroids=kmeans.cluster_centers_
            return cluster_label
        if 30>rank_tier>=20:
            rank==4
            kmeans= KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=500,random_state=0).fit(X_4)###change########################################################33
            cluster_label = np.vstack((Y_4, kmeans.labels_)).T#################change################################################################
            #centroids=kmeans.cluster_centers_
            return cluster_label
    cluster_label=cluster_label_making(rank_tier)
    for i in range(116):
            if cluster_label[i][0]==id:
                goal_label=cluster_label[i][1]
                break
    hero_list=[]
    X=np.empty([116,16],dtype=float)
    HeroIDlist=[]
    for i in range(116):
        if cluster_label[i][1]==goal_label:
            if 30>rank_tier>=20:
                X=X_4
            if 40>rank_tier>=30:
                X=X_3
            if 60>rank_tier>=40:
                X=X_2
            if rank_tier>=60:
                X=X_1
            hero_list.append(((int(cluster_label[i][0]),X[i][-1])))

    def takeSecond(item):
            return item[1]
    hero_list.sort(key=takeSecond,reverse=True)
    HeroIDlist= [i[0] for i in hero_list]
    #return hero_list
    return HeroIDlist
heroIDlist=recommend(rank_tier,id)
print(heroIDlist)

# with open('hero.csv', 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(hero_list)
# csvFile.close()
