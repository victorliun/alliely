from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from lxml import etree

from reuters_article_download.items import ReutersArticleDownloadItem

class ArticleDownloadSpider(CrawlSpider):
    name = 'reuters_article_download'
    allowed_domains = ["reuters.com",]
    start_urls = [
        #"http://www.reuters.com/",
        "http://www.reuters.com/resources/archive/us/2011.html",
    ]
    account = 0
    rules = (
        #first level xpath="//li/a[@class='home_kat_head']/@data-href"
        Rule(SgmlLinkExtractor(allow=(), 
                restrict_xpaths=("//div[@class='moduleBody']//p/a"), 
                attrs=('href',)), callback='parse_item'),# process_links='process_links',  ,

        #second level xpath="//div[@class='div_main_content']/div[starts-with(@class, 'inner')]//a[@class='arial12']/@href"
        #Rule(SgmlLinkExtractor(allow=(), 
        #       restrict_xpaths=("//div[@class='div_main_content']/div[starts-with(@class, 'inner')]//a[@class='arial12']",)),),

        #third level xpath="//ul[@class='uiItemList']/li[contains(concat(' ',normalize-space(@class),' '), 'typeTop')]//h3/a/@href"
        #Rule(SgmlLinkExtractor(allow=(), 
        #        restrict_xpaths=("//ul[@class='uiItemList']/li[contains(concat(' ',normalize-space(@class),' '), 'typeTop')]//h3/a",)),
        #    callback='parse_item'),
        
        #item page xpath="//div[@class='uiMultiBox-bdPrimary']"
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
#        Rule(SgmlLinkExtractor(allow=('item\.php', )), ),
    )
    def process_links(self,links):
        for i, link in enumerate(links):
            link.url = "http://www.reuters.com" + link.url
            links[i] = link
        return links


    def parse_item(self, response):
    #def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        self.account += 1
        print "parse item ", self.account
        
        sel = Selector(response)
        articles = sel.xpath("//div[@class='headlineMed']/a").extract()
        items = []
        for article in articles:
            root = etree.fromstring(article)
            if root.text != "Following Is a Test Release":
                item = ReutersArticleDownloadItem()
                item['article_name'] = root.text
                item['article_url'] = root.attrib['href']
                items.append(item)
        
        return items
