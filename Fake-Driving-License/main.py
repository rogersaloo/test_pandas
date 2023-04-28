from abc import abstractmethod, ABC
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests

original = "images/fake_dl/fake_image.png"
tampered = "images/original_dl/original_image.png"


class LoadImage:
    @staticmethod
    def open_image(org, fake):
        """Load raw images"""
        open_original = Image.open(org)
        open_fake = Image.open(fake)
        return open_original, open_fake

    @staticmethod
    def load_resized_image(org, fake):
        """Load resized images"""
        # load the two input images
        original_resized = cv2.imread('images/fake_dl/fake_resize.png')
        tampered_resized = cv2.imread('images/fake_dl/fake_resize.png')
        return original_resized, tampered_resized


class ImageProperties:
    """ Check the properties onf the images loaded"""

    @abstractmethod
    def __init__(self, org, fake):
        self.original = org
        self.fake = fake

    def check_image_format(self):
        """Check loaded image format"""
        image = LoadImage.open_image(self.original, self.fake)
        original_format = f"Original image format :  {image[0].format}"
        tampered_format = f"Tampered image format :  {image[1].format}"
        return original_format, tampered_format

    def check_image_size(self):
        """ Check the image size"""
        image = LoadImage.open_image(self.original, self.fake)
        original_format = f"Original image size : {image[0].size}"
        tampered_format = f"Tampered image size : {image[1].size}"
        return original_format, tampered_format


class ResizeImage:
    """Resizer the image input"""
    def __init__(self, org, fake, length=250, width=160):
        self.fake_resized = None
        self.original_resized = None
        self.original = org
        self.fake = fake
        self.length = length
        self.width = width

    def resize_image(self):
        """Resize and save image"""
        image = LoadImage.open_image(self.original, self.fake)
        self.original_resized = image[0].resize((self.length, self.width))
        original.save('images/original_dl/original_resize.png')
        self.fake_resized = image[1].resize((self.length, self.width))
        tampered.save('images/fake_dl/fake_resize.png')

    def convert_grayscale(self):
        """Convert from RGB to Grayscale"""
        original_gray = cv2.cvtColor(self.original_resized, cv2.COLOR_BGR2GRAY)
        tampered_gray = cv2.cvtColor(self.fake_resized, cv2.COLOR_BGR2GRAY)

# # def load_images():
#
# # # Resize Image
# # original = original.resize((250, 160))
# # print(original.size)
# # original.save('original_image/image/original.png')#Save image
# # tampered = tampered.resize((250,160))
# # print(tampered.size)
# # tampered.save('fake_image/image/fake.png')#Saves image

def main():
    image_properties = ImageProperties(original, tampered)
    image_format = image_properties.check_image_format()
    image_size = image_properties.check_image_size()
    resize_image = ResizeImage(original, tampered)
    resize_image.resize_image()
    print(f"{image_format} \n{image_size}")


if __name__ == '__main__':
    main()
