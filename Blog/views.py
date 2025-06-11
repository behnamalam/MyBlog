from django.shortcuts import render
from datetime import date
from django.http import HttpResponse

all_posts = [
    {
        "slug": "learning-django",
        "title": "django-course",
        "author": "Behnam alamshahi",
        "image": "django.png",
        "date": date(2023, 4, 5),
        "short_description": "this is django from zero to 100",
        "content": "    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nam alias illum aliquam quos ipsum, quo facilis sapiente numquam. Assumenda dignissimos doloremque exercitationem odio vero temporibus ducimus harum perspiciatis, maiores reprehenderit, praesentium illo dicta. Reiciendis error doloribus ab magni cumque, sapiente tempora cum autem, repellat sed, illo culpa animi fuga. Rerum.",
    },
    {
        "slug": "learning-js",
        "title": "js-course",
        "author": "Behnam alamshahi",
        "image": "js.png",
        "date": date(2023, 2, 5),
        "short_description": "this is django from zero to 100",
        "content": "    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nam alias illum aliquam quos ipsum, quo facilis sapiente numquam. Assumenda dignissimos doloremque exercitationem odio vero temporibus ducimus harum perspiciatis, maiores reprehenderit, praesentium illo dicta. Reiciendis error doloribus ab magni cumque, sapiente tempora cum autem, repellat sed, illo culpa animi fuga. Rerum.",
    },
    {
        "slug": "Machine Learning",
        "title": "Ml-course",
        "author": "Behnam alamshahi",
        "image": "ml.png",
        "date": date(2023, 9, 5),
        "short_description": "this is django from zero to 100",
        "content": "    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nam alias illum aliquam quos ipsum, quo facilis sapiente numquam. Assumenda dignissimos doloremque exercitationem odio vero temporibus ducimus harum perspiciatis, maiores reprehenderit, praesentium illo dicta. Reiciendis error doloribus ab magni cumque, sapiente tempora cum autem, repellat sed, illo culpa animi fuga. Rerum.",
    },
    {
        "slug": "learning-python",
        "title": "python-course",
        "author": "Behnam alamshahi",
        "image": "python.png",
        "date": date(2023, 11, 5),
        "short_description": "this is django from zero to 100",
        "content": "    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nam alias illum aliquam quos ipsum, quo facilis sapiente numquam. Assumenda dignissimos doloremque exercitationem odio vero temporibus ducimus harum perspiciatis, maiores reprehenderit, praesentium illo dicta. Reiciendis error doloribus ab magni cumque, sapiente tempora cum autem, repellat sed, illo culpa animi fuga. Rerum.",
    },
]


# Create your views here.
def get_date(post):
    return post["date"]


def index(request):
    # sorted_post = sorted(all_posts, key=get_date)
    return render(request,"Blog/index.html")
    # return HttpResponse("welcome")


def posts(request):
    return HttpResponse("All posts")


def single_post(request):
    return HttpResponse('every post')
