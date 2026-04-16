from django.http import HttpRequest, HttpResponse


class NoCacheHTMLMiddleware:
    """Prevent Safari 'Add to Dock' web apps from showing stale cached pages."""

    def __init__(self, get_response: object) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        content_type = response.get("Content-Type", "")
        if "text/html" in content_type:
            response["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response
