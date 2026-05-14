import json
import os
from datetime import datetime


def generate_html_report(app_name: str, results: list, output_dir: str = "output"):
    """
    Generate an HTML report from test case results.

    Args:
        app_name: Name of the application
        results: List of dicts with route info and test cases
        output_dir: Directory to save output
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{app_name.lower().replace(' ', '_')}_report_{timestamp}.html"

    # Summary stats
    total_routes = len(results)
    total_tcs = sum(len(r["test_cases"]) for r in results)

    # Build route cards
    route_cards = ""
    for result in results:
        route = result["route"]
        test_cases = result["test_cases"]
        method = route["method"]
        path = route["path"]
        description = route["description"]

        # Method badge color
        method_colors = {
            "GET": "#2ecc71",
            "POST": "#3498db",
            "DELETE": "#e74c3c",
            "PUT": "#f39c12",
            "PATCH": "#9b59b6"
        }
        badge_color = method_colors.get(method, "#95a5a6")

        # Build test case rows
        tc_rows = ""
        for tc in test_cases:
            tc_rows += f"""
            <tr>
                <td class="tc-id">{tc['id']}</td>
                <td>{tc['title']}</td>
                <td>{tc['precondition']}</td>
                <td>{tc['steps']}</td>
                <td>{tc['expected_result']}</td>
            </tr>"""

        if not tc_rows:
            tc_rows = """
            <tr>
                <td colspan="5" class="no-data">No test cases generated</td>
            </tr>"""

        route_cards += f"""
        <div class="route-card">
            <div class="route-header">
                <span class="method-badge" style="background:{badge_color}">{method}</span>
                <span class="route-path">{path}</span>
                <span class="tc-count">{len(test_cases)} test cases</span>
            </div>
            <p class="route-desc">{description}</p>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Precondition</th>
                        <th>Steps</th>
                        <th>Expected Result</th>
                    </tr>
                </thead>
                <tbody>
                    {tc_rows}
                </tbody>
            </table>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app_name} — Test Cases Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #0f1117;
            color: #e0e0e0;
            padding: 30px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            border-radius: 12px;
            border: 1px solid #2a2a4a;
        }}
        .header h1 {{
            font-size: 2rem;
            color: #7c83fd;
            margin-bottom: 8px;
        }}
        .header p {{
            color: #888;
            font-size: 0.9rem;
        }}
        .summary {{
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
            justify-content: center;
        }}
        .summary-card {{
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            border-radius: 10px;
            padding: 20px 40px;
            text-align: center;
        }}
        .summary-card .number {{
            font-size: 2.5rem;
            font-weight: bold;
            color: #7c83fd;
        }}
        .summary-card .label {{
            font-size: 0.85rem;
            color: #888;
            margin-top: 4px;
        }}
        .route-card {{
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 24px;
        }}
        .route-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 8px;
        }}
        .method-badge {{
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: bold;
            color: white;
        }}
        .route-path {{
            font-size: 1.1rem;
            font-family: monospace;
            color: #e0e0e0;
        }}
        .tc-count {{
            margin-left: auto;
            font-size: 0.85rem;
            color: #888;
            background: #0f1117;
            padding: 4px 10px;
            border-radius: 20px;
        }}
        .route-desc {{
            color: #888;
            font-size: 0.9rem;
            margin-bottom: 16px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
        }}
        thead tr {{
            background: #0f1117;
        }}
        th {{
            padding: 10px 12px;
            text-align: left;
            color: #7c83fd;
            font-weight: 600;
            border-bottom: 1px solid #2a2a4a;
        }}
        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #1e1e3a;
            vertical-align: top;
            line-height: 1.5;
        }}
        tr:last-child td {{ border-bottom: none; }}
        tr:hover td {{ background: #16213e; }}
        .tc-id {{
            font-family: monospace;
            color: #7c83fd;
            font-weight: bold;
            white-space: nowrap;
        }}
        .no-data {{
            text-align: center;
            color: #555;
            padding: 20px;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: #555;
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🧪 {app_name} — Test Cases Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Model: qwen2.5:3b</p>
    </div>

    <div class="summary">
        <div class="summary-card">
            <div class="number">{total_routes}</div>
            <div class="label">API Routes</div>
        </div>
        <div class="summary-card">
            <div class="number">{total_tcs}</div>
            <div class="label">Test Cases</div>
        </div>
    </div>

    {route_cards}

    <div class="footer">
        <p>Generated by QA Test Generator Agent</p>
    </div>
</body>
</html>"""

    with open(filename, "w") as f:
        f.write(html)

    print(f"📊 HTML report saved to: {filename}")
    return filename
