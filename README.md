# LoRaSim

## About
**LoRaSim** simulates LoRa traffic by means of Markov Chains as models. These models are readily available in the simulator, but the collection is expandable by the user. Different models can be interleaved for different time intervals in order to observe the effect of interference or of a change in the transceiver settings.

![LoRaSim LoRa Simulator](img/home.png)

The result of the simulation is a plot showing how the delivery probability of a packet changes over time.

![LoRaSim LoRa Simulator](img/plot_1.png)

## Installation
1) Clone the repo and `cd` into it
2) Run `pip install -e .`
3) Launch the simulator with the `LoRaSim` command
