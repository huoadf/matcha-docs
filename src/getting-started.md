This is the documentation for the Matcha LuaVM.

{% hint style="info" %}
Matcha **is not an executor** — it does not hook any functions in the Roblox engine. Instead it emulates them externally, which makes it completely undetected, but also means it has no direct access to internal Roblox API functions.
{% endhint %}

<div class="vault-counter-card" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: linear-gradient(135deg, rgba(140, 198, 63, 0.15) 0%, rgba(15, 25, 15, 0.9) 100%); border: 1px solid rgba(140, 198, 63, 0.55); border-radius: 12px; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.45); backdrop-filter: blur(8px);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
<div style="display: flex; align-items: center; gap: 0.6rem;">
<span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #8cc63f; box-shadow: 0 0 10px #8cc63f;"></span>
<strong style="font-size: 1.05rem; color: #fff; letter-spacing: -0.2px;">Hybrid Update: Delivered by Vault!</strong>
</div>
<span style="display: inline-flex; align-items: center; font-size: 0.75rem; font-weight: 600; padding: 0.2rem 0.55rem; border-radius: 999px; background: rgba(140, 198, 63, 0.18); color: #8cc63f; border: 1px solid rgba(140, 198, 63, 0.5);">🟢 DELIVERED IN PRO</span>
</div>
<div style="margin: 0 0 1rem 0; font-size: 0.88rem; color: var(--text-muted); line-height: 1.45;">
Vault announced incoming Pro Hybrid features on <strong>Sep 13 at 11:03 PM</strong> with a promise of <strong>"upcoming update max 3 days"</strong>. After <strong>35 days past deadline</strong> (38 days total wait), all 3 promised features (<code style="color:#8cc63f;">fireclickdetector</code>, <code style="color:#8cc63f;">fireproximityprompt</code>, <code style="color:#8cc63f;">firetouchinterest</code>) plus a Remote Spy fix have officially arrived!
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.6rem; max-width: 440px; margin-bottom: 0.85rem;" id="vault-timer-grid">
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(140,198,63,0.3); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-days" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">35</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Days Waited</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(140,198,63,0.3); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-hours" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">23</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Hours</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(140,198,63,0.3); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-mins" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">26</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Mins</div>
</div>
<div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(140,198,63,0.3); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-secs" style="font-size: 1.65rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">00</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Secs</div>
</div>
</div>
<div id="v-status-note" style="font-size: 0.82rem; color: #8cc63f; display: flex; align-items: center; gap: 0.4rem;">
<span>✅</span> <span id="v-status-text"><strong>Delivered on Oct 21, 2026</strong> (38 days total wait since announcement)</span>
</div>
<div style="margin-top: 0.85rem; font-size: 0.82rem; color: #8cc63f; background: rgba(140, 198, 63, 0.12); border-left: 3px solid #8cc63f; padding: 0.5rem 0.75rem; border-radius: 0 6px 6px 0; line-height: 1.45;">
🚀 <strong>Released (Oct 21):</strong> <code>firetouchinterest</code>, <code>fireclickdetector</code>, and <code>fireproximityprompt</code> are now live in Matcha Pro! Run loader to update.
</div>
</div>

{% hint style="success" %}
**Changelogs (Oct 21 2026)** ::pro::
- Added `firetouchinterest(origin_part, target_part, state)` — `0 = Touch`, `1 = Untouch`
- Added `fireclickdetector(clickDetector, distance, event)` — events: `MouseClick`, `RightMouseClick`, `MouseHoverEnter`, `MouseHoverLeave` (default `distance = 0.0`, `event = "MouseClick"`)
- Added `fireproximityprompt(prompt)`
- Fixed `RemoteFunction` in Remote Spy

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