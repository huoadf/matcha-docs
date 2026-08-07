This is the documentation for the Matcha LuaVM.

{% hint style="info" %}
Matcha **is not an executor** — it does not hook any functions in the Roblox engine. Instead it emulates them externally, which makes it completely undetected, but also means it has no direct access to internal Roblox API functions.
{% endhint %}

{% hint style="success" %}
**New (Aug 6 2026):**
- Fixed Attributes (`GetAttribute` & `SetAttribute`)
- Fixed `.Text`
- Fixed `AbsoluteSize` & `AbsolutePosition`
- Fixed Decompiler
- *Run loader to update*
{% endhint %}

## Browse the docs

::: cards
[**Globals** loadstring, identifyexecutor, decompile…](/matcha/functions-globals)

[**Console & input** print, keys, mouse, clipboard](/matcha/functions-console-input)

[**Scheduler & misc** wait, task, run_secure, require](/matcha/functions-misc)

[**Memory** getbase, memory_read / memory_write](/matcha/memory)

[**Garbage collector** getgc / setgc / applygc](/matcha/garbage-collector)

[**Classes** game, Players, RunService…](/matcha/classes)

[**Datatypes** Vector3, CFrame, Color3…](/matcha/datatypes)

[**Drawing** the Drawing API](/matcha/drawing)
:::

## AI Agents & MCP Integration

Matcha includes native Model Context Protocol (MCP) support for seamless integration with AI coding assistants like Antigravity and Codex.

### Adding to Antigravity
Go to `C:\Users\<USERNAME>\.gemini\antigravity` and open `mcp_config.json`. Add the Matcha server to your `mcpServers` list:

```json
{
  "mcpServers": {
    "matcha": {
      "serverUrl": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

### Adding to Codex
Run the following command in your terminal:
```bash
codex mcp add matcha --url http://127.0.0.1:8765/mcp
```

## Resources

To understand how the LuaVM works, you first need the basics of Lua(U). For that, visit <https://lua.org>.