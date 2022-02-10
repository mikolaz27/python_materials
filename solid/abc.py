from abc import ABC, abstractmethod


class AbcTest(ABC):
    # def __init__(self):
    #     if type(self) is AbcTest:
    #         raise Exception(
    #             'Base is an abstract class and cannot be instantiated directly')
    @abstractmethod
    def new_method(self):
        print('Test')


class Child(AbcTest):

    # def new_method(self):
    #     passfsdfdsl
    pass
    # def new_method(self):
    #     super().new_method()
    #     print('new_method')
        # passfsdfdsl


new_abc = AbcTest()
print(new_abc)
# new_child = Child()
# new_child.new_method()
