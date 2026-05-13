import argparse
from agent.agent import run_agent


def main():
    parser = argparse.ArgumentParser(
        description="QA Test Case Generator Agent — generates functional test cases from API routes"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="input/skillpulse_routes.json",
        help="Path to the routes JSON file (default: input/skillpulse_routes.json)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="qwen2.5:3b",
        help="Ollama model to use (default: qwen2.5:3b)"
    )

    args = parser.parse_args()
    run_agent(input_file=args.input, model=args.model)


if __name__ == "__main__":
    main()
