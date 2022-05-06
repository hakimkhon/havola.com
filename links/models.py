from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    url = models.URLField() 
    creted_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)


# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
# python manage.py shell
