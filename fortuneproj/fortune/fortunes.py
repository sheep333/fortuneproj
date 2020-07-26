from datetime import datetime

from .models import FortuneBoard, UserFortuneType


class Fortune:

    @classmethod
    def check_usertype(cls, date):
        # 生年月日からタイプを求める
        year = date.year
        month = date.month
        day = date.day
        pattern_num = (year + month + day) % 4
        user_type = UserFortuneType.object.get(name=pattern_num)
        return user_type

    @classmethod
    def check_fortune_direction(cls, user_type):
        date = datetime.now
        year = date.year
        month = date.month
        day = date.day
        pattern_num = ((year + month + day) + 11) % 4
        fortune_direction = FortuneBoard.object.get(name=pattern_num, user_type=user_type)
        return fortune_direction
