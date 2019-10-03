from mptt.admin import DraggableMPTTAdmin


class FilesAdmin(DraggableMPTTAdmin):
    mptt_ident_field = 'name'
