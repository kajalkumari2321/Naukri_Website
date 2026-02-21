import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobhai.settings')
django.setup()

from jobs.models import Job
from django.contrib.auth.models import User

# Get or create an employer user
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
    print(f"✅ Created employer user: {employer.username}")

# Sample jobs data
sample_jobs = [
    {
        'title': 'Python Developer',
        'company': 'TCS',
        'location': 'Mumbai',
        'salary': '₹5-8 LPA',
        'description': 'Looking for experienced Python developer with Django knowledge.',
        'image': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800'
    },
    {
        'title': 'Full Stack Developer',
        'company': 'Infosys',
        'location': 'Bangalore',
        'salary': '₹6-10 LPA',
        'description': 'Full stack developer with React and Node.js experience required.',
        'image': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800'
    },
    {
        'title': 'Data Analyst',
        'company': 'Wipro',
        'location': 'Pune',
        'salary': '₹4-7 LPA',
        'description': 'Data analyst with SQL and Python skills needed.',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800'
    },
    {
        'title': 'UI/UX Designer',
        'company': 'Amazon',
        'location': 'Hyderabad',
        'salary': '₹5-9 LPA',
        'description': 'Creative UI/UX designer with Figma experience.',
        'image': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800'
    },
    {
        'title': 'Digital Marketing Manager',
        'company': 'Flipkart',
        'location': 'Delhi',
        'salary': '₹6-12 LPA',
        'description': 'Experienced digital marketing professional needed.',
        'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800'
    },
    {
        'title': 'Java Developer',
        'company': 'Accenture',
        'location': 'Chennai',
        'salary': '₹5-8 LPA',
        'description': 'Java developer with Spring Boot experience.',
        'image': 'https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800'
    },
    {
        'title': 'DevOps Engineer',
        'company': 'Microsoft',
        'location': 'Bangalore',
        'salary': '₹8-15 LPA',
        'description': 'DevOps engineer with AWS and Docker knowledge.',
        'image': 'https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=800'
    },
    {
        'title': 'Business Analyst',
        'company': 'Google',
        'location': 'Gurgaon',
        'salary': '₹7-12 LPA',
        'description': 'Business analyst with strong analytical skills.',
        'image': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800'
    },
]

# Create jobs
created_count = 0
for job_data in sample_jobs:
    job, created = Job.objects.get_or_create(
        title=job_data['title'],
        company=job_data['company'],
        defaults={
            'location': job_data['location'],
            'salary': job_data['salary'],
            'description': job_data['description'],
            'image': job_data['image'],
            'employer': employer
        }
    )
    if created:
        created_count += 1
        print(f"✅ Created job: {job.title} at {job.company}")
    else:
        print(f"⏭️  Job already exists: {job.title} at {job.company}")

print(f"\n🎉 Total {created_count} new jobs created!")
print(f"📊 Total jobs in database: {Job.objects.count()}")
