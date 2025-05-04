import pytest


# @pytest.fixture
# def initial_transactions():
#     return [1,2,3,4,5]
#
# print(initial_transactions())

import pytest


@pytest.fixture
def my_list():
    return [1, 2, 3, 4, 5]


def reverse_list(lst):
    return lst[::-1]


print(reverse_list(my_list) == [5, 4, 3, 2, 1])
