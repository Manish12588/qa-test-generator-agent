# Test Cases — SkillPulse
Generated: 2026-05-13 23:49:10

---

## GET /api/skills
**Description:** Get all skills

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get all skills | Valid user input | Valid response is returned |  |
| TC002 | Missing required field | Empty request body | 400 Bad Request error |  |
| TC003 | Invalid data type | Non-JSON request body | 415 Unsupported Media Type error |  |
| TC004 | Non-existent resource | Invalid skill ID in path parameter | 404 Not Found error |  |
| TC005 | Boundary value | Skill ID just below the boundary value limit | Valid response is returned with limited data |  |
| TC006 | Negative scenario | No Authorization header provided | Unauthorized error |  |

---

## POST /api/skills
**Description:** Create a new skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Create a new skill | Valid inputs: name "Python", category "Programming", goal_hours 50 | POST /api/skills with request body { "name": "Python", "category": "Programming", "goal_hours": 50 } | Created skill object |
| TC002 | Missing required field or empty input | Required fields missing, empty inputs for name, category, goal_hours | POST /api/skills with request body {} or request body without any of the fields | HTTP status code indicating error (e.g., 400 Bad Request) |
| TC003 | Invalid data type | Goal_hours set to a non-numeric value like "abc" | POST /api/skills with request body { "name": "Python", "category": "Programming", "goal_hours": "abc" } | HTTP status code indicating error (e.g., 400 Bad Request) |
| TC004 | Non-existent resource | Invalid ID used in request | POST /api/skills/999 with valid request body { "name": "Python", "category": "Programming", "goal_hours": 50 } | HTTP status code indicating error (e.g., 404 Not Found) |
| TC005 | Boundary value | Goal_hours set to the minimum allowed value, 1 | POST /api/skills with request body { "name": "Python", "category": "Programming", "goal_hours": 1 } | Created skill object |
| TC006 | Negative scenario | Attempting to create a skill with invalid category (e.g., "InvalidCategory") | POST /api/skills with request body { "name": "Python", "category": "InvalidCategory", "goal_hours": 50 } | HTTP status code indicating error (e.g., 400 Bad Request) |

---

## GET /api/skills/:id
**Description:** Get a single skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get a valid skill by ID | Valid skill ID provided | Verify response contains expected fields and structure | Single skill object returned |
| TC002 | Missing required field or empty input | Empty string for ID, missing required parameter in URL/query | 400 Bad Request error with appropriate validation message | Invalid request details |
| TC003 | Invalid data type | Non-integer ID provided as part of the path or query | 400 Bad Request error | Invalid data type for ID |
| TC004 | Non-existent resource (invalid ID) | Nonexistent skill ID not found in database | 404 Not Found | Resource not found |
| TC005 | Boundary value | Edge case with very large ID value | Valid response returned for the largest possible valid integer | Large positive number valid skill object |
| TC006 | Negative scenario | Negative ID provided as part of the path or query | -1 returns a 400 Bad Request error | Invalid request details |

---

## DELETE /api/skills/:id
**Description:** Delete a skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Delete a valid skill by ID | Skill exists, ID is provided and integer | Verify the DELETE request successfully removes the skill from the database | Success response returned |
| TC002 | Missing required field: Empty input | ID not provided or invalid type | Attempt to delete with missing or incorrect ID; Expect error message indicating resource not found | Error response returned |
| TC003 | Invalid data type: Non-integer ID | ID is string or float | Attempt to delete a skill by non-integer ID; Expect error message indicating ID format issues | Error response returned |
| TC004 | Non-existent resource: Invalid ID | Non-existent or invalid ID provided (e.g., -1, 0, large number) | Request to delete a non-existing or non-existentible skill; Expect error message indicating resource not found | Error response returned |
| TC005 | Boundary value: Max and min ID values | Valid range of IDs, edge cases such as smallest and largest valid IDs | Verify the DELETE request works for boundary values without issues | Success response returned |
| TC006 | Negative scenario: Rate limiting reached | Simulate multiple concurrent DELETE requests within a short time frame | Expect rate limit error messages if API is correctly set up to handle concurrency limitations | Error response indicating too many requests |

---

## POST /api/skills/:id/log
**Description:** Log a learning session for a skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Log a valid learning session | User has a skill ID | POST /api/skills/:id/log with valid hours and notes fields | Created log entry |
| TC002 | Missing required field (hours) | Valid user and skill ID | POST /api/skills/:id/log without 'hours' field | Error response indicating missing required field |
| TC003 | Invalid data type for hours | Valid user, skill ID, invalid data type for hours | POST /api/skills/:id/log with non-numeric value for 'hours' | Error response indicating invalid data type |
| TC004 | Non-existent resource (invalid ID) | User tries to log session with a non-existent skill ID | POST /api/skill/99999/log | Bad request error |
| TC005 | Boundary value (zero hours) | Valid user, valid skill ID, zero 'hours' field | POST /api/skills/:id/log with 'hours': 0 | Created log entry for zero hours session |
| TC006 | Negative scenario (negative hours) | Valid user, valid skill ID, negative 'hours' field | POST /api/skills/:id/log with 'hours': -1 | Error response indicating invalid value |

---

## GET /api/dashboard
**Description:** Get dashboard stats - total skills, hours logged, sessions, top skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get dashboard stats | Valid user input | Verify response includes total skills, hours logged, sessions, top skill | Dashboard stats object |
| TC002 | Missing required field or empty input | Non-existent user ID | Request fails with 400 Bad Request | Error message about missing fields |
| TC003 | Invalid data type | Invalid format for hours logged | Response indicates invalid input | Error message about invalid data types |
| TC004 | Non-existent resource | Invalid dashboard ID | Resource not found response | Status code 404 Not Found |
| TC005 | Boundary value | Maximum number of skills, maximum hours logged | No error, but check for boundary conditions validity | Dashboard stats object with max values |
| TC006 | Negative scenario | Zero total skills, zero hours logged, no sessions | Response indicates invalid data or empty dashboard | Error message about insufficient data |

