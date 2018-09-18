from django.db import models
from django.utils import timezone

# Create your models here.
# creating my post model it defines(its an object)


class Post(models.Model):
    # fields available (properties)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
