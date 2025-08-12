import flwr as fl

def start_server():
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=1.0,
        min_fit_clients=4,
        min_available_clients=4,
        on_fit_config_fn=lambda rnd: {"rnd": rnd},
    )
    fl.server.start_server(server_address="127.0.0.1:8080", strategy=strategy)

if __name__ == "__main__":
    start_server()
