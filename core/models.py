from django.db import models
import datetime

class GuestbookEntry(models.Model):
    message = models.TextField(blank=False)
    name = models.CharField(blank=True,max_length=50)
    display = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_entries():
        return GuestbookEntry.objects.filter(display__exact=True).order_by('-created_date',)

    def __unicode__(self):
        return u"%s" % self.name