from pushgp.push.interpreter import Push


class PushTest(object):

    def test_str(self):
        '''
        Make sure ``__str__`` returns the right
        string version of the Push stacks.
        '''
        p = Push()
        assert str(p) == 'Push: {}'
        p['exec'] = [1, 2]
        assert str(p) == "Push: {'exec': [1, 2]}"

    def test_stack_for_item(self):
        '''
        Make sure stack for item looks at stack_types
        attribute to return the stack name.
        '''
        p = Push()
        p.stack_types = {object: 'object'}
        assert p.stack_for_item(object()) == 'obj'

    def test_stack_for_item_none(self):
        '''
        If a item is not present in the ``stack_types`` it should
        return none for ``stack_for_item``
        '''
        p = Push()
        p.stack_types = {}
        assert p.stack_for_item(object()) is None

    def test_stack_for_item_order(self):
        '''
        Make sure it will choose the first item in the stack
        that corresponds to the type of the item.
        '''
        p = Push()

        class ParentClass(object):
            pass

        class ChildClass(ParentClass):
            pass

        p.stack_types.clear()
        p.stack_types[ParentClass] = 'parent'
        p.stack_types[ChildClass] = 'child'

        assert p.stack_for_item(ChildClass()) == 'child'
        assert p.stack_for_item(ParentClass()) == 'parent'

    def test_default_stack_types(self):
        '''
        Defult python types should be sorted properly into stacks
        '''
        p = Push()
        for item, stack_name in [
                [1, 'int'],
                [0, 'int'],
                [1.0, 'float'],
                [True, 'bool'],
                [False, 'bool'],
                ['', 'str'],
                [[], None],
                [[1, 2], None]]:
            assert p.stack_for_item(item) == stack_name

    def test_execute_pops_exec(self):
        p = Push()
        item = 1
        p['exec'] = [item]

        p.execute()
        assert p['exec'] == []

    def test_execute_sends_literal_to_stack(self):
        p = Push()
        item = 1
        p['exec'] = [item]
        stack = p.stack_for_item(item)

        p.execute()
        assert p[stack] == [item]

    def test_execute_in_correct_order(self):
        item = 1
        second_item = 2

        p = Push()
        p['exec'] = [item]
        p.execute()
        p['exec'] = [second_item]
        p.execute()

        p_2_values_in_exec = Push()
        p_2_values_in_exec['exec'] = [second_item, item]
        p_2_values_in_exec.execute()

        assert p_2_values_in_exec == p

    def test_execute_callable(self):
        p = Push()
        item = lambda p: p['other stack'].append('new value')
        p['exec'] = [item]

        p.execute()
        assert p['other stack'] == ['new value']

    def test_call(self):
        p = Push()
        p(1)
        assert p['int'] == [1]

    def test_call_multiple_arguments_right_order(self):
        p = Push()
        p(1, 2)
        assert p['int'] == [2, 1]

    def test_call_return_push(self):
        p = Push()
        called_p = p(1)
        assert called_p == p
