This is the documentation for the Matcha LuaVM.

{% hint style="info" %}
Matcha **is not an executor** — it does not hook any functions in the Roblox engine. Instead it emulates them externally, which makes it completely undetected, but also means it has no direct access to internal Roblox API functions.
{% endhint %}

{% hint style="success" %}
**New (Jul 20 2026):** Matcha now features a built-in **Remote Spy** in Hybrid mode! You can also invoke remote methods programmatically using `FireServer` and `InvokeFunction`.
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

## Resources

To understand how the LuaVM works, you first need the basics of Lua(U). For that, visit <https://lua.org>.