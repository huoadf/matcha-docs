This guide explains how to find and modify values held in the game's Lua garbage collector (GC), such as weapon stats, flight speeds, or cooldowns.

In Luau, many games store configuration tables (like gun modules or physics settings) inside local variables or local tables. Because these are tracked by the Lua garbage collector, Matcha's GC functions allow you to scan the collector memory, find these values by name, and modify them directly.

---

## GC Functions Overview

Matcha provides three functions for interacting with the garbage collector:

1. **`getgc`**: Scans the garbage collector and returns matching objects. Since scanning the entire GC is slow, you should run `getgc` **once** at the start of your script and save the results (caching them).
2. **`applygc`**: Updates values inside a previously cached scan. This is extremely fast and can be safely run inside loops or events.
3. **`setgc`**: Scans the GC and updates matching values instantly. Because this scans on every call, **do not run this inside loops** as it will lag the game client.

---

## Method 1: Cached Modding (Recommended)

This is the standard and most performant method. You scan the GC once, retrieve a cache of references, and repeatedly apply modifications. This is perfect for values that the game checks constantly or resets (e.g. ammo or recoil).

### Step 1: Scan and Cache
We use `getgc` to search the collector for specific keys we want to modify (e.g. `"FireRate"`, `"SpreadAngle"`, `"MagAmmo"`):

```lua
-- Scan the garbage collector once for our target keys and cache them
local cache = getgc({"FireRate", "SpreadAngle", "MagAmmo"})
```

### Step 2: Apply Modifications
Once you have the cache, you can modify singular values or apply modifications in groups using `applygc`.

#### Modifying a single value:
```lua
-- Set FireRate to 0 (rapid fire)
applygc(cache, "FireRate", 0)

-- Set MagAmmo to 999999
applygc(cache, "MagAmmo", 999999)
```

#### Modifying a group of values:
```lua
-- Apply multiple modifications in one fast operation
applygc(cache, {
    FireRate = 0,
    SpreadAngle = 0,
    MagAmmo = 999999
})
```

---

## Method 2: Instant Modding (One-Offs)

If you only need to modify a value once (e.g., unlocking a game pass state or setting a one-time configuration) and do not need to repeat it, you can use `setgc`.

```lua
-- Singular modification
setgc("FireRate", 0)

-- Group modification
setgc({
    FireRate = 0,
    SpreadAngle = 0,
    CameraRecoilMult = 0,
    MagAmmo = 999999
})
```

---

## Practical Example: Auto-Updating Gun Modifier

Many modern Roblox games (like *Blackhawk Rescue Mission 5*) rebuild or reset your gun configuration tables whenever you respawn, change weapons, or customize a weapon.

To ensure your modifications remain active, you should:
1. Listen for character spawns or weapon changes.
2. Re-run `getgc` to scan for the new tables.
3. Apply modifications.

Here is a complete, ready-to-run template:

```lua
local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer

-- Function to modify our stats
local function modifyWeaponStats()
    print("Scanning garbage collector...")
    
    -- Scan and cache the target properties
    local cache = getgc({
        "FireRate",
        "SpreadAngle",
        "CameraRecoilMult",
        "MagAmmo"
    })
    
    -- Apply modifications
    local modifiedCount = applygc(cache, {
        FireRate = 0.01,         -- Insanely fast fire rate
        SpreadAngle = 0,         -- Zero spread (laser accuracy)
        CameraRecoilMult = 0,    -- Zero recoil
        MagAmmo = 999999         -- Infinite magazine
    })
    
    print("Weapon stats modified! Total changes applied: " .. tostring(modifiedCount))
end

-- Run once on script load
modifyWeaponStats()

-- Automatically re-apply modifications when character respawns
LocalPlayer.CharacterAdded:Connect(function()
    task.wait(1.5) -- Wait a moment for gun tables to load into memory
    modifyWeaponStats()
end)
```
