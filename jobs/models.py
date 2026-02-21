from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# ==============================
# Job Model
# ==============================

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(
        default='https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800'
    )
    posted_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="jobs_posted",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


# ==============================
# User Profile
# ==============================

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True)

    # Seeker Details
    resume_headline = models.CharField(max_length=300, blank=True)
    key_skills = models.TextField(blank=True)
    employment = models.TextField(blank=True)
    degree = models.CharField(max_length=200, blank=True)
    education = models.TextField(blank=True)
    it_skills = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    profile_summary = models.TextField(blank=True)
    accomplishments = models.TextField(blank=True)
    career_profile = models.TextField(blank=True)
    speaks = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    skills = models.TextField(blank=True)
    expected_salary = models.CharField(max_length=100, blank=True)
    aadhar_card = models.FileField(upload_to='documents/', blank=True, null=True)
    bank_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    work_experience = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    marital_status = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# ==============================
# Job Application
# ==============================

class JobApplication(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications"
    )

    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"


# ==============================
# Job Review
# ==============================

class Review(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_reviews'
    )

    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )

    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title} - {self.rating}⭐"


# ==============================
# User Rating
# ==============================

class UserRating(models.Model):

    rated_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_ratings'
    )

    rated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='given_ratings'
    )

    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('rated_user', 'rated_by')

    def __str__(self):
        return f"{self.rated_by.username} rated {self.rated_user.username} - {self.rating}⭐"


# ==============================
# Employee Review
# ==============================

class EmployeeReview(models.Model):

    EMPLOYEE_TYPE = [
        ('current', 'Current Employee'),
        ('former', 'Former Employee'),
    ]

    EMPLOYMENT_TYPE = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('intern', 'Intern'),
        ('contract', 'Contract'),
    ]

    DURATION_CHOICES = [
        ('<6', 'Less than 6 Months'),
        ('6-12', '6–12 Months'),
        ('1-3', '1–3 Years'),
        ('3+', '3+ Years'),
    ]

    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    employee_type = models.CharField(max_length=10, choices=EMPLOYEE_TYPE)

    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    working_duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    work_location = models.CharField(max_length=100)

    work_environment = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    salary_benefits = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    management_support = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    job_security = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    career_growth = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    work_life_balance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    overall_rating = models.FloatField(blank=True, null=True)

    pros = models.TextField()
    cons = models.TextField()
    recommend = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ratings = [
            self.work_environment,
            self.salary_benefits,
            self.management_support,
            self.job_security,
            self.career_growth,
            self.work_life_balance,
        ]
        self.overall_rating = round(sum(ratings) / len(ratings), 1)
        super().save(*args, **kwargs)


# ==============================
# Candidate Rating
# ==============================

class CandidateRating(models.Model):

    EMPLOYMENT_STATUS = [
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
        ('working', 'Working'),
        ('left', 'Left Job'),
    ]

    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="candidate_ratings"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="candidate_ratings"
    )

    rated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ratings_given"
    )

    interview_date = models.DateField()
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS)

    communication_skills = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    technical_knowledge = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    confidence_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    professional_behaviour = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    work_quality = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    punctuality = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    teamwork = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    learning_ability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    responsibility_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    target_achievement = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    recommendation = models.CharField(
        max_length=10,
        choices=[('yes', 'Yes'), ('no', 'No'), ('maybe', 'Maybe')]
    )

    overall_rating = models.FloatField(blank=True, null=True)

    strengths = models.TextField()
    areas_of_improvement = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ratings = [
            self.communication_skills,
            self.technical_knowledge,
            self.confidence_level,
            self.professional_behaviour,
            self.work_quality,
            self.punctuality,
            self.teamwork,
            self.learning_ability,
            self.responsibility_level,
            self.target_achievement,
        ]
        self.overall_rating = round(sum(ratings) / len(ratings), 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate.username} - {self.overall_rating}"
