# 🚀 Job Portal System - Complete Documentation

## 📋 System Overview

**Job_Portal_System** is a complete Django web application that connects employers with job seekers, featuring advanced filtering, rating systems, and comprehensive profile management.

---

## 👥 User Roles

### 1. **Employer**
A registered user who can:
- Post job listings with detailed requirements
- Browse and filter candidate profiles
- Review and rate job seekers
- Manage applications and shortlist candidates
- Access advanced candidate database with filters
- View candidate skills, experience, and ratings

**Key Features:**
- Employer Dashboard
- Job Posting Management
- Candidates List with Filters
- Employee Rating System
- Application Management

### 2. **Job_Seeker**
A registered user who can:
- Browse available job listings
- Submit job applications
- Create and manage detailed profile
- Upload resume and documents
- Track application status
- View recommendations based on skills
- Rate and review companies

**Key Features:**
- Seeker Dashboard with Statistics
- Profile Management (Resume, Skills, Experience)
- Job Application Tracking
- Company Review System
- Document Upload (Resume, Aadhar, Bank Documents)

---

## 🎯 Core Modules

### 1. **Job_Listing**
A posted job opportunity containing:
- **Title**: Job position name
- **Company**: Employer company name
- **Location**: Job location/city
- **Salary**: Salary range
- **Description**: Detailed job requirements
- **Posted Date**: When the job was posted
- **Employer**: Link to employer who posted

**Features:**
- Search and filter jobs
- Job detail page with reviews
- Apply functionality
- Company profile page

### 2. **Application**
Job seeker's submission for a specific job:
- **Job**: Reference to job listing
- **Applicant**: Reference to job seeker
- **Applied Date**: Timestamp of application
- **Status**: pending, shortlisted, rejected

**Features:**
- Application tracking
- Status updates
- Application history
- Filter by status

### 3. **Candidate_Profile**
Comprehensive job seeker profile:
- **Personal Info**: Name, email, phone, location
- **Resume**: Uploaded document
- **Resume Headline**: Professional summary
- **Key Skills**: Comma-separated skills
- **Employment**: Work history
- **Education**: Academic qualifications
- **IT Skills**: Technical skills
- **Projects**: Project portfolio
- **Profile Summary**: Career overview
- **Accomplishments**: Awards and certifications
- **Career Profile**: Career goals
- **Documents**: Aadhar card, bank documents
- **Expected Salary**: Salary expectations
- **Languages**: Languages known

**Features:**
- Complete profile management
- Document upload
- Skills-based recommendations
- Profile visibility to employers

### 4. **Rating System**

#### A. **Employee Review (Job Seeker → Company)**
Employees rate their company on:
- Work Environment (1-5 stars)
- Salary & Benefits (1-5 stars)
- Management Support (1-5 stars)
- Job Security (1-5 stars)
- Career Growth (1-5 stars)
- Work-Life Balance (1-5 stars)
- Pros and Cons (Text)
- Recommendation (Yes/No)
- Overall Rating (Auto-calculated)

**Features:**
- Anonymous review option
- Email verification
- Employment type tracking
- Working duration tracking

#### B. **Candidate Rating (Company → Employee)**
Employers rate candidates on:

**Interview Stage:**
- Communication Skills (1-5 stars)
- Technical Knowledge (1-5 stars)
- Confidence Level (1-5 stars)
- Professional Behaviour (1-5 stars)

**Work Performance (If Selected):**
- Work Quality (1-5 stars)
- Punctuality (1-5 stars)
- Teamwork (1-5 stars)
- Learning Ability (1-5 stars)
- Responsibility Level (1-5 stars)
- Target Achievement (1-5 stars)

**Overall Assessment:**
- Recommendation (Yes/No/Maybe)
- Overall Rating (Auto-calculated)
- Strengths (Text)
- Areas of Improvement (Text)

---

## 🔐 Authentication_System

Django's built-in authentication with custom extensions:

**Features:**
- User Registration (Employer/Job Seeker)
- Login/Logout
- Role-based access control
- Profile creation on registration
- Password management
- Session management

**User Model Extensions:**
- UserProfile model with role field
- Separate dashboards based on role
- Permission-based view access

---

## 🏠 Home_Page

Landing page featuring:

**Sections:**
1. **Hero Section**: Search bar with job count
2. **Quick Links**: Popular job categories
3. **Recommended Jobs**: Job listings grid
4. **Statistics**: Active jobs, companies, seekers
5. **Top Companies**: Company cards
6. **Top Candidates**: Featured job seekers (for employers)

**Features:**
- Job search functionality
- Responsive design
- Dynamic content
- Role-based content display

---

## 📊 Services_Section

Information pages:

### 1. **About Us**
- Company information
- Mission and vision
- Team details

### 2. **Contact Us**
- Contact form
- Contact information
- Location details

### 3. **Rating Options**
- Employee Review Form access
- Company Rating Form access
- Feature descriptions

---

## 🗄️ Database

**Models Structure:**

### Core Models:
1. **User** (Django built-in)
   - username, email, password
   - first_name, last_name

2. **UserProfile**
   - user (OneToOne)
   - role (seeker/employer)
   - All profile fields

3. **Job**
   - title, company, location
   - salary, description
   - employer (ForeignKey)
   - posted_date

4. **JobApplication**
   - job (ForeignKey)
   - applicant (ForeignKey)
   - applied_date, status

5. **Review**
   - job (ForeignKey)
   - user (ForeignKey)
   - rating, comment
   - approved

6. **EmployeeReview**
   - All employee review fields
   - Rating fields (1-5)
   - overall_rating (auto-calculated)

7. **CandidateRating**
   - All candidate rating fields
   - Rating fields (1-5)
   - overall_rating (auto-calculated)

---

## 🎨 Key Features

### For Employers:
✅ Post unlimited jobs
✅ Advanced candidate filtering
✅ Skills-based search
✅ Location-based filtering
✅ Salary budget filtering
✅ Experience filtering
✅ Rate and review candidates
✅ Application management
✅ Candidate database access

### For Job Seekers:
✅ Browse unlimited jobs
✅ Apply to jobs
✅ Complete profile management
✅ Resume upload
✅ Document upload
✅ Application tracking
✅ Statistics dashboard
✅ Skills-based recommendations
✅ Rate and review companies

### Rating System:
✅ Two-way rating (Company ↔ Employee)
✅ Multiple rating categories
✅ Auto-calculated overall ratings
✅ Text feedback (Pros/Cons/Strengths)
✅ Anonymous review option
✅ Verification system

### Advanced Filtering:
✅ Location-based
✅ Salary budget
✅ Skills matching
✅ Experience level
✅ Recent candidates
✅ Database status tracking

---

## 📱 Pages & URLs

### Public Pages:
- `/` - Home page
- `/about/` - About us
- `/contact/` - Contact us
- `/register/` - Registration
- `/login/` - Login
- `/job/<id>/` - Job detail
- `/company/<name>/` - Company profile

### Job Seeker Pages:
- `/seeker-dashboard/` - Dashboard with statistics
- `/profile/<username>/` - Public profile
- `/apply/<id>/` - Apply to job
- `/notifications/` - Application notifications

### Employer Pages:
- `/employer-dashboard/` - Dashboard
- `/candidates/` - Candidates list with filters
- `/notifications/` - Application notifications

### Rating Pages:
- `/rating-options/` - Rating options landing
- `/add-review/` - Employee review form
- `/add-candidate-rating/` - Candidate rating form

---

## 🛠️ Technology Stack

**Backend:**
- Django 5.0
- Python 3.12
- SQLite Database

**Frontend:**
- HTML5
- CSS3 (Custom styling)
- JavaScript (Vanilla)
- Responsive Design

**Features:**
- Django ORM
- Django Authentication
- File Upload System
- Form Validation
- Session Management
- Template Inheritance

---

## 📈 Statistics & Analytics

### Seeker Dashboard:
- Total Applications
- Direct Applies (Pending)
- Recommendations (Skills-based)
- Database Total Jobs
- Shortlisted Count
- Rejected Count

### Employer Dashboard:
- Posted Jobs Count
- Total Applications Received
- Candidates Database Count
- Active Listings

---

## 🔒 Security Features

- Password hashing
- CSRF protection
- Role-based access control
- Login required decorators
- File upload validation
- SQL injection prevention
- XSS protection

---

## 🚀 Sample Data Generator

**Script:** `create_sample_data.py`

**Generates:**
- 20 complete job seeker profiles
- 15 sample jobs
- 60+ job applications
- Realistic data (names, skills, locations)

**Usage:**
```bash
python create_sample_data.py
```

---

## 📝 Summary

This Job Portal System is a complete, production-ready Django application with:
- ✅ Dual user roles (Employer & Job Seeker)
- ✅ Complete CRUD operations
- ✅ Advanced filtering and search
- ✅ Two-way rating system
- ✅ Document management
- ✅ Statistics dashboard
- ✅ Responsive design
- ✅ Sample data generator
- ✅ Professional UI/UX

**Total Features:** 50+
**Total Pages:** 15+
**Total Models:** 7
**Total Views:** 20+

---

## 🎯 Future Enhancements

- Email notifications
- Real-time chat
- Video interviews
- AI-based job matching
- Resume parser
- Payment integration
- Mobile app
- Advanced analytics

---

**Developed with ❤️ using Django**
