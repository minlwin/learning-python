from src.ls02_variable_args import with_variable_args, with_variable_args_first

def test_with_variable_args():
    assert 0 == with_variable_args("Hello Varargs")
    assert 6 == with_variable_args("Hello Varargs", 1, 2, 3)    

def test_with_variable_args_first():
    assert 0 == with_variable_args_first(name ="hello")
    assert 6 == with_variable_args_first(1, 2, 3, name = "Hello Varargs")    
