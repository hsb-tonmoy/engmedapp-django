from PIL import Image
from imagekit import ImageSpec


class ImageThumb(object):

    def process(self, image):

        max_width = 150

        if image.size[0] > 150:
            wpercent = (max_width/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((max_width, hsize), Image.ANTIALIAS)

        return image


class ImageMed(object):

    def process(self, image):

        max_width = 500

        if image.size[0] > 500:
            wpercent = (max_width/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((max_width, hsize), Image.ANTIALIAS)

        return image


class ImageLarge(object):

    def process(self, image):

        max_width = 1024

        if image.size[0] > 1024:
            wpercent = (max_width/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((max_width, hsize), Image.ANTIALIAS)

        return image


class ImageThumbSpec(ImageSpec):
    processors = [ImageThumb()]

    @property
    def cachefile_name(self):
        source_filename = getattr(self.source, 'name', None)
        source_filename = source_filename.split(".")[:-1]
        filename = "".join(source_filename) + "_thumb.png"
        return filename


class ImageMedSpec(ImageSpec):
    processors = [ImageMed()]

    @property
    def cachefile_name(self):
        source_filename = getattr(self.source, 'name', None)
        source_filename = source_filename.split(".")[:-1]
        filename = "".join(source_filename) + "_med.png"
        return filename


class ImageLargeSpec(ImageSpec):
    processors = [ImageLarge()]

    @property
    def cachefile_name(self):
        source_filename = getattr(self.source, 'name', None)
        source_filename = source_filename.split(".")[:-1]
        filename = "".join(source_filename) + "_large.png"
        return filename
