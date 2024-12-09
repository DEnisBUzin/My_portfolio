from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=250)
    title = models.TextField()
    slug = models.SlugField(max_length=250)
    date_create = models.DateField()
    date_update = models.DateField(auto_now=True)
    link_of_git = models.URLField()

    def __str__(self):
        return self.name
