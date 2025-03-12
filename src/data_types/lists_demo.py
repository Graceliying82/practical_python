class ListDemo:
    """
    A class to demonstrate list operations in Python.
    """

    def __init__(self, my_list=None):
        """
        Initialize with a given list or a default list if none is provided.

        :param my_list: List to initialize with, defaults to [1, 2, 3, 4, 5]
        """
        if my_list is None:
            self.list = [1, 2, 3, 4, 5]
        elif isinstance(my_list, list):
            self.list = my_list
        else:
            raise ValueError(f"Expected a list or no param, got {my_list}")

    def create_a_new_list(self):
        """
        Return a copy of the current list.
        :return: a copy of the current list
        """
        return self.list.copy()

    def append_list(self, app):
        """
        Appends an element to the list and returns the list
        :param app: the element to append
        :return: the list with the appended element
        """

        self.list.append(app)
        return self.list

if __name__ == "__main__":
    list_demo = ListDemo(['1', '2', '3'])
    list_demo.append_list('d')

    print(list_demo.list)

