# Base class
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"

# Creating an instance of Network_5G_Airtel
network_object = Network_5G_Airtel()

# Inherited from Network class
print(network_object.connectivity())

# Inherited from Network_5G class
print(network_object.fast_connectivity())

# Inherited from Network_5G_Airtel class
print(network_object.fast_and_stable_connectivity())
