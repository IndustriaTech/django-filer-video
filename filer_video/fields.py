from filer.fields.file import FilerFileField

from .models import Video


class FilerVideoField(FilerFileField):
    default_model_class = Video
