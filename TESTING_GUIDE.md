# Test Script - Candidate Profile Feature

## Testing Checklist ✅

### 1. Database Migration
- [x] Added expected_salary field to UserProfile model
- [x] Created and ran migration successfully

### 2. Job Seeker Dashboard
- [x] Added "Expected Salary" input field
- [x] Field saves properly when profile is updated

### 3. Candidates List Page
- [x] Shows Location
- [x] Shows Expected Salary
- [x] Shows Education
- [x] Shows Speaks (Languages)
- [x] Shows Skills
- [x] Shows Email
- [x] Shows Phone
- [x] "View Full Profile" button works

### 4. Candidate Profile Page
- [x] Shows Expected Salary in contact info
- [x] "View Number" button shows phone in alert
- [x] "Send Message" opens WhatsApp with pre-filled message
- [x] "Invite for Interview" shows email in alert

### 5. Employer Dashboard
- [x] Navigation has "Candidates" link
- [x] Navigation has "Notifications" link
- [x] "Browse Candidates" section added
- [x] "View All Candidates" button works

## How to Test:

### Step 1: Create Test Users
```bash
# Run Django shell
python manage.py shell

# Create employer
from django.contrib.auth.models import User
from jobs.models import UserProfile

employer = User.objects.create_user('testemployer', 'employer@test.com', 'pass123')
UserProfile.objects.create(user=employer, role='employer', company_name='Test Company', phone='9876543210')

# Create job seeker
seeker = User.objects.create_user('testseeker', 'seeker@test.com', 'pass123')
UserProfile.objects.create(
    user=seeker, 
    role='seeker',
    phone='9876543211',
    whatsapp='919876543211',
    resume_headline='Python Developer with 2 years experience',
    key_skills='Python Django JavaScript',
    degree='B.Tech Computer Science',
    location='Delhi',
    speaks='Hindi, English',
    expected_salary='₹5-7 LPA'
)
```

### Step 2: Test Employer Flow
1. Login as employer: `testemployer` / `pass123`
2. Click "👥 Candidates" in navigation
3. Verify all candidate fields are showing
4. Click "View Full Profile" on any candidate
5. Test all three action buttons

### Step 3: Test Job Seeker Flow
1. Login as seeker: `testseeker` / `pass123`
2. Go to dashboard
3. Update profile with expected salary
4. Save and verify

### Step 4: Verify Security
1. Try accessing `/candidates/` as job seeker
2. Should redirect or show warning

## Expected Results:

✅ All fields display correctly
✅ Action buttons work as expected
✅ WhatsApp opens with message
✅ Alerts show correct information
✅ Only employers can access candidates list
✅ Profile updates save properly

---
Test Date: 2024
Status: Ready for Testing 🚀
