from typing import List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from bakery.views import BuildableTemplateView
from landing.models import (Biography,
                            ContactInfo,
                            EducationSection,
                            JobHighlight,
                            HeroSubtitle,
                            Skill)


class ContactButtonFactory:
    class ContactButton:
        contact_link: str
        boxicon_class: str
        button_class: str

        def __init__(self, name):
            contact_type = ContactInfo.ContactType
            contact_info = ContactInfo.objects.get(name=name)
            self.contact_link = contact_info.info
            if contact_info.contact_type == contact_type.GITHUB:
                self.boxicon_class = 'bx bxl-github'
                self.button_class = 'github'
            elif contact_info.contact_type == contact_type.LINKEDIN:
                self.boxicon_class = 'bx bxl-linkedin'
                self.button_class = 'linkedin'
            elif contact_info.contact_type == contact_type.EMAIL:
                self.boxicon_class = 'bx bx-envelope'
                self.button_class = 'email'
                contact_info.info = f'mailto:{contact_info.info}'
            else:
                self.boxicon_class = 'bx bx-paper-plane'

    def create_buttons(self, names: List[str]):
        return [self.ContactButton(name) for name in names]

def landing(self) -> HttpResponse:
    context = LandingPageView().get_context_data()
    return render(self, "index.html", context)


class LandingPageView(BuildableTemplateView):
    template_name = "index.html"
    build_path = template_name

    def get_context_data(self, **kwargs):
        biography = Biography.objects.get(biography_name='landing')
        skills = sorted(Skill.objects.filter(biography=biography), key=lambda x: x.years, reverse=True)

        contact_names = ['E-Mail', 'Github', 'LinkedIn']

        for skill in skills:
            skill.percent = int((skill.years/biography.max_years)*100)

        resume = biography.job_sections.all()
        for resume_item in resume:
            resume_item.job_items = JobItem.objects.filter(biography=resume_item)

        return {
            'hero': biography.hero,
            'biography': biography,
            'left_skills': skills[:len(skills)//2 + 1],
            'right_skills': skills[len(skills)//2 + 1:],
            'contact_info': buttons,
            'resume': sorted(resume, key=lambda x: x.order, reverse=True),
            'education': EducationSection.objects.all(),
            'subtitles': ', '.join([title.name for title in HeroSubtitle.objects.filter(name='Software Engineer')])
        }
