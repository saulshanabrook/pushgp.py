import operator
import math
import random
import functools

import numpy as np

import matplotlib.pyplot as plt

from sklearn.base import BaseEstimator

from . import genetic


class PushGPEstimator(BaseEstimator):

    def __init__(self, pop_size=100):
        self.pop_size = pop_size

    def fit(self, X, y, n_iter=10):

        pop = self.toolbox(X, y).population(n=self.pop_size)
        hof = tools.HallOfFame(1)

        pop = algorithms.eaSimple(
            population=pop,
            toolbox=self.toolbox(X, y),
            cxpb=0.5,
            mutpb=0.1,
            ngen=n_iter,
            halloffame=hof,
            verbose=False)

        self._best_ind = hof[0]

        return self

    def predict(self, X):
        return numpy.vectorize(self.compile(self._best_ind))(X)

    def visualize(self, individual):
        # Won't work in Python 3
        nodes, edges, labels = gp.graph(individual)
        g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        pos = nx.graphviz_layout(g, prog="dot")

        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_edges(g, pos)
        nx.draw_networkx_labels(g, pos, labels)
        plt.show()
