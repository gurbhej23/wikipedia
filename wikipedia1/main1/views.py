from django.http import JsonResponse
from django.shortcuts import render
import wikipediaapi

# Initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(
    user_agent="wikipedia-django-app/1.0",
    language="en",
    extract_format=wikipediaapi.ExtractFormat.WIKI,
)


def home(request):

    if request.method == "POST":
        search = request.POST.get("search", "").strip()

        if not search:
            message = "Please enter something to search."
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": message})
            return render(request, "main/index.html", {"error": message})

        page = wiki.page(search)

        if page.exists():
            result = page.summary[:800]  # limit text length

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "result": result})

            return render(request, "main/index.html", {"result": result})

        else:
            message = "No result found."

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": message})

            return render(request, "main/index.html", {"error": message})

    return render(request, "main/index.html")
