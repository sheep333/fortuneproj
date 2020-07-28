from django.db import models

# Create your models here.


class UserFortuneType(models.Model):
    # 生年月日で４パターンに振り分け
    # FIXME: 選択肢もタプルに変更
    choices = (
        [1, 'moon'],
        [2, 'sun'],
        [3, 'star'],
        [4, 'snow'],
    )

    name = models.IntegerField(choices=choices)

    def __str__(self):
        return self.choices[self.name-1][1]


class FortuneBoard(models.Model):
    # 9パターンの盤のどの位置にいるかを返す
    # 例えばmoonタイプはwhiteの盤では北にいる等
    # FIXME: 選択肢もタプルに変更
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

    name = models.IntegerField(choices=board_choices)
    user_type = models.ForeignKey(UserFortuneType, on_delete=models.CASCADE)
    direction = models.IntegerField(choices=direction_choices)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def get_direction(self):
        return self.direction_choices[self.direction-1][1]

    class Meta:
        models.UniqueConstraint(fields=['name', 'user_type'], name='unique_pos')
