# Scrapy settings for reuters_article_download project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'reuters_article_download'

SPIDER_MODULES = ['reuters_article_download.spiders']
NEWSPIDER_MODULE = 'reuters_article_download.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'reuters_article_download (+http://www.yourdomain.com)'
