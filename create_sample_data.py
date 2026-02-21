import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobhai.settings')
django.setup()

from jobs.models import Job, UserProfile, JobApplication
from django.contrib.auth.models import User

# Sample data for realistic profiles
FIRST_NAMES = ['Raj', 'Priya', 'Amit', 'Sneha', 'Rahul', 'Anjali', 'Vikram', 'Pooja', 'Arjun', 'Neha', 
               'Karan', 'Riya', 'Sanjay', 'Kavita', 'Rohan', 'Divya', 'Aditya', 'Shreya', 'Manish', 'Sakshi']

LAST_NAMES = ['Kumar', 'Sharma', 'Singh', 'Patel', 'Gupta', 'Verma', 'Reddy', 'Joshi', 'Mehta', 'Nair',
              'Rao', 'Desai', 'Iyer', 'Malhotra', 'Kapoor', 'Agarwal', 'Pandey', 'Mishra', 'Jain', 'Shah']

CITIES = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Ahmedabad', 
          'Jaipur', 'Lucknow', 'Chandigarh', 'Indore', 'Nagpur', 'Surat', 'Vadodara']

SKILLS = [
    'Python, Django, REST API, PostgreSQL',
    'Java, Spring Boot, Microservices, MySQL',
    'React, Node.js, MongoDB, Express',
    'MS Excel, Tally Prime, GST Filing, Accounting',
    'Digital Marketing, SEO, Google Ads, Social Media',
    'Data Analysis, SQL, Power BI, Excel',
    'UI/UX Design, Figma, Adobe XD, Photoshop',
    'Sales, CRM, Lead Generation, Client Management',
    'HR Management, Recruitment, Employee Relations',
    'Content Writing, Copywriting, SEO Writing'
]

HEADLINES = [
    'Experienced Software Developer with 3+ years in Python',
    'Full Stack Developer specializing in MERN Stack',
    'Certified Accountant with Tally and GST expertise',
    'Digital Marketing Professional with proven ROI',
    'Data Analyst with strong SQL and visualization skills',
    'Creative UI/UX Designer with modern design approach',
    'Sales Executive with excellent client relationship skills',
    'HR Professional with recruitment and training experience',
    'Content Writer with SEO optimization expertise',
    'Business Analyst with domain knowledge in Finance'
]

DEGREES = ['BCA', 'B.Com', 'MBA', 'MCA', 'B.Tech', 'M.Tech', 'BA', 'MA', 'BBA', '12th Pass']

COMPANIES = ['TCS', 'Infosys', 'Wipro', 'Accenture', 'Cognizant', 'HCL', 'Tech Mahindra', 
             'Capgemini', 'IBM', 'Oracle', 'Amazon', 'Flipkart', 'Paytm', 'Zomato', 'Swiggy']

def create_sample_users_and_profiles(count=20):
    """Create sample job seekers with complete profiles"""
    print(f"\n🚀 Creating {count} sample job seekers...")
    
    created_count = 0
    for i in range(count):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        username = f"{first_name.lower()}{last_name.lower()}{random.randint(100, 999)}"
        email = f"{username}@example.com"
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            continue
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password='demo123',
            first_name=first_name,
            last_name=last_name
        )
        
        # Create profile with complete data
        profile = UserProfile.objects.create(
            user=user,
            role='seeker',
            phone=f'+91 {random.randint(7000000000, 9999999999)}',
            whatsapp=f'+91 {random.randint(7000000000, 9999999999)}',
            resume_headline=random.choice(HEADLINES),
            key_skills=random.choice(SKILLS),
            employment=f'{random.choice(COMPANIES)}, Software Engineer, {random.randint(1, 5)} years',
            degree=random.choice(DEGREES),
            education=f'University of {random.choice(CITIES)}, {random.randint(2015, 2022)}, {random.randint(60, 95)}%',
            it_skills='MS Office, Python, SQL, Git',
            projects='E-commerce Website, Inventory Management System',
            profile_summary=f'Experienced professional with {random.randint(1, 8)} years in the industry.',
            accomplishments='Employee of the Month, Best Performance Award',
            career_profile='Looking for challenging opportunities in tech industry',
            speaks='Hindi, English, Marathi',
            location=random.choice(CITIES),
            expected_salary=f'₹{random.randint(3, 15)}-{random.randint(16, 25)} LPA',
            gender=random.choice(['Male', 'Female']),
            marital_status=random.choice(['Single', 'Married']),
            address=f'{random.randint(1, 999)}, {random.choice(CITIES)}, India',
            work_experience=f'{random.randint(0, 10)} years'
        )
        
        created_count += 1
        print(f"✅ Created: {user.get_full_name()} ({username})")
    
    print(f"\n🎉 Total {created_count} job seekers created!")
    return created_count

def create_sample_jobs(count=15):
    """Create sample jobs"""
    print(f"\n🚀 Creating {count} sample jobs...")
    
    # Get or create employer
    employer, created = User.objects.get_or_create(
        username='employer_demo',
        defaults={
            'email': 'employer@demo.com',
            'first_name': 'Demo',
            'last_name': 'Employer'
        }
    )
    
    if created:
        employer.set_password('demo123')
        employer.save()
    
    job_titles = [
        'Python Developer', 'Java Developer', 'Full Stack Developer', 'Data Analyst',
        'UI/UX Designer', 'Digital Marketing Manager', 'Business Analyst', 'DevOps Engineer',
        'Sales Executive', 'HR Manager', 'Content Writer', 'Accountant', 'Project Manager',
        'Software Tester', 'Network Engineer'
    ]
    
    created_count = 0
    for title in job_titles[:count]:
        company = random.choice(COMPANIES)
        
        # Check if job already exists
        if Job.objects.filter(title=title, company=company).exists():
            continue
        
        job = Job.objects.create(
            title=title,
            company=company,
            location=random.choice(CITIES),
            salary=f'₹{random.randint(3, 12)}-{random.randint(13, 25)} LPA',
            description=f'We are looking for an experienced {title} to join our team.',
            image='https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800',
            employer=employer
        )
        
        created_count += 1
        print(f"✅ Created job: {job.title} at {job.company}")
    
    print(f"\n🎉 Total {created_count} jobs created!")
    return created_count

def create_sample_applications(applications_per_user=3):
    """Create sample job applications"""
    print(f"\n🚀 Creating sample job applications...")
    
    seekers = User.objects.filter(userprofile__role='seeker')
    jobs = Job.objects.all()
    
    if not seekers.exists() or not jobs.exists():
        print("❌ No seekers or jobs found. Create them first!")
        return 0
    
    created_count = 0
    for seeker in seekers:
        # Apply to random jobs
        random_jobs = random.sample(list(jobs), min(applications_per_user, len(jobs)))
        
        for job in random_jobs:
            # Check if already applied
            if JobApplication.objects.filter(job=job, applicant=seeker).exists():
                continue
            
            # Create application
            app = JobApplication.objects.create(
                job=job,
                applicant=seeker,
                status=random.choice(['pending', 'pending', 'pending', 'shortlisted', 'rejected'])
            )
            
            # Set random applied date (within last 30 days)
            days_ago = random.randint(0, 30)
            app.applied_date = datetime.now() - timedelta(days=days_ago)
            app.save()
            
            created_count += 1
    
    print(f"\n🎉 Total {created_count} applications created!")
    return created_count

def main():
    print("=" * 60)
    print("🎯 SAMPLE DATA GENERATOR FOR JOB HAI")
    print("=" * 60)
    
    # Create jobs first
    jobs_created = create_sample_jobs(15)
    
    # Create users and profiles
    users_created = create_sample_users_and_profiles(20)
    
    # Create applications
    apps_created = create_sample_applications(3)
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"✅ Jobs Created: {jobs_created}")
    print(f"✅ Users Created: {users_created}")
    print(f"✅ Applications Created: {apps_created}")
    print(f"\n📈 Total in Database:")
    print(f"   - Jobs: {Job.objects.count()}")
    print(f"   - Job Seekers: {UserProfile.objects.filter(role='seeker').count()}")
    print(f"   - Applications: {JobApplication.objects.count()}")
    print("\n🔐 Login Credentials:")
    print("   Username: Any created username (e.g., rajkumar123)")
    print("   Password: demo123")
    print("=" * 60)

if __name__ == '__main__':
    main()
