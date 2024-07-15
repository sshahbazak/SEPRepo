# import pandas as pd
# import numpy as np
# import gower as gwr
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# from mpl_toolkits import mplot3d
# from sklearn.metrics import silhouette_score
# from sklearn.manifold import TSNE

# # define variable for data & have panda read using file path

df = pd.read_csv(r"C:\Users\Porte\Desktop\notredame_files\L1_TESTS_FINAL_SUBMISSION.csv")
# X = data.throttle
# y = data.mission_complete
# # displays the first 5 lines of the data

# print(data.head())

# # prints the number of records, and fields

# print(data.shape)

# # summary of the structure of the data

# print(data.info())

# # sorting data by mission_complete

# print(data.sort_values(by=['mission_complete'], inplace = False, ascending = True))

# # count all not null data values

# print(pd.notnull(data).sum())

# #

# print(data.sort_values(by=['throttle'], inplace = False, ascending = True))

# #

# print(data.sort_values(by=['Wind'], inplace = False, ascending = True))

# #

# print(data.sort_values(by=['GFPRED'], inplace = False, ascending = True))

# #

# print(data.sort_values(by=['GFACT'], inplace = False, ascending = True))

# # changing the format of columns

# data['NAME'] = data['NAME'].astype('TYPE')

# data['NAME'] = data['NAME'].astype('TYPE')

# # Create a new column, correcting the year

# data['releasedyyyy'] = data['released'].str.extract(pat='([0-9]{4})').astype(int)

# # Drop duplicates shows all mode types used

# print(data['Mode'].drop_duplicates().sort_values(ascending = False))

# #does not work

# print(data.corr(method = 'pearson'))

# #does not work

# pd.set_option('display.max_rows', None)
# cor_mat = data.corr()
# correlations = cor_mat.unstack()
# correlations = correlations.sort_values()
# correlations.head()

# # information about unnamed, throttle, max_deviation, & max_altitude

# print(data.describe())

# #shows unique values for throttle

# print(data['throttle'].unique())

# #replace missing data with True

# data.fillna(value='None', inplace=True)

# #

# data['Wind'] = data['Wind'].apply(lambda x: 1 if x is not None else 0)

# #

# data['duration'] = pd.to_timedelta(data['duration']).dt.total_seconds()

# #shows all unique values of each column

# unique_values = data.apply(lambda x: x.unique())
# print(unique_values)

# #

# print(data)

# #does not work

# print(data.groupby('y').mean())

# #does not work

# print(data.groupby('throttle').mean())

# #not sure this did what I wanted

# data1 = data.copy()
# data11 = pd.get_dummies(data1, columns=['throttle','GF','GFACT','GFPRED'])
# print(data11)

# #find how to display columns not shown in the middle

# #find how to change NaN to 0

# #find how to change No to False and Yes to True

# #find how to change data types

# #find how to fill nulls

# #find how to find and delete duplicate records

# #find how to change MSN State column name to MSN_State

# #ask aout GFPRED_NO & GFPRED_YES being opposites?

# #

# data = np.random.rand(100,3)

# # scatter plot (throttle vs max_deviation)

# plt.scatter(x=data['throttle'], y =data['max_deviation'])
# plt.title('throttle vs max_deviation')
# plt.xlabel('throttle')
# plt.ylabel('mission_complete')
# print(plt.show())

# # Load the Iris dataset (Don't know if i need this)
# iris = load_iris()
# X = iris.data
# y = iris.target

# ## Create a DataFrame
# data = pd.DataFrame(X, columns=data.feature_names)
# data['mission_complete'] = y

# ## Explore the data
# sns.pairplot(data, hue='mission_complete')
# plt.show()

# ## Apply K-means clustering
# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(X)
# clusters = kmeans.predict(X)
# data['cluster'] = clusters

# ## Visualize the clusters
# plt.figure(figsize=(10, 6))
# plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=clusters, cmap='viridis', marker='o')
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='x')
# plt.xlabel(iris.feature_names[0])
# plt.ylabel(iris.feature_names[1])
# plt.title('K-means Clustering on Iris Dataset')
# plt.show()

# ## Evaluate the clustering
# ct = pd.crosstab(df['species'], df['cluster'])
# print(ct)

# accuracy = np.sum(np.max(ct.values, axis=1)) / np.sum(ct.values)
# print(f'Clustering Accuracy: {accuracy * 100:.2f}%')

# #

# #

# #New Code


# #2D RENDERING OF K-MEANS CLUSTERS:

# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the Iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Create a DataFrame
# df = pd.DataFrame(X, columns=iris.feature_names)
# df['species'] = y

# # Explore the data
# sns.pairplot(df, hue='species')
# plt.show()

# # Apply K-means clustering
# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(X)
# clusters = kmeans.predict(X)
# df['cluster'] = clusters

# # Visualize the clusters
# plt.figure(figsize=(10, 6))
# plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=clusters, cmap='viridis', marker='o')
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='x')
# plt.xlabel(iris.feature_names[0])
# plt.ylabel(iris.feature_names[1])
# plt.title('K-means Clustering on Iris Dataset')
# plt.show()

# # Evaluate the clustering
# ct = pd.crosstab(df['species'], df['cluster'])
# print(ct)

# accuracy = np.sum(np.max(ct.values, axis=1)) / np.sum(ct.values)
# print(f'Clustering Accuracy: {accuracy * 100:.2f}%')



# #3D RENDERING OF K-MEANS CLUSTERS:

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
# from sklearn.cluster import KMeans

# # Create a 3D dataset
# data = np.random.rand(100, 3)

# # Fit a KMeans model to the data
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(data)

# # Get the cluster labels
# labels = kmeans.labels_

# # Create a 3D scatter plot of the data, colored by cluster
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=labels)

# # Plot the cluster centers
# ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], c='red', marker='x')

# # Show the plot
# plt.show()

# # Compute the Gower distance matrix
# gower_dist = gwr.gower_matrix(data)

# #Elbow Approach

# # Function to calculate KMeans inertia on the Gower distance matrix
# def calculate_inertia(dist_matrix, max_k):
#     inertias = []
#     for k in range(1, max_k + 1):
#         kmeans = KMeans(n_clusters=k, random_state=0)
#         kmeans.fit(dist_matrix)
#         inertias.append(kmeans.inertia_)
#     return inertias

# # Determine the optimal number of clusters using the elbow method
# max_k = 10
# inertias = calculate_inertia(gower_dist, max_k)

# # Plot the elbow graph
# plt.figure(figsize=(8, 6))
# plt.plot(range(1, max_k + 1), inertias, marker='o')
# plt.xlabel('Number of clusters (k)')
# plt.ylabel('Inertia')
# plt.title('Elbow Method For Optimal k')
# plt.xticks(range(1, max_k + 1))
# plt.grid(True)
# print(plt.show())

# #
# data.fillna(0)

import numpy as np
import pandas as pd
import gower
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE

unique_values = df.apply(lambda x: x.unique())
print(unique_values)

df['throttle'].unique()

df.fillna(value='None', inplace=True)

df['Wind'] = df['Wind'].apply(lambda x: 1 if x is not None else 0)

df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds()

