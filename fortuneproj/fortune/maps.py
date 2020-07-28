from math import atan2, cos, pi, sin, tan
from os import getenv

import googlemaps


class Map:
    def _azimuth(self, x1, y1, x2, y2):
        """
        方位角を計算。地点1からみた地点2の角度を360度で表して返却。
        """
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
        api_key = getenv("MAP_API_KEY")
        # SearchAPIを叩くURLを作成
        gmaps = googlemaps.Client(key=api_key)
        places = gmaps.places_nearby(
            location=kwargs["location"], #現在地
            keyword=kwargs["spot_name"], #検索キーワード
            language='ja',
            radius=100000,
        )
        return places["results"]

    def _calc_direction(self, here, place):
        """
        現在地と場所の緯度経度から現在地からみた場所の方位を返却
        """
        direction = self._azimuth(here['lng'], here['lat'], place['geometry']['location']['lng'], place['geometry']['location']['lat'])
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

    def get_match_spot(self, **kwargs):
        # 現在地
        here = kwargs['location']
        direction = kwargs['direction']

        # 周辺のパワースポットを検索
        spot_list = self._get_spot_from_api(**kwargs)
        # 吉方位に合うもののみリストに追加
        fortune_spot_list = []
        for spot in spot_list:
            spot_direction = self._calc_direction(here, spot)
            if direction == spot_direction:
                fortune_spot_list.append(spot)

        return fortune_spot_list
