# 📈 Stock Price Analysis and Trends

## 📌 Overview

This project analyzes historical stock market data and predicts future stock closing prices using Machine Learning.

The model is built using Linear Regression and provides insights into stock price trends through data visualization and prediction techniques.

---

## 🚀 Features

- Load and preprocess stock market data
- Handle missing values
- Visualize stock closing price trends
- Train a Linear Regression model
- Predict stock closing prices
- Compare actual vs predicted prices
- Calculate Mean Squared Error (MSE)
- Predict future stock prices using sample input data

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## 📂 Dataset

The dataset should contain the following columns:

| Column |
|----------|
| Date |
| Open |
| High |
| Low |
| Close |
| Volume |

Example dataset:

```
TATAMOTORS.csv
```

---

## 📦 Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## ▶️ Running the Project

1. Open integrated Terminal

```bash
PS C:\Users\renu\OneDrive\Desktop\stock price analysis and trends>
```

2. Navigate to the project folder

```bash
cd Stock-Price-Analysis
```

3. Run the Python script

```bash
python Stock analysis.py
```

---

## 📊 Workflow

### Data Preprocessing
- Load dataset
- Convert Date column into datetime format
- Sort data by date
- Handle missing values

### Data Visualization
- Plot stock closing price trend
- Compare actual vs predicted stock prices

### Machine Learning
- Train-Test Split
- Linear Regression Model
- Model Prediction
- Performance Evaluation

---

## 📈 Model Evaluation

The model performance is measured using Mean Squared Error (MSE).

```python
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
```

---

## 🔮 Future Stock Price Prediction

Example:

```python
sample_data = [[150, 155, 148, 3000000]]
future_price = model.predict(sample_data)
print("Predicted Future Price:", future_price[0])
```

---

##  Project Structure

```
Stock-Price-Analysis-and -Trends/
│
├── TATAMOTORS.csv
├── Stock analysis.py
├── README.md
└── requirements.txt
```

---

##  Output

- Stock Closing Price Trend Graph
- Actual vs Predicted Stock Price Graph
- Future Stock Price Prediction

---

##  Learning Outcomes

This project demonstrates:

- Data Analysis using Pandas
- Data Visualization using Matplotlib
- Machine Learning using Scikit-Learn
- Stock Market Data Analysis
- Predictive Modeling

---
##Intern id
CITS1116

