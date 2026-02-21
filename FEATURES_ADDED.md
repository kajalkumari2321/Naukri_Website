# New Features Added - Notifications & Candidates

## ✅ Features Implemented:

### 1. 🔔 Notifications Icon
- **Location**: Navbar (visible when logged in)
- **For Employers**: Shows all job applications received
- **For Job Seekers**: Shows all jobs they have applied to
- **URL**: `/notifications/`

### 2. 👥 Candidates Icon  
- **Location**: Navbar (visible only for employers)
- **Purpose**: View all registered job seekers
- **Features**:
  - Complete candidate profiles
  - Contact information (email, phone)
  - Skills and education
  - Direct link to full profile
- **URL**: `/candidates/`

## 📁 Files Modified/Created:

### Modified:
1. `jobs/views.py` - Added notifications() and candidates_list() views
2. `jobs/urls.py` - Added routes for notifications and candidates
3. `templates/home.html` - Added icons in navbar

### Created:
1. `templates/notifications.html` - Notifications page
2. `templates/candidates_list.html` - Candidates listing page
3. `create_applications.py` - Script to create sample applications

## 🚀 How to Use:

### For Employers:
1. Login as employer (e.g., username: `tcs_hr`, password: `password123`)
2. Click on "👥 Candidates" to see all job seekers
3. Click on "🔔 Notifications" to see applications received
4. View candidate profiles and contact them

### For Job Seekers:
1. Login as job seeker (e.g., username: `rahul_sharma`, password: `password123`)
2. Click on "🔔 Notifications" to see your applied jobs
3. Track application status

## 📊 Sample Data Created:

### 10 Employers:
- TCS, Infosys, Wipro, Amazon India, Flipkart
- Google India, Microsoft, Accenture, Cognizant, HCL Technologies

### 10 Job Seekers:
- Rahul Sharma, Priya Singh, Amit Kumar, Sneha Patel, Vikash Yadav
- Anjali Verma, Rohit Gupta, Pooja Jain, Sanjay Mishra, Kavita Reddy

### 10 Sample Applications:
- Created for testing notifications feature

## 🔐 Test Credentials:

**Employer Login:**
- Username: `tcs_hr` (or any employer username)
- Password: `password123`

**Job Seeker Login:**
- Username: `rahul_sharma` (or any seeker username)
- Password: `password123`

## 🎯 Key Features:

✅ Real-time notifications for job applications
✅ Complete candidate database for employers
✅ Application status tracking
✅ Direct profile access
✅ Contact information display
✅ Responsive design
✅ Clean UI with icons

---
Made with ❤️ for SHANDILYA CONSULTANCY
