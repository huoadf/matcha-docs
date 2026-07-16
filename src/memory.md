{% hint style="warning" %}
You must allow unsafe LuaU execution before using these functions
{% endhint %}

## Memory Types

<table><thead><tr><th valign="middle">Memory Types</th><th>Returns</th></tr></thead><tbody><tr><td valign="middle">int</td><td>int</td></tr><tr><td valign="middle">float</td><td>number</td></tr><tr><td valign="middle">double</td><td>number</td></tr><tr><td valign="middle">byte</td><td>int</td></tr><tr><td valign="middle">string</td><td>string</td></tr><tr><td valign="middle">uintptr_t</td><td>int</td></tr></tbody></table>

## getbase

```lua
function getbase(): int
```

Returns the base address of the `RobloxPlayerBeta.exe` module as a number (e.g. `140698037846016`) — the anchor for turning module offsets into absolute addresses.

## memory_write

```lua
memory_write(memoryType: string, address: int, value: Any): nil
```

Writes `value` to `address`, interpreting it as `memoryType` — the same type set as `memory_read` (`int`, `float`, `double`, `byte`, `string`, `uintptr_t`). Returns nothing.

{% hint style="danger" %}
Ensure the address and value type are correct before writing; a write to the wrong address can crash Roblox.
{% endhint %}

## memory_read

```lua
memory_read(memoryType: string, address: int): Any
```

Reads the value of type `memoryType` at `address` (see the **Memory Types** table). `byte` is 0–255, `int` a signed 32-bit integer, `uintptr_t` an unsigned 64-bit value, and `float`/`double` reinterpret the raw bytes. Reading an unmapped address safely returns `0`. The `string` type reads bytes until the first non-printable one (no length argument).