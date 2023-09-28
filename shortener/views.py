from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from shortener.models import Shorturl
from shortener.forms import ShorturlForm


def home_view(request):
    title = "Welcome!"
    return render(request, "shortener/home.html", {"title": title})


def shorturl_detail(request, identifier):
    """
    Retrieves the redirect URL associated with the given identifier from the Shorturl model.

    Parameters:
    - request: The HTTP request object.
    - identifier: The identifier used to lookup the redirect URL.

    Returns:
    - redirect_url: The redirect URL associated with the given identifier.
    """
    redirect_url = get_object_or_404(Shorturl, identifier=identifier).url
    return redirect(redirect_url, permanent=False)


@login_required
def shorturl_list(request):
    shorturls = Shorturl.objects.filter(user=request.user)
    form = ShorturlForm()

    if request.method == "POST":
        form = ShorturlForm(request.POST)
        if form.is_valid():
            shorturl = form.save(commit=False)
            shorturl.user = request.user
            shorturl.save()
            return redirect("shorturl_list")

    return render(
        request, "shortener/list.html", {"form": form, "shorturls": shorturls}
    )


@login_required
def shorturl_delete(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier")
        Shorturl.objects.get(identifier=identifier, user=request.user).delete()
        return redirect("shorturl_list")
