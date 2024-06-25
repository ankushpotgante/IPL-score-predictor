import pandas as pd
import numpy as np
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedKFold, GridSearchCV
from sklearn.metrics import r2_score

# Read the data
df = pd.read_csv("preprocessed_data.csv")

# Split into train and test data
train_data = df

# Select required columns
train_data = train_data[['batting_team', 'bowling_team', 'venue', 'toss_winner', 'toss_decision', 'wickets','runs_total']]

# Split train_data into train and validation set (called as X_test, y_test)
y = train_data.pop('runs_total')
X = train_data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)


# Define column transformers to Encode categorical data
ct = ColumnTransformer([
    ('ohe', OneHotEncoder(), ['batting_team', 'bowling_team', 'venue', 'toss_decision']),
], remainder='passthrough')


# Transform Data
X_train = ct.fit_transform(X_train)


# Train model
X_train_copy, y_train_copy = X_train.copy(), y_train.copy()

sgd_reg_pipeline = Pipeline([
    ('reg', SGDRegressor(random_state=42)),
])

sgd_reg_pipeline.fit(X_train_copy, y_train_copy)

X_test_copy = X_test.copy()
X_test_copy = ct.transform(X_test_copy)
y_pred = sgd_reg_pipeline.predict(X_test_copy)

print("R2 Score:", r2_score(y_test, y_pred))
scores = cross_val_score(sgd_reg_pipeline, X_train_copy, y_train_copy, cv=5, scoring="r2")
print("Using cross validation:")
print("Minimum Score:",np.min(scores))
print("Maximum Score:",np.max(scores))
print("Average Score:", np.average(scores))

# Save model for later use
joblib.dump(sgd_reg_pipeline, "model.joblib")
joblib.dump(ct, "transformer.joblib")
