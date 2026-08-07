# Frequently Asked Questions (FAQ)

Frequently asked questions regarding Matcha execution, updates, roles, and troubleshooting.

---

## General Questions

### What is Matcha?
Matcha is a **Roblox LuaVM script executor** that emulates Roblox API functions externally without hooking into internal engine functions. This design makes it 100% undetected by server-side or client-side anti-cheat mechanisms.

### Is Matcha detectable?
No. Because Matcha operates externally without memory hook signatures on Roblox engine routines, it is undetected.

### How do I update Matcha?
Whenever a new update is released, simply **reopen the Matcha loader**. The loader will automatically download and apply the latest version.

---

## Troubleshooting

### Why are features not working or broken in-game?
Make sure your Roblox game client is updated to the latest forced version. If Roblox updated recently, you may encounter broken features until you force-update your game client or reopen the loader.

### Why is `loadstring` dropping my return values?
Matcha's `loadstring` implementation drops top-level `return` statements. To pass values out of a `loadstring` execution, set them to global variables (e.g. `_G.MyResult = 5`).

### How do I connect Matcha to Antigravity or Codex?
Matcha Pro features native **Model Context Protocol (MCP)** integration ::pro::.
- **Antigravity**: Open `C:\Users\<USERNAME>\.gemini\antigravity\mcp_config.json` and add `"matcha": { "serverUrl": "http://127.0.0.1:8765/mcp" }` inside `"mcpServers"`.
- **Codex**: Run `codex mcp add matcha --url http://127.0.0.1:8765/mcp` in your terminal.

---

## Roles & Versions

### What is the difference between Buyer and Pro?
- **Buyer ::buyer::**: Standard access to the Matcha executor, drawing API, memory tools, and base Lua library.
- **Pro ::pro::**: Early-access features including Hybrid Mode (Remote Spy, `FireServer`, `InvokeFunction`), and native AI Agent / MCP server integration.
