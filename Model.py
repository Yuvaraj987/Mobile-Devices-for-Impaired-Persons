import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Generate synthetic time series data
def generate_time_series(n_points):
    t = np.linspace(0, 30, n_points)
    y = 0.5 * np.sin(2 * np.pi * 0.1 * t) + np.random.normal(scale=0.1, size=n_points)
    return y

# Create dataset
n_points = 1000
time_series = generate_time_series(n_points)

# Prepare data for training
def prepare_data(time_series, n_steps):
    X, y = [], []
    for i in range(len(time_series) - n_steps):
        X.append(time_series[i:i+n_steps])
        y.append(time_series[i+n_steps])
    return np.array(X), np.array(y)

n_steps = 20
X, y = prepare_data(time_series, n_steps)

# Reshape data for LSTM input (samples, time steps, features)
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential([
    LSTM(20, activation='relu', input_shape=(n_steps, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, y, epochs=20, verbose=1)

# Generate predictions
predicted_values = []
input_sequence = time_series[:n_steps].reshape((1, n_steps, 1))

for _ in range(n_points - n_steps):
    predicted_value = model.predict(input_sequence, verbose=0)[0, 0]
    predicted_values.append(predicted_value)
    input_sequence = np.concatenate([input_sequence[:, 1:, :], [[predicted_value]]])

# Plot results
plt.plot(np.arange(len(time_series)), time_series, label='True Time Series')
plt.plot(np.arange(n_steps, n_points), predicted_values, label='Predicted Time Series', linestyle='--')
plt.legend()
plt.show()