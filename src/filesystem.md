{% hint style="warning" %}
Paths are relative to the Matcha workspace folder (e.g. `C:\matcha\workspace\`). `/` and `\` are interchangeable, and paths are case-insensitive.

`readfile`, `writefile`, and `appendfile` only accept these extensions: **`.txt` `.lua` `.luau` `.json` `.cfg` `.dat` `.ini`**. Any other extension — including images, audio, and executables — raises `file extension not allowed`. Contents are binary-safe, so store raw/binary data under `.dat`.
{% endhint %}

## writefile

```lua
function writefile(path: string, content: string): nil
```

Creates `path` (or overwrites it) with `content`. Missing parent folders are created automatically. Content is written exactly, including binary data. Errors if `path` has a disallowed extension or is an existing folder.

## readfile

```lua
function readfile(path: string): string
```

Returns the contents of `path` as a string (binary-safe). Errors if the file does not exist, so guard with `isfile` or `pcall`.

```lua
if isfile("MyConfig.json") then
    local raw = readfile("MyConfig.json")
end
```

## appendfile

```lua
function appendfile(path: string, content: string): nil
```

Appends `content` to the end of `path`, creating the file if it does not exist. Content is concatenated exactly — no separator is inserted.

## makefolder

```lua
function makefolder(path: string): nil
```

Creates the folder at `path`, including any missing parent folders. Does nothing if the folder already exists. Errors if a file already occupies the path.

## isfile

```lua
function isfile(path: string): boolean
```

Returns `true` only if `path` is an existing file; `false` for folders or missing paths. Never errors.

## isfolder

```lua
function isfolder(path: string): boolean
```

Returns `true` only if `path` is an existing folder; `false` for files or missing paths. Never errors.

## listfiles

```lua
function listfiles(path: string): { string }
```

Returns the immediate children of `path` — files and folders, not recursive — as workspace-relative paths sorted alphabetically (e.g. `listfiles("cfg")` → `{ "cfg\\a.json", "cfg\\sub" }`). Each entry can be passed straight to `isfile`, `isfolder`, or `readfile`. `listfiles("")` lists the workspace root. Errors if `path` does not exist or is a file.

## delfile

```lua
function delfile(path: string): boolean
```

Deletes the file (or empty folder) at `path`. Returns `true` if something was removed, `false` if the path did not exist. Errors if `path` is a non-empty folder — use `delfolder` for those.

## delfolder

```lua
function delfolder(path: string): boolean
```

Recursively deletes the folder (or file) at `path` and everything inside it. Always returns `true`, even if `path` did not exist.