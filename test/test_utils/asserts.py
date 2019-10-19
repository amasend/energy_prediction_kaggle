from typing import List


class CustomAssert:
    def __init__(self):
        pass

    @staticmethod
    def assert_columns_equal(left: List,
                             right: List) -> None:
        if len(left) == len(right) and sorted(left) == sorted(right):
            pass
        else:
            raise ValueError("""Left list is not equal to right list.
            {} not equal {}""".format(left, right))
