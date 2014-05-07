import sklearn.base
import inspyred.ec

from .ec import bounders
from .push.interpreter import Push


class PushGPRegression(sklearn.base.BaseEstimator,
                       sklearn.base.ClassifierMixin):

    def __init__(
            self,
            pop_size=100,
            mutation_rate=0.1,
            crossover_rate=0.1,
            push_max_size=100,
            push_intructions=[],
            random_state=None,
            get_result=lambda Push: Push['float'][0]):
        self.random_state = random_state
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.push_max_size = push_max_size
        self.push_intructions = push_intructions
        self.get_result = get_result

    def compile_instructions(self, push_first, push_second):
        return Push()(push_first)(push_second)

    def predict(self, X):
        pass

    def error(self, candidate, feature, target):
        push_program = self.compile_instructions(
            push_first=feature,
            push_second=candidate
        )
        target_predicted = self.get_result(push_program)
        return abs(target - target_predicted)

    def evaluator(self, candidates):
        pass

    def fit(self, X, y, n_iter=10):
        self.ec_ = inspyred.ec.EvolutionaryComputation(self.random_state)
        bounder = bounders.LengthBounder(
            values=self.push_intructions,
            size_limit=self.push_max_size)
        self.ec_.variator = [
            inspyred.ec.variators.n_point_crossover,
            inspyred.ec.variators.random_reset_mutation,
        ]
        self.ec_.replacer = inspyred.ec.replacers.generational_replacement
        self.ec_.num_selected = self.pop_size
        final_pop = self.ec_.evolve(
            generator='',
            evaluator='',
            pop_size=self.pop_size,
            bounder=bounders.LengthBounder(
                values=self.push_intructions,
                size_limit=self.push_max_size
            ),
            maximize=False
        )
        final_pop.sort(reverse=True)
        self.push_program_ = final_pop[0]
        return self
