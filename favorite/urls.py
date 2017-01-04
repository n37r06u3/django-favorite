from django.conf.urls import url

from favorite.views import add_or_remove

urlpatterns = [
    url(r'^add-or-remove$', add_or_remove, name="favorite-add-or-remove"),
]
