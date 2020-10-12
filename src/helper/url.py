import urllib.parse


def build_sub_url(sub_url, query=None):
    if query is None:
        query = {}
    base = '/' + str(sub_url).strip('/')
    params = urllib.parse.urlencode(query)
    return (base + "?%s") % params if query else base
