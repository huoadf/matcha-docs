# Changelogs

Keep track of all the latest updates, fixes, and new features added to the Matcha Executor and Lua VM from 2025 to 2026.

---

## Aug 18 2026 — Latest Version
**Version:** `version-ce0bcd0fbd484804`

- Updated to the latest Roblox client version.
- *Run loader to update*

---

## Aug 16 2026
- Fixed **Engine Chams** rendering.

---

## Aug 11 2026
**Version:** `version-ddf602d9cfe44005`

- Updated to the latest Roblox client version.

---

## Aug 6 2026 — Auth Fix
- Fixed Auth *(resolves launch issues)*.

---

## Aug 6 2026 — Lua VM Fixes
**Version:** `version-d584fb6c717a43d9`

**Lua VM**
- Fixed Attributes (`GetAttribute`, `SetAttribute`, `GetAttributes`).
- Fixed `.Text` property reads & assignments.
- Fixed `AbsoluteSize` & `AbsolutePosition`.
- Fixed Decompiler stability & output.

---

## Aug 6 2026 — General Update & MCP Integration
**Version:** `version-d584fb6c717a43d9`

**General**
- Updated to the latest Roblox client version.
- Fixed Position Fly.
- Optimized performance for low-end PCs.
- Comparing instances no longer needs `.Address` — direct `==` comparison is now supported.

**Pro (Early Access)** ::pro::
- Added **AI Agent & MCP integration** into Lua VM (`http://127.0.0.1:8765/mcp`).

---

## Aug 1 2026
- Fixed Playerlist.

---

## Jul 29 2026 — UI & Visuals Overhaul

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
- Removed silent launch stream-proof by default due to NVIDIA conflicts (toggleable option).

---

## Jul 20 2026 — Hybrid Mode & Remotes

**Hybrid Mode** ::pro::
- Added **Remote Spy**.
- Added `RemoteEvent:FireServer()` and `RemoteFunction:InvokeFunction()` support in Lua VM.

---

## Jul 17 2026 — Raycasting & New Datatypes

**Lua VM**
- Added `Workspace:Raycast`.
- Native support for `Ray`, `UDim`, and `UDim2`.
- Added `getrbxversion()`.
- Added `gethwid()`.
- Added `Camera.CFrame`.
- Added `Drawing.Fonts.ProximaSoftBold`.

**Misc**
- Interact with Music UI without having the main UI open.
- Fixed in-game input detection.
- Fixed Auth issues.

---

## Jul 1 2026 — Overkill & Environment Overrides
**Version:** `version-5cf2272675e145f5`

**General**
- Independent local `Camera.FieldOfView` and `Lighting` (Ambient, ClockTime, ExposureCompensation) without overlapping with server game state.
- Redesigned Watermark.

**Game Support (Overkill & Rivals)**
- Added Silent Aim (Temu Rivals).
- Added Name & Weapon ESP support.
- Added Team Check Support.
- Added Engine Chams Support.
- Added Memory Aim (with smoothness interpolation).

**Lua VM**
- Added `Player.UserId` property.

---

## Jun 19 2026 — Attribute Overhaul & Long Strings

**Lua VM**
- Complete rewrite for `GetAttributes`, `SetAttributes`, and `GetAttribute`.
- Added full support for long attribute strings and Color3 attributes.

**General**
- Fixed Rivals Team Check.

---

## Jun 15–18 2026 — Engine Chams & Usermode Redirection

- Added **Engine Chams** and redesigned 3D Radar.
- Added Server Region (Notification & Watermark).
- Added outline to healthbars.
- Fixed Raycast visible check accuracy.
- Added Redirection / Magic to usermode (Windows 10 & 11).
- Optimized Lua UI Binding.
- Added partial Overkill support and fixed `DisplayName`.

---

## Jun 7–10 2026 — Garbage Collection Engine

**Lua VM**
- Introduced structured `getgc()` returns (`.key`, `.value`, `.type`, `.addr`, `.vtt`, `.tbl`).
- Added batch `applygc(cache, {...})` and `setgc({...})`.
- Enabled `RunService`, `getgc`, and `setgc` execution inside `run_secure`.
- Tested Decompiler and improved Teleport Handler.

**General**
- Streamproof loading screen.
- Added Eject keybind, Hitbox Extender keybind, and whitelist.
- Fixed BRM5 (Blackhawk Rescue Mission 5) support.

---

## May 15–27 2026

- Added Theme Presets.
- Added Chat Input detection (preventing keybind activation while typing in chat).
- Improved Teleport Handler (Rivals queuing fix).
- Fixed silent aim crash issues.

---

## Apr 20–30 2026 — Magic Bullet & Operation 1

- Added Magic Bullet & Redirection ::pro::.
- Added **Operation 1** game support.
- Added serversided desync ::pro::.

---

## Apr 2 2026 — Full Math & Network LuaVM Release

**Lua VM**
- Full native implementation for `Vector3` and `CFrame`.
- Added `Drawing.Image` (raw byte image rendering).
- Added `RunService` (`RenderStepped`, `Heartbeat`, `Stepped`).
- Added `game:HttpPost()` and custom request headers for `HttpGet` / `HttpPost`.
- Added `GetPingValue()`.
- Added Unsafe Lua Execution prompt for memory APIs.

**General**
- Added Team tab for custom team whitelisting.

---

## Mar 12–18 2026 — MM2 & UI Integration

- Added Murderer & Sheriff detection with team-role coloring for **Murder Mystery 2**.
- Added Keystrokes overlay.
- Added detachable output console.
- Added UI-Lua integration.
- Resizable Music Player with fullscreen mode and animated backgrounds.

---

## Feb 18–26 2026 — v2 Engine & Combat Upgrade

**Combat & Visuals**
- Added Sticky Aim for Aimbot and Silent Aim.
- Rewrote Triggerbot with improved detection.
- Click TP now displays a 3D hit marker.
- Closest part now auto-switches target parts.
- Added Snaplines from cursor to current target.
- Added Crosshair with static/spinning styles, adjustable segments, and center dots.
- Sliders now accept typed values beyond standard range (uncapped).

**Media Player**
- Music Player support for Apple Music, Spotify, SoundCloud, and YouTube with Arabic font support.

---

## Feb 13 2026 — LuaU 10x Performance Overhaul

- **10x Performance Boost**: Zero-delay UI, auto-parry, and memory reads/writes.
- LuaU drawings now render behind Matcha's UI overlay.
- Added `tick()` monotonic clock to LuaU.
- Expanded LuaU memory allocation limits.
- Added Interrupt callback support.

---

## Feb 1–12 2026 — Skeletons & 3D Bounding Boxes

- Added Out-of-FOV (OOF) distance-scaled directional arrows.
- Added 3D Bounding Boxes.
- Redesigned R6 & R15 Skeleton rendering.
- Added Glow effects for visuals, Aimbot FOV, and Silent Aim FOV.
- Added Chat input detection in Options.
- Added standalone health text attached to Health Bar or Name ESP.
- Fixed Resolver for Phantom Forces prediction.

---

## Jan 18–30 2026 — Multi-Game Silent Aim

- Added Silent Aim support for **Temu Rivals**, **Defuse Division**, **Blox Strike**, and **Jailbreak**.
- Added Sky Changer and Time Changer.
- Fixed Lua `task` library execution.
- Fixed memory leaks and improved ESP rendering performance.

---

## Jan 1 2026 — FPS Slider & Phantom Forces

- Added Lua VM FPS slider in Options.
- Fixed Phantom Forces game support.

---

## Dec 19–23 2025 — LuaVM Events & Script Hub

- **Added Event Signals**: `Players.PlayerAdded`, `Players.PlayerRemoving`, `UserInputService.InputBegan`, `UserInputService.InputEnded`.
- **Added `Enum.KeyCode`** (including `KeyCode.MouseButton1`).
- Added in-game **Script Hub** and built-in script dumper.

---

## Dec 3 2025 — World Lighting & Speed Manipulation

- Moved World Lighting to Visuals with real-time update and Brightness controls.
- Added timer speed manipulation (Interaction & Vehicle Speed Up) ::pro::.

---

## Nov 18–22 2025 — First Major Redesign & Property Fixes

- Added new icon, default theme, and launch console redesign.
- Added wait-for-Roblox launch detection.
- Fixed `AbsoluteSize`, `AbsolutePosition`, Team Color, and Spectate.
- Fixed initial attribute handling.

---

## Oct 30 2025 — Skin Colored Chams

- Added Skin Colored Chams with outline transparency toggles.
- Fixed Lag Notifier.
