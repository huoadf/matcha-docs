This is the documentation for the Matcha LuaVM.

{% hint style="info" %}
Matcha **is not an executor** — it does not hook any functions in the Roblox engine. Instead it emulates them externally, which makes it completely undetected, but also means it has no direct access to internal Roblox API functions.
{% endhint %}

<div class="vault-counter-card" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: linear-gradient(135deg, rgba(248, 81, 73, 0.12) 0%, rgba(20, 15, 15, 0.9) 100%); border: 1px solid rgba(248, 81, 73, 0.45); border-radius: 12px; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.45); backdrop-filter: blur(8px);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
<div style="display: flex; align-items: center; gap: 0.6rem;">
<span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #f85149; box-shadow: 0 0 10px #f85149; animation: pulseBeaconRed 1.8s infinite;"></span>
<strong style="font-size: 1.05rem; color: #fff; letter-spacing: -0.2px;">Live Counter: Days Not Added (Waiting on Vault)</strong>
</div>
<span style="display: inline-flex; align-items: center; font-size: 0.75rem; font-weight: 600; padding: 0.2rem 0.55rem; border-radius: 999px; background: rgba(248, 81, 73, 0.18); color: #f85149; border: 1px solid rgba(248, 81, 73, 0.5);">🔴 HYBRID UPDATE OVERDUE</span>
</div>
<div style="margin: 0 0 1rem 0; font-size: 0.88rem; color: var(--text-muted); line-height: 1.45;">
Vault announced incoming Pro Hybrid features on <strong>Sep 13 at 11:03 PM</strong> with a promise of <strong>"upcoming update max 3 days"</strong>: <code style="color:#f85149;">fireclickdetector</code>, <code style="color:#f85149;">fireproximityprompt</code>, <code style="color:#f85149;">firetouchinterest</code>. The 3-day deadline passed on <strong>Sep 16 at 11:03 PM</strong>.
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.6rem; max-width: 440px; margin-bottom: 0.85rem;" id="vault-timer-grid">
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(248,81,73,0.25); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-days" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #f85149; line-height: 1;">1</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Days Overdue</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(248,81,73,0.25); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-hours" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #f85149; line-height: 1;">14</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Hours</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(248,81,73,0.25); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-mins" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #f85149; line-height: 1;">18</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Mins</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(248,81,73,0.25); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-secs" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #f85149; line-height: 1;">42</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Secs</div>
</div>
</div>
<div id="v-status-note" style="font-size: 0.82rem; color: #ff7b72; display: flex; align-items: center; gap: 0.4rem;">
<span>⚠️</span> <span id="v-status-text"><strong>1 day past the 3-day deadline</strong> (3 days, 14 hours total waiting on Vault to add to LuaVM)</span>
</div>
</div>

{% hint style="success" %}
**Changelogs (Sep 18 2026)**
- Fixed Decompiler
- **Version:** [version-4310300497aa4917](https://rdd.whatexpsare.online/?channel=LIVE&binaryType=WindowsPlayer&version=version-4310300497aa4917)
- Updated to the latest version

*Run loader to update* · [Full changelogs →](/matcha/changelogs)
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

[**UI Binding** custom tabs, widgets & hotkeys](/matcha/ui-binding)

[**Code examples** complete script snippets](/matcha/examples)

[**VM limitations** execution rules & workarounds](/matcha/limitations)

[**FAQ** common questions & fixes](/matcha/faq)

[**Changelogs** release history & updates](/matcha/changelogs)
:::

## AI Agents & MCP Integration ::pro::

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