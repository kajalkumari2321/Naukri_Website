import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobhai.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job, JobApplication

print("Creating sample job applications...\n")

# Get some seekers and jobs
seekers = User.objects.filter(userprofile__role='seeker')[:5]
jobs = Job.objects.all()[:5]

count = 0
for seeker in seekers:
    for job in jobs[:2]:  # Each seeker applies to 2 jobs
        app, created = JobApplication.objects.get_or_create(
            job=job,
            applicant=seeker,
            defaults={'status': 'pending'}
        )
        if created:
            count += 1
            print(f"[OK] {seeker.username} applied to {job.title} at {job.company}")

print(f"\nTotal applications created: {count}")
print("Done! Now employers can see notifications.")
