from django.contrib import admin
from models import Artist, Genre, Album, BasketItem, Basket, OrderItem, Order

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = ("name", "get_artist_name", "get_genre", "year")
    fields = ( "artist", "genre", "name", "year", "image_tag", "cover", "price", "quantity", "desc")
    readonly_fields = ("image_tag",)

    def get_artist_name(self, obj):
        return obj.artist.name

    def get_genre(self, obj):
        return obj.genre.name

    get_artist_name.admin_order_field  = 'name'
    get_artist_name.short_description = 'Artist name'
    get_genre.admin_order_field  = 'name'
    get_genre.short_description = 'Genre'


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("id", "start_date", "user", "amount", "status")
    fields = ( "id", "start_date", "user", "amount", "status")
    readonly_fields = ("id", "start_date", "user", "amount")


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Order, OrderAdmin)
