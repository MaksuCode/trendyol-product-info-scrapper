class Product:

    price_locator = 'div.product-price-container span.prc-dsc'
    name_locator = 'h1.pr-new-br span'
    name = 'default_name'
    price = 0

    def __init__(self, url):
        self.url = url


