from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from dirtybot.items import DirtybotItem

class DirtySpider(CrawlSpider):
    name = 'dirtybot'
    allowed_domains = ["erento.com", "erento.de", "miet24.de"]
    start_urls = [
        "http://www.erento.de",
    #    "http://www.miet24.de",
    ]
    account = 0
    rules = (
        #first level xpath="//li/a[@class='home_kat_head']/@data-href"
        Rule(SgmlLinkExtractor(allow=(), 
                restrict_xpaths=("//li/a[@class='home_kat_head']"), 
                attrs=('data-href',)), ),

        #second level xpath="//div[@class='div_main_content']/div[starts-with(@class, 'inner')]//a[@class='arial12']/@href"
        Rule(SgmlLinkExtractor(allow=(), 
                restrict_xpaths=("//div[@class='div_main_content']/div[starts-with(@class, 'inner')]//a[@class='arial12']",)),),

        #third level xpath="//ul[@class='uiItemList']/li[contains(concat(' ',normalize-space(@class),' '), 'typeTop')]//h3/a/@href"
        Rule(SgmlLinkExtractor(allow=(), 
                restrict_xpaths=("//ul[@class='uiItemList']/li[contains(concat(' ',normalize-space(@class),' '), 'typeTop')]//h3/a",)),
            callback='parse_item'),
        
        #item page xpath="//div[@class='uiMultiBox-bdPrimary']"
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
#        Rule(SgmlLinkExtractor(allow=('item\.php', )), ),
    )

    def parse_item(self, response):
    #def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        self.account += 1
        print "parse item ", self.account
        
        sel = Selector(response)
        item = DirtybotItem()
        #sites = sel.xpath("//div[@class='uiMultiBox-bdPrimary']/div[@class='contactDataBox-phone' and not(contains(@style,'display:none'))]//h3").extract()
        sites = sel.xpath("//div[@class='uiMultiBox-bdPrimary']").extract()
        companylink = sel.xpath("//a[@class='hireCompanySerpLink']/@href").extract()
        if not sites and not companylink:
            return
        self.log(sites)
        item["contact_info"] = sites
        item["companylink"] = companylink
        return item
