from django.db import models
from django.utils.translation import gettext_lazy


class ContactInfo(models.Model):
    class ContactType(models.TextChoices):
        OTHER = 'other', gettext_lazy('Other')
        GITHUB = 'github', gettext_lazy('Github')
        MOBILE_PHONE = 'mobile-phone', gettext_lazy('Mobile Phone Number')
        PERSONAL_WEBSITE = 'personal-website', gettext_lazy('Website')
        LINKEDIN = 'linkedin', gettext_lazy('LinkedIn')
        EMAIL = 'email', gettext_lazy('Email')


    name = models.CharField(max_length=31, primary_key=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=31, null=True, blank=True)
    info = models.CharField(max_length=255)
    order = models.IntegerField()
    contact_type = models.CharField(max_length=31, choices=ContactType.choices, default=ContactType.OTHER)
    biography = models.ForeignKey('Biography', on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.display_name:
            self.display_name = self.name
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.display_name or self.name


class EducationSection(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    order = models.IntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=31)
    years = models.PositiveIntegerField()
    biography = models.ForeignKey('Biography', on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.pk}) {self.name}"


class Service(models.Model):
    name = models.CharField(max_length=31)
    description = models.TextField()
    biography = models.ForeignKey('Biography', on_delete=models.CASCADE)


class BootstrapDecorService(Service):
    bootstrap_icon = models.CharField(max_length=31)

    class Meta:
        verbose_name = 'Bootstrap Decor Service Item'
        verbose_name_plural = 'Bootstrap Decor Service Items'


class JobSection(models.Model):
    name = models.CharField(max_length=31)
    years = models.CharField(max_length=15)
    position = models.CharField(max_length=31)
    location = models.CharField(max_length=31)
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f"({self.pk}) {self.name}"


class JobItem(models.Model):
    description = models.TextField()
    biography = models.ForeignKey('landing.JobSection', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Job Item'
        verbose_name_plural = 'Job Items'


class Person(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Biography(models.Model):
    biography_name = models.CharField(max_length=15, primary_key=True)
    hero = models.ForeignKey(Person, on_delete=models.CASCADE)
    summary = models.TextField()
    max_years = models.PositiveIntegerField()
    job_sections = models.ManyToManyField('landing.JobSection', blank=True)
    education_sections = models.ManyToManyField('landing.EducationSection', blank=True)

    def __str__(self):
        return self.biography_name

    class Meta:
        verbose_name_plural = 'Biographies'


class HeroSubtitle(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
