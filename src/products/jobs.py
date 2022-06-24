from products.models import ProductPriceChange, Product


def add_historic_data():
    products = Product.objects.only('id', 'price')
    for product in products:
        try:
            ProductPriceChange.objects.create(product=product.id, price=product.price)
        except Exception as e:
            print(e)
