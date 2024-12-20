import pickle

def deserialize_data(data):
    return pickle.loads(data)  # Vulnerable to insecure deserialization
