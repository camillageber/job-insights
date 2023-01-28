from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    low_case = "javascript"
    upper_case = "JAVASCRIPT"

    assert count_ocurrences(path, low_case) == 122
    assert count_ocurrences(path, upper_case) == 122
