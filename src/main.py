from components.Network import *
from typing import List

def pretty_print_ping(node_from:str, node_to:str, nodes, count:int):
    """Print in a prettier way the output from network print command"""
    to_print = f"ping from {node_from} to {node_to}, " + " -> ".join(nodes) + f", count: {count}"
    print(to_print)


def main():
    """
    Main function, create the networks, add the nodes, create the edges, print the routing tables and print ping output
    """
    network = Network()
    
    for node_id in ['A', 'B', 'C', 'D','E','F','G','H','I']:
        network.add_node(node_id)
    
    network.add_edge('A', 'B', 5)
    network.add_edge('A', 'H', 60)
    network.add_edge('B', 'C', 2)
    network.add_edge('C', 'D', 3)
    network.add_edge('D', 'A', 10)
    network.add_edge('D', 'I', 30)
    network.add_edge('C', 'E', 20)
    network.add_edge('E', 'F', 20)
    network.add_edge('F', 'G', 5)
    network.add_edge('G', 'H', 7)
    network.add_edge('H', 'I', 9)
    network.add_edge('I', 'F', 3)
    
    iterations = network.run_network()
    print(f"\nConvergenza raggiunta in {iterations} iterazioni")
    
    routing_table = network.get_routing_tables_formatted()
    print(routing_table)

    nodes, cost = network.ping("A", "H")
    pretty_print_ping("A", "H", nodes, cost)

if __name__ == "__main__":
    main()