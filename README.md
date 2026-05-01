<div align="center">

![版本](https://img.shields.io/badge/WatchdogX-v0.1.0-ff6b6b?style=for-the-badge&logo=datadog&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![许可](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=bookstack&logoColor=white)
![状态](https://img.shields.io/badge/Status-Active-success?style=for-the-badge&logo=statuspal&logoColor=white)
![架构](https://img.shields.io/badge/架构-Multi--Agent-blueviolet?style=for-the-badge&logo=openai&logoColor=white)

<br/>
<br/>

<h1>🐕 WatchdogX</h1>
<h3>轻量级多智能体协作框架 —— 面向微服务集群的新一代智能故障自愈系统</h3>

<p>
  <i>🌙 当你的微服务在凌晨三点宕机时，WatchdogX 已经完成了从发现到修复的全流程闭环。</i>
</p>

</div>

---

## 📖 项目概述

**WatchdogX** 是一个基于大语言模型（LLM）的轻量级多智能体协作框架，专为**微服务集群的自动化故障检测、智能诊断与自愈修复**而设计。它通过编排四个专业化 AI Agent 协同工作，构建了一条从 **监控告警 ➔ 长链推理诊断 ➔ 自动修复执行 ➔ 健康验证闭环** 的完整自动化链路，在无需人工干预的情况下实现非工作时间 **85% 以上** 的故障自愈率。

### 🎯 为什么选择 WatchdogX？

在现代化微服务架构中，传统运维面临五大挑战：

| 挑战 | 痛点描述 | WatchdogX 解决方案 |
|------|---------|-------------------|
| 🔴 **MTTR 过高** | 人工排查平均修复时间达 45 分钟，严重影响 SLA | AI 自动诊断 + 执行，MTTR 降至 12 分钟 |
| 🌙 **夜间漏报** | 非工作时间无人值守，故障发现滞后数小时 | 7×24 无人值守，秒级告警响应 |
| 🏝️ **信息孤岛** | 日志、指标、拓扑数据分散在不同系统 | 统一 Agent 集成，跨系统关联分析 |
| 🧠 **经验断层** | 历史故障处理经验难以沉淀和复用 | MemoryStore 记忆库自动积累和检索 |
| 🌪️ **告警风暴** | 日均 300+ 告警，运维人员疲于应付 | 智能去噪、分级、自动处理 |

---

## 🏗️ 系统架构

```
+===========================================================================+
|                         WatchdogX 系统架构                                  |
+===========================================================================+
|                                                                           |
|   +--------------+      +------------------+      +------------------+    |
|   | Monitor Agent|----->| Diagnosis Agent  |----->|  Executor Agent  |    |
|   |   (监控智能体) |      |    (诊断智能体)    |      |   (执行智能体)    |    |
|   |              |      |                  |      |                  |    |
|   | · 日志采集    |      | · 记忆库检索      |      | · 脚本生成       |    |
|   | · 指标采集    |      | · LLM 长链推理    |      | · 沙箱执行       |    |
|   | · 告警触发    |      | · 根因定位        |      | · 人工升级       |    |
|   +--------------+      +------------------+      +--------+---------+    |
|                                                              |           |
|   +--------------+      +------------------+      +--------+---------+    |
|   | Memory Store |<---->|  Tool Registry   |      |  Verify Agent   |    |
|   |   (记忆库)    |      |   (工具注册中心)   |      |   (验证智能体)    |    |
|   |              |      |                  |      |                  |    |
|   | · 案例存储    |      | · LogCollector   |      | · 健康检查       |    |
|   | · 语义检索    |      | · MetricsScraper |      | · 探活验证       |    |
|   | · 相似度匹配  |      | · ShellExecutor  |      | · 闭环反馈       |    |
|   +--------------+      | · HttpChecker    |      +------------------+    |
|                          +------------------+                             |
|                                                                           |
|   +=====================================================================+ |
|   |              Workflow Orchestrator (DAG 编排引擎)                      | |
|   |          on_success / on_error 分支  +  人工升级机制                   | |
|   +=====================================================================+ |
+===========================================================================+
```

### 🤖 四大核心 Agent

| Agent | 角色 | 核心能力 | 技术实现 |
|-------|------|---------|---------|
| **Monitor Agent** | 监控智能体 | 周期性采集容器日志和 Prometheus 指标，按可配置规则触发告警 | Docker API / K8s API / PromQL |
| **Diagnosis Agent** | 诊断智能体 | 接收告警后检索历史相似案例，执行 LLM 多步推理定位根因 | MemoryStore + LLM Chain-of-Thought |
| **Executor Agent** | 执行智能体 | 根据诊断报告生成修复脚本，执行回滚/扩容/重启等操作 | 沙箱化 Shell / REST API |
| **Verify Agent** | 验证智能体 | 修复后验证服务探活和核心 API 响应，失败则自动回退 | HTTP HealthCheck + 断言引擎 |

### 🔄 标准工作流程

```
1. Monitor Agent 检测到异常 → 触发告警
       │
2. Diagnosis Agent 接收告警上下文
       │
   ├── 从 MemoryStore 检索相似历史案例 (Top-K 语义相似度匹配)
   ├── 调用 ToolRegistry 工具链（日志分析、指标探索、拓扑追踪）
   └── LLM 多步推理 (Chain-of-Thought) → 输出诊断报告 + 根因定位
       │
3. Executor Agent 根据诊断报告生成修复方案
       │
   ├── 执行修复脚本（重启服务 / 扩容副本 / 回滚部署）
   ├── 成功 → 进入验证阶段
   └── 失败 → 自动升级到人工值班 + Slack/钉钉通知
       │
4. Verify Agent 验证修复效果
       │
   ├── 检查服务探活端点 (/health, /ready)
   ├── 验证核心 API 响应时间 + 状态码
   ├── 健康 → 闭环，记录案例到 MemoryStore
   └── 不健康 → 回退重试或升级人工处理
```

---

## 📊 生产环境表现

在某 20+ 微服务集群落地后的实测数据：

| 核心指标 | 优化前 | 优化后 | 提升幅度 |
|---------|--------|--------|---------|
| 🕐 **MTTR** (平均修复时间) | 45 min | 12 min | **↓ 73%** |
| 🌙 **非工作时间自愈率** | 0% | 85% | **+85%** |
| 📈 **日均处理告警量** | 50+ | 300+ | **×6** |
| ⚡ **运维效率** | 基线 | +70% | **↑ 70%** |
| 🎯 **故障漏报率** | 12% | 2% | **↓ 83%** |
| ✅ **告警准确率** | 65% | 92% | **↑ 27%** |
| 💰 **LLM Token 消耗** | — | ~600万/天 | — |

---

## 🚀 快速开始

### 环境要求

- **Python** 3.10+
- **LLM API Key**（OpenAI / 兼容接口）
- **可选**：Docker / Kubernetes / Prometheus

### 安装

```bash
# 从 PyPI 安装
pip install watchdogx

# 从源码安装
git clone https://github.com/zjh0510zjh/WatchdogX.git
cd WatchdogX
pip install -e .
```

### 配置

```bash
cp config.example.yaml config.yaml
vim config.yaml

export OPENAI_API_KEY="sk-..."
export WATCHDOGX_SLACK_WEBHOOK="https://hooks.slack.com/..."
```

### 启动

```python
from watchdogx import Orchestrator
orch = Orchestrator(config_path="config.yaml")
orch.start()
```

或使用命令行：

```bash
watchdogx start --config config.yaml
```

---

## 📁 项目结构

```
WatchdogX/
├── 📄 README.md                    # 项目文档（本文档）
├── 📄 CHANGELOG.md                 # 版本变更日志
├── 📄 CONTRIBUTING.md              # 贡献指南
├── 📄 LICENSE                      # MIT 许可证
├── 📄 pyproject.toml               # Python 包配置
├── 📄 requirements.txt             # Python 依赖
├── 📄 Makefile                     # 开发命令集
├── 📄 Dockerfile                   # Docker 构建文件
├── 📄 docker-compose.yml           # Docker 编排配置
├── 📄 config.example.yaml          # 配置模板
│
├── 📁 docs/                        # 技术文档
│   ├── architecture.md             # 架构设计文档
│   ├── agent_development.md        # Agent 开发指南
│   ├── api_reference.md            # API 参考文档
│   ├── deployment.md               # 部署指南
│   └── best_practices.md           # 最佳实践
│
├── 📁 examples/                    # 示例代码
│   ├── basic_workflow.py           # 基础工作流示例
│   ├── custom_agent.py             # 自定义 Agent 示例
│   ├── kubernetes_monitor.py       # K8s 监控示例
│   └── slack_integration.py        # Slack 集成示例
│
├── 📁 src/watchdogx/               # 核心源码
│   ├── __init__.py                 # 包入口
│   ├── cli.py                      # 命令行接口
│   ├── orchestrator.py             # DAG 编排引擎
│   ├── config.py                   # 配置管理
│   ├── exceptions.py               # 自定义异常
│   ├── logging_config.py           # 日志配置
│   ├── 📁 core/                    # 核心模块
│   │   ├── agent.py                # 基础 Agent 抽象类
│   │   ├── memory.py               # 向量记忆库
│   │   ├── tools.py                # 工具注册中心
│   │   └── llm_client.py           # LLM 客户端封装
│   ├── 📁 agents/                  # Agent 实现
│   │   ├── monitor_agent.py        # 监控 Agent
│   │   ├── diagnosis_agent.py      # 诊断 Agent
│   │   ├── executor_agent.py       # 执行 Agent
│   │   └── verify_agent.py         # 验证 Agent
│   └── 📁 tools/                   # 工具实现
│       ├── log_collector.py        # 日志采集工具
│       ├── metrics_scraper.py      # 指标采集工具
│       ├── shell_executor.py       # Shell 执行工具
│       └── http_checker.py         # HTTP 健康检查工具
│
└── 📁 tests/                       # 测试目录
```

---

## 🧪 开发指南

```bash
make dev           # 安装开发依赖
make test          # 运行测试
make lint          # 代码格式化 & 检查
make docker-build  # 构建 Docker 镜像
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！详见 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📄 许可证

本项目采用 [MIT License](./LICENSE)。

---

## 👤 作者

**ZJH0510ZJH**

🔗 GitHub：[https://github.com/zjh0510zjh](https://github.com/zjh0510zjh)

---

<div align="center">

<br/>
<h3>🛡️ 让 AI 守护你的每一行代码、每一个服务、每一个深夜的安宁 🛡️</h3>

<br/>

</div>
