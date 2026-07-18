The `UI` global library allows you to create custom menu tabs, sections, and interactive widgets (like toggles, keybinds, and sliders) directly from your Lua scripts.

Using these functions, you can build custom graphical interfaces that integrate seamlessly with the Matcha cheat client.

---

## UI Library API

These functions are available on the global `UI` table:

### `UI.AddTab`
Creates a new menu tab. The callback function `fn(tab)` runs every frame to draw the tab content.
```lua
UI.AddTab(name: string, fn: function)
```
```lua
UI.AddTab("My Script", function(tab)
    -- Create sections and widgets here
end)
```

### `UI.RemoveTab`
Removes a tab by name.
```lua
UI.RemoveTab(name: string)
```

### `UI.GetValue`
Reads the current value of any widget by its unique ID. This is useful for reading settings from other threads or scripts.
```lua
UI.GetValue(id: string): any
```
```lua
while true do
    if UI.GetValue("aim_on") then
        local fov = UI.GetValue("aim_fov")
        -- run aimbot logic
    end
    task.wait()
end
```

### `UI.SetValue`
Programmatically changes the value of any widget by ID.
```lua
UI.SetValue(id: string, val: any)
```

---

## Tabs & Sections

The `tab` object passed to `UI.AddTab`'s callback is used to divide your tab into structural sections.

Sections are arranged in two columns: `"Left"` and `"Right"`.

```lua
tab:Section(name: string, side: string) -> Section
tab:Section(name: string, side: string, pages: table) -> Section (tabbed)
tab:Section(name: string, side: string, pages: table, max_height: number) -> Section (scrollable)
```

### Examples:
```lua
-- Simple left-column section
local sec = tab:Section("Settings", "Left")

-- Tabbed section with multiple sub-pages and scrollable height limit
local aimSec = tab:Section("Aimbot", "Left", {"Main", "Advanced"}, 400)
if aimSec.page == 0 then
    -- Draw main aimbot settings
elseif aimSec.page == 1 then
    -- Draw advanced aimbot settings
end
```
> [!NOTE]
> Sections close automatically when a new section starts in the same column.

---

## Widgets

All widget methods return a **Widget object** you can interact with programmatically:
```lua
local toggle = sec:Toggle("aim_on", "Enabled")
print(toggle.value)         -- current value
print(toggle:GetValue())    -- fresh retrieved value
toggle:SetValue(true)       -- programmatically enable
```
Every widget accepts an **optional callback** as its last argument which triggers whenever the widget value changes.

### Toggle
Creates a boolean checkbox.
```lua
sec:Toggle(id: string, label: string [, default: boolean] [, callback: function]) -> Widget
```
```lua
sec:Toggle("aim_on", "Aimbot", false, function(state)
    print("Aimbot toggled: " .. tostring(state))
end)
```

### Keybind
Allows users to bind hotkeys. Place it immediately after a `Toggle` to bind it to that setting.
* **Interaction:** Left-click the widget in the UI to rebind, right-click to choose keybind mode.
```lua
sec:Keybind(id: string [, key: number [, type: string]]) -> KeybindWidget
```

| Argument | Type | Description |
|---|---|---|
| `key` | `number` | Virtual key (VK) code. `0` = unbound. |
| `type` | `string` | Keybind mode: `"toggle"`, `"hold"`, `"always"`, or `"click"`. |

```lua
sec:Toggle("aim_on", "Aimbot")
local kb = sec:Keybind("aim_kb", 0x46, "hold") -- Binds "F" key to Hold mode

-- Automatically shows the keybind in the client hotkey list overlay when active
kb:AddToHotkey("Aimbot", "aim_on")
```

#### KeybindWidget Methods:
* **`:IsEnabled()`** (or `.value`): Returns `true` if the keybind is currently active.
* **`:GetKey()`**: Returns the current virtual key code (`number`) or `Enum.KeyCode` object.
* **`:SetKey(vk: number)`**: Programmatically changes the keybind.
* **`:GetKeyName()`**: Returns a friendly string name for the key (e.g. `"f"`, `"lmb"`, `"none"`).
* **`:GetType()`**: Returns the current mode (`"toggle"`, `"hold"`, `"always"`, `"click"`).
* **`:SetType(type: string)`**: Changes the mode.
* **`:AddToHotkey(label: string, toggle_id: string)`**: Displays in the screen hotkey overlay when the associated toggle is active.
* **`:RemoveFromHotkey()`**: Hides the keybind from the hotkey list.

---

## Virtual Key (VK) Codes & Enums

You can use raw VK hex codes or standard Roblox `Enum.KeyCode` properties when binding keys:

### Virtual Key (VK) Codes
* **Mouse Buttons:** `0x01` (LMB) · `0x02` (RMB) · `0x04` (MMB) · `0x05` (X1 Extra Button) · `0x06` (X2 Extra Button)
* **Keyboard Keys:** `0x41` - `0x5A` (Keys A - Z) · `0x10` (Shift) · `0x11` (Ctrl) · `0x12` (Alt)

### Enum KeyCodes
* `Enum.KeyCode.MouseButton1` (LMB) · `Enum.KeyCode.MouseButton2` (RMB) · `Enum.KeyCode.MouseButton3` (MMB)
* `Enum.KeyCode.A` - `Enum.KeyCode.Z` (Keys A - Z)
