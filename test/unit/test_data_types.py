from src.data_types.lists_demo import ListDemo

class TestDataType:
    """"
    Tests for different data type classes and their methods
    """
    def test_default_list(self):
        """
        Test ListDemo initializes with the default list.
        """
        my_list = ListDemo()
        assert  my_list.list == [1, 2, 3, 4, 5]
