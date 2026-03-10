# AI 智能终端 (ai_terminal)

`ai_terminal` 是一个将自然语言与 Shell 命令执行完美结合的智能终端工具。它的灵感来源于 Google Cloud Workbench 的远程终端体验，旨在让开发者能够通过自然语言描述意图，自动生成并执行准确的 Shell 命令。

**🚀 针对消费级显卡 (如 GTX 1060 6GB) 进行了优化，支持完全本地化的 LLM 推理。**

## 🌟 主要特性

- **自然语言转 Shell**: 直接输入“列出当前目录下最大的 5 个文件”或“连接到我的远程数据库”，终端将自动翻译为对应的 `ls`、`find` 或 `ssh` 命令。
- **本地 LLM 推理 (Ollama)**: 默认支持 [Ollama](https://ollama.com/)，推荐使用针对 6GB 显存优化的 `deepseek-coder:6.7b-instruct-q4_K_M` 模型。无需云端 API，保护代码隐私。
- **环境上下文感知**: 深度感知当前 Ubuntu/Linux 系统环境。
    - **Docker**: 自动识别正在运行的容器名称。
    - **Conda**: 自动检测现有的虚拟环境及当前激活的环境。
- **安全 & 可控**:
    - **预览机制**: 在执行前展示 AI 生成的命令。
    - **手动编辑 (e)**: 如果 AI 生成的参数有误，可以在执行前快速编辑修改。
- **全功能 PTY 支持**: 采用伪终端 (PTY) 技术，支持在 AI 会话中运行 `vim`、`htop`、`docker exec -it` 等交互式命令。

## 🚀 快速开始

### 1. 准备本地模型 (推荐)

安装 [Ollama](https://ollama.com/) 并拉取优化后的模型：

```bash
ollama pull deepseek-coder:6.7b-instruct-q4_K_M
```

### 2. 安装项目

克隆并以可编辑模式安装：

```bash
git clone https://github.com/your-repo/ai_terminal.git
cd ai_terminal
pip install -e .
```

### 3. 使用方式

1.  **交互模式** (输入 `exit` 退出):
    ```bash
    ai-terminal
    ```
    进入后可直接输入指令，如：`> 帮我清理所有停止运行的 docker 容器`

2.  **直接命令行输入**:
    ```bash
    ai-terminal "在 conda 的 base 环境下安装 numpy"
    ```

3.  **原生 Shell 旁路**:
    在命令前加上 `!` 即可直接执行原生命令：`> !ls -lh`

## 🛠️ 架构设计

```text
ai_terminal/
├── src/
│   └── ai_terminal/
│       ├── __init__.py
│       ├── main.py           # CLI 入口与逻辑编排
│       ├── ollama_client.py   # 本地 LLM 接口 (Ollama)
│       ├── context_engine.py  # 环境感知引擎 (Docker/Conda/OS)
│       └── terminal.py        # PTY 伪终端管理器
├── pyproject.toml            # 项目配置与依赖管理
├── GEMINI.md                 # 核心愿景与规范说明
└── README.md                 # 使用指南
```

## 📅 开发规划

- [x] 基础 PTY 伪终端实现。
- [x] Ollama 本地模型集成。
- [x] 基础环境感知（Ubuntu, Docker, Conda）。
- [x] 命令二次编辑与确认逻辑。
- [ ] 增强的文件系统上下文索引（RAG）。
- [ ] 多轮对话支持。
- [ ] 实时搜索增强 (Google Search Grounding)。

## 📄 许可证

本项目采用 MIT 许可证。
