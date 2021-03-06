import nltk
from nltk.tokenize import word_tokenize


# This function determines some kind of "distance" between sentences of text.
# For now, it uses a basic Levenshtein distance on the token level.
# It uses nltk.words to tokenize the words.
def sentence_distance(sentence1, sentence2):
    tokens1 = word_tokenize(sentence1)
    tokens2 = word_tokenize(sentence2)

    #print("tokens1:", tokens1)
    #print("tokens2:", tokens2)

    return two_level_distance(tokens1, tokens2)

def characterwise_sentence_distance(sentence1, sentence2):
    return levenshtein_distance(sentence1, sentence2, lambda x, y: x == y)

# Take a weighted average of word and character distance
def compromise_sentence_distance(sentence1, sentence2):
    return sentence_distance(sentence1, sentence2) + 0.25 * characterwise_sentence_distance(sentence1, sentence2)

def unit_cost(n):
    return lambda x, y: n

difference_cost = lambda x, y: 0 if x == y else 1

# Accepts 3 cost functions:
# [0] calculates the cost if the first argument is removed
# [1] calculates the cost if the second argument is removed
# [2] calculates the cost if the arguments are both kept
def levenshtein_distance(sequence1, sequence2, cost_functions=[unit_cost(1), unit_cost(1), difference_cost]):
    return _levenshtein_distance_(sequence1, sequence2, cost_functions, {})
    
def _levenshtein_distance_(sequence1, sequence2, cost_functions, memory):
    # Implementation inspired by the pseudocode on Wikipedia
    # https://wikipedia.org/wiki/Levenshtein_distance
    if len(sequence1) == 0:
        return len(sequence2)
    if len(sequence2) == 0:
        return len(sequence1)
    
    sequence1_key = str(sequence1)
    sequence2_key = str(sequence2)
    instance_key = sequence1_key + ';' + sequence2_key
    
    if instance_key in memory:
        return memory[instance_key]
    else:
        last1 = sequence1[-1]
        last2 = sequence2[-1]
        
        distance_if_1_shortened = _levenshtein_distance_(sequence1[:-1], sequence2, cost_functions, memory) + cost_functions[0](last1, last2)
        distance_if_2_shortened = _levenshtein_distance_(sequence1, sequence2[:-1], cost_functions, memory) + cost_functions[1](last1, last2)
        distance_if_characters_preserved = _levenshtein_distance_(sequence1[:-1], sequence2[:-1], cost_functions, memory) + cost_functions[2](last1, last2)

        result = min(distance_if_1_shortened, distance_if_2_shortened, distance_if_characters_preserved)
        memory[instance_key] = result

        return result

# Expects two lists of words.
def two_level_distance(sequence1, sequence2):
    first_removal_distance = lambda x, y: len(y)
    second_removal_distance = lambda x, y: len(x)
    comparison_distance = lambda x, y: levenshtein_distance(x, y)
    cost_functions = [first_removal_distance, second_removal_distance, comparison_distance]
    return levenshtein_distance(sequence1, sequence2, cost_functions)
