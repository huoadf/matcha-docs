# UI Binding (Menu Binding)

Create custom menu tabs, widgets, sections, and hotkey keybinds directly from Lua scripts in Matcha.

> **Source / Script Hub:** [MatchaScripts Repository](https://github.com/cconstellation/MatchaScripts)

---

## Overview

The `UI` global library allows you to build custom menu interfaces that integrate directly into the Matcha UI overlay.

```lua
UI.AddTab("My Script", function(tab)
    local sec = tab:Section("Settings", "Left")
    sec:Toggle("enabled", "Enabled")
    sec:Keybind("enabled_kb", 0x46, "hold")
    sec:SliderInt("range", "Range", 1, 5000, 2000)
end)
```

---

## Global Functions

### `UI.AddTab`

```lua
UI.AddTab(name: string, fn: function)
```

Creates a custom tab with `name`. The callback function `fn(tab)` runs every frame to render and update the tab contents.

### `UI.RemoveTab`

```lua
UI.RemoveTab(name: string)
```

Removes a tab by name.

### `UI.GetValue`

```lua
UI.GetValue(id: string): any
```

Reads the current value of a widget with `id` from anywhere in your script.

### `UI.SetValue`

```lua
UI.SetValue(id: string, value: any)
```

Sets the value of a widget with `id` programmatically.

```lua
while true do
    if UI.GetValue("aim_on") then
        local fov = UI.GetValue("aim_fov")
        -- Aimbot logic here...
    end
    wait()
end
```

---

## Sections

Sections are created from the `tab` object and arrange widgets into standard two-column layouts (`"Left"` or `"Right"`).

```lua
tab:Section(name: string, side: string) -> Section
tab:Section(name: string, side: string, pages: table) -> Section (tabbed)
tab:Section(name: string, side: string, pages: table, max_height: number) -> Section (scrollable)
```

### Tabbed & Scrollable Sections

Passing an array of page names turns a section into a tabbed card container. You can check `sec.page` to render specific widgets on specific pages.

```lua
local sec = tab:Section("Aimbot", "Left", {"Main", "Advanced"}, 400)

if sec.page == 0 then
    -- Main page widgets
elseif sec.page == 1 then
    -- Advanced page widgets
end
```

*Note: Sections close automatically when a new section definition begins.*

---

## Widgets

Every widget method returns an object that you can store to access properties or call methods on.

```lua
local toggle = sec:Toggle("aim_on", "Enabled")
toggle.value            -- current boolean value
toggle:GetValue()       -- gets fresh value
toggle:SetValue(true)   -- updates value programmatically
```

All widgets accept an optional `callback` function as their last argument.

### Toggle

```lua
sec:Toggle(id: string, label: string [, default: boolean] [, callback: function]) -> Widget
```

```lua
sec:Toggle("aim_on", "Aimbot", function(state)
    print("Aimbot: " .. tostring(state))
end)

sec:Toggle("team_check", "Team Check", true)
```

---

### Keybind

Must be placed directly after a `Toggle` widget. Left-click in the UI to rebind key, right-click to pick execution mode.

```lua
sec:Keybind(id: string [, key: number | Enum.KeyCode] [, type: string]) -> KeybindWidget
```

* **`key`**: Virtual-key (VK) code or `Enum.KeyCode`. Default `0` = unbound.
* **`type`**: Keybind mode — `"toggle"`, `"hold"`, `"always"`, or `"click"`.

```lua
sec:Toggle("aim_on", "Aimbot")
local kb = sec:Keybind("aim_kb", 0x46, "hold")  -- F key, hold mode
-- Or with Enum:
-- local kb = sec:Keybind("aim_kb", Enum.KeyCode.F, "hold")
```

#### KeybindWidget Methods & Properties

| Method / Property | Description |
| :--- | :--- |
| `.value` / `:IsEnabled()` | Returns `true` if keybind is currently active |
| `:GetKey()` | Returns current VK code / `Enum.KeyCode` |
| `:SetKey(vk)` | Rebinds the key |
| `:GetKeyName()` | Returns key label string (e.g. `"f"`, `"lmb"`, `"none"`) |
| `:GetType()` | Returns current mode (`"toggle"`, `"hold"`, `"always"`, `"click"`) |
| `:SetType(typeStr)` | Changes keybind mode |
| `:AddToHotkey(label, toggle_id)` | Displays keybind in on-screen hotkey overlay when `toggle_id` is ON |
| `:RemoveFromHotkey()` | Removes keybind from hotkey overlay |

#### Key Codes Reference

* **VK Codes:** `0x01` LMB · `0x02` RMB · `0x04` MMB · `0x05` X1 · `0x06` X2 · `0x41`–`0x5A` (A–Z)
* **Enum.KeyCode:** `Enum.KeyCode.MouseButton1` · `Enum.KeyCode.MouseButton2` · `Enum.KeyCode.MouseButton3` · `Enum.KeyCode.A`–`Enum.KeyCode.Z`

---

### SliderInt

```lua
sec:SliderInt(id: string, label: string, min: number, max: number [, default: number] [, callback: function]) -> Widget
```

```lua
sec:SliderInt("fov", "FOV Size", 10, 800, 180, function(val)
    print("FOV:", val)
end)
```

---

### SliderFloat

```lua
sec:SliderFloat(id: string, label: string, min: number, max: number [, default: number] [, format: string] [, callback: function]) -> Widget
```

```lua
sec:SliderFloat("smooth", "Smoothing", 0.1, 20.0, 6.0, "%.1f", function(val)
    print("Smooth:", val)
end)
```

---

### Combo (Dropdown)

```lua
sec:Combo(id: string, label: string, items: table [, default: number] [, callback: function]) -> ComboWidget
```

```lua
local c = sec:Combo("hitbox", "Target", {"Head", "Torso", "Nearest"}, 0, function(idx, text)
    print("Target:", text)
end)
```

#### ComboWidget Methods

| Method | Description |
| :--- | :--- |
| `c:Add(item: string)` | Appends a new item option |
| `c:Remove(item: string)` | Removes an item option |
| `c:Clear()` | Removes all item options |
| `c:GetItems()` | Returns table of all item strings |
| `c:GetText()` | Returns string of currently selected option |
| `c:SetValue(index: number)` | Selects item at 0-based index |

---

### Button

```lua
sec:Button(label: string [, callback: function])
sec:Button(label: string, width: number, height: number [, callback: function])
```

```lua
sec:Button("Reset All", function()
    UI.SetValue("aim_on", false)
    UI.SetValue("fov", 180)
end)
```

---

### ColorPicker

Must be placed directly after a `Toggle` widget. Callback receives `(Color3, alpha)`.

```lua
sec:ColorPicker(id: string [, r: number, g: number, b: number, a: number] [, callback: function]) -> Widget
```

```lua
sec:Toggle("box_on", "Box ESP")
sec:ColorPicker("box_col", 1, 0, 0, 1, function(color, alpha)
    print("Color RGB:", color.R, color.G, color.B, "Alpha:", alpha)
end)
```

---

### ColorPicker2 (Dual Color Picker)

Must be placed directly after a `Toggle` widget. Callback receives `(Color3_1, alpha1, Color3_2, alpha2)`.

```lua
sec:ColorPicker2(id1: string, {r, g, b, a}, id2: string, {r, g, b, a} [, callback: function])
```

```lua
sec:Toggle("vis_check", "Visible Check")
sec:ColorPicker2("vis_col", {0, 1, 0, 1}, "invis_col", {1, 0, 0, 1}, function(c1, a1, c2, a2)
    print("Visible R:", c1.R, "Invisible R:", c2.R)
end)
```

---

### InputText

Callback triggers when the input field loses focus (Enter, Escape, or clicking away).

```lua
sec:InputText(id: string, label: string [, default: string] [, callback: function]) -> Widget
```

```lua
sec:InputText("webhook", "Webhook URL", "", function(text)
    print("Saved Webhook:", text)
end)
```

---

### Text · Tip · Spacing

```lua
sec:Text("Label text")
sec:Tip("Tooltip shown on the right side of previous widget")
sec:Spacing()
```

---

## Widget Summary & Callbacks

| Widget | Value Type | Callback Arguments | When Triggered |
| :--- | :--- | :--- | :--- |
| **Toggle** | `boolean` | `state` | Toggled |
| **SliderInt** | `integer` | `value` | Dragging slider |
| **SliderFloat** | `float` | `value` | Dragging slider |
| **Combo** | `integer` (0-based) | `index, text` | Option selected |
| **Button** | N/A | None | Clicked |
| **ColorPicker** | `Color3, alpha` | `Color3, alpha` | Color changed |
| **ColorPicker2** | `Color3, a, Color3, a` | `c1, a1, c2, a2` | Either color changed |
| **InputText** | `string` | `text` | Field loses focus |
| **Keybind** | `boolean` | N/A | Key state change |

---

## Complete Examples

### 1. Full Aimbot + ESP Menu

```lua
UI.AddTab("Script", function(tab)
    local aim = tab:Section("Aimbot", "Left", {"Targeting", "Silent"})

    if aim.page == 0 then
        aim:Toggle("aim_on", "Enabled")
        local kb = aim:Keybind("aim_kb", 0x02, "hold")
        kb:AddToHotkey("Aimbot", "aim_on")

        aim:Toggle("aim_tc", "Team Check", true)
        aim:Tip("Ignores teammates")
        aim:Combo("aim_bone", "Hitbox", {"Head", "Torso", "Nearest"}, 0)
        aim:SliderInt("aim_fov", "FOV", 10, 800, 180)
        aim:SliderFloat("aim_smooth", "Smoothing", 0.0, 20.0, 6.0, "%.1f")

    elseif aim.page == 1 then
        aim:Toggle("aim_silent", "Silent Aim")
        local skb = aim:Keybind("aim_skb", 0x04, "hold")
        skb:AddToHotkey("Silent Aim", "aim_silent")
        aim:SliderInt("aim_hc", "Hitchance", 1, 100, 85)
    end

    local gun = tab:Section("Weapon", "Left")
    gun:Toggle("gun_norecoil", "No Recoil")
    gun:Toggle("gun_nospread", "No Spread")
    gun:Toggle("gun_infammo", "Infinite Ammo")

    local esp = tab:Section("ESP", "Right")
    esp:Toggle("esp_on", "Enabled")
    local ekb = esp:Keybind("esp_kb")
    ekb:AddToHotkey("ESP", "esp_on")

    esp:Toggle("esp_box", "Box")
    esp:ColorPicker("esp_boxcol", 1, 0, 0, 1)
    esp:Toggle("esp_vis", "Visible Check")
    esp:ColorPicker2("vis_col", {0,1,0,1}, "invis_col", {1,0,0,1})
    esp:Toggle("esp_name", "Name")
    esp:Toggle("esp_hp", "Health Bar")
    esp:SliderInt("esp_dist", "Distance", 100, 20000, 8000)

    local misc = tab:Section("Misc", "Right")
    misc:InputText("webhook", "Webhook", "", function(text)
        print("Webhook: " .. text)
    end)
    misc:Button("Reset", function()
        UI.SetValue("aim_on", false)
        UI.SetValue("aim_smooth", 6.0)
        UI.SetValue("esp_on", false)
        UI.SetValue("esp_dist", 8000)
    end)
end)
```

### 2. Widget Object Manipulation

```lua
UI.AddTab("Demo", function(tab)
    local sec = tab:Section("Objects", "Left")

    local t = sec:Toggle("demo_t", "Toggle")
    local k = sec:Keybind("demo_k", 0x46, "toggle")
    local s = sec:SliderInt("demo_s", "Slider", 0, 100, 50)
    local c = sec:Combo("demo_c", "Combo", {"A", "B", "C"})
    local i = sec:InputText("demo_i", "Input", "hello")

    local actions = tab:Section("Actions", "Right")

    actions:Button("Read All", function()
        print("toggle: " .. tostring(t.value))
        print("slider: " .. s:GetValue())
        print("combo: " .. c:GetText() .. " [" .. c.value .. "]")
        print("input: " .. i.value)
        print("key: " .. k:GetKeyName() .. " [" .. k:GetType() .. "]")
        print("active: " .. tostring(k:IsEnabled()))
    end)

    actions:Button("Write All", function()
        t:SetValue(true)
        s:SetValue(75)
        c:SetValue(2)
        i:SetValue("world")
        k:SetKey(0x47)
        k:SetType("hold")
    end)

    actions:Button("Combo Items", function()
        c:Add("D")
        c:Remove("A")
        local items = c:GetItems()
        for idx, name in ipairs(items) do
            print(idx .. ": " .. name)
        end
    end)
end)
```
