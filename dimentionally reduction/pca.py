# this file is intended to be used as a module of learning about the PCA
# algorithm. which is a dimensionality reduction algorithm that is used to
# reduce the dimensionality of a dataset using the eigenvalues and eigenvectors
# of the covariance matrix of the dataset.

# first we import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

# sklearn iris dataset
from sklearn.datasets import load_iris
# load the iris dataset
iris = load_iris()
# create a dataframe from the iris dataset
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# add the target column
df['target'] = iris.target
# print the dataframe
print(df)

# first we create a PCA object
pca = PCA(n_components=2)
# fit the PCA object to the dataframe
pca.fit(df)
# transform the dataframe
df_pca = pca.transform(df)
# print the transformed dataframe
print(df_pca)

# here we can see that the first two columns are the principal components
# of the dataframe. the first column is the principal component that
# explains the most variance in the dataframe. the second column is the
# principal component that explains the second most variance in the dataframe.
# this could be used to plot the dataframe in 2 dimensions. and see any patterns



