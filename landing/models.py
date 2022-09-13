from django.db import models


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


class ResumeItem(models.Model):
    name = models.CharField(max_length=31)
    years = models.CharField(max_length=15)
    position = models.CharField(max_length=31)
    location = models.CharField(max_length=31)
    order = models.IntegerField()

    class Meta:
        verbose_name = 'Resume Item'
        verbose_name_plural = 'Resume Items'

    def __str__(self):
        return f"({self.pk}) {self.name}"


class JobItem(models.Model):
    description = models.TextField()
    biography = models.ForeignKey('ResumeItem', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Job Item'
        verbose_name_plural = 'Job Items'


class Biography(models.Model):
    name = models.CharField(max_length=15, primary_key=True)
    summary = models.TextField()
    max_years = models.PositiveIntegerField()
    resume_item = models.ManyToManyField('ResumeItem', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Biographies'


class HeroSubtitle(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
