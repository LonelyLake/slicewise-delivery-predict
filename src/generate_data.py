import pandas as pd
import numpy as np
from pathlib import Path
from loguru import logger

def generate_pizza_data(n_orders=10000):
    logger.info(f"Generating {n_orders} orders for SliceWise Dynamics...")
    
    np.random.seed(42)
    
    data = pd.DataFrame({
        'order_id': range(1, n_orders + 1),
        'distance_km': np.random.uniform(0.5, 10.0, n_orders),
        'pizza_count': np.random.randint(1, 6, n_orders),
        'courier_experience_orders': np.random.randint(1, 500, n_orders),
        'hour': np.random.randint(10, 23, n_orders),
        'day_of_week': np.random.randint(0, 7, n_orders),
        'is_rainy': np.random.choice([0, 1], n_orders, p=[0.8, 0.2])
    })

    # Delivery time logic
    base_time = 12 + (data['distance_km'] * 4.5)
    traffic_effect = np.where((data['hour'] >= 17) & (data['hour'] <= 19), 12, 0)
    rain_effect = data['is_rainy'] * 8
    exp_effect = -(data['courier_experience_orders'] / 60)
    
    noise = np.random.normal(0, 2.5, n_orders)
    data['delivery_time_min'] = base_time + traffic_effect + rain_effect + exp_effect + noise
    data['delivery_time_min'] = data['delivery_time_min'].clip(lower=15).round(1)

    # Save path (using Path for Windows)
    output_path = Path("data/raw/delivery_history.csv")
    data.to_csv(output_path, index=False)
    
    logger.success(f"Data successfully created: {output_path}")

if __name__ == "__main__":
    generate_pizza_data()
    