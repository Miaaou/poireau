from __future__ import unicode_literals

from django.views.generic import View, ListView, DetailView
from django import http
from django.core.urlresolvers import reverse_lazy as reverse

from poireau.common.views import BaseViewMixin
from poireau.songs.models import Song


class SongMixin(BaseViewMixin):
    model = Song


class SongListView(SongMixin, ListView):
    template_name = "songs/list.html"
    menu_list = ["songs"]

    def get_queryset(self):
        return super(SongListView, self).get_queryset().order_by("path")


class SongDetailView(SongMixin, DetailView):
    template_name = "songs/detail.html"
    menu_list = ["songs"]


class SongRandomView(SongMixin, View):

    def get(self, request):
        song = Song.objects.order_by("?").first()
        if song:
            return http.HttpResponseRedirect(song.get_absolute_url())
        else:
            return http.HttpResponseRedirect(reverse("song_list"))
