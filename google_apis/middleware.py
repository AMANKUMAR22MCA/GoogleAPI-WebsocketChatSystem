# from django.utils.deprecation import MiddlewareMixin

# class CSPMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         response["Content-Security-Policy"] = (
#             "default-src 'self' https://apis.google.com https://accounts.google.com; "
#             "script-src 'self' 'unsafe-inline' https://apis.google.com https://accounts.google.com; "
#             "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
#             "frame-src 'self' https://drive.google.com https://accounts.google.com https://content.googleapis.com;"
#         )
#         return response
