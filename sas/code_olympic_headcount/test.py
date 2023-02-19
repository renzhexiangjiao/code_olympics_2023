from solution import co_headcount


def test_headcount_1_test_case():
    x = [[1, 1, 0, 0, 0, 0, 1, 1],

         [1, 1, 0, 1, 1, 0, 1, 1],

         [0, 0, 0, 1, 1, 0, 0, 0],

         [1, 1, 0, 1, 1, 0, 1, 1],

         [1, 1, 0, 0, 0, 0, 1, 1]]

    assert co_headcount(x) == "5 teams of [6, 4, 4, 4, 4] totalling 22"


def test_headcount_2_test_case():
    x = [[0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0],

         [0, 0, 0, 0, 0, 0, 0, 0]]

    assert co_headcount(x) == "0 teams"


def test_headcount_3_test_case():
    x = [[1, 1, 1, 1, 1, 1, 1, 1],

         [1, 0, 0, 0, 0, 0, 0, 1],

         [1, 0, 0, 1, 1, 0, 0, 1],

         [1, 0, 0, 0, 0, 0, 0, 1],

         [1, 1, 1, 1, 1, 1, 1, 1]]

    assert co_headcount(x) == "2 teams of [22, 2] totalling 24"


def test_headcount_4_test_case():
    x = [[1]]

    assert co_headcount(x) == "1 team of [1] totalling 1"
