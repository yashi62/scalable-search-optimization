import joblib

# Dummy training script
# In practice, you would load a dataset, train a model, and save it
model = {"dummy": "model"}
joblib.dump(model, 'model.joblib')
print("Model saved as 'model.joblib'")
