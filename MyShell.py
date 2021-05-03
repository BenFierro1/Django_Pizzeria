import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()

#alt way
p = Pizza.objects.get(id=1)
print(p)
topping = p.topping_set.all()
print(topping)
