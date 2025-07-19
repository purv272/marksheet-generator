from .models import Marksheet

def create_sample_data():
    sample_marksheet = Marksheet(
        student_id="23AIML076",
        student_name="VIRANI DAX JAYSUKHBHAI",
        institute="CHARUSAT",
        degree="BTECH (AIML)",
        semester="4",
        exam="April 2025",
        aiml206_theory="AB",
        aiml206_practical="AB",
        aiml207_theory="BC",
        aiml207_practical="BB",
        aiml208_theory="BB",
        aiml208_practical="AA",
        aiml209_theory="BB",
        aiml209_practical="AA",
        aiml210_theory="BC",
        aiml210_practical="BC",
        aiml211_practical="BB",
        hs11103a_practical="AB",
        it284_practical="AA"
    )
    sample_marksheet.save()
