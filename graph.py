class Node:
    node_count = 0
    index_look_up_dict = {}
    
    @staticmethod
    def reset():
        Node.node_count = 0
        Node.index_look_up_dict = {}
    
    def __init__(self, paper_id, paper_name):
        self.node_index = Node.node_count
        self.paper_id = paper_id
        self.paper_name = paper_name
        Node.node_count += 1
        self.rank = 0
        self.out_edges = []
        self.in_edges = []
        Node.index_look_up_dict[paper_id] = self.node_index
        
    
    def add_edge(self, edge, out=True):
        if out:
            self.out_edges.append(edge)
        else:
            self.in_edges.append(edge)


class Edge:
    edge_count = 0
    
    @staticmethod
    def reset():
        Edge.edge_count = 0
    
    def __init__(self, node_from: Node, node_to: Node):
        self.node_from = node_from
        self.node_to = node_to
        self.weight = 0
        self.edge_index = Edge.edge_count
        Edge.edge_count += 1
        
        node_from.add_edge(edge=self, out=True)
        node_to.add_edge(edge=self, out=False)
    
class Graph:
    
    def __init__(self):
        self.node_list = []
        self.edge_list = []
        Node.reset()
        Edge.reset()
    
    def create_node(self, paper_id, paper_name):
        
        '''
        creates new node on the graph, does not check if the node already exists or not
        
        paper_id: arxiv id of the paper,
        paper_name: name of the paper
        
        returns the created node
        '''
        node = Node(paper_id, paper_name)
        self.node_list.append(node)
        return node
    
    def add_edge(self, from_paper_id, to_paper_id):
        '''
        add edge from one paper to another
        indicates that one paper is reference of another paper
        
        from_paper_id: the id of the original paper
        to_paper_id: id of the reference paper
        
        
        returns the edge
        '''
        
        from_node_index = Node.index_look_up_dict[from_paper_id]
        to_node_index = Node.index_look_up_dict[to_paper_id]
        
        to_node = self.node_list[to_node_index]
        from_node = self.node_list[from_node_index]
        
        edge = Edge(from_node, to_node)
        self.edge_list.append(edge)
        return edge
    
    def print_edges(self):
        for edge in self.edge_list:
            print(f"from: {edge.node_from.node_index}, to: {edge.node_to.node_index}")
            
    def assign_ranks(self, ranks):
        for index, rank in enumerate(ranks):
            self.node_list[index].rank = rank
    
    def get_nodes(self, sorted=True, ascending=True):
        
        temp = []
        
        for node in self.node_list:
            temp.append([node.paper_id, node.paper_name, node.rank])
            
        temp.sort(key=lambda x: x[2], reverse=not ascending)
        
        return temp
    
    def get_node_rank(self, paper_id):
        paper_index = Node.index_look_up_dict[paper_id]
        
        node = self.node_list[paper_index]
        return [node.paper_id, node.paper_name, node.rank]
        
            