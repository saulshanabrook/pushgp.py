import operator
import math
import random
import functools

import numpy

import matplotlib.pyplot as plt

import networkx as nx

from sklearn.base import BaseEstimator

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp


class TreeSREstimator(BaseEstimator):

    def __init__(self, pop_size=100):
        self.pop_size = pop_size

    @functools.lru_cache()
    def pset(self):
        pset = gp.PrimitiveSet("MAIN", 1)
        pset.addPrimitive(operator.add, 2)
        pset.addPrimitive(operator.sub, 2)
        pset.addPrimitive(operator.mul, 2)
        #pset.addPrimitive(numpy.divide, 2)
        pset.addPrimitive(operator.neg, 1)
        pset.addPrimitive(math.cos, 1)
        pset.addPrimitive(math.sin, 1)
        pset.addEphemeralConstant("rand1011", lambda: random.randint(-1, 1))
        pset.renameArguments(ARG0='x')
        return pset

    def creator(self):
        creator.create(
            "FitnessMin",
            base.Fitness,
            weights=(-1.0,))
        creator.create(
            "Individual",
            gp.PrimitiveTree,
            fitness=creator.FitnessMin)
        return creator

    def compile(self, individual):
        def compiled_function(inputs):
            return gp.compile(expr=individual, pset=self.pset())(*inputs)
        return compiled_function

    def tree_program_mean_error(self, individual, x_list, y_list):
        func = self.compile(individual)
        errors = numpy.vectorize(func)(x_list) - y_list
        errors_abs = numpy.absolute(errors)
        return [numpy.mean(errors_abs)]

    def toolbox(self, x_list, y_list):
        '''
        Returns a Toolbbox with the methods:
        mate, mutate, select, evaluate
        '''
        toolbox = base.Toolbox()
        toolbox.register(
            "expr",
            gp.genHalfAndHalf,
            pset=self.pset(),
            min_=1,
            max_=2)
        toolbox.register(
            "individual",
            tools.initIterate,
            self.creator().Individual,
            toolbox.expr)
        toolbox.register(
            "population",
            tools.initRepeat,
            list,
            toolbox.individual)
        toolbox.register(
            "evaluate",
            self.tree_program_mean_error,
            x_list=x_list,
            y_list=y_list)
        toolbox.register(
            "select",
            tools.selTournament,
            tournsize=3)
        toolbox.register(
            "mate",
            gp.cxOnePoint)
        toolbox.register(
            "expr_mut",
            gp.genFull,
            min_=0,
            max_=2)
        toolbox.register(
            "mutate",
            gp.mutUniform,
            expr=toolbox.expr_mut,
            pset=self.pset())
        return toolbox

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
