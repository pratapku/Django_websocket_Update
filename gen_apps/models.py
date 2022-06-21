from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    change_variable = models.IntegerField()
    change_variable1 = models.IntegerField()
    # change_variable2 = models.IntegerField()
    # change_variable3 = models.IntegerField()



    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.room