import scipy.io
import numpy as np
import pandas as pd
# Load the .mat file
file_path = 'E:\Coding\Python-1\Machine Learning\\File.mat'
mat_data = scipy.io.loadmat(file_path)
for key, value in mat_data.items():
    if not key.startswith('__'):
        if isinstance(value, (np.ndarray, pd.DataFrame)):
            # Convert numpy array to pandas DataFrame if necessary
            if isinstance(value, np.ndarray):
                df = pd.DataFrame(value)
            else:
                df = value
            
            # Save the DataFrame to a CSV file
            csv_file = f"{key}.csv"
            df.to_csv(csv_file, index=False)
            print(f"Saved {key} to {csv_file}")
        else:
            print(f"Variable '{key}' is not a 2D array or DataFrame.")