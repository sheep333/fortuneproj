from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    lng= models.FloatField()
    lat = models.FloatField()
    attribute = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PlaceComment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user_name = models.CharField('ユーザ名', max_length=50)
    text = models.TextField('コメント')

    def __str__(self):
        return f"{self.place}に対する{self.user_name}のコメント"
