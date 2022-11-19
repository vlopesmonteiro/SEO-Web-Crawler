import advertools as adv
from advertools import crawl
import pandas as pd


url_list = ['https://shopee.com.br/m/black-friday', 
            'https://www.americanas.com.br/especial/black-friday', 
            'https://www.mercadolivre.com.br/black-friday', 
            'https://www.shoptime.com.br/especial/black-friday', 
            'https://www.submarino.com.br/especial/black-friday'
            ]

adv.crawl(url_list, 'crawler.jl', follow_links=False)
crawl_df = pd.read_json('crawler.jl', lines=True)
crawl_df.head()
 

columns_df = crawl_df[['url', 'title', 'meta_desc', 'canonical', 'h1', 'h2', 'h3', 'og:title', 'og:description', 'og:type', 'og:image', 'og:url', 'img_alt', 'jsonld_@type']]


# Export the data to CSV
crawl_df.to_csv('output.csv', index=False)
