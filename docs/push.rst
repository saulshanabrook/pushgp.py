:mod:`pushgp.push`
---------------

    >>> from pushgp.push.interpreter import Push
    >>> from pushgp.push.instructions import bool, float, str
    >>> p = Push()
    >>> p(1.0, 3.0)
    Push: {'exec': [], 'float': [3.0, 1.0]}
    >>> p(float.div)
    Push: {'exec': [], 'float': [0.3333333333333333]}
    >>> p(True, False)
    Push: {'exec': [], 'float': [0.3333333333333333], 'bool': [False, True]}
    >>> p(bool.or_)
    Push: {'exec': [], 'float': [0.3333333333333333], 'bool': [True]}
    >>> p(bool.from_float)
    Push: {'exec': [], 'float': [], 'bool': [True, True]}


.. automodule:: pushgp.push
   :members:
   :undoc-members:

.. toctree::
   :maxdepth: 2

   interpreter
   instructions

