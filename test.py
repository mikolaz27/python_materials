# """
#   Multiple Inheritance
#    - allows to merge data+methods from parents...
#    - ...but introduces diamond problem
# """
#
#
# class Person:
#     def __init__(self, first_name, last_name, **kwargs):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# class TeamMember(Person):
#     def __init__(self, first_name, last_name, **kwargs):
#         super().__init__(first_name, last_name, **kwargs)
#         self.salary = kwargs.get("salary", 0)
#         self.jobtitle = kwargs.get("jobtitle", 'N/A')
#
#
# class TeamLeader(TeamMember):
#     def __init__(self, first_name, last_name, **kwargs):
#         super().__init__(first_name, last_name, **kwargs)
#         self.soft_skills = kwargs.get("soft_skills", [])
#
#
# #         self.jobtitle = 'TeamLeader'
#
# #     def __str__(self):
# #         return 'TL'
#
# class Architect(TeamMember):
#     def __init__(self, first_name, last_name, **kwargs):
#         super().__init__(first_name, last_name, **kwargs)
#         self.certificates = kwargs.get("certificates", [])
#
#
# #         self.jobtitle = 'Architect'
#
#
# class CTO(Architect, TeamLeader):
#     def __init__(self, first_name, last_name, **kwargs):
#         super().__init__(first_name, last_name, **kwargs)
#         self.projects = kwargs.get("projects")
#         self.soft_skills += ['Leadership', 'EQ']
#         self.certificates += ['ITIL', 'PMA']
#
#
# #         self.jobtitle = 'CTO'
#
# #     def __str__(self): # overriding (!= method overloading)
# #         return f'{result}\nCTO: {self.first_name}, {self.last_name}'
#
#
# cto = CTO(
#     first_name='Jake',
#     last_name='Smith',
#     salary=250000
# )
#
# # will it be taken from TeamLeader or Architect?
# print(cto.jobtitle)
# # print(cto.__main__)
# print(CTO.mro())
#
# # class WalkInterface:
# #
# #     def walk(self):
# #         print("work")
# #
# #
# # class TalkInterface:
# #
# #     def talk(self):
# #         pass
# #
# #
# # class SwimInterface:
# #
# #     def swim(self):
# #         pass
# #
# #
# # class Cat(SwimInterface, WalkInterface):
# #     def walk(self):
# #         pass
# #
# #
# # cat1 = Cat()
# # cat1.walk()
#
# # from time import sleep
# #
# #
# # class InfiniteCounter:
# #     def __init__(self, value):
# #         self._value = value
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         value = self._value
# #         self._value += 1
# #         return value
# #
# #
# # # for i in InfiniteCounter(42):
# # #     print(i)
# # #     sleep(1)
# #
# # # class Player(object):
# # #     def test(self):
# # #         print("Player")
# # #
# # # class Enemy(Player):
# # #     def test(self):
# # #         print("Enemy")
# # #
# # #
# # # class GameObject(Player, Enemy):
# # #     def test(self):
# # #         print("GameObject")
# #
# #
# # # g = GameObject()
# #
# # 1 + 1
# #
# #
# # # test_list = [1,2,3,4]
# # #
# # # x = iter(test_list)
# # #
# # # print(next(x))
# # # print(next(x))
# #
# # class Fibonacci:
# #     def __init__(self):
# #         self.pre_previous = 0
# #         self.previous = 1
# #
# #     def __next__(self):
# #         result = self.pre_previous + self.previous
# #         self.pre_previous = self.previous
# #         self.previous = result
# #         return self.pre_previous
# #
# #     def __iter__(self):
# #         return self
# #
# #
# # # for n, fibon_value in enumerate(Fibonacci(), start=1):
# # #     if n == 10:
# # #         break
# # #     print(fibon_value, n)
# # #     sleep(1)
# #
# #
# # for i in range(1, 10, 0.1):
# #     print(i)
#
# list_1 = [1, 2, 3, 4, 5, 6]
# iter_1 = iter(list_1)
#
# print(iter_1)
# print(next(iter_1))
# print(next(iter_1))
# print(next(iter_1))
# print(list_1)

# "SELECT BillingCountry FROM invoices WHERE BillingCountry=="

# query_country_list = "SELECT DISTINCT BillingCountry  FROM invoices"
#     countries = execute_query(query=query_country_list, args=tuple(fields.values()))
# import aggregate as aggregate
# from mypy.messages import capitalize
from jinja2.nodes import Test

countries = [('Germany',), ('Norway',), ('Belgium',), ('Canada',), ('USA',),
             ('France',), ('Ireland',), ('United Kingdom',), ('Australia',)]

countries_2 = [('Germany',), ('Norway',), ('Belgium',), ('Canada',), ('USA',),
               ('France',), ('Ireland',), ('United Kingdom',), ('Australia',)]
target = "Germany"

# 1. map -> capitalize
# 2. map -> add some data
# 3. filter ->
# 4. aggregate ->
#
# 1. filter ->
# 1. map -> capitalize
# 2. map -> add some data
# 4. aggregate ->

x = target if target else "else"

print([country for country in countries if country[0] == target])

result = list(filter(lambda x: x[0] == target, countries))


# if len(result):
#     print(result)
# for items in countries:
#     for values in items:
#         countries2.append(values)


class Test:

    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        return self._value == other._value


x1 = [Test(1), Test(2), Test(3)]

print("Yes" if Test(2) in x1 else "NIT")


def test():
    print(Test.__name__)

test()

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')