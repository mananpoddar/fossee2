from django.conf.urls import url
from fossee2 import views
app_name = "fossee2"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadDocument$', views.uploadDocument, name='uploadDocument'),
    url(r'^viewDocument$', views.viewDocument, name='viewDocument'),

]