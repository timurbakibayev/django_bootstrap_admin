from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def html(request, filename):
    context = {"filename": filename,
               "collapse": ""}
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)
