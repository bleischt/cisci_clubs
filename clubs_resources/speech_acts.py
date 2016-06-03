#Speech acts represent single kernels of information that a user
#can request in various forms.
#Example:
#   ->Who is the advisor of pgr?
#   ->Which professor advises pgr?
#       ->[Advisor] advises [CLUB]

class SpeechActs:
    resources = {}

    def __init__(self, resources):
        self.resources = resources

    #There are currently [NUMBER] tutors
    def num_tutors():
        tutors = self.resources['TUTOR']
        num_tutors = 0
        for tutor in tutors:
            num_tutors += 1
        return "There are currently " + num_tutors + " tutors"


    #The tutors are: [PERSON]
    def list_of_tutors():
        tutors = self.resources['TUTOR']
        list_tutors = ""
        for tutor in tutors:
            list_tutors += tutor + "\n"
        return "The tutors are:\n" + list_tutors 


    #Here is some information about the tutor: [DESCRIPTION]
    def tutor_information(tutor):
        tutors = self.resources['TUTOR']
        specific_tutor = tutors[tutor]
        tutor_info = ""
        for info, value in specific_tutor.items():
            tutor_info += info + " : " + value + ", "
        return tutor_info

    #Tutor works on [DAY] at [TIME]
    def tutor_work_days(tutor):
        tutors = self.resources['TUTOR']
        specific_tutor = tutors[tutor]
        date = specific_tutor['work_date']
        return tutor + " works on " + date
        
    #Tutoring is offered for [COURSE]
    def courses_tutored():
        courses = self.resources['COURSE']
        list_courses = ""
        for course in courses:
            list_courses += course + "\n"
        return "Tutoring is offered for:\n" + list_tutors

    #[PERSON] is currently the lead tutor.
    def lead_tutor():
        tutor_info = self.resources['TUTOR_INFO']
        lead = tutor_info['lead']
        return lead + " is currently the lead tutor."

    #Tutoring is held on [DATE] in building [BUILDING] room [ROOM] from [TIME] to [TIME]
    def tutor_meeting_info():
        tutor_info = self.resources['TUTOR_INFO']
        date = tutor_info['tutor_date']
        building = tutor_info['tutor_building']
        room = tutor_info['tutor_room']
        start_time = tutor_info['tutor_start_time']
        end_time = tutor_info['tutor_end_time']
        return "Tutoring is held on " + date + " in building " + building + " room " + room + " from " + start_time + " to " + end_time

    #You can become a tutor if you've passed CPE 103. Email [PERSON] at [EMAIL] to schedule an interview.
    def become_a_tutor():
        tutor_info = self.resources['TUTOR_INFO']
        lead = tutor_info['lead']
        lead_email = tutor_info['lead_email']
        return "You can become a tutor if you've passed CPE 103. Email " + lead + " at " + lead_email + " to schedule an interview"

    #Please email the current lead tutor [PERSON] at [EMAIL] for more info.
    def tutoring_more_info():
        tutor_info = self.resources['TUTOR_INFO']
        lead = tutor_info['lead']
        lead_email = tutor_info['lead_email']
        return "Please email the current lead tutor " + lead + " at " + lead_email + " for more information"
        return None


    #Here are the list of official clubs within the Computer Science department: [CLUB]
    def list_of_clubs():
        clubs = self.resources['CLUB']
        list_club = ""
        for club in clubs:
            list_club += club + "\n"
        return "Here are the list of official clubs within the Computer Science Department:\n" + list_club

    #Here's the club's website: [URL]
    def club_more_info(club):
        specific_club = self.resources['CLUB'][club]
        url = specific_club['club_url']
        return "Here's the club's website: " + url

    #[DESCRIPTION]
    #(about section)
    def club_description(club):
        specific_club = self.resources['CLUB'][club]
        description = specific_club['description']
        return description

    #[CLUB] meets on [DAY] at [TIME] in building [BUILDING] room [ROOM]
    def club_meeting_info(club):
        specific_club = self.resources['CLUB'][club]
        day = specific_club['meeting_day']
        time = specific_club['meeting_time']
        building = specific_club['meeting_building']
        room = specific_club['meeting_room']
        return club + " meets on " + day + " at " + time + " in building " + building + " room " + room

    #The current officers are: [OFFICER]
    def club_officers(club):
        specific_club = self.resources['CLUB'][club]
        club_officers = ""
        for officer, value in specific_club['officers'].items():
            club_officers += officer + " : " + value + ", "
        return club_officers

    #You can contact [PERSON] for more info: [EMAIL] [PHONE]
    def club_contact(club):
        specific_club = self.resources['CLUB'][club]
        contact_person = specific_club['contact_person']
        contact_email = specific_club['contact_email']
        contact_phone = specific_club['contact_phone']
        return "You can contact " + contact_person + " for more info: " + contact_email + " " + contact_phone

    #Here are the upcoming events: [EVENT]
    def list_of_club_events(club):
        specific_club = self.resources['CLUB'][club]
        list_events = specific_club['club_events_list']
        events = ""
        for event in list_events:
            events += event + "\n"
        return "Here are the upcoming events: \n" + events

    #[DESCRIPTION]
    def event_description(event):
        clubs = self.resources['CLUB']
        for club in clubs:
            for event_name in club['club_events_list']:
                if event_name == event:
                    return event['description']

    #The event is taking place on [DATE] in building [BUILDING] room [ROOM] from [TIME] to [TIME]
    def event_meeting_info(event):
        clubs = self.resources['CLUB']
        for club in clubs:
            for event_name in club['club_events_list']:
                if event_name == event:
                    event_date = event_name['event_date']
                    event_building = event_name['event_building']
                    event_room = event_name['event_room']
                    event_start_time = event_name['event_start_time']
                    event_end_time = event_name['event_end_time']
                    return ("The event is taking palce on " + event_date + " in building " 
                        + event_building + " room " + event_room + " from " + event_start_time + " to " + event_end_time)