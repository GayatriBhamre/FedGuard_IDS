import flwr as fl
import numpy as np
import tensorflow as tf

def get_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_shape,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile("adam", "binary_crossentropy", metrics=["accuracy"])
    return model

def load_client_data(index):
    data = np.load(f"data/clients/client_{index}.npz")
    return data['X'], data['y']

def main(client_idx):
    X_train, y_train = load_client_data(client_idx)
    model = get_model(X_train.shape[1])

    class FlowerClient(fl.client.NumPyClient):
        def get_parameters(self, config): return model.get_weights()
        def fit(self, parameters, config):
            model.set_weights(parameters)
            model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=0)
            return model.get_weights(), len(X_train), {}
        def evaluate(self, parameters, config):
            model.set_weights(parameters)
            loss, acc = model.evaluate(X_train, y_train, verbose=0)
            return loss, len(X_train), {"accuracy": acc}

    fl.client.start_numpy_client(server_address="127.0.0.1:8080", client=FlowerClient())

if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))
