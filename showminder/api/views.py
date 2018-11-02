
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

from .models import ApiNotification
from .utils import parse_filename
from frontend.models import TvShow


@method_decorator(csrf_exempt, name="dispatch")
class UpdateView(View):
    def post(self, request, *args, **kwargs):
        try:
            filename = request.POST["filename"]
        except KeyError:
            return HttpResponse("Bad POST data. must include 'filename'", status=400)

        try:
            title, season, episode = parse_filename(filename)
        except:
            ApiNotification.add_message("Parse error", f"Failed to parse '{filename}'!")
            return HttpResponse(f"unable to get info from filename {filename}", status=400)

        tvs = TvShow.objects.filter(title__icontains=title)
        if tvs.count() == 0:
            ApiNotification.add_message("Not found", f"title '{title}' not found in db!")
            return HttpResponse(f"unable to find {title} in db", status=404)
        elif tvs.count() > 1:
            ApiNotification.add_message(
                "Multiple Results",
                f"Filename {filename} returned {', '.join([tv.title for tv in tvs])}! {tvs[0].title} was updated!",
            )

        # take always the newest one
        tv = tvs[0]
        if tv.season < season:
            # update season and episode in this case
            tv.season = season
            tv.episode = episode
        elif tv.episode < episode:
            tv.episode = episode
        tv.save()

        return HttpResponse(
            f"""filename - title: {title} season: {season} episode: {episode} | db - title: {tv.title} season: {tv.season} episode: {tv.episode} """
        )


class DeleteNotificationView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        an = get_object_or_404(ApiNotification, pk=kwargs["pk"])
        an.delete()
        return super().get_redirect_url(*args, **kwargs)
