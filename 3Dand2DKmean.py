from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('clustering_2.csv')
N = 4
epsilon = 0.001
iteration = 0
centroides = df.sample(N) #pioche 4 ligens aux hasards
while iteration < 30:
	Cluster = []
	for j in range(len(df)) : #association des points aux clusters
		distances = [(sum((df.iloc[j]-centroides.iloc[i])**2))**0.5 for i in range(0,N)] #liste distances entre centre et point
		Cluster.append(distances.index(min(distances))) #quel cluster associe
	if 'z' in df.columns:
		c=[0 for i in range(4*N)]
		for k in range(len(df)) : #creation nouveau cluster
			for i in range(N) :
				if Cluster[k]== i: 
					c[4*i]+=df.iloc[k]['x'] #valeur de somme en x
					c[4*i+1]+=df.iloc[k]['y'] #valeur de somme en y
					c[4*i+2]+=df.iloc[k]['z'] #valeur de somme en z
					c[4*i+3]+=1 #nb delement dans le cluster
		nouveaux_centroides = pd.DataFrame([(c[4*k]/c[4*k+3] if c[4*k+3]>0 else centroides.iloc[k]['x'],
		c[4*k+1]/c[4*k+3] if c[4*k+3]>0 else centroides.iloc[k]['y'],c[4*k+2]/c[4*k+3] if c[4*k+3]>0 else centroides.iloc[k]['z'])for k in range(N)], columns=['x', 'y','z'])
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(df['x'], df['y'],df['z'], c=Cluster, alpha=0.5)
		ax.scatter(centroides['x'], centroides['y'],centroides['z'], c='red', s=100)
		ax.scatter(nouveaux_centroides['x'], nouveaux_centroides['y'],nouveaux_centroides['z'], c='green', s=100)
	else : 
		c=[0 for i in range(3*N)]
		for k in range(len(df)) : #creation nouveau cluster
			for i in range(N) :
				if Cluster[k]== i: 
					c[3*i]+=df.iloc[k]['x'] #valeur de somme en x
					c[3*i+1]+=df.iloc[k]['y'] #valeur de somme en y
					c[3*i+2]+=1 #nb delement dans le cluster
		nouveaux_centroides = pd.DataFrame([(c[3*k]/c[3*k+2] if c[3*k+2]>0 else centroides.iloc[k]['x'],c[3*k+1]/c[3*k+2] if c[3*k+2]>0 else centroides.iloc[k]['y'])for k in range(N)], columns=['x', 'y'])
		plt.scatter(df['x'], df['y'], c=Cluster, alpha=0.5)
		plt.scatter(centroides['x'], centroides['y'], c='red', s=100)
		plt.scatter(nouveaux_centroides['x'], nouveaux_centroides['y'], c='green', s=100)
	plt.title("iteration"+str(iteration))
	plt.show()
	if max([(sum((nouveaux_centroides.iloc[i]-centroides.iloc[i])**2))**0.5 for i in range(N)]) < epsilon:
		break
	iteration += 1
	centroides = nouveaux_centroides.copy() #actualisation des centroides