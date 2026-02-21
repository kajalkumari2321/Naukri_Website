import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobhai.settings')
django.setup()

from jobs.models import Job

# Clear existing jobs (optional - use only in development)
Job.objects.all().delete()

jobs_data = [
    Job(
        title='Full Stack Developer',
        company='Tech Solutions India',
        location='Mumbai, Maharashtra',
        salary='₹8-12 LPA',
        description='We are looking for an experienced Full Stack Developer skilled in React and Django.',
        image='https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800'
    ),
    Job(
        title='Digital Marketing Manager',
        company='Creative Minds Agency',
        location='Delhi NCR',
        salary='₹6-10 LPA',
        description='Manage digital marketing campaigns. Expertise in SEO, SEM required.',
        image='https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800'
    ),
    Job(
        title='Sales Executive',
        company='Bright Future Enterprises',
        location='Lucknow',
        salary='₹3-6 LPA',
        description='Generate leads and achieve monthly sales targets.',
        image='https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800'
    ),
   
    Job(
        title='Academic Counselor',
        company='Future Skills Institute',
        location='Ranchi',
        salary='₹3-5 LPA',
        description='Guide students regarding courses and admissions.',
        image='https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800'
    ),
    Job(
        title='Accountant',
        company='Prime Finance Solutions',
        location='Varanasi',
        salary='₹4-8 LPA',
        description='Handle GST filing and financial reports.',
        image='https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800'
    ),
    Job(
        title='Data Scientist',
        company='Analytics Pro',
        location='Bangalore, Karnataka',
        salary='₹10-15 LPA',
        description='Machine Learning and Data Analysis expert required.',
        image='https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800'
    ),
   
    
    Job(
        title='UI/UX Designer',
        company='Design Studio',
        location='Pune, Maharashtra',
        salary='₹5-8 LPA',
        description='Create user-friendly designs using Figma and Adobe XD.',
        image='https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800'
    ),
    
    Job(
        title='Content Writer',
        company='Media House',
        location='Hyderabad, Telangana',
        salary='₹3-5 LPA',
        description='Create engaging Hindi and English content.',
        image='https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800'
    ),
    Job(
        title='Sales Executive',
        company='Business Solutions Ltd',
        location='Ahmedabad, Gujarat',
        salary='₹4-7 LPA',
        description='B2B sales and client relationship building.',
        image='https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800'
    ),
    
    Job(
        title='Sales Executive',
        company='Skyline Marketing',
        location='Bhopal, Madhya Pradesh',
        salary='₹4-8 LPA',
        description='Direct sales and customer handling.',
        image='https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800'
    ),
  
    Job(
        title='Accountant',
        company='Prime Finance Solutions',
        location='Varanasi',
        salary='₹4-8 LPA',
        description='Handle GST filing and financial reports.',
        image='https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800'
    ),
    Job(
        title='Data Scientist',
        company='Analytics Pro',
        location='Bangalore, Karnataka',
        salary='₹10-15 LPA',
        description='Machine Learning and Data Analysis expert required.',
        image='https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800'
    ),
]

Job.objects.bulk_create(jobs_data)
print("Sample jobs added successfully!")
