## Console

### print / printl

```lua
function print(...)
```

Prints its arguments to the console, space-separated. `printl` behaves identically.

### warn

```lua
function warn(...)
```

Prints its arguments as a yellow, warning-styled line, space-separated.

### error

```lua
function error(...)
```

Prints its arguments as a red, error-styled line; returns `nil`.

{% hint style="danger" %}
Despite the name, `error` does **not** raise an error or halt execution — it only prints. To raise a `pcall`-catchable error, use `assert(false, message)`.
{% endhint %}

### errorl

```lua
function errorl(...)
```

Identical to `error` — a red, error-styled console line. The error-level counterpart to `warn`.



## Input

List of key codes can be found here: <https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes>

### setrobloxinput

```lua
function setrobloxinput(state: boolean): nil
```

Toggles whether Matcha's injected input is sent to the game.

### isrbxactive

```lua
function isrbxactive(): boolean
```

Returns `true` while the Roblox window is the active (foreground) window.

### setclipboard

```lua
function setclipboard(value: string): nil
```

Copies `value` to the system clipboard.

### keypress

```lua
function keypress(keycode: int): boolean
```

Sends a key-down for `keycode` — a Windows virtual-key code (e.g. `0x41` = `A`). Pair with `keyrelease` to release it. Returns `true`.

### keyrelease

```lua
function keyrelease(keycode: int): boolean
```

Sends a key-up for `keycode`. Returns `true`.

### iskeypressed

```lua
function iskeypressed(keycode: int): boolean
```

Returns `true` while the key for `keycode` (Windows VK code) is currently held. Reads live keyboard state.

### ismouse1pressed

```lua
function ismouse1pressed(): boolean
```

Returns `true` while the left mouse button is currently held.

### ismouse2pressed

```lua
function ismouse2pressed(): boolean
```

Returns `true` while the right mouse button is currently held.

### mouse1press

```lua
function mouse1press(): nil
```

Presses and holds the left mouse button.

### mouse1release

```lua
function mouse1release(): nil
```

Releases the left mouse button.

### mouse1click

```lua
function mouse1click(): nil
```

Performs a full left click (press + release).

### mouse2press

```lua
function mouse2press(): nil
```

Presses and holds the right mouse button.

### mouse2release

```lua
function mouse2release(): nil
```

Releases the right mouse button.

### mouse2click

```lua
function mouse2click(): nil
```

Performs a full right click (press + release).

### mousemoveabs

```lua
function mousemoveabs(x: int, y: int): nil
```

Moves the cursor to the absolute pixel position `(x, y)` in the Roblox viewport's coordinate space — origin top-left, the same space as `Camera.ViewportSize` and `WorldToScreen`. A `WorldToScreen` result can be fed straight in.

### mousemoverel

```lua
function mousemoverel(x: int, y: int): nil
```

Moves the cursor by a relative offset `(x, y)` in pixels from its current position.

### mousescroll

```lua
function mousescroll(amount: int): nil
```

Scrolls the mouse wheel by `amount`; the sign sets the direction.