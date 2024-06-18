import pandas as pd

# df = pd.read_csv('L1_TESTS_FINAL_SUBMISSION.csv')

# unique_values = df.apply(lambda x: x.unique())
# print(unique_values)

# df['throttle'].unique()

# df.fillna(value='None', inplace=True)

# df['Wind'] = df['Wind'].apply(lambda x: 1 if x is not None else 0)

# df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds()

# df = df.drop(columns='Unnamed: 0')
# # df.columns

# # Convert 'throttle' column to string type
# df['throttle'] = df['throttle'].astype(str)

# # Fill NaN values with 'None'
# df['throttle'] = df['throttle'].fillna('None')

# df = df.rename(columns={'MSN State': 'states'})

# df = df.rename(columns={'mode_switch': 'modes'})

# df = df.rename(columns={'Mode': 'initial_mode'})

# df.columns

# df.to_csv('test.csv', index=False)

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# # Sample DataFrame creation
# data = {
#     'Wind': np.random.rand(100),
#     'throttle': np.random.rand(100),
#     'max_deviation': np.random.rand(100),
#     'max_altitude': np.random.rand(100),
#     'duration': np.random.rand(100),
#     'category1': np.random.choice(['A', 'B', 'C'], 100),
#     'category2': np.random.choice(['X', 'Y', 'Z'], 100)
# }

# df = pd.DataFrame(data)

# Define the numerical and categorical columns

df = pd.read_csv('sample.csv')
numerical_cols = ['Wind', 'max_deviation', 'max_altitude', 'duration']
categorical_cols = [col for col in df.columns if col not in numerical_cols]

# One-hot encode categorical variables
encoder = OneHotEncoder()
encoded_categorical = encoder.fit_transform(df[categorical_cols]).toarray()

# Create a DataFrame from the encoded categorical variables
encoded_categorical_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_cols))

# Combine numerical and encoded categorical columns
df_combined = pd.concat([df[numerical_cols], encoded_categorical_df], axis=1)

# Fit Isolation Forest model for anomaly detection
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(df_combined)

# Predict anomalies
y_pred = clf.predict(df_combined)

# Get anomaly scores
anomaly_scores = clf.decision_function(df_combined)

# Add anomaly scores and predictions to the DataFrame
df['anomaly_score'] = anomaly_scores
df['anomaly'] = y_pred

# Visualize the results using t-SNE
tsne = TSNE(n_components=2, random_state=42)
tsne_results = tsne.fit_transform(df_combined)

# Add t-SNE results to the DataFrame
df['tsne_1'] = tsne_results[:, 0]
df['tsne_2'] = tsne_results[:, 1]

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(df.loc[df['anomaly'] == 1, 'tsne_1'], df.loc[df['anomaly'] == 1, 'tsne_2'], c='b', label='Normal points')
plt.scatter(df.loc[df['anomaly'] == -1, 'tsne_1'], df.loc[df['anomaly'] == -1, 'tsne_2'], c='r', label='Anomalies')
plt.title('Isolation Forest: Anomaly Detection with t-SNE Visualization')
plt.xlabel('t-SNE Feature 1')
plt.ylabel('t-SNE Feature 2')
plt.legend()
plt.show()

# Display random sample of rows with their anomaly scores
sampled_rows = df.sample(n=5, random_state=42)
print(sampled_rows)


