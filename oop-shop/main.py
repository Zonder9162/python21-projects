from shop.models import Product
from shop.serializers import ProductSerializer

cat = Category()
obj1 = Product("iphone", 234, "...", 3)
obj2 = Product("lenovo", 543, "...", 3)
obj3 = Product("sumsung", 214, "...", 3)

res = ProductSerializer().serialize_queryset([obj1, obj2, obj3])
print(res)