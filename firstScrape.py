#!/usr/bin/env python
# coding: utf-8

# In[56]:


import scrapy

class FirstScrape(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            'https://www.ulta.com/hair-treatment-oils-serums?N=27ft'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        for content in response.css('div.productQvContainer'):
#             form = response.css('div.FormContainer')
#             yield {
            s = ""
            item = {}
            product_title = content.css('div.prod-title-desc > .prod-title > a::text').extract()[0].strip(),
            item["product_title"] = s.join(product_title)
            product_description = content.css('div.prod-title-desc > .prod-desc > a::text').extract()[0].strip(),
            item["product_description"] = s.join(product_description)
            product_price = content.css('div.productPrice > span::text').extract()[0].strip(),
            item["product_price"] = s.join(product_price)
#             }
            with open('result.json', 'a') as f:
                print(item, file=f)
#             print(item)
    
#             print(f'product-title: {product_title}\nproduct-description: {product_description}\nproduct-price: {product_price}'/)


# In[ ]:




