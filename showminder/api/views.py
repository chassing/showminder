from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .utils import parse_filename
from frontend.models import TvShow


@method_decorator(csrf_exempt, name='dispatch')
class UpdateView(View):  # noqa

    def post(self, request, *args, **kwargs):
        try:
            filename = request.POST['filename']
        except KeyError:
            return HttpResponse("Bad POST data. must include 'filename'", status_code=400)

        try:
            title, season, episode = parse_filename(filename)
        except:
            return HttpResponse(f"unable to get info from filename {filename}", status_code=500)

        try:
            tv = TvShow.objects.get(title__icontains=title)
        except TvShow.DoesNotExist:
            return HttpResponse(f"unable to find {title}in db", status_code=404)

        if tv.season < season:
            # update season and episode in this case
            tv.season = season
            tv.episode = episode
        elif tv.episode < episode:
            tv.episode = episode
        tv.save()

        return HttpResponse(f"""filename - title: {title} season: {season} episode: {episode} | db - title: {tv.title} season: {tv.season} episode: {tv.episode} """)
