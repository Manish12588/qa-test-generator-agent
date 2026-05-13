# Test Cases — SkillPulse
Generated: 2026-05-13 23:43:46

---

## GET /api/skills
**Description:** Get all skills

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get all skills | Valid input: user has added at least one skill | Verify response contains list of skill objects | List of skill objects returned |
| TC002 | Missing required field or empty input | Empty request body or missing required fields in valid JSON | Verify response indicates missing parameters or invalid data format | Bad Request (400) with error details |
| TC003 | Invalid data type | Use non-JSON format for request body, e.g., HTML form submission | Verify server responds with error indicating malformed content or wrong media type | Internal Server Error (500) |
| TC004 | Non-existent resource | Request ID does not exist in the system | Verify response indicates resource not found | Not Found (404) with message |
| TC005 | Boundary value | Use minimum and maximum valid values for search parameters, e.g., first skill added and last skill added IDs | Verify response contains list of skills within boundary range | List of skills between specified boundaries |
| TC006 | Negative scenario | Request with very high or extremely low pagination offset or limit | Verify response indicates inappropriate request (e.g., too many results) | Too Many Requests (429) |

---

## POST /api/skills
**Description:** Create a new skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|

---

## GET /api/skills/:id
**Description:** Get a single skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get a valid skill by ID | Skill exists, ID provided | Verify response contains expected fields for the skill object | Valid skill data returned |
| TC002 | Missing required field or empty input | Empty ID or missing body content | Receive 400 Bad Request with error message indicating missing or invalid parameters | Error handling as expected |
| TC003 | Invalid data type | Non-integer ID provided, correct JSON structure in body | Return 400 Bad Request with error message about incorrect ID format | Validation rules enforced |
| TC004 | Non-existent resource (invalid ID) | Nonexistent non-negative integer ID provided | Receive 404 Not Found | Resource not found response |
| TC005 | Boundary value | Minimum and maximum valid IDs tested | Correctly respond for both minimum and maximum IDs as per API specifications | Valid responses at boundaries |
| TC006 | Negative scenario | Specified negative number as skill ID, correct JSON structure in body | Return 400 Bad Request with error message about incorrect ID format | Invalid input validation |

---

## DELETE /api/skills/:id
**Description:** Delete a skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Delete a valid skill | Skill exists and has correct ID | Send DELETE request to /api/skills/valid_id | Success response with message "Skill deleted successfully" |
| TC002 | Missing required field (invalid input) | Invalid skill ID | Send DELETE request to /api/skills/ | 456789 |
| TC003 | Invalid data type (empty input) | Empty string as skill ID | Send DELETE request to /api/skills/"" | Error response indicating invalid or missing resource |
| TC004 | Non-existent resource (invalid ID) | Invalid non-existent skill ID | Send DELETE request to /api/skills/nonexistent_id | Error response indicating the requested resource could not be found |

---

## POST /api/skills/:id/log
**Description:** Log a learning session for a skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Log a learning session successfully with valid inputs | Valid skill ID and hours field provided | POST /api/skills/valid_id/log with request body: { "hours": 2.5, "notes": "Completed Python Basics" } | Created log entry is returned |
| TC002 | Missing required hours field or empty input | Invalid or missing hour value in the request body | POST /api/skills/valid_id/log with request body: { "notes": "Missing Hours" }, POST /api/skills/valid_id/log with request body: {} | Status code 400 Bad Request |
| TC003 | Invalid data type for hours field or missing required notes field | Non-numeric value provided for hours, or only providing hour without notes | POST /api/skills/valid_id/log with request body: { "hours": "two" }, POST /api/skills/valid_id/log with request body: {} | Status code 400 Bad Request |
| TC004 | Non-existent resource (invalid ID) | Invalid skill ID provided in the path | POST /api/skill_not_exists/log with request body: { "hours": 2.5, "notes": "Invalid ID" } | Status code 404 Not Found |
| TC005 | Boundary value for hours field | Maximum and minimum values of hours tested (e.g., max = 23.99, min = 0) | POST /api/skills/valid_id/log with request body: { "hours": 23.99 }, POST /api/skills/valid_id/log with request body: { "hours": 0 } | Created log entry is returned |
| TC006 | Negative scenario - concurrency and retries | Attempt to add log for an existing session, expecting a conflict or update error | POST /api/skills/valid_id/log with request body: { "hours": 1.5 }, wait for response, then POST again with same hour value | Status code 409 Conflict or 201 Created (indicating the second attempt overwrote the first due to concurrency) |

---

## GET /api/dashboard
**Description:** Get dashboard stats - total skills, hours logged, sessions, top skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get dashboard stats | Valid user input provided | Make a GET request to /api/dashboard with valid user token and no missing fields | Dashboard stats object is returned |
| TC002 | Missing required field or empty input | One of the required fields for dashboard stats (total skills, hours logged, sessions) is missing or sent as an empty string | GET request fails due to invalid payload | Error response indicating missing or invalid data |
| TC003 | Invalid data type | Dashboard stats object contains non-integer values for numeric statistics like hours_logged and total_skills | GET request returns error indicating non-integer value in input | Error response with validation message |
| TC004 | Non-existent resource (invalid ID) | Request includes an invalid or non-existent user ID that does not exist on the system | Valid user token but invalid/missing ID in query parameters | Resource not found error is returned |
| TC005 | Boundary value | Dashboard stats object contains boundary values for numeric statistics like total_skills and hours_logged | GET request with extreme boundaries (e.g., max integer) for skills or sessions | Error response indicating out-of-bound input |
| TC006 | Negative scenario | Simulate a situation where the server is under heavy load and cannot process requests within expected time limits | Delayed API response due to server issues | Timeout error is returned |

