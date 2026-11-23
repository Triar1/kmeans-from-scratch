from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('clustering_1.csv')
N = 4
epsilon = 0.001
iteration = 0
centroides = df.sample(N) #pioche 4 ligens aux hasards

while iteration < 30:
	Cluster = []
	for j in range(len(df)) : #association des points aux clusters
		distances = [(sum((df.iloc[j]-centroides.iloc[i])**2))**0.5 for i in range(0,N)] #liste distances entre centre et point
		Cluster.append(distances.index(min(distances))) #quel cluster associe

	c=[0 for i in range(3*N)]
	for k in range(len(df)) : #creation nouveau cluster
		for i in range(N) :
			if Cluster[k]== i: 
				c[3*i]+=df.iloc[k]['x'] #valeur de somme en x
				c[3*i+1]+=df.iloc[k]['y'] #valeur de somme en y
				c[3*i+2]+=1 #nb delement dans le cluster
	nouveaux_centroides = pd.DataFrame([(c[3*k]/c[3*k+2] if c[3*k+2]>0 else centroides.iloc[k]['x'],c[3*k+1]/c[3*k+2] if c[3*k+2]>0 else centroides.iloc[k]['y'])for k in range(N)], columns=['x', 'y'])

	#plt.plot(df['x'], df['y'],'+')
	plt.scatter(df['x'], df['y'], c=Cluster, alpha=0.5)
	plt.scatter(centroides['x'], centroides['y'], c='red', s=100)
	plt.scatter(nouveaux_centroides['x'], nouveaux_centroides['y'], c='green', s=100)
	plt.title(str(iteration))
	plt.show()
	if max([(sum((nouveaux_centroides.iloc[i]-centroides.iloc[i])**2))**0.5 for i in range(N)]) < epsilon:
		break
	iteration += 1
	centroides = nouveaux_centroides.copy() #actualisation des centroides