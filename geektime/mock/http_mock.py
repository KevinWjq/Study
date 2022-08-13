from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "value"
    flow.request.query["q"] = "appium"


def response(flow: http.HTTPFlow):
    if "search" in flow.request.path and flow.request.query.get("q") == "appium":
        flow.response.text = flow.response.text.replace("appium", "MOCK")
