class APIError(Exception):
    """Base class for API exceptions"""
    status_code = 500
    
    def __init__(self, message, status_code=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        
class ExternalAPIError(APIError):
    """Error when calling external APIs"""
    status_code = 503