# QA Test Generator Agent 🤖

An AI-powered agent that automatically generates functional test cases for REST APIs using a local LLM (Ollama). Takes API route definitions as input and produces structured test cases in both Markdown and HTML formats.

---

## 📌 Table of Contents

- [About](#about)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Adding a New App](#adding-a-new-app)

---

## About

Built as a learning project to explore AI agent development applied to QA automation. The agent is generic — point it at any REST API's route definitions and it generates test cases covering happy paths, edge cases, negative scenarios, and boundary values.

Currently demonstrated on the [SkillPulse](https://github.com/Manish12588/skillpulse) API.

---

## How It Works

```
input/skillpulse_routes.json
           │
           ▼
   prompt_builder.py
   (builds structured prompt per route)
           │
           ▼
   Ollama (qwen2.5:3b)
   (generates test cases)
           │
           ▼
     agent.py parser
   (extracts structured data)
           │
           ├──▶ output/test_cases_TIMESTAMP.md
           └──▶ output/report_TIMESTAMP.html
```

**Agent flow per route:**
1. Read route definition (method, path, fields, response)
2. Build a structured prompt with QA context
3. Call local LLM via Ollama
4. Parse response into structured test cases
5. Save to Markdown + HTML report

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3 |
| LLM Runtime | Ollama |
| Model | qwen2.5:3b (local, no API key needed) |
| Input Format | JSON |
| Output Formats | Markdown, HTML |

---

## Project Structure

```
qa-test-generator-agent/
├── agent/
│   ├── __init__.py
│   ├── agent.py          ← core agent logic + parser
│   ├── prompt_builder.py ← builds LLM prompts per route
│   └── reporter.py       ← generates HTML report
├── input/
│   └── skillpulse_routes.json   ← API route definitions
├── output/               ← generated files (gitignored)
├── main.py               ← CLI entry point
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed and running
- `qwen2.5:3b` model pulled

### Install Ollama and pull model

```bash
# Install Ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model
ollama pull qwen2.5:3b
```

### Clone and install dependencies

```bash
git clone https://github.com/Manish12588/qa-test-generator-agent.git
cd qa-test-generator-agent

pip install -r requirements.txt
```

### Make sure Ollama is running

```bash
ollama serve
```

---

## Usage

### Run with default settings (SkillPulse API)

```bash
python main.py
```

### Run with a custom routes file

```bash
python main.py --input input/your_app_routes.json
```

### Run with a different model

```bash
python main.py --model qwen2.5:3b
```

**Output files are saved to `output/` with timestamps:**
```
output/skillpulse_test_cases_20260514_142223.md
output/skillpulse_report_20260514_142223.html
```

---

## Sample Output

### Terminal
```
🚀 Starting QA Test Generator Agent
📂 Input: input/skillpulse_routes.json
🤖 Model: qwen2.5:3b

📋 App: SkillPulse
📍 Routes found: 6

[1/6] Processing: GET /api/skills
  Calling LLM (qwen2.5:3b)...
  ✅ Generated 6 test cases
...
✅ Test cases saved to: output/skillpulse_test_cases_20260514_142223.md
📊 HTML report saved to: output/skillpulse_report_20260514_142223.html
🎉 Agent completed successfully!
```

### Generated Test Cases (example)

| ID | Title | Precondition | Steps | Expected Result |
|----|-------|-------------|-------|-----------------|
| TC001 | Create a new skill | Valid inputs provided | POST /api/skills with `{"name": "Python", "category": "Programming", "goal_hours": 50}` | Created skill object returned with status 201 |
| TC002 | Missing required field | Required fields missing | POST /api/skills with empty body `{}` | Status 400 Bad Request with error details |
| TC003 | Invalid data type | Non-numeric goal_hours | POST /api/skills with `{"goal_hours": "abc"}` | Status 400 with validation error |

---

## Adding a New App

Create a new JSON file in `input/` following this schema:

```json
{
  "app_name": "YourApp",
  "base_url": "http://localhost:3000",
  "description": "Brief description of what the app does",
  "routes": [
    {
      "method": "GET",
      "path": "/api/resource",
      "description": "Get all resources",
      "request_body": null,
      "response": "List of resource objects"
    },
    {
      "method": "POST",
      "path": "/api/resource",
      "description": "Create a resource",
      "request_body": {
        "name": "string, required",
        "value": "number, required"
      },
      "response": "Created resource object"
    }
  ]
}
```

Then run:
```bash
python main.py --input input/your_app_routes.json
```

---

## Credits

Built as part of a DevOps + QA automation learning journey.
Demonstrated on [SkillPulse](https://github.com/Manish12588/skillpulse) — a skill tracking application.

---

## Author

**Manish Kumar**
QA Automation Engineer | DevOps Practitioner

- GitHub: [@Manish12588](https://github.com/Manish12588)
- LinkedIn: [linkedin.com/in/kumar05](https://www.linkedin.com/in/kumar05/)