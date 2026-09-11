from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # PUBLIC PORTFOLIO
    # =========================

    path(
        "",
        views.home,
        name="home"
    ),


    # =========================
    # DASHBOARD AUTH
    # =========================

    path(
        "login/",
        views.dashboard_login,
        name="dashboard_login"
    ),

    path(
        "logout/",
        views.dashboard_logout,
        name="dashboard_logout"
    ),


    # =========================
    # DASHBOARD
    # =========================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # =========================
    # PROFILE
    # =========================

    path(
        "dashboard/profile/",
        views.profile_edit,
        name="profile_edit"
    ),


    # =========================
    # SKILLS
    # =========================

    path(
        "dashboard/skills/",
        views.skill_list,
        name="skill_list"
    ),

    path(
        "dashboard/skills/add/",
        views.skill_create,
        name="skill_create"
    ),

    path(
        "dashboard/skills/<int:pk>/edit/",
        views.skill_edit,
        name="skill_edit"
    ),

    path(
        "dashboard/skills/<int:pk>/delete/",
        views.skill_delete,
        name="skill_delete"
    ),


    # =========================
    # PROJECTS
    # =========================

    path(
        "dashboard/projects/",
        views.project_list,
        name="project_list"
    ),

    path(
        "dashboard/projects/add/",
        views.project_create,
        name="project_create"
    ),

    path(
        "dashboard/projects/<int:pk>/edit/",
        views.project_edit,
        name="project_edit"
    ),

    path(
        "dashboard/projects/<int:pk>/delete/",
        views.project_delete,
        name="project_delete"
    ),


    # =========================
    # EXPERIENCE
    # =========================

    path(
        "dashboard/experience/",
        views.experience_list,
        name="experience_list"
    ),

    path(
        "dashboard/experience/add/",
        views.experience_create,
        name="experience_create"
    ),

    path(
        "dashboard/experience/<int:pk>/edit/",
        views.experience_edit,
        name="experience_edit"
    ),

    path(
        "dashboard/experience/<int:pk>/delete/",
        views.experience_delete,
        name="experience_delete"
    ),


    # =========================
    # EDUCATION
    # =========================

    path(
        "dashboard/education/",
        views.education_list,
        name="education_list"
    ),

    path(
        "dashboard/education/add/",
        views.education_create,
        name="education_create"
    ),

    path(
        "dashboard/education/<int:pk>/edit/",
        views.education_edit,
        name="education_edit"
    ),

    path(
        "dashboard/education/<int:pk>/delete/",
        views.education_delete,
        name="education_delete"
    ),


    # =========================
    # CERTIFICATIONS
    # =========================

    path(
        "dashboard/certifications/",
        views.certification_list,
        name="certification_list"
    ),

    path(
        "dashboard/certifications/add/",
        views.certification_create,
        name="certification_create"
    ),

    path(
        "dashboard/certifications/<int:pk>/edit/",
        views.certification_edit,
        name="certification_edit"
    ),

    path(
        "dashboard/certifications/<int:pk>/delete/",
        views.certification_delete,
        name="certification_delete"
    ),


    # =========================
    # SOCIAL LINKS
    # =========================

    path(
        "dashboard/social/",
        views.social_list,
        name="social_list"
    ),

    path(
        "dashboard/social/add/",
        views.social_create,
        name="social_create"
    ),

    path(
        "dashboard/social/<int:pk>/edit/",
        views.social_edit,
        name="social_edit"
    ),

    path(
        "dashboard/social/<int:pk>/delete/",
        views.social_delete,
        name="social_delete"
    ),

]