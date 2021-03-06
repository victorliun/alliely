"""
This module privides an api talks to url2png server. 
"""
import urllib
from lxml import html
from PIL import Image

import os, logging

class URL2PNGClient():
    """
    A Client class, it will send request to the url2png server.
    Parse the response, get the expect png file url, then Create a Thumbnail.
    NOTE: User should get a plan from url2png(http://url2png.com/plans/)
    site before this goes online.
    """
    URL2PNG_URL="http://www.url2png.com/"

    def __init__(self, options):
        """
        Initialize it by giving an option dict.
        """
        self.query_string = urllib.urlencode(options)
        #TODO: Add follows after having a plan from url2png
        #self.apikey = 'PXXXX'
        #self.secret = 'SXXXX'
        #self.token = hashlib.md5(self.query_string + self.secret).hexdigest()
 
    @property
    def get_png_url(self):
        """
        This function will return the url of the png file generated by server.
        """

        url = "%s?%s" %(self.URL2PNG_URL, self.query_string)
        tree = html.parse(url)
        #Here I expect to find a link of png file.
        #*Warning: This is hard code, may not work if the site updated.
        tag_a = tree.find("//div[@class='alert alert-success']/a")

        if tag_a is not None:
            logging.info("Get png url: %s" %tag_a.attrib['href'])
            return tag_a.attrib['href']
        else:
            logging.warning("Can't find the png file url from %s" %url)
            return None
 
def save_image_from_url(url, path):
    """
    This function saves any image from url to the path.
    url: The image url to save.
    path: where to save this image.
    """
    try:
        urllib.urlretrieve(url,path)
    except IOError, err:
        logging.error("Save failed. %s" %err)
        return False
    except Exception, err:
        logging.error("Unknow Error: %s" %err)
        return False
    return True

def create_thumbnail(image_path, image_type="PNG", save_to=None):
    """
    This function will create a thumbnail file for the image, 
    Save to the same path if no save to path given.
    """

    thumbnail_width, thumbnail_height = 300, 300
    img = Image.open(image_path)
    img.convert('RGB')
    img.thumbnail((thumbnail_width, thumbnail_height), Image.ANTIALIAS)

    img_name, img_ext = image_path.split('.')
    if not save_to:
        file_name = "%s-thumbnail%dx%d.%s" %(img_name, thumbnail_width, 
            thumbnail_height, img_ext)
    else:
        file_name = "%s-thumbnail%dx%d.%s" %(save_to, thumbnail_width,
            thumbnail_height, img_ext)
    try:
        img.save(file_name, image_type)
    except IOError, err:
        logging.error("Save %s failed. %s" %(file_name, err))
        return False
    return True


def test_url2png():
    """
    This function test if every functions works fine.
    """
    options = {'url': "http://www.google.com"}
    image_url = URL2PNGClient(options).get_png_url
    assert image_url

    save_image_from_url(image_url, 'test.png')
    assert os.path.exists("test.png")

    create_thumbnail("test.png")
    assert os.path.exists("test-thumbnail300x300.png") 

    if os.path.exists("test-thumbnail300x300.png"):
        os.remove("test-thumbnail300x300.png")
    if os.path.exists("test.png"):
        os.remove("test.png")
