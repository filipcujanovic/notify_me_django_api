# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class Busses(models.Model):
    bus_route_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notify_busses'

    def delete(self):
        self.deleted_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.save()


class BussesUsers(models.Model):
    bus_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notify_busses_users'
        unique_together = (('bus_id', 'user_id'),)

    def delete(self):
        self.deleted_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.save()


class CurrentBussesRouteChanges(models.Model):
    bus_id = models.IntegerField()
    route_change = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notify_current_busses_route_changes'

    def delete(self):
        self.deleted_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.save()
