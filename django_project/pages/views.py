from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list":["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THank you FOR visitING.",
    }
    return render(request, "home.html", context)

