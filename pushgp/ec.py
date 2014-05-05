from future.builtins import super

import inspyred.ec.ec
import inspyred.ec.variators
import inspyred.ec.replacers
from . import bounders


class PushGP(inspyred.ec.ec.EvolutionaryComputation):
    '''Evoluiontary computation representing genetic programming using Push


    Optional keyword arguments in ``evolve``:

    - *pop_size* -- the number of individuals to be created
    - *mutation_rate* -- the rate at which mutation is performed (default 0.1)
    - *crossover_rate* -- the rate at which crossover is performed
      (default 1.0)

    - *push_max_size* -- the maximum number of instructions in a Push
      program (default 500)
    - *push_instructions* -- a list of possible push intructions to use
    (default [])
    '''

    def __init__(self, random):
        super().__init__(self, random)
        self.bounder = bounders.ArbitraryBounder()
        self.variator = [
            inspyred.ec.variators.n_point_crossover,
            inspyred.ec.variators.random_reset_mutation,
        ]
        self.replacer = inspyred.ec.replacers.generational_replacement

    def evolve(self, *args, **kwargs):

        kwargs.setdefault('pop_size', 100)
        kwargs.setdefault('num_selected', kwargs['pop_size'])

        kwargs.setdefault('push_max_size', 500)
        kwargs.setdefault('push_instructions', [])

        self.bounder = bounders.LengthBounder(
            values=kwargs['push_max_size']
        )
        super().evolve(*args, **kwargs)
