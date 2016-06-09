import nltk, random, sys
import json
import math
import re


from clubs_resources.sentence_distance import sentence_distance
from clubs_resources.variable_replace import tag_query
from clubs_resources.variable_replace import get_key_from_value
from clubs_resources.speech_acts import *
from clubs_resources.scrapers.scrape_all import get_all_data
from nltk.corpus import stopwords

path_to_data = "clubs_resources/data/"

class clubs:
    moduleContributors = ['Edgard Arroliga', 'Tobias Bleisch', 'Michael Casebolt', 'Justin Postigo', 'Wasae Qureshi',
                          'Logan Williams']
    moduleName = "Clubs and Tutoring"
    moduleDescription = "This module is for information about clubs and tutoring. The data repository is located in /mnt/cisci/modules/clubs_resources."
    module_questions = "clubs_resources/questions.txt"

    resources = {}
    numberOfResponses = 0
    type_of_question = {}

    # load dicts
    id_to_clubVariations = {}
    # print(id_to_clubVariations)
    variable_to_values = {}
    # print(variable_to_values)

    def __init__(self):
        self.dataStore = {}  # you may read data from a pickeled file or other sources
        self.id_to_clubVariations = json.loads(open("clubs_resources/data/id_to_clubVariations.json").read())
        self.variable_to_values = json.loads(open("clubs_resources/data/variable_to_values.json").read())
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
            question_type = line_spl_at_bar[0][len(line_spl_at_bar[0]) - 2:].strip()
            question = line_spl_at_bar[0][2:-2].strip().lower()
            answer = line_spl_at_bar[2].strip()
            question = re.sub('[^0-9a-zA-Z\s]+', '', question)
            question_answer[question] = answer
            self.type_of_question[line_spl_at_bar[2][1:].strip()] = question_type
        self.dataStore = question_answer
        
        #self.resources = get_all_data()
        self.resources = json.load(open(path_to_data + "all_data.json", 'r'))
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
    def replace_variable_in_answer(self, response_string, tags):
        speechact = SpeechActs(self.resources)
        if response_string == "There are currently [NUMBER] tutors":
            return speechact.num_tutors()
        elif response_string == "The tutors are: [PERSON]":
            return speechact.list_of_tutors()
        elif response_string == "Here is some information about the tutor: [DESCRIPTION]":
            return speechact.tutor_information(tags['TUTOR'])
        elif response_string == "Tutor works on [DAY] at [TIME]":
            return speechact.tutor_work_days(tags['TUTOR'])
        elif response_string == "Tutoring is offered for [COURSE]":
            return speechact.courses_tutored()
        elif response_string == "[PERSON] is currently the lead tutor.":
            return speechact.lead_tutor()
        elif response_string == "Tutoring is held on [DATE] at [LOCATION] from [TIME] to [TIME]":
            return speechact.tutor_meeting_info()
        elif response_string == "You can become a tutor if you've passed CPE 103. Email [PERSON] at [EMAIL] to schedule an interview.":
            return speechact.become_a_tutor()
        elif response_string == "Please email the current lead tutor [PERSON] at [EMAIL] for more info.":
            return speechact.tutoring_more_info()
        elif response_string == "Here are the list of official clubs within the Computer Science department: [CLUB]":
            return speechact.list_of_clubs()
        elif response_string == "Here's the club's website: [URL]":
            return speechact.club_more_info(tags['CLUB'])
        elif response_string == "Here is a description of the club: [DESCRIPTION]":
            return speechact.club_description(tags['CLUB'])
        elif response_string == "[CLUB] meets on [DAY] at [TIME] at [LOCATION]":
            return speechact.club_meeting_info(tags['CLUB'])
        elif response_string == "The current officers are: [OFFICER]":
            return speechact.club_officers(tags['CLUB'])
        elif response_string == "You can contact [PERSON] for more info: [EMAIL] [PHONE]":
            return speechact.club_contact(tags['CLUB'])
        elif response_string == "Here are the upcoming events: [EVENT]":
            return speechact.list_of_club_events(tags['CLUB'])
        elif response_string == "Here is a description of the event: [DESCRIPTION]":
            return speechact.event_description(tags['EVENT'])
        elif response_string == "The event is taking place on [DATE] at [LOCATION] from [TIME] to [TIME]":
            return speechact.event_meeting_info(tags['EVENT'])
        elif response_string == "Here is where the study sessions are being held: [LOCATION]":
            return speechact.study_sessions_location()
        elif response_string == "Here is the study session coordinator: [PERSON]":
            return speechact.study_session_coordinator()
        elif response_string == "Here is the advisor of the club: [PERSON] [PHONE] [EMAIL]":
            return speechact.club_advisor(tags['CLUB'])
        else:
            return "Function not made for that answer."
    def response(self, normal_query, history=[]):
        query_tag = tag_query(normal_query, self.variable_to_values, self.id_to_clubVariations)
        query = query_tag[0]
        tags = query_tag[1]
        query = re.sub('[^0-9a-zA-Z\s]+', '', query)
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
            rating = 1.0
        else:
            #Commenting out levenstien to try tf-idf
            """
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
            """
            stopset = stopwords.words('english')
            # Remove ?., from question and query
            #Doing TF on the questions
            term_frequency = {}
            for question in self.dataStore.keys():
                term_frequency[question] = {}
                for word in question.split(" "):
                    temp_freq = term_frequency[question]
                    #if word not in stopset:
                    if word in temp_freq:
                        temp_freq[word] += 1
                    else:
                        temp_freq[word] = 1
                    term_frequency[word] = temp_freq

            #Normalizing
            for doc, freq in term_frequency.items():
                num_words = 0
                for word in freq:
                    num_words += freq[word]
                for word in freq:
                    term_frequency[doc][word] = freq[word]/num_words

            #idf 
            term_idf = {}
            for word in query.split(" "):
                docs_occurs = 0
                for question in self.dataStore.keys():
                    if word in question:
                        docs_occurs += 1
                if docs_occurs != 0:
                    if "[" in word and "]" in word:
                        term_idf[word] = 5 + math.log(len(self.dataStore.keys())/docs_occurs)
                    else:
                        term_idf[word] = 1 + math.log(len(self.dataStore.keys())/docs_occurs)

                else:
                    term_idf[word] = 0

            #tf*idf
            tf_idf = {}
            for question in self.dataStore.keys():
                tf_idf[question] = {}
                tf_idf_words = {}
                for word in query.split(" "):
                    if word in term_frequency[question]:
                        tf_word = term_frequency[question][word]
                        idf_word = term_idf[word]
                        tf_mult_idf = tf_word * idf_word
                        tf_idf_words[word] = tf_mult_idf
                    else:
                        tf_idf_words[word] = 0
                tf_idf[question] = tf_idf_words

            results = {}
            for question, words in tf_idf.items():
                result_value = 0
                for word, v in words.items():
                    result_value += v
                results[question] = result_value - sentence_distance(query, question)

            final_result = list(reversed(sorted(results, key= results.get)))
            estimate_query = final_result[0]
            response_string = self.dataStore[estimate_query]
            signal = "Normal"
        if response_string in self.type_of_question and self.type_of_question[response_string] == "1":
            try:
                response_string = self.replace_variable_in_answer(response_string, tags)
            except:
                response_string = "Not enough data to respond to this question:\n" + response_string
        return [rating, signal, response_string]

def run():
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
        if query.lower() != 'quit' and query.lower() != 'exit':
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
