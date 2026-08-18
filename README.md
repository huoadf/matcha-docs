# Matcha Documentation

[![Docs Live](https://img.shields.io/badge/docs-live-8cc63f?style=flat-square)](https://huoadf.github.io/matcha-docs/)
[![Matcha Version](https://img.shields.io/badge/roblox_version-ce0bcd0fbd484804-blue?style=flat-square)](https://huoadf.github.io/matcha-docs/changelogs/)
[![AI Ready](https://img.shields.io/badge/AI_Ready-llms.txt-purple?style=flat-square)](https://huoadf.github.io/matcha-docs/llms.txt)

Official, comprehensive documentation for the **Matcha LuaVM** — an external, undetected LuaVM emulator for Roblox.

📖 **Live Documentation:** [https://huoadf.github.io/matcha-docs/](https://huoadf.github.io/matcha-docs/)

---

## 🤖 AI & MCP Integration (Pro)

Matcha provides direct support for AI coding assistants (Antigravity, Codex, Cursor, Claude Code) via native Model Context Protocol (MCP) and structured LLM indices.

### Connect AI to Matcha Docs
* **Quick Read Index:** [`https://huoadf.github.io/matcha-docs/llms.txt`](https://huoadf.github.io/matcha-docs/llms.txt)
* **Full API Context:** [`https://huoadf.github.io/matcha-docs/llms-full.txt`](https://huoadf.github.io/matcha-docs/llms-full.txt)

### Connect AI to Live Matcha Game Bridge (Port 8765)
When Matcha is running in-game, it exposes an MCP server at `http://127.0.0.1:8765/mcp`.

#### Google Antigravity
Add this to `C:\Users\<USERNAME>\.gemini\antigravity\mcp_config.json`:
```json
{
  "mcpServers": {
    "matcha": {
      "serverUrl": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

#### Codex
```bash
codex mcp add matcha --url http://127.0.0.1:8765/mcp
```

---

## 📁 Repository Structure

```
├── src/                 # Markdown documentation source files
│   ├── getting-started.md
│   ├── functions-globals.md
│   ├── ui-binding.md
│   ├── drawing.md
│   ├── memory.md
│   ├── changelogs.md
│   └── ...
├── assets/              # Animated logo GIF, CSS, JS, and Search Index
├── template.html        # HTML layout template
├── generate.py          # Python static site & search index compiler
├── llms.txt             # Concise entry-point index for AI models
└── llms-full.txt        # Complete concatenated docs text for AI models
```

---

## 🛠️ Building & Updating the Site

To compile edits made to any `.md` file in `src/`:

1. Run the build generator:
   ```bash
   python generate.py
   ```
2. Commit and push changes:
   ```bash
   git add .
   git commit -m "Docs: Update documentation"
   git push origin main
   ```
The static generator automatically compiles the HTML pages, builds `search-index.json` for client-side search, and regenerates both `llms.txt` and `llms-full.txt`.
