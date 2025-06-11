from django.conf import settings
from django.http import JsonResponse

def require_api_key(view_func):
    def wrapper(request, *args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        valid_keys = getattr(settings, "VALID_API_KEYS", [])
        if not api_key or api_key not in valid_keys:
            return JsonResponse({"error": "INVALID_API_KEY", "message": "Missing or invalid API key"}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapper
