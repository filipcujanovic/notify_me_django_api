from django.db import models


class NotifyMunicipalities(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notify_municipalities'


class NotifyMunicipalitiesUsers(models.Model):
    municipalitiy_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notify_municipalities_users'
        unique_together = (('municipalitiy_id', 'user_id'),)
