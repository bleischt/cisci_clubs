# Functions to be used for replacing variables in queries and responses.

#Logan Williams 5/28
#Tobias Bleisch 6/1

import json

id_to_clubVariations = "data/id_to_clubVariations.json"

# Finds a Key in a dictionary based on it's value. Also works if dict value is a list.
# Useful for: finding a variation's standardized version
# Example:
#   get_key_from_value("women in software and hardware", id_to_clubVariations) => "wish"
#   get_key_from_value("Cal Poly Game Development", variable_to_values) => "CLUB"
# This allows the string_to_var function to utilize cleaner dictionaries
# by mapping variations of variables to a single variable.
def get_key_from_value(value, dictionary):

    for key,values in dictionary.items():
        if value in values:
                return key
    print(str(value) + " was not found in " + str(dictionary))
    return None


# Returns the standardized version of the given club
def standardize_club(club, id_to_variations):
   f = open(id_to_variations, 'r')
   return get_key_from_value(club.lower(), json.load(f))


#Replaces a value in the input query with the key of a matching value
#in the supplied dictionary. Used for standardizaton of club names mostly.
#Example:
#   value_replacement("Where does wish meet?", {women involved in software and hardware : [wish, women in hardware, ...], ...})
#        => "Where does women involved in software and hardware meet?"
def value_replacement(query, id_to_variations):
    for id, variations in id_to_variations.items():
        for var in sorted(variations, key=len, reverse=True):
            if var in query:
                query = query.replace(var, id)
                break

    return query

# Takes in a whole query string and returns a tuple of the string with tagged
# values and a dictionary mapping tags to values.
# Example:
#   tag_query("Who is the president of Women in Software and Hardware?") => 
#             ("Who is the [POSITION] of [CLUB]?", 
#              {"POSITION": "president", "CLUB": "Women in Software and Hardware"})
# NOTE: This will currently not work properly if there are two of the same tags in a query.
#       To get this working with tags appearing more than once, would have to add some way
#       of marking which value in the dict comes first in the query so that we can tell
#       which variable goes to which position. Also, after we find the variable and do the 
#       replacing, we should go back and repeat that until we don't see any more of those
#       specific variable occurrences in the string; otherwise, we will never tag a variable
#       if it has already been tagged in the string.
def tag_query(query, variable_to_values, id_to_clubVariations):

    result_dict = {}
    query = value_replacement(query, id_to_clubVariations)
    print(query)
    for tag_key,values in variable_to_values.items():
        for variation in sorted(values, key=len, reverse=True):
            print(variation)
            if variation in query:
                result_dict[tag_key] = variation
                query = query.replace(variation, '['+ tag_key.upper() + ']')

    return (query, result_dict)

if __name__ == "__main__":
   pass 
