# Logan Williams 
# 5/28/16

# Functions to be used for replacing variables in queries and responses.
#
# NOTE: still needs the pre_process implemented with the corresponding data tables (5/28)
#       and still needs tag_values data for the string_to_tag function (5/28)



# Takes a variation of a variable and returns its standardized version.
# For example:
#   pre_process("women in software and hardware") => "WISH"
# This allows the string_to_var function to utilize cleaner dictionaries
# by mapping variations of variables to a single variable.
def pre_process(var):
    
    # ********* 
    return



# Takes a variable variation and returns the list of all other possible 
# variations of it.
# For example: 
#   un_pre_process("wish") => ["wish",
#                              "women in software and hardware", 
#                              "women involved in software and hardware",
#                              etc.]
def un_pre_process(var):
    
    # *********
    return



# Takes a string variable and returns the corresponding tag word.
# 'None' is returned if there is no matching tag found.
# For example:
#   string_to_tag("Cal Poly Game Development") => "CLUB"
def string_to_tag(string):

    string = pre_process(string)

    tag = None

    # ********** tag_values needs to be implemented ************* 
    # tag_values is the dictionary of tags mapped to a list of the possible
    # variables for that tag. For example, an entry might look like:
    #  {'CLUB':['CPGD', 'WISH', 'White Hat']} 
    for tag_key in tag_values:
        if string in tag_values[tag_key]:
            if tag == None:
                print("var '" + string + "' was already labeled '" + tag + "' and is now being renamed '" + tag_key + "'.")
            tag = tag_key

    return tag

        

# Takes in a whole query string and returns a tuple of the string with tagged
# values and a dictionary mapping tags to values.
# For example:
#   tag_query("Who is the president of Women in Software and Hardware?") => 
#             ("Who is the [POSITION] of [CLUB]?", 
#              {"POSITION": "president", "CLUB": "Women in Software and Hardware"})
# NOTE: This will currently not work properly if there are two of the same tags in a query.
#       To get this working with tags appearing more than once, would have to add some way
#       of marking which value in the dict comes first in the query so that we can tell
#       which variable goes to which position. Also, after we find the variable and do the 
#       replacing, we should go back and repeat that until we don't see any more of those
#       specific variable occurences in the string; otherwise, we will never tag a variable
#       if it has already been tagged in the string.
def tag_query(query):

    result_dict = {}

    # **(same as prev)** tag_values needs to be implemented ************* 
    # tag_values is the dictionary of tags mapped to a list of the possible
    # variables for that tag. For example, an entry might look like:
    #  {'CLUB':['CPGD', 'WISH', 'White Hat']} 
    for tag_key in tag_values:
        for val in tag_values[tag_key]:
            variations = un_pre_process(val)
            for variation in variations:
                if variation in query:
                    result_dict[tag_key] = variation
                    query = query.replace(variation, '['+ tag_key + ']')

    return (query, result_dict)


