import re
import structlog

from django.utils import timezone
from stackdriverlog.conf import settings


class RequestLoggingMiddleware(object):
    """
    Adds request.logger to each request to use structlog.
    Makes log on each response
    """
    IGNORE_PATHS = list(map(re.compile, settings.REQUEST_MIDDLEWARE_IGNORE_PATHS))

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.pre_response(request)
        response = self.get_response(request)
        self.post_response(request, response)
        return response

    def process_exception(self, request, exception):
        request.logger.exception(exception)

    @staticmethod
    def pre_response(request):
        request.start = timezone.now()
        message = f"{request.method} {request.path}"
        request.logger = structlog.getLogger(__name__).bind(message=message,
            path=request.path, method=request.method, query_params=dict(request.GET))

        if hasattr(request, 'tracking_id'):
            request.logger = request.logger.bind(tracking_id=request.tracking_id)

    def post_response(self, request, response):
        request.logger = request.logger.bind(status=response.status_code,
                                             duration_ms=(timezone.now() - request.start).microseconds / 1000)

        # Check if request path matches any ignore patterns. If not, log the request.
        if not any([expr.match(request.path) for expr in self.IGNORE_PATHS]) and not request.method in ['OPTIONS']:
            request.logger.info(event='request')
        return response
