# Create your views here.
import json
from django.shortcuts import render
from django.template import RequestContext

from apps.oncommands.scripts.word_guess import word_guess

def word_guess_view(request, letters=None, length=None):
    """Process the porsible word of the length from those letters"""

    import re
    if re.findall("[^a-zA-Z]",letters):
        error_msg = "Please only put letters"
    letters = letters.lower()
    letters = letters.replace(" ", '')

    possible_words = word_guess(letters, length)

    return render(request, "commands/word_guess.html", {"words":possible_words,})

def dirtybot_view(request):
    """test command for scraping"""

    new_data = []
    with open('dirtybot/dirtybot/items2.json') as data_file:
        data = json.load(data_file)
        for item in data:
            new_item = {}
            new_item['companylink'] = item['companylink'][0] if item["companylink"] else ""
            contact_info = item['contact_info'][0]
            new_item['contact_info'] = ' '.join(contact_info.split())
            new_data.append(new_item)

    return render(request, "commands/scraper_test.html", {"data":new_data,})