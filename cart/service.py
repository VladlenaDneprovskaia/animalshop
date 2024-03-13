from shop.models import Product


class Cart:
    __key = 'cart'
    __model = Product

    def __init__(self, request):
        self.__request = request
        self.__dict = request.session.get(self.__key, {})

    def add(self, product_id):
        serialize_id = str(product_id)
        self.__dict[serialize_id] = 1 if serialize_id not in self.__dict else self.__dict[serialize_id] + 1
        self.__save()

    def add_pluralise(self, product_id, count):
        serialize_id = str(product_id)
        self.__dict[serialize_id] = count if serialize_id not in self.__dict else self.__dict[serialize_id] + count
        self.__save()

    def put(self, product_id):
        serialize_id = str(product_id)
        if serialize_id in self.__dict:
            self.__dict[serialize_id] -= 1

            if self.__dict[serialize_id] <= 0:
                self.remove(serialize_id)

            self.__save()

    def remove(self, product_id):
        serialize_id = str(product_id)
        if serialize_id in self.__dict:
            del self.__dict[serialize_id]
            self.__save()

    def clear(self):
        self.__request.session[self.__key] = {}

    def get_item(self, product_id):
        serialize_id = str(product_id)
        return self.__to_cart_item(serialize_id, self.get_product_count(serialize_id))

    def get_items(self):
        return [self.get_item(product_id) for product_id in self.__dict]

    def get_product_count(self, product_id):
        serialize_id = str(product_id)
        return self.__dict.get(serialize_id, 0)

    def get_total_count(self):
        return sum(map(lambda x: int(x), self.__dict.values()))

    def get_total_price(self):
        return sum(
            map(lambda item: self.__model.objects.get(id=item[0]).get_new_price() * int(item[1]),
                self.__dict.items()))

    def __save(self):
        self.__request.session[self.__key] = self.__dict

    def __to_cart_item(self, product_id, count):
        product = self.__model.objects.get(id=product_id)
        count = int(count)
        return {
            'product': product,
            'count': count,
            'total_old_price': product.get_old_price() * count,
            'total_new_price': product.get_new_price() * count,
            'has_discount': product.has_discount()
        }
