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

    return levenshtein_distance(tokens1, tokens2, lambda x, y: x == y)

def characterwise_sentence_distance(sentence1, sentence2):
    return levenshtein_distance(sentence1, sentence2, lambda x, y: x == y)

# Take a weighted average of word and character distance
def compromise_sentence_distance(sentence1, sentence2):
    return sentence_distance(sentence1, sentence2) + 0.25 * characterwise_sentence_distance(sentence1, sentence2)

def levenshtein_distance(sequence1, sequence2, equals):
    return _levenshtein_distance_(sequence1, sequence2, equals, {})
    
def _levenshtein_distance_(sequence1, sequence2, equals, memory):
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
        last_items_match = equals(sequence1[-1], sequence2[-1])
        
        distance_if_1_shortened = _levenshtein_distance_(sequence1[:-1], sequence2, equals, memory) + 1
        distance_if_2_shortened = _levenshtein_distance_(sequence1, sequence2[:-1], equals, memory) + 1
        distance_if_characters_preserved = _levenshtein_distance_(sequence1[:-1], sequence2[:-1], equals, memory) + (0 if last_items_match else 1)

        result = min(distance_if_1_shortened, distance_if_2_shortened, distance_if_characters_preserved)
        memory[instance_key] = result

        # print(instance_key + " : " + str(result))

        return result
