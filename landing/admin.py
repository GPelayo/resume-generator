from django.contrib import admin

from landing.models import Biography, ResumeItem, JobItem, Skill, BootstrapDecorService, HeroSubtitle


class JobItemInline(admin.StackedInline):
    model = JobItem
    extra = 1


class ResumeItemAdmin(admin.ModelAdmin):
    fields = ['name', 'years', 'position', 'location', 'order']
    inlines = [JobItemInline]


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class ServicesInline(admin.StackedInline):
    model = BootstrapDecorService
    extra = 1


class BiographyAdmin(admin.ModelAdmin):
    fields = ['name', 'summary', 'max_years', 'resume_item']
    inlines = [SkillInline, ServicesInline]


admin.site.register(Biography, BiographyAdmin)
admin.site.register(ResumeItem, ResumeItemAdmin)
admin.site.register(HeroSubtitle)
admin.site.register(Skill)
