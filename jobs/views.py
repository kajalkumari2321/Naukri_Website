from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
import urllib.parse

from .models import Job, UserProfile, JobApplication, Review, EmployeeReview, CandidateRating
from .forms import CandidateRatingForm, EmployeeReviewForm



def home(request):
    search_query = request.GET.get('search', '')

    if search_query:
        jobs = Job.objects.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    else:
        jobs = Job.objects.all()

    jobs = jobs.order_by('-posted_date')

    seekers = UserProfile.objects.filter(
        role='seeker'
    ).exclude(resume_headline='').order_by('-id')[:6]

    return render(request, 'home.html', {
        'jobs': jobs,
        'seekers': seekers
    })


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, JobApplication, UserProfile

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    # Get or create user profile with default role as seeker
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'seeker'}
    )

    # Check if user is a seeker
    if profile.role != 'seeker':
        messages.warning(request, 'Only job seekers can apply.')
        return redirect('job_detail', pk=pk)

    # Prevent duplicate applications
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=pk)

    # Create application
    JobApplication.objects.create(
        job=job,
        applicant=request.user
    )

    messages.success(request, 'Application submitted successfully!')
    return redirect('seeker_dashboard')


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    reviews = job.reviews.filter(approved=True)

    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating and comment:
            Review.objects.create(
                job=job,
                user=request.user,
                rating=rating,
                comment=comment
            )
            messages.success(request, 'Review submitted! Waiting for admin approval.')
        else:
            messages.error(request, 'Please provide rating and comment.')

        return redirect('job_detail', pk=pk)

    return render(request, 'job_detail.html', {
        'job': job,
        'reviews': reviews
    })


def company_profile(request, company_name):
    company_name = urllib.parse.unquote(company_name)
    jobs = Job.objects.filter(company__iexact=company_name)

    if not jobs.exists():
        messages.warning(request, f'No jobs found for {company_name}')

    return render(request, 'company_profile.html', {
        'company_name': company_name,
        'jobs': jobs
    })


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        phone = request.POST.get('phone', '')
        company_name = request.POST.get('company_name', '')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role,
            phone=phone,
            company_name=company_name
        )

        messages.success(request, 'Registration successful! Please login.')
        return redirect('login_view')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            profile = get_object_or_404(UserProfile, user=user)

            if profile.role == 'employer':
                return redirect('employer_dashboard')
            return redirect('seeker_dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def seeker_dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user, role='seeker')
    applications = JobApplication.objects.filter(
        applicant=request.user
    ).order_by('-applied_date')

    # Calculate statistics
    total_applications = applications.count()
    pending_applications = applications.filter(status='pending').count()
    shortlisted_applications = applications.filter(status='shortlisted').count()
    rejected_applications = applications.filter(status='rejected').count()
    
    # Get all available jobs for recommendations
    total_jobs = Job.objects.count()
    
    # Jobs matching user's skills (recommendations)
    recommended_jobs = 0
    if profile.key_skills:
        skills = [s.strip().lower() for s in profile.key_skills.split(',')[:3]]
        for skill in skills:
            recommended_jobs += Job.objects.filter(
                Q(title__icontains=skill) | Q(description__icontains=skill)
            ).distinct().count()

    if request.method == 'POST':
        fields = [
            'phone', 'whatsapp', 'resume_headline', 'key_skills',
            'employment', 'degree', 'education', 'it_skills',
            'projects', 'profile_summary', 'accomplishments',
            'career_profile', 'speaks', 'location',
            'expected_salary', 'gender', 'marital_status', 'address'
        ]

        for field in fields:
            setattr(profile, field, request.POST.get(field, getattr(profile, field)))

        if request.POST.get('date_of_birth'):
            profile.date_of_birth = request.POST.get('date_of_birth')

        if request.FILES.get('resume'):
            profile.resume = request.FILES['resume']

        if request.FILES.get('aadhar_card'):
            profile.aadhar_card = request.FILES['aadhar_card']

        if request.FILES.get('bank_documents'):
            profile.bank_documents = request.FILES['bank_documents']

        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('seeker_dashboard')

    return render(request, 'seeker_dashboard.html', {
        'profile': profile,
        'applications': applications,
        'total_applications': total_applications,
        'pending_applications': pending_applications,
        'shortlisted_applications': shortlisted_applications,
        'rejected_applications': rejected_applications,
        'total_jobs': total_jobs,
        'recommended_jobs': recommended_jobs,
    })


@login_required
def employer_dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user, role='employer')
    jobs = Job.objects.filter(employer=request.user).order_by('-posted_date')

    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            location=request.POST.get('location'),
            salary=request.POST.get('salary'),
            description=request.POST.get('description'),
            employer=request.user
        )

        messages.success(request, 'Job posted successfully!')
        return redirect('employer_dashboard')

    return render(request, 'employer_dashboard.html', {
        'profile': profile,
        'jobs': jobs
    })


def seeker_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user, role='seeker')

    return render(request, 'seeker_profile.html', {
        'profile': profile
    })


def about_us(request):
    return render(request, 'about_us.html')


def rating_options(request):
    """Rating options page - choose between employee review or company rating"""
    return render(request, 'rating_options.html')


def contact_us(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you! Your message has been sent successfully.')
        return redirect('contact_us')

    return render(request, 'contact_us.html')


@login_required
def notifications(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile.role == 'employer':
        applications = JobApplication.objects.filter(
            job__employer=request.user
        ).order_by('-applied_date')
    else:
        applications = JobApplication.objects.filter(
            applicant=request.user
        ).order_by('-applied_date')

    return render(request, 'notifications.html', {
        'applications': applications
    })


@login_required
def candidates_list(request):
    # Get or create profile
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'employer'}
    )
    
    if profile.role != 'employer':
        messages.warning(request, 'Only employers can view candidates.')
        return redirect('home')

    # Start with all seekers
    seekers = UserProfile.objects.filter(role='seeker')

    # Filter by location
    location = request.GET.get('location', '')
    if location:
        seekers = seekers.filter(location__icontains=location)

    # Filter by salary budget
    min_salary = request.GET.get('min_salary', '')
    max_salary = request.GET.get('max_salary', '')
    if min_salary:
        seekers = seekers.filter(expected_salary__gte=min_salary)
    if max_salary:
        seekers = seekers.filter(expected_salary__lte=max_salary)

    # Filter by skills
    skills = request.GET.get('skills', '')
    if skills:
        skill_list = [s.strip() for s in skills.split(',')]
        for skill in skill_list:
            seekers = seekers.filter(key_skills__icontains=skill)

    # Filter by status (database status)
    status = request.GET.get('status', 'all')
    # Note: You can extend this with actual status field in UserProfile model
    # For now, all candidates are shown as "live"

    # Sort options
    sort_by = request.GET.get('sort', 'recent')
    if sort_by == 'name':
        seekers = seekers.order_by('user__username')
    elif sort_by == 'experience':
        seekers = seekers.order_by('-work_experience')
    elif sort_by == 'salary':
        seekers = seekers.order_by('-expected_salary')
    else:  # recent
        seekers = seekers.order_by('-id')

    # Process skills for display (split into list)
    seekers_with_skills = []
    for seeker in seekers:
        seeker_data = {
            'seeker': seeker,
            'skills_list': []
        }
        if seeker.key_skills:
            skills_raw = seeker.key_skills.split(',')
            seeker_data['skills_list'] = [s.strip() for s in skills_raw[:5]]  # First 5 skills
        seekers_with_skills.append(seeker_data)

    return render(request, 'candidates_list.html', {
        'seekers': seekers,
        'seekers_with_skills': seekers_with_skills
    })


def add_review(request):
    """Employee reviews their company"""
    if request.method == 'POST':
        try:
            # Handle recommend field properly
            recommend_value = request.POST.get('recommend', 'no')
            recommend_bool = True if recommend_value == 'yes' else False
            
            EmployeeReview.objects.create(
                full_name=request.POST.get('full_name', ''),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile', ''),
                employee_type=request.POST.get('employee_type'),
                designation=request.POST.get('designation'),
                department=request.POST.get('department'),
                employment_type=request.POST.get('employment_type'),
                working_duration=request.POST.get('working_duration'),
                work_location=request.POST.get('work_location'),
                work_environment=int(request.POST.get('work_environment')),
                salary_benefits=int(request.POST.get('salary_benefits')),
                management_support=int(request.POST.get('management_support')),
                job_security=int(request.POST.get('job_security')),
                career_growth=int(request.POST.get('career_growth')),
                work_life_balance=int(request.POST.get('work_life_balance')),
                pros=request.POST.get('pros'),
                cons=request.POST.get('cons'),
                recommend=recommend_bool
            )
            messages.success(request, '✅ Thank you! Your review has been submitted successfully.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'❌ Error submitting review: {str(e)}')

    return render(request, 'employee_review.html')


def add_candidate_rating(request):
    """Company rates their employee/candidate"""
    # Get or create profile
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to rate employees.')
        return redirect('login_view')
    
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'employer'}
    )
    
    if profile.role != 'employer':
        messages.warning(request, 'Only employers can rate employees.')
        return redirect('home')

    if request.method == 'POST':
        try:
            employment_status = request.POST.get('employment_status')
            
            # Work performance fields are optional for rejected candidates
            work_quality = request.POST.get('work_quality', 3)
            punctuality = request.POST.get('punctuality', 3)
            teamwork = request.POST.get('teamwork', 3)
            learning_ability = request.POST.get('learning_ability', 3)
            responsibility_level = request.POST.get('responsibility_level', 3)
            target_achievement = request.POST.get('target_achievement', 3)
            
            # Convert to int, use default if empty
            work_quality = int(work_quality) if work_quality else 3
            punctuality = int(punctuality) if punctuality else 3
            teamwork = int(teamwork) if teamwork else 3
            learning_ability = int(learning_ability) if learning_ability else 3
            responsibility_level = int(responsibility_level) if responsibility_level else 3
            target_achievement = int(target_achievement) if target_achievement else 3
            
            CandidateRating.objects.create(
                candidate_id=request.POST.get('candidate'),
                job_id=request.POST.get('job'),
                rated_by=request.user,
                interview_date=request.POST.get('interview_date'),
                employment_status=employment_status,
                communication_skills=int(request.POST.get('communication_skills')),
                technical_knowledge=int(request.POST.get('technical_knowledge')),
                confidence_level=int(request.POST.get('confidence_level')),
                professional_behaviour=int(request.POST.get('professional_behaviour')),
                work_quality=work_quality,
                punctuality=punctuality,
                teamwork=teamwork,
                learning_ability=learning_ability,
                responsibility_level=responsibility_level,
                target_achievement=target_achievement,
                recommendation=request.POST.get('recommendation'),
                strengths=request.POST.get('strengths'),
                areas_of_improvement=request.POST.get('areas_of_improvement')
            )
            messages.success(request, '✅ Employee rating submitted successfully!')
            return redirect('employer_dashboard')
        except Exception as e:
            messages.error(request, f'❌ Error submitting rating: {str(e)}')

    # Get all users and jobs for the form
    users = User.objects.filter(userprofile__role='seeker')
    jobs = Job.objects.filter(employer=request.user)

    return render(request, 'candidate_rating.html', {
        'users': users,
        'jobs': jobs
    })


