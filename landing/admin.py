from django.contrib import admin

from landing.models import (Biography,
                            BootstrapDecorService,
                            ContactInfo,
                            EducationSection,
                            HeroSubtitle,
                            JobItem,
                            Person,
                            ResumeItem,
                            Skill)


class JobItemInline(admin.StackedInline):
    model = JobItem
    extra = 1


class JobSectionAdmin(admin.ModelAdmin):
    fields = ['name', 'years', 'position', 'location', 'order']
    inlines = [JobItemInline]


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class ServicesInline(admin.StackedInline):
    model = BootstrapDecorService
    extra = 1


class BiographyAdmin(admin.ModelAdmin):
    fields = ['name', 'summary', 'max_years', 'job_sections', 'education_sections']
    inlines = [SkillInline, ServicesInline]


class EducationAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'country', 'degree', 'graduation_year']


class ContactInfoAdmin(admin.ModelAdmin):
    fields = ['name', 'display_name', 'info']


admin.site.register(Biography, BiographyAdmin)
admin.site.register(ResumeItem, ResumeItemAdmin)
admin.site.register(HeroSubtitle)
admin.site.register(Skill)
admin.site.register(ContactInfo)
admin.site.register(EducationSection)
admin.site.register(Person)
