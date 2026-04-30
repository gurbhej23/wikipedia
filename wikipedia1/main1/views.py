from django.http import JsonResponse
from django.shortcuts import render
import wikipedia


def home(request):

    if request.method == "POST":
        search = request.POST.get("search", "").strip()

        if not search:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse(
                    {"success": False, "error": "Please enter something to search."}
                )
            return render(
                request,
                "main/index.html",
                {"error": "Please enter something to search."},
            )

        try:
            result = wikipedia.summary(search, sentences=10)
        except Exception:
            message = "Could not find a matching Wikipedia summary."
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": message})
            return render(request, "main/index.html", {"error": message})

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"success": True, "result": result})

        return render(request, "main/index.html", {"result": result})

    return render(request, "main/index.html")
