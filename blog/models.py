# criado em 30/06/2016 - Raymundo Eduado Santos Junior
# fonte: http://tutorial.djangogirls.org/pt/django_models/
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # 30/06/2016 FONTE: http://stackoverflow.com/questions/25455379/django-auth-model-error-name-user-is-not-defined
# se acima, ...contrib.auth..., for comentado em author = models.ForeignKey('auth.User') será usado auth.User entre aspas simples

# Create your models here.

class Post(models.Model):
    #author = models.ForeignKey('auth.User') ERRADO
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)


def publish(self):
    self.publish_date = timezone.now()
    self.save()


def __str__(self):
    return self.title
