from django.shortcuts import render, redirect
from .models import Pizza, Topping, Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.
def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)

def new_review(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.pizza = pizza
            new_review.save()
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)
    context = {'form': form, 'pizza':pizza}
    return render(request, 'pizzas/new_review.html', context)