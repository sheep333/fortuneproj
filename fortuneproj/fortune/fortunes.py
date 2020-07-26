from datetime import datetime

from .models import FortuneBoard, UserFortuneType


class Fortune:

    def check_usertype(self, date):
        # 生年月日からタイプを求める
        year = date.year
        month = date.month
        day = date.day
        # とりあえず4で割った余りによってユーザのタイプを分けているだけ
        pattern_num = (year + month + day) % 4
        user_type = UserFortuneType.objects.get(name=pattern_num)
        return user_type

    def check_fortune_direction(self, user_type):
        date = datetime.now
        year = date.year
        month = date.month
        day = date.day

        # とりあえず11を足して4で割ってみただけ
        # これを条件に方位盤を取得して吉方位を取得
        pattern_num = ((year + month + day) + 11) % 4
        # 通常であれば1つしか結果が返ってこない
        fortune_board = FortuneBoard.objects.filter(
            name=pattern_num,
            user_type=user_type,
            start_at__lte=date,
            end_at__gte=date
        ).get()
        return fortune_board.direction
