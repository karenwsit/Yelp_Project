from scrapy.item import Item, Field

class YelpReview(Item):
    """Yelp container (dictionary-like object) for scraped data"""

    review_id = Field()
    text = Field()
    rating = Field()
    date = Field()
    reviewer_location = Field()
    restaurant_id = Field()
