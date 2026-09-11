from django.contrib import admin

from .models import (
    Profile,
    Skill,
    Project,
    Experience,
    Education,
    Certification,
    SocialLink,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "email",
        "updated_at",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "order",
    )

    list_filter = (
        "category",
    )

    ordering = (
        "order",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "featured",
        "order",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
    )

    ordering = (
        "order",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "job_title",
        "company",
        "start_date",
        "end_date",
        "currently_working",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "start_year",
        "end_year",
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
        "issue_date",
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "order",
    )