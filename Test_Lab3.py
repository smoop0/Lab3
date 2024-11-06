import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_elem_overflow():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3]
    test = 1

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == test)

def test_bubble_sort_elem_none():
    result = []
    input_arr = []
    test = 0

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == test)

def test_bubble_sort_elem_string():
    result = []
    input_arr = ["asdaai", 1, 2342, 436]
    test = 2

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == test)