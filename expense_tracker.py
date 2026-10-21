
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="CLI Expense Tracker"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="1.0"
    )

    parser.parse_args()

if __name__ == "__main__":
    main()
