# WatchdogX

Lightweight Multi-Agent Collaboration Framework for Microservice Self-Healing

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/status-active-brightgreen.svg)]()

## Overview

WatchdogX is a lightweight, LLM-powered multi-agent collaboration framework designed for microservice incident management. It automatically monitors, diagnoses, and remediates production issues — achieving **85% off-hour self-healing rate** in production.

### Architecture

Three specialized AI agents collaborate in a DAG-based workflow:

- **Monitor Agent** — Periodic log/metrics collection with configurable alert rules
- **Diagnosis Agent** — Long-chain reasoning over logs/traces/topology with LLM root-cause analysis
- **Executor Agent** — Generates and executes remediation scripts (rollback/scale/restart)
- **Verify Agent** — Post-remediation health checks with automatic rollback on failure

## Quick Start

```bash
pip install watchdogx
watchdogx start --config config.yaml
```

## Performance

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| MTTR | 45 min | 12 min | 73% ↓ |
| Off-hour self-healing | 0% | 85% | — |
| Operator efficiency | baseline | +70% | — |

## License

MIT © ZJH0510ZJH