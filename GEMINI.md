# AI Terminal (ai_terminal)

An intelligent terminal project that bridges natural language with shell execution, inspired by Google Cloud Workbench and modern AI-powered CLI tools.

## Project Vision
To create a seamless terminal experience where natural language intent is translated into precise, context-aware shell commands, enabling developers to focus on "what" to do rather than "how" to type it. **Optimized for local deployment on consumer-grade hardware (e.g., GTX 1060).**

## Core Features
- **Natural Language to Shell:** Convert human-readable instructions into executable terminal commands (e.g., Ubuntu/Linux commands, `docker`, `conda`, `git`, `gcloud`).
- **Local LLM Backend:** Native support for local inference (e.g., via Ollama/Llama.cpp). Recommended models for 6GB VRAM (GTX 1060): DeepSeek-Coder-7B-Instruct (4-bit), Llama-3-8B (4-bit).
- **Contextual Awareness:** Deep integration with the local codebase, project environment, and command history.
- **Intelligent Error Handling:** Automatically analyze command failures and suggest fixes or explanations.
- **Safety & Control:** A "Human-in-the-Loop" approach where all AI-generated commands require explicit approval by default.
- **Interactive Pseudo-Terminal (PTY):** Support for interactive applications (vim, htop) within the AI-managed session.
- **Search-Powered Grounding:** Real-time access to documentation and troubleshooting guides via integrated search.

## Project Mandates

### 1. Security & Privacy
- **Local-First Inference:** Prioritize local LLMs to ensure data privacy and zero dependency on cloud services for sensitive operations.
- **Zero Secret Leaks:** Never log, store, or transmit API keys, secrets, or sensitive environment variables.
- **Explicit Approval:** No destructive or modifying commands shall be executed without user confirmation.

### 2. Performance & Efficiency
- **GTX 1060 Optimization:** Specifically target performance for 6GB VRAM hardware using quantized models (GGUF/EXL2).
- **Minimal Latency:** Use local API endpoints and optimized context management for near-instant feedback.

### 3. Engineering Standards
- **Idiomatic Code:** Follow Python PEP 8 best practices.
- **Test-Driven Development:** Every new feature must be accompanied by comprehensive tests.
- **Clean Abstractions:** Separate terminal logic, LLM providers (Ollama, Gemini, OpenAI), and context management.

## Proposed Architecture

### 1. AI Shell Wrapper
Intercepts user input and determines if it's a direct command (prefixed with `!`) or a natural language request.

### 2. LLM Provider Layer
Abstraction for different backends. Default: **Ollama** (Local). Optional: Gemini Pro (Remote).

### 3. Context Engine
Indexes the current directory, project structure, environment (Docker/Conda info), and history.

### 4. Terminal Emulator (PTY)
A robust PTY implementation that handles terminal sequences and interactive applications.

## Development Roadmap
1. [ ] Core PTY implementation and basic shell bypass.
2. [ ] **Ollama Integration** for local NL-to-Command translation.
3. [ ] System Context Engine (detect Ubuntu version, Docker, Conda).
4. [ ] Support for interactive apps (Vim, etc.).
5. [ ] Search-Powered Grounding.

---
*This document serves as the foundational mandate for the ai_terminal project. All development must align with these principles.*
