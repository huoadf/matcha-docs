# Game Features & Combat Systems

Documentation for Matcha's built-in visuals, combat engine features, and game-specific support modules (Overkill, Temu Rivals, etc.).

---

## Combat & Targeting Systems

### Silent Aim
Matches player target trajectory silently without overriding the camera CFrame.
* **Hitchance Configuration**: Configurable integer percentage (`1` to `100`).
* **Target Bone Selection**: Supports `Head`, `Torso`, or `Nearest` bone targeting.
* **Team Check**: Toggles filtering out players on the same team as `LocalPlayer`.
* **Keybind Modes**: Supports `hold`, `toggle`, `click`, and `always` activation modes.

```lua
-- Example using UI Binding
aim:Toggle("aim_silent", "Silent Aim")
aim:SliderInt("aim_hc", "Hitchance", 1, 100, 85)
aim:Combo("aim_bone", "Hitbox", {"Head", "Torso", "Nearest"}, 0)
```

### Memory Aim (Smooth Aim)
Direct memory-based aiming vector calculations with adjustable smoothness to ensure natural movement.
* **Smoothness Range**: `0.0` (instant snap) to `20.0` (ultra smooth interpolation).
* **FOV Circle**: Independent screen FOV boundary (`10` to `800` pixels).

```lua
aim:SliderFloat("aim_smooth", "Smoothing", 0.0, 20.0, 6.0, "%.1f")
```

---

## Visuals & Engine ESP

### Engine Chams & Glow ESP
Redesigned visual overlay system for player models and world objects.
* **Glow ESP**: Outer model glow outline rendering.
* **Name & Weapon ESP**: Displays player display names, username, and equipped weapon names.
* **Health Bar**: Dynamic health indicator showing current vs max health.
* **Visible Check**: Dual-color configuration for visible vs occluded target parts (`ColorPicker2`).
* **Distance Scaling**: Dynamic box/text size calculations based on distance from `Camera.CFrame.Position`.

```lua
esp:Toggle("esp_vis", "Visible Check")
esp:ColorPicker2("vis_col", {0, 1, 0, 1}, "invis_col", {1, 0, 0, 1})
```

---

## Environment & Lighting Overrides

Matcha allows overriding local rendering parameters **without altering server or game environment state**, preventing server rollback detection.

### Field of View (FOV) Override
Adjusts local `Camera.FieldOfView` without triggering server camera checks or overlapping with game script FOV changes.

### Environment Lighting
Overrides `Lighting.Ambient`, `Lighting.ClockTime` (Time of Day), and `Lighting.ExposureCompensation` locally for full night-vision or full-bright visual control.

```lua
local Lighting = game:GetService("Lighting")
Lighting.ClockTime = 12 -- Force noon locally
Lighting.Ambient = Color3.fromRGB(255, 255, 255) -- Full-bright
```

---

## Supported Games Matrix

| Game Title | Supported Features | Status |
| :--- | :--- | :---: |
| **Temu Rivals** | Silent Aim, Name, Weapon ESP, Team Check, Memory Aim | ✅ Supported |
| **Overkill** | Engine Chams, Silent Aim, Team Check, Recoil Reduction | ✅ Supported |
| **Generic Roblox Games** | Universal ESP, Box ESP, Memory Aim, Lighting Overrides, UI Binding | ✅ Supported |
