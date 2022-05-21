from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


    class Meta:
        ordering = ['-updated']



## user=ugyen
## pw = ugendi


## python -m pip install django-cors-headers

## INSTALLED_APPS = [
#     ...,
#     "corsheaders",
#     ...,
# ]



# You will also need to add a middleware class to listen in on responses:

# MIDDLEWARE = [
#     ...,
#     "corsheaders.middleware.CorsMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     .




### CORS_ALLOW_ALL_ORIGINS