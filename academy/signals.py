from django.template.loader import render_to_string

from LMS.settings import SENDGRID_KEY, EMAIL_SENDER, EMAIL_RECEIVER

from academy.models import Group, Lecturer, Student, Message

from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import Mail


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
def send_notification(sender, instance, **kwargs):
    context = {'message': instance}
    content = render_to_string('academy/added_message.html', context)
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=EMAIL_RECEIVER,
        subject='Added new comment',
        html_content=content
    )
    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message)
