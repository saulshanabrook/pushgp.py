from pushgp.push.instructions import base


class TestSimpleInstruction(object):
    def test_annotated_returns_to_exec(self):
        @base.simple_instruction
        def f(a_item: 'a'):
            return a_item ** 2
        stacks = {'a': [2], 'exec': []}
        f(stacks)
        assert stacks == {'a': [], 'exec': [4]}

    def test_not_enough_args_no_op(self):
        @base.simple_instruction
        def f(a_item: 'a'):
            return a_item ** 2
        stacks = {'a': [], 'exec': []}
        f(stacks)
        assert stacks == {'a': [], 'exec': []}

    def test_none_result_is_discarded(self):
        @base.simple_instruction
        def f(a: 'a'):
            return
        stacks = {'a': [1], 'exec': []}
        f(stacks)
        assert stacks == {'a': [], 'exec': []}

    def test_multiple_return_items(self):
        @base.simple_instruction(multiple_return_items=True)
        def f_multi(a: 'a'):
            return [a]

        @base.simple_instruction()
        def f(a: 'a'):
            return a

        stacks = {'exec': [], 'a': [1]}
        stack_for_multi = {'exec': [], 'a': [1]}
        f(stacks)
        f_multi(stack_for_multi)
        assert stacks == stack_for_multi
