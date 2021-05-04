"""Explore Iris dataset."""
import seaborn as sns

# ======================================================================================================================
# Load data
# ======================================================================================================================
iris = sns.load_dataset("iris")
# ======================================================================================================================
# Simple exploration
# ======================================================================================================================
iris.sample(10)
iris.describe()
iris.groupby("species").describe()
# ======================================================================================================================
# Plot data
# ======================================================================================================================
sns.pairplot(iris, hue="species")
