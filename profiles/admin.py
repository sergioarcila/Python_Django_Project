from django.contrib import admin
from profiles.models import PlayerProfile, VideoLink, GeneralPicture

class PlayerProfileAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(PlayerProfile, PlayerProfileAdmin)
admin.site.register(VideoLink)
admin.site.register(GeneralPicture)
