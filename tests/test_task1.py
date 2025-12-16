import sys
from io import StringIO 


def import_and_run_task1():
    """Helper function to import task1 and capture output"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        if 'task1' in sys.modules:
            del sys.modules['task1']
        import task1
        output = sys.stdout.getvalue()
        return task1, output
    except Exception as e:
        return None, ""
    finally:
        sys.stdout = old_stdout


def test_01_candy_total_variable_exists():
    """Test that candy_total variable exists"""
    task1, output = import_and_run_task1()
    assert task1 is not None, "Could not import task1.py"
    assert hasattr(task1, 'candy_total'), "Missing required variable: candy_total"


def test_02_share_variable_exists():
    """Test that share variable exists"""
    task1, output = import_and_run_task1()
    assert task1 is not None, "Could not import task1.py"
    assert hasattr(task1, 'share'), "Missing required variable: share"


def test_03_leftover_variable_exists():
    """Test that leftover variable exists"""
    task1, output = import_and_run_task1()
    assert task1 is not None, "Could not import task1.py"
    assert hasattr(task1, 'leftover'), "Missing required variable: leftover"


def test_04_candy_total():
    """Test total candy calculation - 2 points"""
    task1, output = import_and_run_task1()
    expected_total = 97
    assert str(expected_total) in output, "candy_total miscalculated or not printed"
    if task1:
        assert task1.candy_total == expected_total, "candy_total miscalculated"


def test_05_first_each_share():
    """Test first division - share with 5 people - 2 points"""
    task1, output = import_and_run_task1()
    expected_share = 19
    assert str(expected_share) in output, "share miscalculated in scenario 1"


def test_06_first_leftover():
    """Test first division - leftover with 5 people - 2 points"""
    task1, output = import_and_run_task1()
    expected_leftover = 2
    assert str(expected_leftover) in output, "leftover miscalculated in scenario 1"


def test_07_second_each_share():
    """Test second division - share with 7 people - 2 points"""
    task1, output = import_and_run_task1()
    expected_share = 13
    lines = output.split('\n')
    assert str(expected_share) in '\n'.join(lines[-3:]), "share miscalculated in scenario 2"
    if task1:
        assert task1.share == expected_share, "share miscalculated in scenario 2"


def test_08_second_leftover():
    """Test second division - leftover with 7 people - 2 points"""
    task1, output = import_and_run_task1()
    expected_leftover = 6
    lines = output.split('\n')
    assert str(expected_leftover) in '\n'.join(lines[-2:]), "leftover miscalculated in scenario 2"
    if task1:
        assert task1.leftover == expected_leftover, "leftover miscalculated in scenario 2"


def test_09_no_hardcoding():
    """Test with different input values to detect hard-coding"""
    task1, output = import_and_run_task1()
    if task1 is None:
        return  # Skip test if import failed
    
    # Read and modify the student's code
    with open('task1.py', 'r') as f:
        code = f.read()
    
    # Replace with test dataset
    modified_code = code.replace('people = 4', 'people = 5')
    modified_code = modified_code.replace('bg1 = 37', 'bg1 = 40')
    modified_code = modified_code.replace('bg2 = 22', 'bg2 = 30')
    modified_code = modified_code.replace('bg3 = 8', 'bg3 = 15')
    modified_code = modified_code.replace('bg4 = 30', 'bg4 = 25')
    
    # Execute modified code and capture output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        namespace = {}
        exec(modified_code, namespace)
        output = sys.stdout.getvalue()
    except Exception as e:
        assert False, "Code failed with test data"
    finally:
        sys.stdout = old_stdout
    
    # Check for expected values with test dataset
    expected_total = 110  # 40 + 30 + 15 + 25
    expected_first_share = 18  # 110 // 6 (5 friends + you)
    expected_second_share = 13  # 110 // 8 (5 friends + you + 2 sick)
    
    if 'candy_total' in namespace:
        assert namespace['candy_total'] == expected_total, "Hard-coding detected"
    
    assert str(expected_total) in output, "Hard-coding detected"
    assert str(expected_first_share) in output, "Hard-coding detected"
    assert str(expected_second_share) in output, "Hard-coding detected"
