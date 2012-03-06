from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from jarchive.items import JarchiveItem

def first(l):
  if isinstance(l, list) and len(l) > 0:
    return l[0]
  else:
    return None


class JarchiveSpider(CrawlSpider):
  name = 'jarchive'
  start_urls = ['http://www.j-archive.com/listseasons.php']
  allowed_domains = ['www.j-archive.com']
  
  rules = (Rule(SgmlLinkExtractor(allow=('showseason\.php'))),
           Rule(SgmlLinkExtractor(allow=('showgame\.php')), callback='parse_game'))
  
  def parse_game(self, response):
    self.log("Found game page %s" % response.url)
    hxs = HtmlXPathSelector(response)
    clues = hxs.select('//td[@class="clue"]')
    jitems = []
    game = first(hxs.select('//div[@id="game_title"]/h1/text()').extract())
    cats = hxs.select('//td[@class="category_name"]/text()').extract()
    self.log(game)
    for clue in clues:
      jitem = JarchiveItem()
      found = clue.select('table/tr/td/div/@onmouseover').extract()

      if len(found) > 0:
        clueinfo = first(clue.select('.//td[@class="clue_text"]/@id').extract()).split("_")
        round = clueinfo[1]
        cluecol = int(clueinfo[2])-1
        if round == "DJ":
          cluecol+=6
        togglebox = found[0].split("', '")
        cr = HtmlXPathSelector(text=togglebox[2]).select(".//em[@class='correct_response']/text()")
        cr = first(cr.extract())
        v = first(clue.select('.//td[@class="clue_value"]/text()').extract())
        if v:
          v = v[1:]
        c = first(clue.select('.//td[@class="clue_text"]/text()').extract())
        (jitem['correct_response'], jitem['value'], jitem['clue'], jitem['game'], jitem['category']) = cr, v, c, game, cats[cluecol]
        jitems.append(jitem)
    return jitems
