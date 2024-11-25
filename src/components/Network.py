from typing import Dict
import copy
from components.Node import *

class Network:
    """
    A simulated network with a list of Nodes.
    
    Attributes:
        nodes (Dict): The network nodes
    """
    
    def __init__(self):
        """Initialize a new empty Network."""
        self.nodes = {}

    def add_node(self, node_id: str):
        """
        Add a node in the net (using node unique ID).
        
        Args:
            node_id (str): new node unique ID
        """
        self.nodes[node_id] = Node(node_id)

    def add_edge(self, first_node_id: str, second_node_id: str, cost: int):
        """
        Add an edge between two nodes.
        
        Args:
            node1_id (str): First node unique ID
            node2_id (str): Second node unique ID
            cost (int): Edge cost
        """
        self.nodes[first_node_id].add_neighbor(second_node_id, cost)
        self.nodes[second_node_id].add_neighbor(first_node_id, cost)
        

    def run_network(self, max_iterations: int = 100) -> int:
        """
        Simulate the start of the network where all the nodes try to exchange their routing table since convergence
        
        Args:
            max_iterations (int): Max table exchange number
            
        Returns:
            int: Number of exchange required for make the net routing table exchange process to converge
        """
        iteration = 0
        changes = True
        
        while changes and iteration < max_iterations:
            changes = False
            iteration += 1
            
            for node in self.nodes.values():
                for neighbor_id in node.neighbors:
                    if self.nodes[neighbor_id].update_routing_table(
                        node.node_id, node.get_routing_info()
                    ):
                        changes = True
                        
        return iteration

    def get_routing_tables_formatted(self):
        """Return each node routing table as a string in a human readable format"""
        return_string = ""
        for node_id, node in self.nodes.items():
            return_string = return_string + f"\nTabella di routing per il nodo {node_id}:\n"
            return_string = return_string + "Destinazione | Costo | Next Hop\n"
            return_string = return_string +"-" * 35 + "\n"
            for dest, (cost, next_hop) in sorted(node.routing_table.items()):
                return_string = return_string + f"{dest:^12} | {cost:^5} | {next_hop:^8}\n"
        return return_string
    
    def ping(self, from_node_id: str, to_node_id: str):
        """
        Simulate a ping
        
        Args:
            from_node_id (str): the starting ping node 
            to_node_id (str): the destination ping node 
            
        Returns:
            str[]: the list of node that ping pass
            int: the cost of the passed edge
        """

        current_node = from_node_id
        passed_nodes = []
        cost = 0
        
        while current_node is not to_node_id:
            passed_nodes.append(current_node)
            if to_node_id in self.nodes[current_node].routing_table:
                last_current_node = current_node
                current_node = self.nodes[current_node].routing_table[to_node_id][1]
                cost = cost + self.nodes[last_current_node].routing_table[current_node][0]
            else:
                return []
            
        if current_node == to_node_id:
            passed_nodes.append(current_node)
        
        return passed_nodes, cost

    