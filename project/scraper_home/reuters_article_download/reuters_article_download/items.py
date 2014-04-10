# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ReutersArticleDownloadItem(Item):
    # define the fields for your item here like:
    # name = Field()
    article_name = Field()
    article_url = Field()
    pub_date_time = Field()
    
