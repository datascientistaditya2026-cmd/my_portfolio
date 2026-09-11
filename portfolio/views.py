from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required

from .forms import (
    ProfileForm,
    SkillForm,
    ProjectForm,
    ExperienceForm,
    EducationForm,
    CertificationForm,
    SocialLinkForm,
)

from .models import (
    Profile,
    Skill,
    Project,
    Experience,
    Education,
    Certification,
    SocialLink,
)


# =========================================================
# PUBLIC PORTFOLIO
# =========================================================

def home(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all().order_by("order")

    projects = Project.objects.all().order_by("order")

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by("order")

    experiences = Experience.objects.all().order_by("-start_date")

    education = Education.objects.all().order_by("-start_year")

    certifications = Certification.objects.all().order_by("-issue_date")

    social_links = SocialLink.objects.all().order_by("order")

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "featured_projects": featured_projects,
        "experiences": experiences,
        "education": education,
        "certifications": certifications,
        "social_links": social_links,
    }

    return render(
        request,
        "portfolio/home.html",
        context
    )


# =========================================================
# LOGIN
# =========================================================

def dashboard_login(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login successful."
            )

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "portfolio/dashboard/login.html"
    )


# =========================================================
# LOGOUT
# =========================================================

@staff_member_required
def dashboard_logout(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("dashboard_login")


# =========================================================
# DASHBOARD HOME
# =========================================================


@staff_member_required
def dashboard(request):

    recent_projects = Project.objects.all().order_by("-created_at")[:5]

    recent_experiences = Experience.objects.all().order_by("-start_date")[:5]

    context = {
        "profile_count": Profile.objects.count(),
        "skill_count": Skill.objects.count(),
        "project_count": Project.objects.count(),
        "experience_count": Experience.objects.count(),
        "education_count": Education.objects.count(),
        "certification_count": Certification.objects.count(),
        "social_count": SocialLink.objects.count(),

        "recent_projects": recent_projects,
        "recent_experiences": recent_experiences,
    }

    return render(
        request,
        "portfolio/dashboard/dashboard.html",
        context
    )

# =========================================================
# PROFILE
# =========================================================

@staff_member_required
def profile_edit(request):

    profile = Profile.objects.first()

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile_edit")

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "portfolio/dashboard/profile_form.html",
        {
            "form": form,
            "profile": profile,
        }
    )


# =========================================================
# SKILLS
# =========================================================

@staff_member_required
def skill_list(request):

    skills = Skill.objects.all().order_by("order")

    return render(
        request,
        "portfolio/dashboard/skill_list.html",
        {
            "skills": skills
        }
    )


@staff_member_required
def skill_create(request):

    if request.method == "POST":

        form = SkillForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Skill added successfully."
            )

            return redirect("skill_list")

    else:

        form = SkillForm()

    return render(
        request,
        "portfolio/dashboard/skill_form.html",
        {
            "form": form,
            "title": "Add Skill",
        }
    )


@staff_member_required
def skill_edit(request, pk):

    skill = get_object_or_404(
        Skill,
        pk=pk
    )

    if request.method == "POST":

        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Skill updated successfully."
            )

            return redirect("skill_list")

    else:

        form = SkillForm(
            instance=skill
        )

    return render(
        request,
        "portfolio/dashboard/skill_form.html",
        {
            "form": form,
            "title": "Edit Skill",
        }
    )


@staff_member_required
def skill_delete(request, pk):

    skill = get_object_or_404(
        Skill,
        pk=pk
    )

    if request.method == "POST":

        skill.delete()

        messages.success(
            request,
            "Skill deleted successfully."
        )

    return redirect("skill_list")


# =========================================================
# PROJECTS
# =========================================================

@staff_member_required
def project_list(request):

    projects = Project.objects.all().order_by("order")

    return render(
        request,
        "portfolio/dashboard/project_list.html",
        {
            "projects": projects
        }
    )


@staff_member_required
def project_create(request):

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project added successfully."
            )

            return redirect("project_list")

    else:

        form = ProjectForm()

    return render(
        request,
        "portfolio/dashboard/project_form.html",
        {
            "form": form,
            "title": "Add Project",
        }
    )


@staff_member_required
def project_edit(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project updated successfully."
            )

            return redirect("project_list")

    else:

        form = ProjectForm(
            instance=project
        )

    return render(
        request,
        "portfolio/dashboard/project_form.html",
        {
            "form": form,
            "title": "Edit Project",
            "project": project,
        }
    )


@staff_member_required
def project_delete(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        project.delete()

        messages.success(
            request,
            "Project deleted successfully."
        )

    return redirect("project_list")


# =========================================================
# EXPERIENCE
# =========================================================

@staff_member_required
def experience_list(request):

    experiences = Experience.objects.all().order_by(
        "-start_date"
    )

    return render(
        request,
        "portfolio/dashboard/experience_list.html",
        {
            "experiences": experiences
        }
    )


@staff_member_required
def experience_create(request):

    if request.method == "POST":

        form = ExperienceForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Experience added successfully."
            )

            return redirect("experience_list")

    else:

        form = ExperienceForm()

    return render(
        request,
        "portfolio/dashboard/experience_form.html",
        {
            "form": form,
            "title": "Add Experience",
        }
    )


@staff_member_required
def experience_edit(request, pk):

    experience = get_object_or_404(
        Experience,
        pk=pk
    )

    if request.method == "POST":

        form = ExperienceForm(
            request.POST,
            instance=experience
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Experience updated successfully."
            )

            return redirect("experience_list")

    else:

        form = ExperienceForm(
            instance=experience
        )

    return render(
        request,
        "portfolio/dashboard/experience_form.html",
        {
            "form": form,
            "title": "Edit Experience",
        }
    )


@staff_member_required
def experience_delete(request, pk):

    experience = get_object_or_404(
        Experience,
        pk=pk
    )

    if request.method == "POST":

        experience.delete()

        messages.success(
            request,
            "Experience deleted successfully."
        )

    return redirect("experience_list")


# =========================================================
# EDUCATION
# =========================================================

@staff_member_required
def education_list(request):

    education = Education.objects.all().order_by(
        "-start_year"
    )

    return render(
        request,
        "portfolio/dashboard/education_list.html",
        {
            "education": education
        }
    )


@staff_member_required
def education_create(request):

    if request.method == "POST":

        form = EducationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Education added successfully."
            )

            return redirect("education_list")

    else:

        form = EducationForm()

    return render(
        request,
        "portfolio/dashboard/education_form.html",
        {
            "form": form,
            "title": "Add Education",
        }
    )


@staff_member_required
def education_edit(request, pk):

    education = get_object_or_404(
        Education,
        pk=pk
    )

    if request.method == "POST":

        form = EducationForm(
            request.POST,
            instance=education
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Education updated successfully."
            )

            return redirect("education_list")

    else:

        form = EducationForm(
            instance=education
        )

    return render(
        request,
        "portfolio/dashboard/education_form.html",
        {
            "form": form,
            "title": "Edit Education",
        }
    )


@staff_member_required
def education_delete(request, pk):

    education = get_object_or_404(
        Education,
        pk=pk
    )

    if request.method == "POST":

        education.delete()

        messages.success(
            request,
            "Education deleted successfully."
        )

    return redirect("education_list")


# =========================================================
# CERTIFICATIONS
# =========================================================

@staff_member_required
def certification_list(request):

    certifications = Certification.objects.all().order_by(
        "-issue_date"
    )

    return render(
        request,
        "portfolio/dashboard/certification_list.html",
        {
            "certifications": certifications
        }
    )


@staff_member_required
def certification_create(request):

    if request.method == "POST":

        form = CertificationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Certification added successfully."
            )

            return redirect("certification_list")

    else:

        form = CertificationForm()

    return render(
        request,
        "portfolio/dashboard/certification_form.html",
        {
            "form": form,
            "title": "Add Certification",
        }
    )


@staff_member_required
def certification_edit(request, pk):

    certification = get_object_or_404(
        Certification,
        pk=pk
    )

    if request.method == "POST":

        form = CertificationForm(
            request.POST,
            request.FILES,
            instance=certification
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Certification updated successfully."
            )

            return redirect("certification_list")

    else:

        form = CertificationForm(
            instance=certification
        )

    return render(
        request,
        "portfolio/dashboard/certification_form.html",
        {
            "form": form,
            "title": "Edit Certification",
        }
    )


@staff_member_required
def certification_delete(request, pk):

    certification = get_object_or_404(
        Certification,
        pk=pk
    )

    if request.method == "POST":

        certification.delete()

        messages.success(
            request,
            "Certification deleted successfully."
        )

    return redirect("certification_list")


# =========================================================
# SOCIAL LINKS
# =========================================================

@staff_member_required
def social_list(request):

    social_links = SocialLink.objects.all().order_by(
        "order"
    )

    return render(
        request,
        "portfolio/dashboard/social_list.html",
        {
            "social_links": social_links
        }
    )


@staff_member_required
def social_create(request):

    if request.method == "POST":

        form = SocialLinkForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Social link added successfully."
            )

            return redirect("social_list")

    else:

        form = SocialLinkForm()

    return render(
        request,
        "portfolio/dashboard/social_form.html",
        {
            "form": form,
            "title": "Add Social Link",
        }
    )


@staff_member_required
def social_edit(request, pk):

    social = get_object_or_404(
        SocialLink,
        pk=pk
    )

    if request.method == "POST":

        form = SocialLinkForm(
            request.POST,
            instance=social
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Social link updated successfully."
            )

            return redirect("social_list")

    else:

        form = SocialLinkForm(
            instance=social
        )

    return render(
        request,
        "portfolio/dashboard/social_form.html",
        {
            "form": form,
            "title": "Edit Social Link",
        }
    )


@staff_member_required
def social_delete(request, pk):

    social = get_object_or_404(
        SocialLink,
        pk=pk
    )

    if request.method == "POST":

        social.delete()

        messages.success(
            request,
            "Social link deleted successfully."
        )

    return redirect("social_list")