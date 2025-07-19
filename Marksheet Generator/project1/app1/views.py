from django.http import HttpResponse
from django.shortcuts import render
from app2.models import Marksheet
from datetime import datetime

GRADE_POINTS = {
    'AA': 10,
    'AB': 9,
    'BB': 8,
    'BC': 7,
    'CC': 6,
    'CD': 5,
    'DD': 4,
    'FF': 0,
}

NUMERIC_TO_LETTER_GRADE = {
    '1': 'AA',
    '2': 'AB',
    '3': 'BB',
    '4': 'BC',
    '5': 'CC',
    '6': 'CD',
    '7': 'DD',
    '8': 'FF',
}

def calculate_sgpa(courses):
    total_credits = 0
    total_points = 0
    backlogs = 0
    for course in courses:
        credit = float(course['credit'])
        grade = course['grade']
        if grade:
            grade = grade.strip().upper()
        else:
            grade = ''
        grade_point = GRADE_POINTS.get(grade, 0)
        total_credits += credit
        total_points += credit * grade_point
        if grade == 'FF':
            backlogs += 1
    sgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0
    return sgpa, total_credits, backlogs

def calculate_cgpa(previous_credits, previous_cgpa, current_credits, sgpa):
    if previous_credits + current_credits == 0:
        return 0
    cgpa = ((previous_credits * previous_cgpa) + (current_credits * sgpa)) / (previous_credits + current_credits)
    return round(cgpa, 2)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def student(request):
    if request.method == 'POST':
        institute = request.POST.get('institute')
        degree = request.POST.get('degree')
        semester = request.POST.get('semester')
        exam = request.POST.get('exam')
        student_id = request.POST.get('student_id')

        marksheets = Marksheet.objects.filter(
            student_id=student_id,
            degree=degree,
            semester=semester,
            exam=exam,
            institute=institute
        )

        if not marksheets.exists():
            context = {
                'message': 'No marksheet data found for the given details.'
            }
            return render(request, 'student_result.html', context)

        student_name = marksheets.first().student_name
        marksheet = marksheets.first()

        def map_grade(grade):
            if grade is None:
                return ''
            grade_str = str(grade).strip()
            # If grade is numeric, map to letter grade
            if grade_str in NUMERIC_TO_LETTER_GRADE:
                return NUMERIC_TO_LETTER_GRADE[grade_str]
            # Otherwise, assume it's already a letter grade
            return grade_str

        # Prepare course data list with mapped letter grades
        courses = [
            {'code': 'AIML206', 'title': 'DATABASE MANAGEMENT SYSTEM', 'component': 'THEORY', 'credit': 3.00, 'grade': map_grade(marksheet.aiml206_theory)},
            {'code': 'AIML206', 'title': 'DATABASE MANAGEMENT SYSTEM', 'component': 'PRACTICAL', 'credit': 1.00, 'grade': map_grade(marksheet.aiml206_practical)},
            {'code': 'AIML207', 'title': 'DESIGN & ANALYSIS OF ALGORITHMS', 'component': 'THEORY', 'credit': 3.00, 'grade': map_grade(marksheet.aiml207_theory)},
            {'code': 'AIML207', 'title': 'DESIGN & ANALYSIS OF ALGORITHMS', 'component': 'PRACTICAL', 'credit': 1.00, 'grade': map_grade(marksheet.aiml207_practical)},
            {'code': 'AIML208', 'title': 'OPERATING SYSTEM', 'component': 'THEORY', 'credit': 3.00, 'grade': map_grade(marksheet.aiml208_theory)},
            {'code': 'AIML208', 'title': 'OPERATING SYSTEM', 'component': 'PRACTICAL', 'credit': 1.00, 'grade': map_grade(marksheet.aiml208_practical)},
            {'code': 'AIML209', 'title': 'PROBABILISTIC MODELLING AND REASONING WITH PYTHON', 'component': 'THEORY', 'credit': 3.00, 'grade': map_grade(marksheet.aiml209_theory)},
            {'code': 'AIML209', 'title': 'PROBABILISTIC MODELLING AND REASONING WITH PYTHON', 'component': 'PRACTICAL', 'credit': 1.00, 'grade': map_grade(marksheet.aiml209_practical)},
            {'code': 'AIML210', 'title': 'R PROGRAMMING FOR DATA SCIENCE AND DATA ANALYSIS', 'component': 'THEORY', 'credit': 2.00, 'grade': map_grade(marksheet.aiml210_theory)},
            {'code': 'AIML210', 'title': 'R PROGRAMMING FOR DATA SCIENCE AND DATA ANALYSIS', 'component': 'PRACTICAL', 'credit': 1.00, 'grade': map_grade(marksheet.aiml210_practical)},
            {'code': 'AIML211', 'title': 'PROJECT - I', 'component': 'PRACTICAL', 'credit': 2.00, 'grade': map_grade(marksheet.aiml211_practical)},
            {'code': 'HS111.03 A', 'title': 'HUMAN VALUES AND ETHICS', 'component': 'PRACTICAL', 'credit': 2.00, 'grade': map_grade(marksheet.hs11103a_practical)},
            {'code': 'IT284', 'title': 'DATA VISUALIZATION', 'component': 'PRACTICAL', 'credit': 2.00, 'grade': map_grade(marksheet.it284_practical)},
        ]

        sgpa, _, backlogs = calculate_sgpa(courses)

        context = {
            'university_name': 'CHARUSAT',
            'faculty_name': 'FACULTY OF TECHNOLOGY AND ENGINEERING',
            'programme_name': degree,
            'semester': semester,
            'month_year': exam,
            'student_name': student_name,
            'student_id': student_id,
            'courses': courses,
            'sgpa': sgpa,
            'backlogs': backlogs,
            'print_date': datetime.now().strftime('%d/%m/%Y'),
        }
        return render(request, 'student_result.html', context)
    else:
        return render(request, 'student.html')
