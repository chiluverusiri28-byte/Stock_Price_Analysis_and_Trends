# Stock Price Analysis and Prediction

# Install libraries before running:
# pip install pandas numpy matplotlib scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
# Replace with your dataset file name
df = pd.read_csv(r"C:\Users\renu\OneDrive\Desktop\stock price analysis and trends\TATAMOTORS.csv")
# Show first 5 rows
print(df.head())

# Convert Date column
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df.ffill(inplace=True)

# Plot Closing Price Trend
plt.figure(figsize=(12,6))
plt.plot(df['Close'])
plt.title("Stock Closing Price Trend")
plt.xlabel("Days")
plt.ylabel("Closing Price")
plt.show()

# Features and Target
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Error
mse = mean_squared_error(y_test, predictions)

print("\nMean Squared Error:", mse)

# Compare Actual vs Predicted
comparison = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions
})

print("\nActual vs Predicted:")
print(comparison.head())

# Plot Predictions
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label='Actual')
plt.plot(predictions, label='Predicted')
plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Samples")
plt.ylabel("Price")
plt.legend()
plt.show()

# Future Prediction Example
sample_data = [[150, 155, 148, 3000000]]

future_price = model.predict(sample_data)

print("\nPredicted Future Price:", future_price[0])

plt.show(block=True)