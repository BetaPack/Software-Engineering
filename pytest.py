from operations import add, subtract

def test_add():
    # This is a passing test
    result = add(2, 3)
    assert result == 5, f"Test Failed: Expectected 5 and got {result}"
    print("Test Passed!!!")

def test_subtract():
    # This is a failing test
    div = subtract(5,3)
    assert div==2, f"Test Failed: Expectected 2 and got {div}"
    print("Test Passed!!!")

def test_divide():
    result = divide(5,2)
    assert result==2.5, f"Test Failed: Expectected 2.5 and got {div}"
    print("Test Passed!!!")

if __name__ == "__main__":
    
    try:
        test_add()
    except AssertionError as e:
        print(e)

    try:
        test_subtract()
    except AssertionError as e:
        print(e)

    try:
        test_divide()
    except AssertionError as e:
        print(e)
