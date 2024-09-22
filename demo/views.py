import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from django.conf import settings


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'name': 'Царский омлет специально для вас',
        'recipe': {key: val*servings for key, val in DATA['omlet'].items()}
    }
    return render(request, 'index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'name': 'Самая волшебная паста в мире',
        'person': f'Количество персон: {servings}',
        'recipe': {key: round(val*servings, 3) for key, val in DATA['pasta'].items()}
    }
    return render(request, 'index.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'name': 'Бутерброд обыкновенный, но вкусный и приготовленный с душой',
        'recipe': {key: val*servings for key, val in DATA['buter'].items()}
    }
    return render(request, 'index.html', context)
