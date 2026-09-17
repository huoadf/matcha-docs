This is the documentation for the Matcha LuaVM.

{% hint style="info" %}
Matcha **is not an executor** — it does not hook any functions in the Roblox engine. Instead it emulates them externally, which makes it completely undetected, but also means it has no direct access to internal Roblox API functions.
{% endhint %}

<div class="vault-counter-card" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: linear-gradient(135deg, rgba(140, 198, 63, 0.08) 0%, rgba(18, 22, 18, 0.85) 100%); border: 1px solid rgba(140, 198, 63, 0.35); border-radius: 12px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35); backdrop-filter: blur(8px);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
<div style="display: flex; align-items: center; gap: 0.6rem;">
<span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #8cc63f; box-shadow: 0 0 10px #8cc63f; animation: pulseBeacon 1.8s infinite;"></span>
<strong style="font-size: 1.05rem; color: #fff; letter-spacing: -0.2px;">Live Counter: Waiting for Vault to add to LuaVM</strong>
</div>
<span style="display: inline-flex; align-items: center; font-size: 0.75rem; font-weight: 600; padding: 0.2rem 0.55rem; border-radius: 999px; background: rgba(140, 198, 63, 0.18); color: #8cc63f; border: 1px solid rgba(140, 198, 63, 0.4);">★ PRO HYBRID UPDATE</span>
</div>
<div style="margin: 0 0 1rem 0; font-size: 0.88rem; color: var(--text-muted); line-height: 1.45;">Vault announced incoming Pro Hybrid features within <strong>max 3 days</strong> (announced Sep 13, 11:03 PM): <code style="color:#8cc63f;">fireclickdetector</code>, <code style="color:#8cc63f;">fireproximityprompt</code>, <code style="color:#8cc63f;">firetouchinterest</code>.</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.6rem; max-width: 440px; margin-bottom: 0.85rem;" id="vault-timer-grid">
<div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-days" style="font-size: 1.55rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">0</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Days</div>
</div>
<div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-hours" style="font-size: 1.55rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">00</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Hours</div>
</div>
<div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-mins" style="font-size: 1.55rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">00</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Mins</div>
</div>
<div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 0.4rem; text-align: center;">
<div id="v-secs" style="font-size: 1.55rem; font-weight: 700; font-family: ui-monospace, monospace; color: #8cc63f; line-height: 1;">00</div>
<div style="font-size: 0.68rem; text-transform: uppercase; color: var(--text-muted); margin-top: 0.35rem; font-weight: 600; letter-spacing: 0.5px;">Secs</div>
</div>
</div>
<div id="v-status-note" style="font-size: 0.8rem; color: #e5c07b; display: flex; align-items: center; gap: 0.4rem;">
<span>⏳</span> <span id="v-status-text">Calculating elapsed time since Vault's announcement...</span>
</div>
</div>
<style>
@keyframes pulseBeacon {
0% { transform: scale(0.95); opacity: 0.8; box-shadow: 0 0 4px #8cc63f; }
50% { transform: scale(1.15); opacity: 1; box-shadow: 0 0 14px #8cc63f; }
100% { transform: scale(0.95); opacity: 0.8; box-shadow: 0 0 4px #8cc63f; }
}
</style>
<script>
(function() {
var deadline = new Date("2026-09-16T23:03:00+01:00").getTime();
function updateVaultCounter() {
var now = new Date().getTime();
var dEl = document.getElementById("v-days");
var hEl = document.getElementById("v-hours");
var mEl = document.getElementById("v-mins");
var sEl = document.getElementById("v-secs");
var statusEl = document.getElementById("v-status-text");
if (!dEl || !hEl || !mEl || !sEl) return;
if (now >= deadline) {
var diffOverdue = now - deadline;
var days = Math.floor(diffOverdue / (1000 * 60 * 60 * 24));
var hours = Math.floor((diffOverdue % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var mins = Math.floor((diffOverdue % (1000 * 60 * 60)) / (1000 * 60));
var secs = Math.floor((diffOverdue % (1000 * 60)) / 1000);
dEl.innerText = days;
hEl.innerText = (hours < 10 ? "0" : "") + hours;
mEl.innerText = (mins < 10 ? "0" : "") + mins;
sEl.innerText = (secs < 10 ? "0" : "") + secs;
dEl.style.color = "#f85149";
hEl.style.color = "#f85149";
mEl.style.color = "#f85149";
sEl.style.color = "#f85149";
if (statusEl) {
statusEl.innerHTML = "<strong>Overdue by " + days + "d " + hours + "h " + mins + "m " + secs + "s</strong> — 3-day window elapsed, waiting on Vault!";
}
} else {
var diffRemain = deadline - now;
var days = Math.floor(diffRemain / (1000 * 60 * 60 * 24));
var hours = Math.floor((diffRemain % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var mins = Math.floor((diffRemain % (1000 * 60 * 60)) / (1000 * 60));
var secs = Math.floor((diffRemain % (1000 * 60)) / 1000);
dEl.innerText = days;
hEl.innerText = (hours < 10 ? "0" : "") + hours;
mEl.innerText = (mins < 10 ? "0" : "") + mins;
sEl.innerText = (secs < 10 ? "0" : "") + secs;
if (statusEl) {
statusEl.innerHTML = "Estimated time remaining: <strong>" + days + "d " + hours + "h " + mins + "m " + secs + "s</strong> (3-day max window)";
}
}
}
setInterval(updateVaultCounter, 1000);
updateVaultCounter();
})();
</script>

{% hint style="success" %}
**Changelogs (Sep 15 2026)**
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