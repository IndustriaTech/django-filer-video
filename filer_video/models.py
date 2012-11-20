import os

from filer.models.filemodels import File

# we'll need to refer to filer settings
from filer import settings as filer_settings


class Video(File):
    # the icon it will use
    _icon = "video"

    # declare the file_type for the list template
    file_type = 'Video'

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.dv', '.mov', '.mp4', '.avi', 'mpeg', '.wmv', '.flv']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions
