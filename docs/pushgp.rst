.. module:: pushgp

:mod:`pushgp`
---------------

PushGP is really a collection of various interlocking piece, enabling
you to run symbolic regression using the Push programming language.

At the most high level is :py:class:`pushgp.estimators.PushGPRegression`, built on
scikit-learn. This allows you to use genetic programming in your machine
learning toolchain, as you would any other technique, such as linear regression.

Then there is :py:class:`pushgp.ec.ec.PushGP` which performs the actual evolution
of Push programs. This is implemented as an evolutionary computation
engine for Inspyred.

That module, in turn, makes use of :py:class:`pushgp.push.interpreter.Push`,
which handles all of the language logic.

Right now, the only part to be fully implemented and test is
the :py:class:`~pushgp.push.interpreter.Push` interpreter.

.. toctree::
   :maxdepth: 3

   estimators
   ec
   push
