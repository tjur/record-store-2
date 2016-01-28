from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^albums/(?P<album_id>[0-9]+)/$', views.album_desc, name='album_desc'),
    url(r'^albums/(?P<album_id>[0-9]+)/add$', views.add_to_basket, name='add_to_basket'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.account, name='account'),
    url(r'^user/(?P<user_id>[0-9]+)/basket$', views.basket, name='basket'),
    url(r'^user/(?P<user_id>[0-9]+)/delete_basket_item/(?P<basket_item_id>[0-9]+)$', views.delete_basket_item, name='delete_basket_item'),
    url(r'^user/(?P<user_id>[0-9]+)/create_order$', views.create_order, name='create_order'),
    url(r'^user/(?P<user_id>[0-9]+)/orders$', views.orders, name='orders'),
]