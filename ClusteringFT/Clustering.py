import numpy as np
import pandas as pd
import gower
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
import os

def Clustering():
    DATA_FILE = 'ClusteringFT/L1_TESTS_FINAL_SUBMISSION.csv'

    df = pd.read_csv(DATA_FILE)

    df.fillna(value='None', inplace=True)

    df['Wind'] = df['Wind'].apply(lambda x: 1 if x is not None else 0)

    df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds()

    df = df.drop(columns='Unnamed: 0')
    # df.columns

    # Convert 'throttle' column to string type
    # df['throttle'] = df['throttle'].astype(str)

    # Fill NaN values with 'None'
    df['throttle'] = df['throttle'].fillna('None')

    df = df.rename(columns={'MSN State': 'states'})

    df = df.rename(columns={'mode_switch': 'modes'})

    df = df.rename(columns={'Mode': 'initial_mode'})

    # df.fillna(value='None', inplace=True)

    # df['Wind'] = df['Wind'].apply(lambda x: 1 if x is not None else 0)

    # df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds()

    # df = df.drop('Unnamed: 0', axis=1)
    gower_dist = gower.gower_matrix(df)

    #Applying the optimal k value to perform k-means clustering

    # Compute the Gower distance matrix
    gower_dist = gower.gower_matrix(df)

    # Perform KMeans clustering
    # Number of clusters (k) - choose appropriate value
    k = 3
    kmeans = KMeans(n_clusters=k, random_state=0)

    # Fit the model on the Gower distance matrix
    kmeans.fit(gower_dist)

    # Get cluster labels
    labels = kmeans.labels_


    df_with_clusters = df.copy()
    df_with_clusters['cluster'] = labels


    # df_with_clusters

    # Calculate centroid coordinates
    centroids = kmeans.cluster_centers_

    # Initialize a list to store closest points to centroids
    closest_points_to_centroids = []

    # Find closest points to each centroid
    for i, centroid in enumerate(centroids):
        # Calculate distances from each point to the centroid
        distances_to_centroid = gower_dist[:, i]
        # Find the index of the closest point
        closest_index = np.argmin(distances_to_centroid)
        # Get the point and its distance
        closest_point = df.iloc[closest_index]
        distance_to_centroid = distances_to_centroid[closest_index]
        # Append to list
        closest_points_to_centroids.append(closest_point)

    # Convert the list of dictionaries to a DataFrame
    closest_points_to_centroids_df = pd.DataFrame(closest_points_to_centroids)
    

    # Visualization with Grower and KMeans clustering

    # # Compute the Gower distance matrix
    # gower_dist = gower.gower_matrix(df)

    # # Perform KMeans clustering
    # k = 3
    # kmeans = KMeans(n_clusters=k, random_state=0)
    # kmeans.fit(gower_dist)

    # # Get cluster labels
    # labels = kmeans.labels_

    # # Apply t-SNE for dimensionality reduction
    # tsne = TSNE(n_components=2, random_state=0)
    # X_tsne = tsne.fit_transform(gower_dist)

    # # Visualize clusters
    # plt.figure(figsize=(8, 6))
    # for i in range(k):
    #     plt.scatter(X_tsne[labels == i, 0], X_tsne[labels == i, 1], label=f'Cluster {i}')
    # plt.title('t-SNE Visualization of Clusters')
    # plt.xlabel('t-SNE Component 1')
    # plt.ylabel('t-SNE Component 2')
    # plt.legend()
    # plt.show()

    return closest_points_to_centroids_df

if __name__ == '__main__':
    print(Clustering())
