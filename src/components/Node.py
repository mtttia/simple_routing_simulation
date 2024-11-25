from typing import Dict
import copy

class Node:
    """
    A Node in a Network with his own routing table .
    
    Attributes:
        node_id (str): Unique node identifier
        routing_table (Dict): updated routing table with destination node, cost, and next hop
        neighbors (Dict): Dictionary of neighbors with relative edge cost
    """
    
    def __init__(self, node_id: str):
        """
        Initialize a new node.
        
        Args:
            node_id (str): Node unique identifier
        """
        self.node_id = node_id
        self.routing_table = {node_id: (0, node_id)}  # (cost, next_hop)
        self.neighbors = {}

    def add_neighbor(self, neighbor_id: str, cost: int):
        """
        Add new edge with neighbor unique ID and edge cost .
        
        Args:
            neighbor_id (str): neighbor unique ID 
            cost (int): edge cost
        """
        self.neighbors[neighbor_id] = cost
        self.routing_table[neighbor_id] = (cost, neighbor_id)

    def update_routing_table(self, sender_id: str, received_table: Dict) -> bool:
        """
        Receive neighbor routing table, update self routing table cost.
        
        Args:
            sender_id (str): routing table node unique ID
            received_table (Dict): neighbor routing table
            
        Returns:
            bool: True if changes has been made, False otherwise
        """
        changed = False
        if sender_id not in self.neighbors:
            return False
        cost_to_sender = self.neighbors[sender_id]

        for dest, (dest_cost, _) in received_table.items():
            new_cost = cost_to_sender + dest_cost
            
            if (dest not in self.routing_table or 
                new_cost < self.routing_table[dest][0]):
                self.routing_table[dest] = (new_cost, sender_id)
                changed = True
                
        return changed

    def get_routing_info(self) -> Dict:
        """
        Return a defensive copy of the self routing table .
        
        Returns:
            Dict: self routing table
        """
        return copy.deepcopy(self.routing_table)