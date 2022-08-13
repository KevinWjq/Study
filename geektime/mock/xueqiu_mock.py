from mitmproxy import http


def response(flow: http.HTTPFlow):
    flow.response.text = flow.response.text.replace("中通客车", "七七卡车")
    flow.response.text = flow.response.text.replace(":-", ":")
