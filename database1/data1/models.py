from django.db import models
class Faculty(models.Model):
    fid = models.CharField(primary_key=True, max_length=9)
    fname = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty'


