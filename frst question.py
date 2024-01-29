import re

def parse_requests(valid_auth_tokens, requests):
    result = []

    for request in requests:
        # Split the request into request type, URL, and parameters
        request_type, url, *params = request.split(',')

        # Extract authentication token and CSRF token (if present)
        auth_token = None
        csrf_token = None
        for param in params:
            key, value = param.strip().split('=')
            if key == 'token':
                auth_token = value
            elif key == 'CSRF_token':
                csrf_token = value

        # Check if authentication token is valid
        if auth_token not in valid_auth_tokens:
            result.append("INVALID")
        else:
            # Check if it's a POST request and has a valid CSRF token
            if request_type == 'POST' and (csrf_token is None or not re.match("^[a-zA-Z0-9]{8,}$", csrf_token)):
                result.append("INVALID")
            else:
                # Parse URL parameters as a comma-separated string
                parsed_params = []
                for param in params:
                    key, value = param.strip().split('=')
                    parsed_params.extend([key, value])

                # Construct the result string
                result.append("VALID," + ','.join(parsed_params))

    return result

# Example usage:
valid_auth_tokens = ["safh34ywb0p5", "another_valid_token"]
requests = ["GET,https://www.youtube.com/", "GET,http://example.com?token=safh34ywb0p5&name=sam",
            "POST,http://example.com?token=safh34ywb0p5", "POST,http://example.com?token=safh34ywb0p5&CSRF_token=ak2sh32dy&name=chris"]

responses = parse_requests(valid_auth_tokens, requests)
print(responses)
