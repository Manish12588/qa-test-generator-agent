# Test Cases — SkillPulse
Generated: 2026-05-13 23:37:38

---

## GET /api/skills
**Description:** Get all skills

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get all skills | Ensure API returns an empty list when there are no skills added | Perform GET request to /api/skills; Expect status code 200 and JSON body: [] |  |
| TC002 | Get valid skills | Verify fetching a non-empty list of skills with proper IDs, names, levels | Add three testable skills with unique IDs, names, levels; Perform GET request to /api/skills; Expect status code 200 and JSON body containing at least three skill objects with matching IDs |  |
| TC003 | Get empty list with boundary value | Test the API's behavior when given an invalid or out-of-bound ID (e.g., 1000, -1) | Perform GET request to /api/skills?skillId=1000; Expect status code and response as expected for non-existent resources |  |
| TC004 | Get skills with edge value | Validate the API's handling of special characters or invalid data types in a skill (e.g., null, undefined, large numbers) | Add one testable skill with an ID and replace other fields with edge values; Perform GET request to /api/skills; Expect status code and response as expected for non-existent resources |  |
| TC005 | Get skills with missing field | Ensure the API returns a valid list of skills when a required field is omitted (e.g., level) | Add one testable skill without specifying the level field; Perform GET request to /api/skills; Expect status code 200 and JSON body containing at least one skill object |  |
| TC006 | Invalid ID authorization scenario | Test API behavior with non-existent skill IDs in the path, expecting a proper error response | Perform GET request to /api/skills?skillId=1000; Expect status code and error message indicating resource not found |  |
| TC007 | Valid ID authorization scenario | Validate fetching of specific skills by their valid IDs | Add two testable skills with unique IDs (e.g., 1, 2); Perform GET request to /api/skills?skillId=1&skillId=2; Expect status code 200 and JSON body containing at least two skill objects |  |
| TC008 | Invalid ID authorization scenario | Validate API behavior when non-existent skill IDs are provided in the path | Add a testable skill with an ID (e.g., 5); Perform GET request to /api/skills?skillId=10; Expect status code and error message indicating resource not found |  |
| TC009 | Non-existent ID authorization scenario | Validate API behavior when non-existent skill IDs are provided in the path | Add a testable skill with an ID (e.g., 3); Perform GET request to /api/skills?skillId=10; Expect status code and error message indicating resource not found |  |
| TC010 | Invalid data type for fields | Ensure API handles incorrect data types gracefully, e.g., non-integer levels or invalid characters in skill names | Add one testable skill with an ID and modify other fields to invalid data types (e.g., a string instead of an integer for level) ; Perform GET request to /api/skills; Expect status code and error message indicating validation failure |  |

---

## POST /api/skills
**Description:** Create a new skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Create valid skill | None | 1. Send POST request to /api/skills with body: {"name": "Skill Name", "category": "Category", "goal_hours": 25} <br> 2. Check response status is 201 and check if the returned skill object contains all fields including name, category, goal_hours | TC002 |

---

## GET /api/skills/:id
**Description:** Get a single skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Get valid skill by ID | Valid skill ID provided in the URL | Verify that fetching a skill with an existing ID returns the correct skill object | HTTP Status: 200, JSON Response contains all expected fields and data |
| TC002 | Get empty list for non-existing skill ID | Non-existent skill ID provided in the URL | Verify that attempting to fetch a non-existing skill results in a status code of 404 with an appropriate error message | HTTP Status: 404, JSON Response contains "message": "Skill not found" |
| TC003 | Get empty list for invalid ID type | Invalid ID format (e.g., string instead of number) provided in the URL | Verify that attempting to fetch a skill with an invalid ID results in a status code of 400 and returns an error message indicating the issue | HTTP Status: 400, JSON Response contains "message": "Invalid ID" |
| TC004 | Get empty list for missing ID parameter | Skill ID is not provided in the URL (e.g., /api/skills/ instead of /api/skills/:id) | Verify that attempting to fetch a skill without an ID results in a status code of 400 and returns an error message indicating the issue | HTTP Status: 400, JSON Response contains "message": "Skill ID is required" |
| TC005 | Get empty list for missing ID value | Invalid or non-existent string provided as ID parameter (e.g., 'abc' instead of 123) | Verify that attempting to fetch a skill with an invalid ID results in a status code of 400 and returns an error message indicating the issue | HTTP Status: 400, JSON Response contains "message": "Invalid ID value" |
| TC006 | Get authorized user's skills | Valid authorization token provided | Verify that fetching skills for a logged-in user with valid credentials results in a status code of 200 and returns all their skill objects | HTTP Status: 200, JSON Response contains all skills owned by the authenticated user |
| TC007 | Get unauthorized access to other users' skills | Invalid authorization token provided | Verify that attempting to fetch skills for another user with an invalid token results in a status code of 401 and returns an error message indicating the lack of permission | HTTP Status: 401, JSON Response contains "message": "Unauthorized" |
| TC008 | Get empty list for ID not specified or incorrect format | Invalid or non-existent ID (e.g., 'invalidID', 1.23) provided in the URL | Verify that attempting to fetch a skill with an invalid or non-existent ID results in a status code of 404 and returns an error message indicating the issue | HTTP Status: 404, JSON Response contains "message": "Skill not found" |
| TC009 | Get empty list for large number as skill ID | Extremely large number (e.g., 10^100) provided in the URL | Verify that attempting to fetch a skill with an extremely large ID results in a status code of 400 and returns an error message indicating the issue | HTTP Status: 400, JSON Response contains "message": "Invalid skill ID" |
| TC100 | Get empty list for negative number as skill ID | Negative number (e.g., -5) provided in the URL | Verify that attempting to fetch a skill with a negative ID results in a status code of 400 and returns an error message indicating the issue | HTTP Status: 400, JSON Response contains "message": "Invalid skill ID" |

---

## DELETE /api/skills/:id
**Description:** Delete a skill by ID

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|

---

## POST /api/skills/:id/log
**Description:** Log a learning session for a skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Log valid learning session successfully | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 2.5, "notes": "Completed Python Basics" } | The API returns HTTP status code 201 and includes the newly created log entry in the response |
| TC002 | Log learning session with max hours limit | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 8.99999, "notes": null } | The API returns HTTP status code 201 and includes the newly created log entry in the response |
| TC003 | Log learning session without notes field | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 4.75 } | The API returns HTTP status code 201 and includes the newly created log entry in the response |
| TC004 | Log learning session with invalid hours value (too low) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 0.5, "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the hours must be greater than zero |
| TC005 | Log learning session with invalid hours value (too high) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 16.99999, "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the hours must be less than or equal to 8 |
| TC006 | Log learning session with invalid ID | None | As a user, I send a POST request to /api/skills/invalid/log with the body { "hours": 3.5 } | The API returns HTTP status code 404 and includes an error message indicating that the skill with the given ID does not exist |
| TC007 | Log learning session without hours field | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the required 'hours' field is missing |
| TC008 | Log learning session with invalid hours value (negative) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": -2.5, "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the 'hours' must be greater than zero |
| TC009 | Log learning session without valid hours value (empty string) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": "", "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the 'hours' must be greater than zero |
| TC010 | Log learning session without valid hours value (null) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": null, "notes": null } | The API returns HTTP status code 422 and includes an error message indicating that the 'hours' must be greater than zero |
| TC011 | Log learning session without valid notes value (empty string) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": "", "hours": 5.25 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC012 | Log learning session without valid notes value (null) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": null, "hours": 5.75 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC013 | Log learning session without valid notes value (only whitespace) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": "   ", "hours": 4.25 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC014 | Log learning session without valid notes value (null, empty array) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": [], "hours": 2.5 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC015 | Log learning session without valid notes value (only array) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": [1], "hours": 2.5 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC016 | Log learning session without valid notes value (only array of objects) | None | As a user, I send a POST request to /api/skills/1/log with the body { "notes": [{"text":"test"}], "hours": 2.5 } | The API returns HTTP status code 422 and includes an error message indicating that the 'notes' must be a non-empty string |
| TC017 | Log learning session without valid hours value (only number) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 4 } | The API returns HTTP status code 422 and includes an error message indicating that the 'hours' must be greater than zero |
| TC018 | Log learning session without valid hours value (only number, negative) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": -4 } | The API returns HTTP status code 422 and includes an error message indicating that the 'hours' must be greater than zero |
| TC019 | Log learning session without valid hours value (only number, floating point) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 4.5 } | The API returns HTTP status code 201 and includes the newly created log entry in the response |
| TC020 | Log learning session without valid hours value (only number, integer) | None | As a user, I send a POST request to /api/skills/1/log with the body { "hours": 4 } | The API returns HTTP status code 201 and includes the newly created log entry in the response |

---

## GET /api/dashboard
**Description:** Get dashboard stats - total skills, hours logged, sessions, top skill

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|

