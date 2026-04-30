"""Command-line interface for WatchdogX."""

import argparse
import sys
from watchdogx.orchestrator import Orchestrator


def main():
    parser = argparse.ArgumentParser(
        prog="watchdogx",
        description="WatchdogX - Multi-Agent Self-Healing Framework",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Start the orchestrator")
    start_parser.add_argument(
        "--config", type=str, default="config.yaml", help="Path to config file"
    )
    start_parser.add_argument(
        "--daemon", action="store_true", help="Run as daemon"
    )

    subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "start":
        print(f"[WatchdogX] Starting with config: {args.config}")
        orch = Orchestrator(config_path=args.config)
        orch.start()
    elif args.command == "version":
        from watchdogx import __version__
        print(f"WatchdogX v{__version__}")


if __name__ == "__main__":
    main()
