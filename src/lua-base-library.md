Matcha runs on a Luau-based VM, so the standard Lua(U) global functions are available and behave per the [Lua 5.1 reference](https://www.lua.org/manual/5.1/) **except** where noted below. This page lists what the VM actually exposes and flags the Matcha-specific differences — it does not re-document standard Lua semantics.

## Type & conversion

### type

```lua
function type(value: any): string
```

Standard. Roblox datatypes (`Vector3`, `CFrame`, …) and Instances all report as `"userdata"` — use `typeof` for the specific name.

### tostring

```lua
function tostring(value: any): string
```

Standard, and honors `__tostring`. Matcha formats Roblox datatypes differently from Roblox itself — `tostring(Vector3.new(1, 2, 3))` returns `"Vector3(1.0000, 2.0000, 3.0000)"`, not `"1, 2, 3"`.

### tonumber

```lua
function tonumber(value: any, base: number?): number?
```

Standard. Trims surrounding whitespace, parses `0x` hex, and accepts a `base` (2–36) — `tonumber("ff", 16)` returns `255`. Returns `nil` if the value can't be parsed.

## Iteration & varargs

### pairs / ipairs / next

```lua
function pairs(t: table): (function, table, any)
function ipairs(t: table): (function, table, number)
function next(t: table, key: any?): (any, any)
```

Standard iteration; `ipairs` stops at the first `nil` hole.

{% hint style="warning" %}
`pairs` does **not** honor the Luau `__iter` metamethod — it always iterates the raw table.
{% endhint %}

### select

```lua
function select(n: number | "#", ...): ...
```

Standard, including **negative indices**: `select(-1, ...)` returns the last argument.

### unpack

```lua
function unpack(t: table, i: number?, j: number?): ...
```

Returns `t[i]` through `t[j]` (defaults `i = 1`, `j = #t`). Exposed as a **global** — mainline Luau only provides `table.unpack`. `unpack` and `table.unpack` are separate function objects but behave identically.

## Errors & protected calls

### assert

```lua
function assert(value: any, message: string?, ...): ...
```

Raises a catchable error (`Matcha:<line>: <message>`, or `assertion failed!` with no message) if `value` is falsy; otherwise returns its arguments unchanged — the way to raise a catchable error in Matcha.

### pcall

```lua
function pcall(f: function, ...): (boolean, ...)
```

Standard. Returns `true` plus `f`'s results on success, or `false, "Matcha:<line>: <message>"` on a runtime fault.

### xpcall

```lua
function xpcall(f: function, handler: function, ...): (boolean, ...)
```

Standard, and **forwards extra arguments to `f`** (Luau-style): `xpcall(fn, handler, 3, 4)` calls `fn(3, 4)`. On a real error, `handler` runs with the error message.

## Metatables

### setmetatable / getmetatable

```lua
function setmetatable(t: table, mt: table?): table
function getmetatable(t: any): table | any
```

Standard. `getmetatable` returns the `__metatable` field when set; `setmetatable` on a table with a protected (`__metatable`) metatable raises `cannot change a protected metatable`.

### newproxy

```lua
function newproxy(addMetatable: boolean?): userdata
```

Lua 5.1 holdover, fully supported. Returns a blank `userdata`; with `newproxy(true)` it gets a fresh, settable metatable (retrieved via `getmetatable`), so metamethods like `__index` and `__tostring` work.

## Raw access

### rawget / rawset / rawequal / rawlen

```lua
function rawget(t: table, key: any): any
function rawset(t: table, key: any, value: any): table
function rawequal(a: any, b: any): boolean
function rawlen(t: table | string): number
```

Standard. These bypass metamethods; `rawset` returns the table.

## Memory

### gcinfo

```lua
function gcinfo(): number
```

Returns the VM's current memory usage in kilobytes.