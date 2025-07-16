from mitmproxy import http

class CustomProxy:
    def request(self, flow: http.HTTPFlow):
        # Log requests
        print(f"[REQUEST] {flow.request.method} {flow.request.pretty_url}")
        
        # Example: Add custom header
        flow.request.headers["X-Custom-Header"] = "MyProxy"

    def response(self, flow: http.HTTPFlow):
        # Log responses
        print(f"[RESPONSE] {flow.response.status_code} {flow.request.pretty_url}")
        
        # Example: Modify HTML content (only for text/html)
        if "text/html" in flow.response.headers.get("content-type", ""):
            flow.response.text = flow.response.text.replace("Example", "Intercepted Example")

addons = [CustomProxy()]
