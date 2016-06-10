cat ./apidb/views-1.py | sed -e '/^def.*$/a\    postRequest = None\n    if request.method == "POST":\n        postRequest = json.loads(request.raw_post_data)'  \
    | sed -e 's/request\.POST/postRequest/g' > ./apidb/views.py
