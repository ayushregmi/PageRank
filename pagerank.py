from graph import *
import numpy as np

class PageRank:
    def __init__(self, graph: Graph):
        self.graph = graph
        
        # setting the initial rank of all the nodes to 1
        self.rank_matrix = np.ones((len(graph.node_list), 1))
        
        # getting the update relationship
        self.relationship_matrix = np.zeros((len(graph.node_list), len(graph.node_list)))
        for edge in graph.edge_list:
            i = edge.node_from.node_index
            j = edge.node_to.node_index
            self.relationship_matrix[j, i] = 1
        self.relationship_matrix = self.relationship_matrix / (self.relationship_matrix.sum(axis=0) + 0.0001)
    
    def update_rank(self, iter, d=0.85):
        self.rank_cache = []
        self.change_cache = []
        for i in range(iter):
            self.rank_cache.append(self.rank_matrix)
            self.rank_matrix = (1 - d) + d * np.matmul(self.relationship_matrix, self.rank_matrix)
            self.change_cache.append(abs((self.rank_cache[-1] - self.rank_matrix)).sum())
        
        self.change_cache = np.array(self.change_cache)
        self.rank_cache = np.array(self.rank_cache)
        self.graph.assign_ranks(self.rank_matrix)
    
    def get_nodes(self, ascending=True):
        return self.graph.get_nodes(ascending=ascending)
    
    def get_rank(self, paper_id):
        return self.graph.get_node_rank(paper_id)
        