from math import atan2, cos, pi, sin, tan


class Map:
    def _azimuth(self, x1, y1, x2, y2):
        # Radian角に修正
        _x1, _y1, _x2, _y2 = x1*pi/180, y1*pi/180, x2*pi/180, y2*pi/180
        Δx = _x2 - _x1
        _y = sin(Δx)
        _x = cos(_y1) * tan(_y2) - sin(_y1) * cos(Δx)

        psi = atan2(_y, _x) * 180 / pi
        if psi < 0:
            return 360 + psi
        else:
            return psi

    def _get_spot_from_api(self, **kwargs):
        # envからAPI KEYを取得
        # SearchAPIを叩くURLを作成
        # JSONをListに変換
        spot_list = []
        return spot_list

    def _calc_direction(self, here, place):
        direction = self._azimuth(here['lan'], here['lat'], place['lan'], place['lat'])
        if (direction > 0 and direction < 45) or (direction > 315 and direction < 360):
            return 'north'
        elif direction > 45 and direction < 135:
            return 'east'
        elif direction > 135 and direction < 225:
            return 'south'
        elif direction > 225 and direction < 315:
            return 'west'
        else:
            return None

    @classmethod
    def get_match_spot(cls, **kwargs):
        fortune_spot_list = []
        # 検索したいパワースポット名
        spot_name = kwargs['spot_name']
        # 吉方位
        direction = kwargs['direction']
        # 現在地
        here = kwargs['here']

        # 周辺のパワースポットを検索
        spot_list = cls._get_spot_from_api(spot_name=spot_name)
        # 条件の合うもののみリストに追加
        for spot in spot_list:
            spot_direction = cls._calc_direction(here, spot)
            if direction == spot_direction:
                fortune_spot_list.append(spot)

        return fortune_spot_list
