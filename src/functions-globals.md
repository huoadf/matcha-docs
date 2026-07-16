## loadstring / load

```lua
function loadstring(chunk: string, chunkname: string?): function
function load(chunk: string, chunkname: string?): function
```

Compiles `chunk` into a callable function (`load` is equivalent for string chunks).

{% hint style="warning" %}
Two Matcha-specific differences: a syntax error still returns a function (the error only prints when the function is called — never `nil` + message, so it isn't catchable), and a chunk's top-level `return` values are dropped (`loadstring("return 5")()` yields nothing — pass results out via globals).
{% endhint %}

## decompile

```lua
function decompile(script: Instance): string
```

Returns the decompiled source of `script` (a `LocalScript`, `ModuleScript`, or `Script`) as a string. If decompilation fails, an error message is printed to the console.

## WorldToScreen

```lua
function WorldToScreen(position: Vector3): (Vector2, boolean)
```

Projects a 3D world `position` into 2D screen space. Returns the screen position in **pixels** (top-left origin) and a boolean that is `true` when the point is on screen; off screen or behind the camera returns `(0, 0)` and `false`.

```lua
local pos, onScreen = WorldToScreen(part.Position)
if onScreen then
    -- pos.X, pos.Y are valid pixel coordinates
end
```

## notify

```lua
function notify(message: string, title: string, duration: number)
```

Shows a Matcha notification with the given message, title, and duration (seconds). Returns nothing.

## identifyexecutor

```lua
function identifyexecutor(): (string, string)
```

Returns **two** strings — the executor name (`"Matcha"`) and its version (e.g. `"1.0.0"`).

## getscripthash

```lua
function getscripthash(script: Instance): string
```

Returns the FNV-1a 64-bit hash of `script`'s bytecode, as a decimal string (e.g. `"9950850631277792934"`).

## getgamename

```lua
function getgamename(): string
```

Returns the name of the current place (e.g. `"Baseplate"`). This is the place title, distinct from `game.Name`.

## getscripts

```lua
function getscripts(): { Instance }
```

Returns an array of every loaded script instance (`LocalScript`, `ModuleScript`, `Script`) — a large list on a real place.

## getscriptbytecode

```lua
function getscriptbytecode(script: Instance): string
```

Returns the raw compiled bytecode of `script` as a binary string.

## base64encode

```lua
function base64encode(data: string): string
```

Encodes `data` to a standard Base64 string.

{% hint style="warning" %}
`data` is treated as null-terminated: encoding **stops at the first `\0` byte** (`base64encode("a\0b")` encodes only `"a"`). Base64 here is therefore not safe for arbitrary binary that may contain null bytes.
{% endhint %}

## base64decode

```lua
function base64decode(data: string): string
```

Decodes a Base64 string back to the original bytes. `base64decode("")` returns `""`.

## GetPingValue

```lua
function GetPingValue(): number
```

Returns the current ping value (latency to the server) in milliseconds.

## tick

```lua
function tick(): number
```

Returns a high-precision time in seconds, advancing in real time. It's a **monotonic clock**, not a Unix timestamp like Roblox's `tick` — use it for measuring elapsed time.

## typeof

```lua
function typeof(value: any): string
```

Like `type`, but returns the specific name for Roblox datatypes and objects (`Vector3`, `CFrame`, `Instance`, `Drawing`, …) instead of `userdata`.

## getfenv

```lua
function getfenv(target: function | number): table
```

Returns an environment table. With no argument, `0`, or `1`, it returns the global environment (`_G`). Passing a function returns that function's environment (which differs from `_G` only if it was changed with `setfenv`).

## setfenv

```lua
function setfenv(f: function, env: table): function
```

Sets the environment of function `f` to `env` and returns `f`. Global lookups inside `f` are then resolved from `env` instead of `_G`.

```lua
local sandbox = { print = print }
setfenv(f, sandbox) -- f now only sees `sandbox` as its globals
```


## getrbxversion

```lua
function getrbxversion(): string
```

Returns the current Roblox client version (e.g. `"0.635.0.6350567"`).


## gethwid

```lua
function gethwid(): string
```

Returns the unique hardware identifier (HWID) of the current machine.