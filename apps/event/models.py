from django.db import models
from enum import Enum

# Create your models here.
class Portal(models.Model):
    about_us: models.TextField()
    be_a_coach: models.TextField()
    title_coach_session: models.TextField()
    title_sponsor_session: models.TextField()
    site: models.IntegerField()

class Event(models.Model):
    name: models.TextField(max_length=255)
    about: models.TextField()
    begin_date: models.DateTimeField()
    end_date: models.DateTimeField()
    place: models.TextField()
    map_dir: models.TextField()
    portal: models.ForeignKey(Portal, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    event = models.ForeignKey(Event, related_name='faqs', on_delete=models.CASCADE)
    question: models.CharField(max_length=64)
    answer: models.TextField()

    def __str__(self):
        return self.question

class Person(models.Model):
    name: models.TextField()
    email: models.TextField()
    phone: models.TextField()
    city: models.TextField()
    birthdate: models.DateField()
    image: models.ImageField()

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name: models.TextField()
    pic: models.ImageField()
    link: models.TextField()

    def __str__(self):
        return self.name

class OperatingSystem(models.Model):
    name: models.TextField()

    def __str__(self):
        return self.name

class StatusParticipant(models.Model):
    name: models.TextField()

    def __str__(self):
        return self.name
    
class Participant(models.Model):
    operating_system: models.ForeignKey(OperatingSystem, on_delete=models.DO_NOTHING)
    programing_level: models.TextField()
    programming_knowledge: models.TextField()
    current_ocupation: models.TextField()
    reason_assistence: models.TextField()
    status: models.ForeignKey(StatusParticipant, on_delete=models.DO_NOTHING) 
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)

class StatusCoach(models.Model):
    name: models.TextField()

    def __str__(self):
        return self.name


class Language(models.Model):
    name: models.TextField()

    def __str__(self):
        return self.name

class Coach(models.Model):
    github_user: models.TextField()
    operating_systems: models.ManyToManyField(OperatingSystem)
    comfortable_windows: models.BooleanField()
    languages: models.ManyToManyField(Language)
    help_installing: models.BooleanField()
    meet_team: models.BooleanField()
    experience_teaching: models.TextField()
    agree_display_portal: models.BooleanField()
    status: models.ForeignKey(StatusCoach, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, related_name='coaches', on_delete=models.CASCADE)

class Organizer(models.Model):
    name: models.TextField()
    email: models.TextField()
    phone: models.TextField()
    pic: models.ImageField()
    event = models.ForeignKey(Event, related_name='organizers', on_delete=models.CASCADE)





