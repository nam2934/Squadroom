from django.conf import settings
from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=50, null=True,default='')
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    content = models.TextField(max_length=1000, default='')
    pub_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
    #def get_absolute_url(self): #8
    #    return reverse("book-detail", args=[str(self.id)]