These functions find and modify values held in the game's Lua garbage collector by name, such as weapon stats and other values stored in Lua tables.

## getgc

```lua
function getgc(name: string): { table }
function getgc(names: { string }): { table }
```

Returns every garbage-collected value stored under `name`. Pass a list of names to collect them all in a single scan. The result is an array of entries; each entry is a table:

- `key` — the name the value was found under
- `value` — the current value
- `type` — the value's type (`number`, `string`, `boolean`, `table`, `function`, `userdata`, ...)
- `addr` — the value's memory address

The same name can be stored in many places, so multiple entries are normal. Returns an empty table if nothing is found.

## setgc

```lua
function setgc(key: string, value: Any): int
function setgc(values: { [string]: Any }): int
```

Sets every garbage-collected value stored under `key` to `value`, scanning the collector on each call. Pass a table to set multiple keys at once. Only values whose type matches `value` are changed. Returns the number of values set.

```lua
-- singular
setgc("FireRate", 0)

-- group
setgc({
    FireRate = 0,
    SpreadAngle = 0,
    CameraRecoilMult = 0,
    MagAmmo = 999999
})
```

## applygc

```lua
function applygc(cache: table, key: string, value: Any): int
function applygc(cache: table, values: { [string]: Any }): int
```

Same as `setgc`, but applies to a `cache` returned by `getgc` instead of scanning again. Call `getgc` once and reuse the cache with `applygc` when setting values repeatedly, such as inside a loop or for values the game keeps resetting. Run `getgc` again to refresh the cache if the values are rebuilt, for example after respawning or switching weapons. Returns the number of values set.

```lua
local cache = getgc({ "FireRate", "SpreadAngle", "MagAmmo" })

-- singular
applygc(cache, "FireRate", 0)
applygc(cache, "MagAmmo", 999999)

-- group
applygc(cache, { FireRate = 0, SpreadAngle = 0, MagAmmo = 999999 })
```