# Defines a J! Archive Item.
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class JarchiveItem(Item):
    # define the fields for your item here like:
    # name = Field()
    correct_response = Field()
    clue = Field()
    value = Field()
    game = Field()
    category = Field()
