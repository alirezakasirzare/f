from carts.models import Orders
from products.models import Products,ProductsScores

def BestSelling_products():
    products = Orders.objects.filter(payment_status=True).all()
    List1 = [p.product_id for p in products]
    data = {}

    for p in List1:
        data[List1.count(p)] = p

    result = []

    for _ in range(len(data)):
        if len(result) == 12:
            break
        key = max(data.keys())
        value = data.get(key)
        result.append(value)
        data.pop(key)


    return result



def cheapest_products():
    products = Products.objects.filter(status=True,inventory__gt=0).all()
    data = {}

    for p in products:
        if p.discounted_price:
            data[p.discounted_price] = p.id
        else:
            data[p.price] = p.id

    result = []
    for _ in range(len(data)):
        if len(result) == 6:
            break
        key = min(data.keys())
        value = data.get(key)
        result.append(value)
        data.pop(key)


    return result

def latest_discounts_products():
    products = Products.objects.filter(status=True,inventory__gt=0).all()
    result = []
    for p in products:
        if p.discounted_price:
            result.append(p.id)

    return result


def most_expensive_prodcuts():
    products = Products.objects.filter(status=True,inventory__gt=0).all()
    data = {}

    for p in products:
        if p.discounted_price != 0:
            data[p.discounted_price] = p.id
        else:
            data[p.price] = p.id

    result = []
    for _ in range(len(data)):
        if len(result) == 6:
            break
        key = max(data.keys())
        value = data.get(key)
        result.append(value)
        data.pop(key)

    return result



def specialProducts():
    scores = ProductsScores.objects.all()
    List1 = [x.score for x in scores]
    List2 = []

    for _ in range(len(List1)):
        if len(List2) == 12:
            break
        result = max(List1)
        List2.append(result)
        List1.remove(result)

    result = [ProductsScores.objects.filter(score=L).first().id for L in List2]
    return result
