# Test Cases — SkillPulse
Generated: 2026-05-14 14:22:23

---

## GET /api/skills
**Description:** Get all skills

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get all skills | Valid input: No precondition needed | Call GET /api/skills with no query parameters | Returns a list of skill objects |
| TC002 | Missing required field or empty input | Valid input except for one field (e.g., name, level) set to null or empty string | Call GET /api/skills with only the valid fields and an invalid field set to null or empty string | Returns error indicating missing or invalid fields |
| TC003 | Invalid data type | Use a non-string value for a field that expects a string (e.g., using 123 instead of "123" for name) | Call GET /api/skills with a field containing a non-string value | Returns error indicating an invalid format for the input |
| TC004 | Non-existent resource | Use an ID not present in the database | Call GET /api/skills with an invalid or non-existent ID | Returns 404 Not Found error |
| TC005 | Boundary value | Use a very large number (e.g., max integer +1) as an input parameter to simulate boundary condition testing | Call GET /api/skills with the large number as a valid query parameter | Returns list of skills up to the maximum possible based on the endpoint's logic |
| TC006 | Negative scenario | Request more resources than available in the database or exceed rate limits | Simulate making multiple calls to the endpoint quickly (e.g., by adding 10 GET /api/skills requests consecutively) | Returns error indicating request limit exceeded or similar limitation errors |

---

## POST /api/skills
**Description:** Create a new skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Create a new skill | API endpoint is up and running | Send POST request to /api/skills with valid fields, name="Learning Python", category="Programming", goal_hours=50 | Created skill object with status 201 |
| TC002 | Missing required field (name) | API endpoint is up and running | Send POST request to /api/skills without the "name" field, category="Learning Python", goal_hours=10 | Error response indicating missing mandatory field |
| TC003 | Invalid data type for name | API endpoint is up and running | Send POST request to /api/skills with a non-string value for the "name" field, category="Learning Python", goal_hours=10 | Error response indicating invalid input format |
| TC004 | Non-existent resource (invalid ID) | API endpoint is up and running | Send POST request to /api/skills with a non-existent ID in the headers, name="New Skill", category="Data Science", goal_hours=30 | Error response indicating invalid resource |
| TC005 | Boundary value (goal_hours) | API endpoint is up and running | Send POST request to /api/skills with goal_hours set to the upper boundary, name="Advanced Math", category="Academics", goal_hours=1000 | Error response indicating invalid input |
| TC006 | Negative scenario (duplicate skill) | API endpoint is up and running | Send POST request to /api/skills with valid data fields, name="Python Programming", category="Programming", goal_hours=20 | Error response indicating a duplicate skill already exists |

---

## GET /api/skills/:id
**Description:** Get a single skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get a valid skill by ID | The endpoint exists and the SkillPulse application is running | Verify that fetching a skill with an existing ID returns the correct skill object | Single skill object returned |
| TC002 | Missing required field - Skill name | Valid API URL, missing required "name" parameter in request body | Attempt to fetch a skill without specifying the "name", expect error response indicating invalid or incomplete data | Error response indicating invalid or incomplete data |
| TC003 | Invalid data type for skill name | Valid API URL, "name" field as an integer instead of string in request body | Attempt to fetch a skill with "name" parameter as integer, expect error response indicating incorrect data type for the "name" field | Error response indicating incorrect data type for the "name" field |
| TC004 | Non-existent resource - Invalid ID | Valid API URL, invalid ID (e.g., "-1") in request parameters | Attempt to fetch a skill with an invalid or non-existent ID, expect error response indicating invalid input | Error response indicating invalid input |
| TC005 | Boundary value for skill name | Valid API URL, "name" parameter set to the maximum length allowed by the application | Test fetching a skill where the "name" is at its maximum length, expect successful response with no issues | Successful response with no issues |
| TC006 | Negative scenario - Empty input for all fields | Valid API URL, empty request body sent | Attempt to fetch a skill without specifying any fields, expect error response indicating missing required data or incomplete data | Error response indicating missing required data or incomplete data |

---

## DELETE /api/skills/:id
**Description:** Delete a skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Delete a valid skill by ID | Skill exists, ID is provided and correct | Verify response indicates successful deletion | Success |
| TC002 | Missing required field - invalid input | ID missing or empty | Validate API returns error message for incorrect input format | Error: Required field ID is missing or not provided |
| TC003 | Invalid data type - ID as string | Non-numeric value for ID | Validate API responds with an error indicating wrong data type for ID | Error: ID must be a valid numeric integer |
| TC004 | Non-existent resource - invalid ID | Nonexistent skill ID provided | Verify response indicates resource not found or deletion failed | Error: Resource not found, skill does not exist |
| TC005 | Boundary value - maximum ID range | Highest possible skill ID + 1 | Validate API handles the edge case of out-of-range IDs and returns appropriate error | Error: Requested resource not found |
| TC006 | Negative scenario - delete all skills (not implemented) | No preconditions as scenario is theoretical | Scenario description only, no steps or results | Not Implemented |

---

## POST /api/skills/:id/log
**Description:** Log a learning session for a skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Log a learning session successfully | Valid ID and fields are provided | POST /api/skills/123/log with hours=4.5 & notes="Overview of Python" | Created log entry for skill with id 123 |
| TC002 | Missing required field - hours | Valid ID but missing or empty "hours" field | POST /api/skills/123/log with hours="" | HTTP status code: 400 Bad Request |
| TC003 | Invalid data type - invalid hours input | Valid ID and non-numeric value for "hours" field | POST /api/skills/123/log with hours="abc" | HTTP status code: 400 Bad Request |
| TC004 | Non-existent resource (invalid ID) | Valid fields but non-existent ID | POST /api/skills/-999/log with hours=5.5 & notes="Introduction to Java" | HTTP status code: 404 Not Found |
| TC005 | Boundary value - minimum hour input | Valid field and at minimum boundary | POST /api/skills/123/log with hours=0 & notes="" | Created log entry for skill with id 123 with zero duration and no notes |
| TC006 | Negative scenario - negative hour input | Valid ID but non-numeric value for "hours" field as negative number | POST /api/skills/123/log with hours="-5.5" & notes="" | HTTP status code: 400 Bad Request |

---

## GET /api/dashboard
**Description:** Get dashboard stats - total skills, hours logged, sessions, top skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get dashboard stats | User is logged in | Call /api/dashboard with valid JWT token and no input parameters | Dashboard stats object returned |
| TC002 | Missing required field or empty input | User is logged in | Call /api/dashboard without providing any fields | Error response indicating missing required fields |
| TC003 | Invalid data type | User is logged in | Attempt to call /api/dashboard with non-JSON formatted body or incorrect types for properties | Bad Request error indicating invalid content type or field types |
| TC004 | Non-existent resource | User is logged in | Call /api/dashboard with a non-existent ID parameter | Error response indicating resource not found |
| TC005 | Boundary value | User is logged in | Call /api/dashboard with extreme values for hours logged, session count | Dashboard stats object returned with boundary values as expected |
| TC006 | Negative scenario | User is not logged in | Attempt to call /api/dashboard without providing any authentication | Unauthorized error |

