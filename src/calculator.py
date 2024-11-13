import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_array = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            np.mean(np_array, axis=0).tolist(),
            np.mean(np_array, axis=1).tolist(),
            np.mean(np_array).tolist()
        ],
        'variance': [
            np.var(np_array, axis=0).tolist(),
            np.var(np_array, axis=1).tolist(),
            np.var(np_array).tolist()
        ],
        'standard deviation': [
            np.std(np_array, axis=0).tolist(),
            np.std(np_array, axis=1).tolist(),
            np.std(np_array).tolist()
        ],
        'max': [
            np.max(np_array, axis=0).tolist(),
            np.max(np_array, axis=1).tolist(),
            np.max(np_array).tolist()
        ],
        'min': [
            np.min(np_array, axis=0).tolist(),
            np.min(np_array, axis=1).tolist(),
            np.min(np_array).tolist()
        ],
        'sum': [
            np.sum(np_array, axis=0).tolist(),
            np.sum(np_array, axis=1).tolist(),
            np.sum(np_array).tolist()
        ]
    }

    return calculations
