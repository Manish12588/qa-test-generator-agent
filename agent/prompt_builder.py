def build_prompt(app_name: str, app_description: str, route: dict) -> str:
    method = route.get("method", "")
    path = route.get("path", "")
    description = route.get("description", "")
    request_body = route.get("request_body", None)
    response = route.get("response", "")

    request_body_section = ""
    if request_body:
        fields = "\n".join([f"  - {k}: {v}" for k, v in request_body.items()])
        request_body_section = f"""
Request Body Fields:
{fields}
"""

    prompt = f"""You are a senior QA engineer. Generate exactly 6 test cases for this API endpoint.

Application: {app_name}
Description: {app_description}

Endpoint:
Method: {method}
Path: {path}
Description: {description}
{request_body_section}
Expected Response: {response}

STRICT OUTPUT FORMAT — each line must follow this exact pattern:
TC001 | <title> | <precondition> | <test steps> | <expected result>
TC002 | <title> | <precondition> | <test steps> | <expected result>

Cover these scenarios:
- TC001: Happy path (valid inputs)
- TC002: Missing required field or empty input
- TC003: Invalid data type
- TC004: Non-existent resource (invalid ID)
- TC005: Boundary value
- TC006: Negative scenario

RULES:
- Output ONLY the 6 test case lines
- NO introductions, NO explanations, NO markdown, NO numbered lists
- Each test case on ONE line only
- Use pipe | as separator
- Start with TC001
"""
    return prompt
