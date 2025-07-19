from django.shortcuts import render

# Create your views here.

def teacher(request):
    # For now, redirect to login page
    from django.shortcuts import redirect
    return redirect('teacher_login')

def teacher_login(request):
    from django.shortcuts import redirect
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # For demonstration, simple static check
        if username == 'teacher' and password == 'password123':
            # Redirect to teacher dashboard page
            return redirect('teacher_dashboard')
        else:
            error = "Invalid username or password"
            return render(request, 'teacher_login.html', {'error': error})
    else:
        return render(request, 'teacher_login.html')

from .models import Marksheet
from django.shortcuts import redirect, render

from .sample_data import create_sample_data

def teacher_dashboard(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        institute = request.POST.get('institute')
        degree = request.POST.get('degree')
        semester = request.POST.get('semester')
        exam = request.POST.get('exam')

        aiml206_theory = request.POST.get('aiml206_theory')
        aiml206_practical = request.POST.get('aiml206_practical')

        aiml207_theory = request.POST.get('aiml207_theory')
        aiml207_practical = request.POST.get('aiml207_practical')

        aiml208_theory = request.POST.get('aiml208_theory')
        aiml208_practical = request.POST.get('aiml208_practical')

        aiml209_theory = request.POST.get('aiml209_theory')
        aiml209_practical = request.POST.get('aiml209_practical')

        aiml210_theory = request.POST.get('aiml210_theory')
        aiml210_practical = request.POST.get('aiml210_practical')

        aiml211_practical = request.POST.get('aiml211_practical')

        hs11103a_practical = request.POST.get('hs11103a_practical')

        it284_practical = request.POST.get('it284_practical')

        marksheet = Marksheet(
            student_id=student_id,
            student_name=student_name,
            institute=institute,
            degree=degree,
            semester=semester,
            exam=exam,
            aiml206_theory=aiml206_theory,
            aiml206_practical=aiml206_practical,
            aiml207_theory=aiml207_theory,
            aiml207_practical=aiml207_practical,
            aiml208_theory=aiml208_theory,
            aiml208_practical=aiml208_practical,
            aiml209_theory=aiml209_theory,
            aiml209_practical=aiml209_practical,
            aiml210_theory=aiml210_theory,
            aiml210_practical=aiml210_practical,
            aiml211_practical=aiml211_practical,
            hs11103a_practical=hs11103a_practical,
            it284_practical=it284_practical
        )
        marksheet.save()

        # Limit to most recent 5 marksheet entries in DB
        all_marksheets = Marksheet.objects.order_by('-id')
        if all_marksheets.count() > 5:
            for old_marksheet in all_marksheets[5:]:
                old_marksheet.delete()

        # Write most recent 5 marksheet data to a file
        import os
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marksheet_data.txt')
        with open(file_path, 'w') as f:
            recent_marksheets = Marksheet.objects.order_by('-id')[:5]
            for ms in recent_marksheets:
                f.write(f"Student ID: {ms.student_id}, Name: {ms.student_name}, Institute: {ms.institute}, Degree: {ms.degree}, Semester: {ms.semester}, Exam: {ms.exam}\n")
                f.write(f"AIML206 Theory: {ms.aiml206_theory}, Practical: {ms.aiml206_practical}\n")
                f.write(f"AIML207 Theory: {ms.aiml207_theory}, Practical: {ms.aiml207_practical}\n")
                f.write(f"AIML208 Theory: {ms.aiml208_theory}, Practical: {ms.aiml208_practical}\n")
                f.write(f"AIML209 Theory: {ms.aiml209_theory}, Practical: {ms.aiml209_practical}\n")
                f.write(f"AIML210 Theory: {ms.aiml210_theory}, Practical: {ms.aiml210_practical}\n")
                f.write(f"AIML211 Practical: {ms.aiml211_practical}\n")
                f.write(f"HS111.03 A Practical: {ms.hs11103a_practical}\n")
                f.write(f"IT284 Practical: {ms.it284_practical}\n")
                f.write("------------------------------------------------------------\n")

        return redirect('teacher_dashboard')
    else:
        # Create sample data if no data exists
        if not Marksheet.objects.exists():
            create_sample_data()

        marksheets = Marksheet.objects.all()
        return render(request, 'teacher_dashboard.html', {'marksheets': marksheets})

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse

def view_marksheet_file(request):
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marksheet_data.txt')
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Split entries by separator line
            entries = content.strip().split("------------------------------------------------------------")
            entries = [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        entries = []

    return render(request, 'view_marksheet_file.html', {'entries': entries})

@csrf_exempt
def delete_marksheet_entry(request, entry_index):
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marksheet_data.txt')
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            entries = content.strip().split("------------------------------------------------------------")
            entries = [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        entries = []

    try:
        index = int(entry_index)
        if 0 <= index < len(entries):
            entries.pop(index)
            # Rewrite file without the deleted entry
            with open(file_path, 'w') as f:
                for entry in entries:
                    f.write(entry + "\n------------------------------------------------------------\n")
    except ValueError:
        pass

    return HttpResponseRedirect(reverse('view_marksheet_file'))

def edit_marksheet_entry(request, entry_index):
    import os
    from django.shortcuts import get_object_or_404
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'marksheet_data.txt')
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            entries = content.strip().split("------------------------------------------------------------")
            entries = [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        entries = []

    if request.method == 'POST':
        # Update the marksheet entry in DB and file
        marksheet = get_object_or_404(Marksheet, pk=entry_index + 1)  # Assuming entry_index corresponds to pk-1
        marksheet.student_id = request.POST.get('student_id')
        marksheet.student_name = request.POST.get('student_name')
        marksheet.institute = request.POST.get('institute')
        marksheet.degree = request.POST.get('degree')
        marksheet.semester = request.POST.get('semester')
        marksheet.exam = request.POST.get('exam')
        marksheet.aiml206_theory = request.POST.get('aiml206_theory')
        marksheet.aiml206_practical = request.POST.get('aiml206_practical')
        marksheet.aiml207_theory = request.POST.get('aiml207_theory')
        marksheet.aiml207_practical = request.POST.get('aiml207_practical')
        marksheet.aiml208_theory = request.POST.get('aiml208_theory')
        marksheet.aiml208_practical = request.POST.get('aiml208_practical')
        marksheet.aiml209_theory = request.POST.get('aiml209_theory')
        marksheet.aiml209_practical = request.POST.get('aiml209_practical')
        marksheet.aiml210_theory = request.POST.get('aiml210_theory')
        marksheet.aiml210_practical = request.POST.get('aiml210_practical')
        marksheet.aiml211_practical = request.POST.get('aiml211_practical')
        marksheet.hs11103a_practical = request.POST.get('hs11103a_practical')
        marksheet.it284_practical = request.POST.get('it284_practical')
        marksheet.save()

        # Update the marksheet_data.txt file with recent 5 entries
        recent_marksheets = Marksheet.objects.order_by('-id')[:5]
        with open(file_path, 'w') as f:
            for ms in recent_marksheets:
                f.write(f"Student ID: {ms.student_id}, Name: {ms.student_name}, Institute: {ms.institute}, Degree: {ms.degree}, Semester: {ms.semester}, Exam: {ms.exam}\n")
                f.write(f"AIML206 Theory: {ms.aiml206_theory}, Practical: {ms.aiml206_practical}\n")
                f.write(f"AIML207 Theory: {ms.aiml207_theory}, Practical: {ms.aiml207_practical}\n")
                f.write(f"AIML208 Theory: {ms.aiml208_theory}, Practical: {ms.aiml208_practical}\n")
                f.write(f"AIML209 Theory: {ms.aiml209_theory}, Practical: {ms.aiml209_practical}\n")
                f.write(f"AIML210 Theory: {ms.aiml210_theory}, Practical: {ms.aiml210_practical}\n")
                f.write(f"AIML211 Practical: {ms.aiml211_practical}\n")
                f.write(f"HS111.03 A Practical: {ms.hs11103a_practical}\n")
                f.write(f"IT284 Practical: {ms.it284_practical}\n")
                f.write("------------------------------------------------------------\n")

        return HttpResponseRedirect(reverse('view_marksheet_file'))
    else:
        # GET request: show form with existing data
        marksheet = get_object_or_404(Marksheet, pk=entry_index + 1)
        return render(request, 'edit_marksheet_entry.html', {'marksheet': marksheet})
