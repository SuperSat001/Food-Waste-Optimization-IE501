from sklearn.neighbors import KernelDensity
import numpy as np

demand_data = [30, 25, 28, 35, 40, 32, 27, 31]

demand_data = np.array(demand_data).reshape(-1, 1)

kde = KernelDensity(bandwidth=2.0, kernel='gaussian')
kde.fit(demand_data)

# New data for prediction (e.g., demand observed for a new Monday)
new_demand_data = np.array([27, 29, 33]).reshape(-1, 1)  # Example new demand data

log_density = kde.score_samples(new_demand_data)
density = np.exp(log_density)

most_likely_demand = new_demand_data[np.argmax(density)]
print("Predicted demand (most likely value):", most_likely_demand)
