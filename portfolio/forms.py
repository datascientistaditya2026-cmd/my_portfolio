from django import forms
from .models import (
    Profile,
    Skill,
    Project,
    Experience,
    Education,
    Certification,
    SocialLink,
)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            "name",
            "designation",
            "bio",
            "profile_image",
            "email",
            "phone",
            "location",
            "github_url",
            "linkedin_url",
            "resume",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name",
            }),

            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "AI/ML Engineer",
            }),

            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your professional bio...",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "your@email.com",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+91 XXXXX XXXXX",
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Delhi, India",
            }),

            "github_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://github.com/username",
            }),

            "linkedin_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://linkedin.com/in/username",
            }),
        }


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill

        fields = [
            "name",
            "category",
            "description",
            "icon",
            "order",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Python",
            }),

            "description": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Programming language",
            }),

            "icon": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "fa-brands fa-python",
            }),

            "order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "title",
            "category",
            "description",
            "image",
            "technologies",
            "github_url",
            "live_url",
            "featured",
            "order",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Automatic Number Plate Recognition",
            }),

            "category": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Computer Vision",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your project...",
            }),

            "technologies": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Python, YOLO, OpenCV, Django",
            }),

            "github_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://github.com/username/project",
            }),

            "live_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
            }),

            "order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
        }


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience

        fields = [
            "job_title",
            "company",
            "location",
            "start_date",
            "end_date",
            "currently_working",
            "description",
            "technologies",
        ]

        widgets = {
            "job_title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "AI/ML Engineer",
            }),

            "company": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name",
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Noida, India",
            }),

            "start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "end_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your responsibilities...",
            }),

            "technologies": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Python, Django, ML, Docker",
            }),
        }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education

        fields = [
            "degree",
            "institution",
            "start_year",
            "end_year",
            "description",
        ]

        widgets = {
            "degree": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "MBA / B.Tech / M.Tech",
            }),

            "institution": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "University Name",
            }),

            "start_year": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "2020",
            }),

            "end_year": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "2022",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Education details...",
            }),
        }


class CertificationForm(forms.ModelForm):

    class Meta:
        model = Certification

        fields = [
            "name",
            "organization",
            "issue_date",
            "credential_url",
            "certificate_image",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Machine Learning Certification",
            }),

            "organization": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Organization",
            }),

            "issue_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "credential_url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://...",
            }),
        }


class SocialLinkForm(forms.ModelForm):

    class Meta:
        model = SocialLink

        fields = [
            "name",
            "url",
            "icon",
            "order",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "GitHub",
            }),

            "url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://github.com/username",
            }),

            "icon": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "fa-brands fa-github",
            }),

            "order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
        }