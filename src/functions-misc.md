## run_secure

```lua
function run_secure(text: string)
```

Runs protected code. `text` must be a **base64-encoded protected payload** — passing plain Lua source raises `Invalid base64 encoded data - Size not divisible by 4`. Since the protection tooling isn't public, this function isn't usable with ordinary scripts.

{% hint style="warning" %}
Code protection is not available to the public.
{% endhint %}

## Set Fast Flag

```lua
function setfflag(FFlag: string, value: string)
```

Intended to set the fast flag `FFlag` to `value`. Marked incomplete (below) — setting a flag has no effect that `getfflag` can read back.

{% hint style="danger" %}
This function is not complete.
{% endhint %}

## Get Fast Flag

```lua
function getfflag(FFlag: string): number
```

Intended to read the fast flag `FFlag`, but currently a stub — it returns `0` for every flag, real or not.

{% hint style="danger" %}
This function is not complete.
{% endhint %}

## require

```lua
function require(path: string): table
```

Loads a `.lua` / `.luau` module by path. The extension is required and validated — `require("mod")` raises `File has no extension`, and any other extension raises `Unsupported file extension: .x`.

{% hint style="warning" %}
`require` resolves from its own module root, **separate from the `writefile`/`readfile` workspace** — a file that `isfile` confirms exists is still reported `Module file does not exist`, so you can't `writefile` a module and `require` it.
{% endhint %}

## wait

```lua
function wait(time: number)
```

Yields the current thread for `time` seconds. Returns nothing — unlike Roblox's `wait`, which returns the elapsed time.

## spawn

```lua
function spawn(target: function): nil
```

Runs `target` on a new thread; its body executes right away.

## task.spawn

```lua
function task.spawn(target: function): nil
```

Runs `target` immediately on a new thread (synchronously — code after the call waits until `target` yields).

{% hint style="info" %}
`task.spawn` does not forward extra arguments to `target`; use a closure: `task.spawn(function() myFunc(arg) end)`.
{% endhint %}

## task.defer

```lua
function task.defer(target: function): nil
```

Intended to defer `target` to the next cycle, but in the current build the callback **never runs** (a no-op). Use `task.spawn` instead.

## task.delay

```lua
function task.delay(time: number, target: function): nil
```

Intended to run `target` after `time` seconds, but in the current build the callback **never runs** (a no-op, like `task.defer`). For delayed work, use `wait(time)` inside a `task.spawn`'d thread.

## task.wait

```lua
function task.wait(time: number?)
```

Yields the current thread for `time` seconds, or until the next frame if `time` is omitted. Returns nothing — unlike Roblox's `task.wait`, which returns the elapsed time.