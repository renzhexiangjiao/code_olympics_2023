from solution import decipherer


def test_example_test_case():
    input_x = [[1, 3, 2, 4, 1],

               [3, 1, 2, 4, 3],

               [2, 3, 4, 1, 2],

               [2, 1, 4, 3, 1],

               [4, 1, 2, 3, 4]]

    assert decipherer(input_x) == "33311"
