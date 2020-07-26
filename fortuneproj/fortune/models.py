from django.db import models

# Create your models here.


class UserFortuneType(models.Model):
    # 生年月日で４パターンに振り分け
    choices = (
        [1, 'moon'],
        [2, 'sun'],
        [3, 'star'],
        [4, 'snow'],
    )

    name = models.CharField(choices=choices, max_length=255)


class FortuneBoard(models.Model):
    # 9パターンの盤のどの位置にいるかを返す
    # 例えばmoonタイプはwhiteの盤では北にいる等
    board_choices = (
        [1, 'white'],
        [2, 'red'],
        [3, 'black'],
        [4, 'blue'],
    )

    direction_choices = (
        [1, 'north'],
        [2, 'south'],
        [3, 'east'],
        [4, 'west'],
    )

    name = models.CharField(choices=board_choices, max_length=255)
    user_type = models.ForeignKey(UserFortuneType,on_delete=models.CASCADE)
    direction_choices = models.CharField(choices=direction_choices, max_length=255)

    class Meta:
        models.UniqueConstraint(fields=['name', 'user_type'], name='unique_pos')
