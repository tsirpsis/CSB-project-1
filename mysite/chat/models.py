from django.db import models

class Thread(models.Model):
    header = models.CharField(max_length=500)
    content = models.TextField()
    pub_date = models.DateTimeField('date sent')

    def __str__(self):
        return self.header

class Message(models.Model):
    thread =  models.ForeignKey(Thread, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message
