from django.db import models
from django.utils import timezone

#class is a special keyword that indicates that we are defining an object.

#Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.

#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  #note: you indent the methods inside the class.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
