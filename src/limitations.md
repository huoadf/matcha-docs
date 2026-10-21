# VM Limitations & API Differences

Matcha is an **external LuaVM emulator** — it does not inject into or hook Roblox engine memory functions directly. This design guarantees **100% undetected execution**, but introduces specific differences and limitations compared to internal executors or standard Luau environment behavior.

AI coding assistants and script authors should keep these rules in mind when writing code for Matcha.

---

## Key Differences & Unsupported Features

### 1. No `Instance.new()`
- Matcha cannot instantiate new Roblox engine objects externally.
- **Workaround:** Clone existing instances in the hierarchy or manipulate existing objects.

### 2. No `game:HttpGet()` or `game:HttpPost()`
- Engine HTTP methods on `game` are not directly hooked.
- **Workaround:** Use Matcha's native global functions: `httpget(url)` and `httppost(url, data, contentType)`.

### 3. Syntax Errors in `loadstring` Are Not Catchable
- In standard Luau, `loadstring("invalid syntax")` returns `nil, "error message"`.
- In Matcha, `loadstring()` **always returns a function**. Syntax errors are printed to the console only when the returned function is executed.
- Top-level `return` statements in `loadstring("return 5")()` drop return values — pass results out via global variables.

### 4. `RunService.Stepped` Callback Arguments
- Standard Roblox `Stepped` event passes `(time, deltaTime)`.
- In Matcha, `Stepped` passes **only `deltaTime`** as a single argument: `RunService.Stepped:Connect(function(deltaTime))`

### 5. `base64encode` Null-Byte Truncation
- `base64encode(data)` stops processing at the first `\0` null byte.
- Do not use `base64encode` for arbitrary binary data containing null bytes.

### 6. Instance Comparison (Updated Aug 6 2026)
- Comparing instances using `==` **is fully supported** (`instA == instB`).
- You no longer need to compare `.Address` manually.

### 7. Remote Event & RemoteFunction Handling (Pro ::pro::)
- `RemoteEvent:FireServer(...)` is fully supported in Hybrid mode.
- `RemoteFunction:InvokeServer(...)` and `RemoteFunction:InvokeFunction(...)` are both fully supported in Hybrid mode (Fixed Sep 11 2026, Remote Spy logging fixed Oct 21 2026).

### 8. Hybrid Interactions (Pro ::pro:: - Added Oct 21 2026)
- `firetouchinterest(origin_part, target_part, state)`: Direct native touch simulation (`0 = Touch`, `1 = Untouch`).
- `fireclickdetector(clickDetector, distance, event)`: Simulates `MouseClick`, `RightMouseClick`, `MouseHoverEnter`, `MouseHoverLeave`.
- `fireproximityprompt(prompt)`: Instantly fires ProximityPrompts bypassing hold durations.

---

## Compatibility Quick Reference Table

| Feature / Pattern | Supported in Matcha? | Replacement / Workaround |
| :--- | :---: | :--- |
| `Instance.new()` | ❌ No | Clone existing instances |
| `game:HttpGet()` | ❌ No | Use `httpget(url)` |
| `loadstring()` | ⚠️ Partial | Top-level returns drop; errors print on call |
| `Stepped` event | ⚠️ Partial | Receives 1 arg (`deltaTime`) instead of 2 |
| `base64encode()` | ⚠️ Partial | Truncates at first `\0` byte |
| `inst1 == inst2` | ✅ Yes | Direct comparison supported |
| `GetAttribute()` | ✅ Yes | Supported (Fixed Aug 6) |
| `SetAttribute()` | ✅ Yes | Supported (Fixed Aug 6) |
| `RemoteEvent:FireServer` | ✅ Yes | Supported ::pro:: |
| `RemoteFunction:InvokeServer` | ✅ Yes | Supported ::pro:: (Fixed Sep 11, Spy fixed Oct 21) |
| `firetouchinterest` | ✅ Yes | Supported ::pro:: (Added Oct 21) |
| `fireclickdetector` | ✅ Yes | Supported ::pro:: (Added Oct 21) |
| `fireproximityprompt` | ✅ Yes | Supported ::pro:: (Added Oct 21) |
