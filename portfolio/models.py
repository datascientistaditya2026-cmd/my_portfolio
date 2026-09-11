from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("ml", "Machine Learning"),
        ("dl", "Deep Learning"),
        ("cv", "Computer Vision"),
        ("nlp", "NLP"),
        ("genai", "Generative AI"),
        ("backend", "Backend"),
        ("tools", "Tools"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    icon = models.CharField(
        max_length=100,
        blank=True
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Example: Python, YOLO, OpenCV, Django"
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class Experience(models.Model):

    job_title = models.CharField(
        max_length=150
    )

    company = models.CharField(
        max_length=150
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(
        default=False
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=500,
        blank=True
    )

    def __str__(self):
        return f"{self.job_title} - {self.company}"


class Education(models.Model):

    degree = models.CharField(
        max_length=150
    )

    institution = models.CharField(
        max_length=200
    )

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):

    name = models.CharField(
        max_length=200
    )

    organization = models.CharField(
        max_length=200
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    credential_url = models.URLField(
        blank=True
    )

    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class SocialLink(models.Model):

    name = models.CharField(
        max_length=50
    )

    url = models.URLField()

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.name