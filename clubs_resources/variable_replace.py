# Logan Williams 
# 5/28/16

# Replacing variables in queries and responses.



# Takes a string and returns the standardized version of it.
# For example:
#   pre_process("women in software and hardware") => "WISH"
# This allows the string_to_var function to utilize cleaner dictionaries
# by mapping variations of variables to a single variable.
def pre_process(string):
    
    # ********* 


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
        
