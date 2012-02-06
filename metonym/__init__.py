MAX_LENGTH = 100
import networkx as nx
class WordNetGraph(object):
    def __init__(self, graphfile):
        self.graph = nx.read_adjlist(graphfile)

    def shortest_path_distance(self, synset1, synset2):
        try:
            return nx.shortest_path_length(self.graph, synset1.name, synset2.name)
        except nx.NetworkXNoPath:
            return None

    def path_similarity(self, synset1, synset2) :
        distance = self.shortest_path_distance(synset1, synset2)
        if distance is None:
            distance = MAX_LENGTH
        if distance == 0:
            return 1
        else:
            return (1.0/distance)
