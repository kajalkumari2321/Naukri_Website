# Candidate Profile Feature 

## Feature Added: Employer can view Candidate Profiles

### What's New:

1. **Employer Dashboard Updates** 🏢
   - Added "👥 Candidates" link in navigation
   - Added "🔔 Notifications" link in navigation
   - Added "Browse Candidates" section with button to view all candidates

2. **Candidates List Page** 📋
   - Shows all registered job seekers
   - Displays candidate cards with:
     - Name
     - Resume Headline
     - Location
     - Expected Salary
     - Education
     - Speaks (Languages)
     - Skills
     - Email
     - Phone 
           
   - "View Full Profile" button for each candidate

3. **Candidate Profile Page** 👤
   - Complete profile view with:
     - Profile photo
     - Contact information (Phone, Email, Expected Salary)
     - Resume headline
     - Key skills
     - Work experience
     - Education
     - IT skills
     - Projects
     - Profile summary
     - Documents (resume download)
   - Action buttons:
     - 📞 View Number (shows phone in alert)
     - 💬 Send Message (opens WhatsApp)
     - 📧 Invite for Interview (shows email in alert)

### How to Use:

**For Employers:**
1. Login to employer dashboard
2. Click on "👥 Candidates" in navigation OR
3. Click "View All Candidates" button in dashboard
4. Browse through candidate cards
5. Click "View Full Profile" to see complete candidate details
6. Use action buttons to contact candidates

**For Job Seekers:**
1. Login to seeker dashboard
2. Fill your complete profile
3. Your profile will be visible to all employers
4. Employers can view your profile and contact you

### Files Modified:
- `jobs/models.py` - Added expected_salary field to UserProfile
- `jobs/views.py` - Added expected_salary handling in seeker_dashboard
- `templates/seeker_dashboard.html` - Added expected_salary input field
- `templates/candidates_list.html` - Added expected_salary and speaks display
- `templates/seeker_profile.html` - Updated action buttons with proper functionality
- `templates/employer_dashboard.html` - Added navigation links and Browse Candidates section

### URLs Available:
- `/candidates/` - View all candidates (Employer only)
- `/profile/<username>/` - View specific candidate profile

### Features:
✅ Employer can browse all candidates
✅ Employer can view complete candidate profiles
✅ Employer can view candidate phone numbers
✅ Employer can send WhatsApp messages to candidates
✅ Employer can see candidate email for interview invitations
✅ Candidates can add expected salary
✅ Candidates can add languages they speak
✅ Clean and professional UI
✅ Responsive design
✅ Secure (only employers can access candidates list)

---
Made with ❤️ for Job Hai Portal
