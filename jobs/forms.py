from django import forms
from .models import CandidateRating, EmployeeReview

class CandidateRatingForm(forms.ModelForm):
    class Meta:
        model = CandidateRating
        fields = '__all__'


class EmployeeReviewForm(forms.ModelForm):
    class Meta:
        model = EmployeeReview
        fields = '__all__'
