#Speech acts represent single kernels of information that a user
#can request in various forms.
#Example:
#   ->Who is the advisor of pgr?
#   ->Which professor advises pgr?
#       ->[Advisor] advises [CLUB]
import re 
class SpeechActs:
    resources = {}

    def __init__(self, resources):
        self.resources = resources

    #There are currently [NUMBER] tutors
    def num_tutors(self):
        tutors = self.resources['tutors']
        num_tutors = 0
        for tutor in tutors:
            num_tutors += 1
        return "There are currently " + str(num_tutors) + " tutors"


    #The tutors are: [PERSON]
    def list_of_tutors(self):
        tutors = self.resources['tutors']
        list_tutors = ""
        for tutor in tutors:
            list_tutors += tutor + "\n"
        return "The tutors are:\n" + list_tutors 


    #Here is some information about the tutor: [DESCRIPTION]
    def tutor_information(self, tutor):
        tutors = self.resources['tutors']
        for tutor_name in tutors:
            if tutor in tutor_name:
                tutor = tutor_name
        specific_tutor = tutors[tutor]
        tutor_info = ""
        for info, value in specific_tutor.items():
            tutor_info += info + " : " + value + ", "
        return tutor_info

    #Tutor works on [DAY] at [TIME]
    def tutor_work_days(self, tutor):
        tutors = self.resources['tutors']
        specific_tutor = tutors[tutor]
        times = specific_tutor['times']
        days = specific_tutor['days']
        return tutor + " works on " + days + " at " + times
        
    #Tutoring is offered for [COURSE]
    def courses_tutored(self):
        tutor_info = self.resources['tutor_info']
        courses = tutor_info['courses']
        list_courses = ""
        for course in courses.split(","):
            num_class = re.findall('[0-9]+', course.strip())
            class_name = num_class[0]
            list_courses += "CPE " + str(class_name) + "\n"
        return "Tutoring is offered for:\n" + list_tutors

    #[PERSON] is currently the lead tutor.
    def lead_tutor(self):
        tutor_info = self.resources['tutor_info']
        lead = tutor_info['lead_tutor']
        return lead + " is currently the lead tutor."

    #Tutoring is held on [DATE] at [LOCATION] from [TIME] to [TIME]
    def tutor_meeting_info(self):
        tutor_info = self.resources['tutor_info']
        location = tutor_info['building'] + "-" + tutor_info['room']
        start_time = tutor_info['startTime']
        end_time = tutor_info['endTime']
        startDay = tutor_info['startDay']
        endDay = tutor_info['endDay']
        return "Tutoring is held from " + startDay + " to " + endDay + " at " + location + " from " + start_time + " to " + end_time

    #You can become a tutor if you've passed CPE 103. Email [PERSON] at [EMAIL] to schedule an interview.
    def become_a_tutor(self):
        tutor_info = self.resources['tutor_info']
        lead = tutor_info['lead_tutor']
        lead_email = tutor_info['contact_email']
        return "You can become a tutor if you've passed CPE 103. Email " + lead + " at " + lead_email + " to schedule an interview"

    #Please email the current lead tutor [PERSON] at [EMAIL] for more info.
    def tutoring_more_info(self):
        tutor_info = self.resources['tutor_info']
        lead = tutor_info['lead_tutor']
        lead_email = tutor_info['contact_email']
        return "Please email the current lead tutor " + lead + " at " + lead_email + " for more information"
        return None


    #Here are the list of official clubs within the Computer Science department: [CLUB]
    def list_of_clubs(self):
        clubs = self.resources['club']
        list_club = ""
        for club in clubs:
            list_club += club + "\n"
        return "Here are the list of official clubs within the Computer Science Department:\n" + list_club

    #Here's the club's website: [URL]
    def club_more_info(self, club):
        specific_club = self.resources['club'][club]
        url = specific_club['homepage']
        return "Here's the club's website: " + url

    #Here is a description of the club: [DESCRIPTION] works
    def club_description(self, club):
        specific_club = self.resources['club'][club]
        description = specific_club['description']
        return description

    #[CLUB] meets on [DAY] at [TIME] at [LOCATION]
    def club_meeting_info(self, club):
        # specific_club = self.resources['club'][club]
        # day = specific_club['meeting_day']
        # time = specific_club['meeting_time']
        # location = specific_club['location']
        # return club + " meets on " + day + " at " + time + " at " + location
        contact_email = self.resources['club']['contact_email']
        contact_person = self.resources['club']['contact_person']
        return "I am not sure when they meet. But you can contact " + contact_person + " for more information: " + contact_email
    
    #The current officers are: [OFFICER] works
    def club_officers(self, club):
        specific_club = self.resources['club'][club]
        club_officers = ""
        for officer, value in specific_club['officers'].items():
            club_officers += officer + " : " + value + ", "
        return club_officers

    #You can contact [PERSON] for more info: [EMAIL] [PHONE] works
    def club_contact(self, club):
        specific_club = self.resources['club'][club]
        contact_person = specific_club['contact_person']
        contact_email = specific_club['contact_email']
        contact_phone = specific_club['contact_phone']
        return "You can contact " + contact_person + " for more info: " + contact_email + " " + contact_phone

    #Here are the upcoming events: [EVENT]
    def list_of_club_events(self, club):
        specific_club = self.resources['club'][club]
        list_events = specific_club['event_list']
        events = ""
        for event in list_events:
            events += event + "\n"
        return "Here are the upcoming events: \n" + events

    #Here is a description of the event: [DESCRIPTION]
    def event_description(self, event):
        clubs = self.resources['club']
        for club in clubs:
            for event_name in club['event_list']:
                if event_name == event:
                    return event['description']

    #The event is taking place on [DATE] at [LOCATION] from [TIME] to [TIME]
    def event_meeting_info(self, event):
        clubs = self.resources['club']
        for club in clubs:
            for event_name in club['event_list']:
                if event_name == event:
                    event_date = event_name['event_date']
                    event_location = event_name['event_location']
                    event_start_time = event_name['event_start_time']
                    event_end_time = event_name['event_end_time']
                    return ("The event is taking palace on " + event_date + " at " + event_location 
                        + " from " + event_start_time + " to " + event_end_time)
        return "The event does not exist!"



    #Here is where the study sessions are being held: [LOCATION] works
    def study_sessions_location(self):
        study_session = self.resources['study_session']
        location = study_session['location']
        return "Here is where the study sessions are being held: " + location
    
    #Here is the study session coordinator: [PERSON] works
    def study_session_coordinator(self):
        study_session = self.resources['study_session']
        coordinator = study_session['coordinator']
        return "Here is the study session coordinator: " + coordinator
    
    #Here is the advisor of the club: [PERSON] [PHONE] [EMAIL] works
    def club_advisor(self, club):
        clubs = self.resources['club']
        specific_club = clubs[club]
        club_advisor = specific_club['advisor']
        club_advisor_phone = specific_club['advisor_phone']
        club_advisor_email = specific_club['advisor_email']
        return "Here is the advisor of the club: " + club_advisor + " "  + club_advisor_phone + " " + club_advisor_email

