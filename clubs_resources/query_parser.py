import re

# Abstract text example:
# [PERSON] walks to [PLACE].
#
# This method returns a list of text pieces.
# Each text piece is either only text, or only a variable.
def parse_abstract_text(abstract_text):
    variable_matcher = re.compile(r"(\[[A-Z_-]+\])")
    return variable_matcher.split(abstract_text)

# Check if a string is a variable, e.g. "[FOOD]" or "[C]"
def is_variable(string):
    if len(string) < 3:
        return False

    middle = string[1:-1]
    return string[0] == '[' and string[-1] == ']' and middle == middle.upper()

def get_variables_from_abstract_text(abstract_text):
    return [string for string in parse_abstract_text(abstract_text) if is_variable(string)]

def get_text_pieces_from_abstract_text(abstract_text):
    return [string for string in parse_abstract_text(abstract_text) if not is_variable(string)]

# Use this to figure out the value of variables in the user's query,
# once you already know which abstract query to use.
def get_variable_values(user_query, abstract_query):
    pass
    # TODO: this is going to be incredibly complicated.
