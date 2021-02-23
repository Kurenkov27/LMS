from academy.models import Group, Lecturer, Student, Message

from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver

from .tasks import send_email


@receiver(pre_save, sender=Student)
def capitalize_student(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Lecturer)
def capitalize_lecturer(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Group)
def capitalize_person(sender, instance, **kwargs):
    instance.course = instance.course.capitalize()


@receiver(post_save, sender=Message)
def initiate_sending_email(sender, instance, **kwargs):
    send_email.delay(instance.to_dict())

