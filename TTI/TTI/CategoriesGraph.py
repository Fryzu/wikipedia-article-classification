import networkx as nx
import pandas as pd
import os

base_path = os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))
CATEGORIES_PATH = os.path.join(
    base_path, "data", "wikipedia_topics_nowikidata.csv")


class SingletonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CategoriesGraph(metaclass=SingletonMetaClass):
    """
    Provides abstraction for the Categories graph.
    Its singleton importing data from data/wikipedia_topics_nowikidata.csv, creating networkx graph from it.
    """

    _graph = None
    _edge_list = None

    def __init__(self):
        print("Reading topics graph")
        topic_nodes = pd.read_csv(CATEGORIES_PATH)
        topic_graph = nx.from_pandas_edgelist(
            topic_nodes, source="category", target="subcategory")

        self._edge_list = topic_nodes
        self._graph = topic_graph

    @property
    def categories(self):
        return [i[9:] for i in self._graph.nodes]


if __name__ == "__main__":
    s1 = CategoriesGraph()
    s2 = CategoriesGraph()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    print("edges: ", s1._edge_list.shape)
    print("nodes: ", s1._graph.number_of_nodes())
