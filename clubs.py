import nltk, random, sys
import json
from clubs_resources.sentence_distance import sentence_distance
from clubs_resources.variable_replace import tag_query
from clubs_resources.variable_replace import get_key_from_value

class clubs:
    moduleContributors = ['Edgard Arroliga', 'Tobias Bleisch', 'Michael Casebolt', 'Justin Postigo', 'Wasae Qureshi',
                          'Logan Williams']
    moduleName = "Clubs and Tutoring"
    moduleDescription = "This module is for information about clubs and tutoring. The data repository is located in /mnt/cisci/modules/clubs_resources."
    module_questions = "clubs_resources/questions.txt"

    numberOfResponses = 0

    def __init__(self):
        self.dataStore = {}  # you may read data from a pickeled file or other sources
        self.update()

    def id(self):
        return [self.moduleName, self.moduleDescription]

    def credits(self):
        return ', '.join(self.moduleContributors)

    def update(self):
        # some update procedure dealing with dataStore,
        # if items need to be crawled and saved, this is the place to do that

        # Build up a dictionary of our predefined questions and answers
        file_resources = open(clubs.module_questions, 'r')
        question_answer = {}
        for line in file_resources.read().splitlines():
            line_spl_at_bar = line.split("|")
            question = line_spl_at_bar[0][2:-2].strip().lower()
            answer = line_spl_at_bar[2].strip()
            question_answer[question] = answer
        self.dataStore = question_answer

        return True

    def getRating(self, query, history=[]):  # get rating based on query and (if you wish) the history
        return random.random()

    def searchHistory(self, query, history=[]):
        # this is the case where the question has already been asked
        for q_a in history:
            question = q_a[0]
            rating = q_a[1][0]
            signal = q_a[1][1]
            response_string = q_a[1][2]
            if signal == "End":
                return ""
            if query == question:
                return "You already asked this question. Here's the answer: "
        return ""

    def response(self, query, history=[]):
        threshold = 11
        min_distance = threshold
        query = query.strip().lower()
        rating = 0  #self.getRating(query)
        if len(query) <= 0:  # signals can be "Normal", "Error", "Question", "Unknown" or "End"
            signal = "Error"

        response_string = ""
        if query in self.dataStore.keys():
            history_response = self.searchHistory(query, history)
            response_string = history_response + self.dataStore[query]
            signal = "Normal"
        else:
            min_query = None
            for question in self.dataStore.keys():
                distance = sentence_distance(query, question)
                if distance < min_distance:
                    min_distance = distance
                    min_query = question
                    rating = 1 - (distance / threshold)
            if min_query == None:
                response_string = "Sorry, I don't know the answer to that."
                signal = "Unknown"
            else:
                response_string = self.dataStore[min_query]
                signal = "Normal"

        return [rating, signal, response_string]

def run():
    myModule = clubs()
    print("module name: ", myModule.id()[0])
    print("module description: ", myModule.id()[1])
    print("credits:", myModule.credits())
    print("update results: ", myModule.update())

    # load dicts
    id_to_clubVariations = json.loads(open("clubs_resources/data/id_to_clubVariations.json").read())
    # print(id_to_clubVariations)
    variable_to_values = json.loads(open("clubs_resources/data/variable_to_values.json").read())
    # print(variable_to_values)

    query = ""
    response = ""
    history = []
    while query.strip().lower() not in ['quit', 'exit']:
        print("How can I help you? (\"quit\" to exit)", end=" ")
        query = input()
        query = tag_query(query, variable_to_values, id_to_clubVariations)[0]
        response = myModule.response(query, history)
        history.append([query, response])
        if response[1] is "Error":
            print(response[1])
            continue
        else:
            print(response[2], response[0])


def test():
    myModule = clubs()
    print("module name: ", myModule.id()[0])
    print("module description: ", myModule.id()[1])
    print("credits:", myModule.credits())
    print("update results: ", myModule.update())
    query = ""
    response = ""
    history = []
    while query.strip().lower() not in ['quit', 'exit']:
        print("How can I help you? (\"quit\" to exit)", end=" ")
        query = input()
        if query.strip().lower() in ['quit', 'exit']:
            sys.exit()
        response = myModule.response(query, history)
        history.append([query, response])
        if response[1] is "Error":
            print(response[1])
            continue
        else:
            print(response[2])

def test_variable_replace():
    #load dicts
    id_to_clubVariations = json.loads(open("clubs_resources/data/id_to_clubVariations.json").read())
    # print(id_to_clubVariations)
    variable_to_values = json.loads(open("clubs_resources/data/variable_to_values.json").read())
    # print(variable_to_values)

    query = "Where does wish meet?"
    query1 = "Is Jasper Kahn president of society of women engineers?"
    print(query)
    print(tag_query(query, variable_to_values, id_to_clubVariations))
    print(query1)
    print(tag_query(query1, variable_to_values, id_to_clubVariations))
    print(get_key_from_value("association for computing machinery", variable_to_values))

if __name__ == "__main__":
    run()
    # test()
    # test_variable_replace()