from django.conf.urls import url
from relative_urls import views

# TEMPLATE TAGGING
app_name = 'relative_urls'

urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other')
]
