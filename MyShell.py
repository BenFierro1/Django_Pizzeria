import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping, Review

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()
reviews = Review.objects.all()

#alt way
p = Pizza.objects.get(id=1)
print(p)
topping = p.topping_set.all()
print(topping)
review = p.review_set.all()
print(review)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)