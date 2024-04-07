import pandas as pd
import joblib

# Load the trained classifier from file
loaded_rf_classifier = joblib.load('random_forest_classifier.joblib')

# New data with multiple inputs
data = {'TIME_DIFF': [0.000001, 0.0000001,0.03],'Length': [114, 114,60]}

# Convert data to DataFrame
new_data_df = pd.DataFrame(data)

# Convert categorical features to numerical using one-hot encoding
new_data_df = pd.get_dummies(new_data_df)

# Get the feature names after one-hot encoding
new_data_features = new_data_df.columns

# Load feature names used during training (assuming they were saved previously)
# Replace 'feature_names.pkl' with the file path used to save feature names during training
# You need to ensure that this file exists and contains the correct feature names
with open('data.pkl', 'rb') as f:
    trained_features = joblib.load(f)

# Ensure that feature names match and reorder columns if necessary
new_data_df = new_data_df.reindex(columns=trained_features, fill_value=0)

# Make predictions on new data
predictions = loaded_rf_classifier.predict(new_data_df)

# Print predictions
print("Predictions:", predictions)
