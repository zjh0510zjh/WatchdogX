# WatchdogX

<div align="center">

**轻量级多智能体协作框架 —— 面向微服务集群的智能故障自愈系统**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 项目简介

WatchdogX 是一个基于大语言模型（LLM）的轻量级多智能体协作框架，专为微服务集群的自动化故障检测、诊断与自愈而设计。

## 核心功能

- 四大 AI Agent 协作：Monitor 监控 → Diagnosis 诊断 → Executor 执行 → Verify 验证
- 支持 Docker / Kubernetes / Prometheus 集成
- DAG 工作流编排引擎，支持异常分支处理和人工升级
- 记忆库 MemoryStore，支持历史案例相似度检索
- 工具注册中心 ToolRegistry，支持 LLM Function Calling
- 命令行工具、Docker 部署、CI/CD 流水线

## 快速开始

```bash
pip install watchdogx
watchdogx start --config config.yaml
```

## 项目结构

```
WatchdogX/
├── README.md, CHANGELOG.md, CONTRIBUTING.md, LICENSE
├── pyproject.toml, requirements.txt, Makefile
├── Dockerfile, docker-compose.yml, config.example.yaml
├── docs/ (5篇技术文档)
├── examples/ (4个示例)
├── src/watchdogx/
│   ├── cli.py, orchestrator.py, config.py
│   ├── core/ (agent.py, memory.py, tools.py, llm_client.py)
│   ├── agents/ (4个Agent实现)
│   └── tools/ (4个工具实现)
└── tests/
```

## 作者

**ZJH0510ZJH** — [GitHub](https://github.com/zjh0510zjh)
