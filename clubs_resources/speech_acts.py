

#Speech acts represent single kernels of information that a user
#can request in various forms.
#Example:
#   ->Who is the advisor of pgr?
#   ->Which professor advises pgr?
#       ->[Advisor] advises [CLUB]


class SpeechActs:



    #[CLUB] meets at [LOCATION] on [DAY] at [TIME]
    def club_meeting_info(club):
        return None


    #There are currently [NUMBER] tutors
    def num_tutors():
        return None


    #The tutors are: [PERSON]
    def list_of_tutors():
        return None


    #[DESCRIPTION]
    def tutor_information():
        return None

    #[PERSON] works on [DATE]
    def tutor_work_days(tutor):
        return None

    #Tutoring is offered for [COURSE]
    def courses_tutored():
        return None

    #[PERSON] is currently the lead tutor.
    def lead_tutor():
        return None

    #Tutoring is held on [DATE] in building [BUILDING] room [ROOM] from [TIME] to [TIME]
    def tutor_meeting_info():
        return None

    #You can become a tutor if you've passed CPE 103. Email [PERSON] at [EMAIL] to schedule an interview.
    def become_a_tutor():
        return None

    #Please email the current lead tutor [PERSON] at [EMAIL] for more info.
    def tutoring_more_info():
        return None


    #Here are the list of official clubs within the Computer Science department: [CLUB]
    def list_of_clubs():
        return None

    #Here's the club's website: [URL]
    def club_more_info(club):
        return None

    #[DESCRIPTION]
    #(about section)
    def club_description(club):
        return None

    #The current officers are: [OFFICER]
    def club_officers(club):
        return None

    #You can contact [PERSON] for more info: [EMAIL] [PHONE]
    def club_contact(club):
        return None

    #Here are the upcoming events: [EVENT]
    def list_of_club_events(club):
        return None

    #[DESCRIPTION]
    def event_description(event):
        return None

    #The event is taking place on [DATE] in building [BUILDING] room [ROOM] from [TIME] to [TIME]
    def event_meeting_info(event):
        return None
