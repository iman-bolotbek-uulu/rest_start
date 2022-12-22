from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def str(self):
        return f'{self.author} - {self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Mark(models.Model):
    mark_value = models.IntegerField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='marks')

    def __str__(self):
        return self.mark_value
