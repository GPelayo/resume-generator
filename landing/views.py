from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from bakery.views import BuildableTemplateView
from landing.models import Biography, BootstrapDecorService, Skill, JobItem, HeroSubtitle


def landing(request: HttpRequest) -> HttpResponse:
    context = LandingPageView().get_context_data()

    return render(request, "index.html", context)


class LandingPageView(BuildableTemplateView):
    template_name = "index.html"
    build_path = template_name

    def get_context_data(self, **kwargs):
        biography = Biography.objects.get(name='landing')
        services = BootstrapDecorService.objects.filter(biography=biography)
        skills = sorted(Skill.objects.filter(biography=biography), key=lambda x: x.years, reverse=True)

        for skill in skills:
            skill.percent = int((skill.years/biography.max_years)*100)

        resume = biography.job_sections.all()
        for resume_item in resume:
            resume_item.job_items = JobItem.objects.filter(biography=resume_item)

        return {
            'summary': biography.summary,
            'left_skills': skills[:len(skills)//2 + 1],
            'right_skills': skills[len(skills)//2 + 1:],
            'services': services,
            'resume': sorted(resume, key=lambda x: x.order, reverse=True),
            'subtitles': ', '.join([title.name for title in HeroSubtitle.objects.all()])
        }
