import requests

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

def home(request):
    return HttpResponse("Use /parse")

def parse(request):
    try:
        # See if post field link is supplied to pass on a web line
        link = request.POST['link']
        # Download the file and extract raw content
        try:
            r = requests.get(link)
        except requests.exceptions.MissingSchema:
            return HttpResponseBadRequest("url scheme required")
        data = r.content
    except KeyError:
        data = request.body
        if len(data) == 0:
            return HttpResponseBadRequest("/parse requires link or file upload")

    # Send parsing request to tika
    headers = {}

    """
    Get mode parameter from GET variable, default "meta"
    Modes available: meta,content(tika),raw_content
    """
    try:
        mode = request.GET['mode']
        if mode not in ["meta", "content", "raw_content"]:
            return HttpResponseBadRequest("mode, '%s' invalid" % mode)
        elif mode == "content":
            mode = "tika"
        elif mode == "raw_content":
            return HttpResponse(data)
        else:
            headers.update({'Accept': 'application/json'})
    except KeyError:
        mode = "meta"

    parsed_r = requests.put("http://localhost:9998/%s" % mode, data=data, headers=headers)
    return HttpResponse(parsed_r.content)
