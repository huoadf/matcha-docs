# Changelogs

Keep track of all the latest updates, fixes, and new features added to the Matcha Executor and Lua VM.

---

## Aug 6 2026
**Version:** `d584fb6c717a43d9`

**General & Fixes**
- Fixed Auth launch issue.
- Fixed Position Fly.
- Optimized performance for low-end PCs.
- Fixed Playerlist *(Aug 1)*.

**Lua VM**
- Comparing `Instance`s no longer requires using `.Address` (direct `==` comparison is now supported).
- Fixed `Instance:GetAttribute()` and `Instance:SetAttribute()`.
- Fixed `TextLabel.Text` property assignments.
- Fixed `GuiObject.AbsoluteSize` & `GuiObject.AbsolutePosition`.
- Fixed Decompiler stability and output.

**Pro (Early Access)**
- Added **AI Agent & MCP integration** into Lua U (currently in testing).
  - *Antigravity users can now add Matcha to their `mcp_config.json` via `http://127.0.0.1:8765/mcp`.*

---

## Jul 29 2026

**UI Redesign**
- Redesigned Target HUD, Lag Notifier, Explorer List, Popup UI, Slider, and Dropdown.
- Redesigned Lua VM UI layout.
- Added exclusive **Glass Design** (for Watermark, Hotkeys, Notification, and Array List).
- Added Glass UI to Options (Windows 11 Only).
- Added animations for most UI elements.
- New Loading Screen design (no longer blocks input).

**Visuals**
- Redesigned Glow for ESP.
- Redesigned Name Background.

**General**
- Fixed ESP and Aim not working on certain games.
- Removed Script Hub (outdated).
- Removed silent launch stream-proof by default due to NVIDIA conflicts (will return as a toggleable option later).

---

## Jul 20 2026

**Hybrid Mode**
- Added **Remote Spy**.
- Added `RemoteEvent:FireServer()` and `RemoteFunction:InvokeFunction()` support.

---

## Jul 17 2026

**Fixes**
- Fixed Auth Issues.
- Fixed in-game input detection.

**Lua VM additions**
- Added `Workspace:Raycast`.
- Native support for `Ray`, `UDim`, and `UDim2`.
- Added `getrbxversion()`.
- Added `gethwid()`.
- Added `Camera.CFrame`.
- Added `Drawing.Fonts.ProximaSoftBold`.

**Misc**
- You can now interact with Music UI without having the main UI open.

---

## Jul 1 2026
**Version:** `5cf2272675e145f5`

**General**
- Now using Camera FOV and Lighting (Ambient, ClockTime, Exposure) independently without overlapping with the game environment.
- Redesigned Watermark.

**Game Support (Overkill)**
- Added Silent Aim (Temu Rivals).
- Added Name & Weapon ESP support.
- Added Team Check Support.
- Added Engine Chams Support.
- Added Memory Aim (Works with smoothness).

**Lua VM**
- Added `Player.UserId` property.
