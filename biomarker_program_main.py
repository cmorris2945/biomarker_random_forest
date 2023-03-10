# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('data.csv')

# Split the data into training and testing sets
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train the random forest model
classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, y_train)

# Test the model and calculate feature importance scores
importances = classifier.feature_importances_
y_pred = classifier.predict(X_test)

# Sort genes by importance score and select top N genes as potential biomarkers
gene_names = list(data.columns)[1:-1]
sorted_genes = sorted(zip(importances, gene_names), reverse=True)
top_N_genes = [gene[1] for gene in sorted_genes[:10]]

print(top_N_genes)
