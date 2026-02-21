import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobhai.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job, UserProfile
from datetime import date

# 10 Employers create karo
employers_data = [
    {'username': 'tcs_hr', 'email': 'hr@tcs.com', 'company': 'TCS', 'phone': '9876543210'},
    {'username': 'infosys_hr', 'email': 'hr@infosys.com', 'company': 'Infosys', 'phone': '9876543211'},
    {'username': 'wipro_hr', 'email': 'hr@wipro.com', 'company': 'Wipro', 'phone': '9876543212'},
    {'username': 'amazon_hr', 'email': 'hr@amazon.com', 'company': 'Amazon India', 'phone': '9876543213'},
    {'username': 'flipkart_hr', 'email': 'hr@flipkart.com', 'company': 'Flipkart', 'phone': '9876543214'},
    {'username': 'google_hr', 'email': 'hr@google.com', 'company': 'Google India', 'phone': '9876543215'},
    {'username': 'microsoft_hr', 'email': 'hr@microsoft.com', 'company': 'Microsoft', 'phone': '9876543216'},
    {'username': 'accenture_hr', 'email': 'hr@accenture.com', 'company': 'Accenture', 'phone': '9876543217'},
    {'username': 'cognizant_hr', 'email': 'hr@cognizant.com', 'company': 'Cognizant', 'phone': '9876543218'},
    {'username': 'hcl_hr', 'email': 'hr@hcl.com', 'company': 'HCL Technologies', 'phone': '9876543219'},
]

# 10 Job Seekers create karo
seekers_data = [
    {'username': 'rahul_sharma', 'email': 'rahul@gmail.com', 'first_name': 'Rahul', 'last_name': 'Sharma', 'phone': '8765432101', 'location': 'Delhi', 'degree': 'B.Tech in Computer Science', 'skills': 'Python, Django, React', 'headline': 'Full Stack Developer with 2 years experience'},
    {'username': 'priya_singh', 'email': 'priya@gmail.com', 'first_name': 'Priya', 'last_name': 'Singh', 'phone': '8765432102', 'location': 'Mumbai', 'degree': 'MBA in Marketing', 'skills': 'Digital Marketing, SEO, Content Strategy', 'headline': 'Digital Marketing Specialist'},
    {'username': 'amit_kumar', 'email': 'amit@gmail.com', 'first_name': 'Amit', 'last_name': 'Kumar', 'phone': '8765432103', 'location': 'Bangalore', 'degree': 'M.Tech in Data Science', 'skills': 'Python, Machine Learning, SQL', 'headline': 'Data Scientist with AI expertise'},
    {'username': 'sneha_patel', 'email': 'sneha@gmail.com', 'first_name': 'Sneha', 'last_name': 'Patel', 'phone': '8765432104', 'location': 'Pune', 'degree': 'B.Des in UI/UX', 'skills': 'Figma, Adobe XD, Prototyping', 'headline': 'Creative UI/UX Designer'},
    {'username': 'vikash_yadav', 'email': 'vikash@gmail.com', 'first_name': 'Vikash', 'last_name': 'Yadav', 'phone': '8765432105', 'location': 'Hyderabad', 'degree': 'B.A in English', 'skills': 'Content Writing, Copywriting, SEO', 'headline': 'Professional Content Writer'},
    {'username': 'anjali_verma', 'email': 'anjali@gmail.com', 'first_name': 'Anjali', 'last_name': 'Verma', 'phone': '8765432106', 'location': 'Chennai', 'degree': 'BBA in Sales', 'skills': 'Sales, Client Management, CRM', 'headline': 'Sales Executive with proven track record'},
    {'username': 'rohit_gupta', 'email': 'rohit@gmail.com', 'first_name': 'Rohit', 'last_name': 'Gupta', 'phone': '8765432107', 'location': 'Kolkata', 'degree': 'B.Tech in IT', 'skills': 'Java, Spring Boot, Microservices', 'headline': 'Backend Developer'},
    {'username': 'pooja_jain', 'email': 'pooja@gmail.com', 'first_name': 'Pooja', 'last_name': 'Jain', 'phone': '8765432108', 'location': 'Jaipur', 'degree': 'BCA', 'skills': 'HTML, CSS, JavaScript, Bootstrap', 'headline': 'Frontend Developer'},
    {'username': 'sanjay_mishra', 'email': 'sanjay@gmail.com', 'first_name': 'Sanjay', 'last_name': 'Mishra', 'phone': '8765432109', 'location': 'Lucknow', 'degree': 'B.Com with Tally', 'skills': 'Accounting, Tally, GST, Excel', 'headline': 'Accountant with 3 years experience'},
    {'username': 'kavita_reddy', 'email': 'kavita@gmail.com', 'first_name': 'Kavita', 'last_name': 'Reddy', 'phone': '8765432110', 'location': 'Ahmedabad', 'degree': 'MBA in HR', 'skills': 'Recruitment, HR Management, Training', 'headline': 'HR Manager'},
]

# Jobs data for each employer
jobs_data = [
    {'title': 'Software Engineer', 'location': 'Noida', 'salary': '₹6-8 LPA', 'description': 'Looking for skilled software engineer with Java/Python experience', 'image': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800'},
    {'title': 'Senior Developer', 'location': 'Bangalore', 'salary': '₹10-15 LPA', 'description': 'Experienced developer needed for enterprise projects', 'image': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800'},
    {'title': 'Project Manager', 'location': 'Pune', 'salary': '₹12-18 LPA', 'description': 'Lead technical projects and manage teams', 'image': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800'},
    {'title': 'Cloud Engineer', 'location': 'Hyderabad', 'salary': '₹8-12 LPA', 'description': 'AWS/Azure cloud infrastructure specialist needed', 'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800'},
    {'title': 'Data Analyst', 'location': 'Mumbai', 'salary': '₹5-7 LPA', 'description': 'Analyze business data and create insights', 'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800'},
    {'title': 'Product Manager', 'location': 'Gurgaon', 'salary': '₹15-20 LPA', 'description': 'Drive product strategy and roadmap', 'image': 'https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800'},
    {'title': 'DevOps Engineer', 'location': 'Bangalore', 'salary': '₹9-14 LPA', 'description': 'CI/CD pipeline and infrastructure automation', 'image': 'https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a?w=800'},
    {'title': 'Business Analyst', 'location': 'Chennai', 'salary': '₹6-9 LPA', 'description': 'Bridge between business and technology teams', 'image': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800'},
    {'title': 'QA Engineer', 'location': 'Noida', 'salary': '₹4-6 LPA', 'description': 'Manual and automation testing expertise required', 'image': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800'},
    {'title': 'Tech Lead', 'location': 'Pune', 'salary': '₹18-25 LPA', 'description': 'Lead technical team and architecture decisions', 'image': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800'},
]

print("Starting user and job creation...\n")

# Create Employers
print("Creating 10 Employers...")
for i, emp_data in enumerate(employers_data):
    user, created = User.objects.get_or_create(
        username=emp_data['username'],
        defaults={
            'email': emp_data['email'],
            'first_name': emp_data['company'].split()[0],
            'last_name': 'HR'
        }
    )
    if created:
        user.set_password('password123')
        user.save()
        
        UserProfile.objects.create(
            user=user,
            role='employer',
            phone=emp_data['phone'],
            company_name=emp_data['company']
        )
        
        # Create job for this employer
        Job.objects.create(
            title=jobs_data[i]['title'],
            company=emp_data['company'],
            location=jobs_data[i]['location'],
            salary=jobs_data[i]['salary'],
            description=jobs_data[i]['description'],
            image=jobs_data[i]['image'],
            employer=user
        )
        print(f"[OK] {emp_data['company']} - {emp_data['username']} created with job: {jobs_data[i]['title']}")
    else:
        print(f"[SKIP] {emp_data['username']} already exists")

print("\nCreating 10 Job Seekers...")
for seeker_data in seekers_data:
    user, created = User.objects.get_or_create(
        username=seeker_data['username'],
        defaults={
            'email': seeker_data['email'],
            'first_name': seeker_data['first_name'],
            'last_name': seeker_data['last_name']
        }
    )
    if created:
        user.set_password('password123')
        user.save()
        
        UserProfile.objects.create(
            user=user,
            role='seeker',
            phone=seeker_data['phone'],
            location=seeker_data['location'],
            degree=seeker_data['degree'],
            key_skills=seeker_data['skills'],
            resume_headline=seeker_data['headline'],
            date_of_birth=date(1995, 1, 1),
            gender='Male' if seeker_data['first_name'] in ['Rahul', 'Amit', 'Vikash', 'Rohit', 'Sanjay'] else 'Female'
        )
        print(f"[OK] {seeker_data['first_name']} {seeker_data['last_name']} - {seeker_data['username']} created")
    else:
        print(f"[SKIP] {seeker_data['username']} already exists")

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Total Employers: {User.objects.filter(userprofile__role='employer').count()}")
print(f"Total Job Seekers: {User.objects.filter(userprofile__role='seeker').count()}")
print(f"Total Jobs Posted: {Job.objects.count()}")
print("\nLogin Credentials:")
print("   Username: (any username above)")
print("   Password: password123")
print("\nDone! Visit http://127.0.0.1:8000/ to see all jobs and seekers!")
