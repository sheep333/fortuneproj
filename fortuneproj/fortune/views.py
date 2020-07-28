from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView

from .forms import UserInfoForm
from .fortunes import Fortune
from .maps import Map


class Top(FormView):
    form_class = UserInfoForm
    template_name = 'fortune/top.html'
    success_url = reverse_lazy('fortune:top')

    def form_valid(self, form):
        birthday = form.cleaned_data["birthday"]
        here_lng= float(self.request.POST["lng"])
        here_lat = float(self.request.POST["lat"])
        location = {
            "lng": here_lng,
            "lat": here_lat
        }

        # ユーザのタイプと吉方位を返却
        fortune = Fortune()
        user_type = fortune.check_usertype(birthday)
        fortune_direction = fortune.check_fortune_direction(user_type)

        # 現在地と比較してGoogleMap or Placeモデルから場所を取得
        gmap = Map()
        # とりあえずスポット検索キーワードは固定
        spot_name = "パワースポット"
        fortune_spot_list = gmap.get_match_spot(
            location=location,
            direction=fortune_direction,
            spot_name=spot_name,
        )

        context = {
            "user_type": user_type,
            "fortune_direction": fortune_direction,
            "spot_list": fortune_spot_list,
        }

        return render(self.request, 'place/fortune_list.html', context)



