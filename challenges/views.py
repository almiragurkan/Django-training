from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Take time for yourself!",
    "february": "Walk every day!",
    "march": "Learn Django every day!",
    "april": "Take time for yourself!",
    "may": "Walk every day!",
    "june": "Learn Django every day!",
    "july": "Take time for yourself!",
    "august": "Walk every day!",
    "september": "Learn Django every day!",
    "october": "Take time for yourself!",
    "november": "Walk every day!",
    "december": None
}


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #    month_path = reverse("month-challenge", args=[month])
    #    list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    #response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, 'challenges/index.html', {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]  # because list index start 0
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string(challenges/challenge.html)
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month_name": month
        })

    except:
        raise Http404()
