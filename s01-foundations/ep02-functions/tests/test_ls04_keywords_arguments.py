from src.ls04_keywords_arguments import keywords_with_var_args, with_keywords

def test_with_keywords():
    assert {"One" : 1, "Two" : 2} == with_keywords(One = 1, Two = 2)

def test_keywords_with_var_args():
    assert (6, {"One" : 1, "Two" : 2}) == keywords_with_var_args(1, 2, 3, One = 1, Two = 2)