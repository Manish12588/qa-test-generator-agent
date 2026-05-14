import json
import os
import re
from datetime import datetime
import ollama
from agent.prompt_builder import build_prompt
from agent.reporter import generate_html_report


def load_routes(input_file: str) -> dict:
    with open(input_file, "r") as f:
        return json.load(f)


def call_llm(prompt: str, model: str = "qwen2.5:3b") -> str:
    print(f"  Calling LLM ({model})...")
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def parse_test_cases(raw_output: str) -> list:
    """
    Parse LLM output into structured test case list.
    Handles inconsistent formatting from smaller LLMs.
    """
    test_cases = []

    for line in raw_output.strip().split("\n"):
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Must start with TC pattern
        if not re.match(r'^TC\d+', line):
            continue

        # Split by pipe
        parts = [p.strip() for p in line.split("|")]

        if len(parts) >= 5:
            # Clean up "Precondition:", "Test steps:", "Expected result:" labels
            precondition = re.sub(r'^Precondition:\s*', '', parts[2], flags=re.IGNORECASE)
            steps = re.sub(r'^Test steps?:\s*', '', parts[3], flags=re.IGNORECASE)
            expected = re.sub(r'^Expected results?:\s*', '', parts[4], flags=re.IGNORECASE)

            test_cases.append({
                "id": parts[0],
                "title": parts[1],
                "precondition": precondition,
                "steps": steps,
                "expected_result": expected
            })

        elif len(parts) == 4:
            # LLM merged steps and expected — still save it
            test_cases.append({
                "id": parts[0],
                "title": parts[1],
                "precondition": parts[2],
                "steps": parts[3],
                "expected_result": "See steps"
            })

    return test_cases


def save_output(app_name: str, results: list, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{app_name.lower().replace(' ', '_')}_test_cases_{timestamp}.md"

    with open(filename, "w") as f:
        f.write(f"# Test Cases — {app_name}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for result in results:
            route = result["route"]
            test_cases = result["test_cases"]

            f.write(f"---\n\n")
            f.write(f"## {route['method']} {route['path']}\n")
            f.write(f"**Description:** {route['description']}\n\n")
            f.write(f"| ID | Title | Precondition | Steps | Expected Result |\n")
            f.write(f"|----|-------|-------------|-------|-----------------|\n")

            if test_cases:
                for tc in test_cases:
                    f.write(
                        f"| {tc['id']} | {tc['title']} | {tc['precondition']} "
                        f"| {tc['steps']} | {tc['expected_result']} |\n"
                    )
            else:
                f.write(f"| — | No test cases generated | — | — | — |\n")
            f.write("\n")

    print(f"\n✅ Test cases saved to: {filename}")
    return filename


def run_agent(input_file: str, model: str = "qwen2.5:3b"):
    print(f"🚀 Starting QA Test Generator Agent")
    print(f"📂 Input: {input_file}")
    print(f"🤖 Model: {model}\n")

    data = load_routes(input_file)
    app_name = data["app_name"]
    app_description = data["description"]
    routes = data["routes"]

    print(f"📋 App: {app_name}")
    print(f"📍 Routes found: {len(routes)}\n")

    results = []

    for i, route in enumerate(routes, 1):
        print(f"[{i}/{len(routes)}] Processing: {route['method']} {route['path']}")
        prompt = build_prompt(app_name, app_description, route)
        raw_output = call_llm(prompt, model)
        test_cases = parse_test_cases(raw_output)
        print(f"  ✅ Generated {len(test_cases)} test cases")

        results.append({
            "route": route,
            "test_cases": test_cases,
            "raw_output": raw_output
        })

    save_output(app_name, results)
    generate_html_report(app_name,results)
    print("\n🎉 Agent completed successfully!")
