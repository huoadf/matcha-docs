# Code Examples

A collection of complete, functional script examples demonstrating common patterns in the Matcha LuaVM. These examples are optimized for AI reference and developer usage.

---

## 1. 2D Box ESP Overlay

Draws bounding boxes around all players in the game using `WorldToScreen` and `Drawing.new("Square")`.

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local LocalPlayer = Players.LocalPlayer
local Camera = workspace.CurrentCamera

local boxes = {}

local function createBox(player)
    if player == LocalPlayer then return end
    
    local box = Drawing.new("Square")
    box.Color = Color3.fromRGB(0, 255, 120)
    box.Thickness = 2
    box.Filled = false
    box.Visible = false
    
    boxes[player] = box
end

for _, player in ipairs(Players:GetPlayers()) do
    createBox(player)
end

Players.PlayerAdded:Connect(createBox)

Players.PlayerRemoving:Connect(function(player)
    if boxes[player] then
        boxes[player]:Remove()
        boxes[player] = nil
    end
end)

RunService.RenderStepped:Connect(function()
    for player, box in pairs(boxes) do
        local character = player.Character
        local hrp = character and character:FindFirstChild("HumanoidRootPart")
        
        if hrp then
            local pos, onScreen = WorldToScreen(hrp.Position)
            if onScreen then
                -- Calculate dynamic size based on distance
                local dist = (Camera.CFrame.Position - hrp.Position).Magnitude
                local size = math.clamp(1000 / dist, 10, 300)
                
                box.Position = Vector2.new(pos.X - size / 2, pos.Y - size / 2)
                box.Size = Vector2.new(size, size)
                box.Visible = true
            else
                box.Visible = false
            end
        else
            box.Visible = false
        end
    end
end)
```

---

## 2. Memory Read / Write (Unlimited Health / Speed)

Reading and writing engine memory using `getbase` and `memory_write`.

```lua
-- Get Roblox process base address
local baseAddr = getbase()

-- Example: Modify player speed at a known offset
local walkSpeedOffset = 0x1A2B3C -- Example offset
local targetAddr = baseAddr + walkSpeedOffset

-- Write float value
memory_write("float", targetAddr, 100.0)

-- Read back float value
local currentSpeed = memory_read("float", targetAddr)
print("Current WalkSpeed:", currentSpeed)
```

---

## 3. Remote Event Invocation (Pro ::pro::)

Firing remote events programmatically using Hybrid mode methods.

```lua
-- Fire a RemoteEvent to the server
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local GiveMoneyRemote = ReplicatedStorage:FindFirstChild("GiveMoney", true)

if GiveMoneyRemote then
    -- Fires RemoteEvent on the server
    GiveMoneyRemote:FireServer(1000000)
end

-- Invoke a RemoteFunction
local GetPlayerData = ReplicatedStorage:FindFirstChild("GetPlayerData", true)
if GetPlayerData then
    local data = GetPlayerData:InvokeFunction()
    print("Received player data:", data)
end
```

---

## 4. Garbage Collector Scanning (`getgc`)

Iterating through Lua garbage collector objects to find tables, functions, or upvalues.

```lua
local gc = getgc(true) -- Get all tables and functions

for _, item in ipairs(gc) do
    if type(item) == "table" and rawget(item, "WalkSpeed") then
        print("Found Movement Config Table!")
        item.WalkSpeed = 500
    end
end
```

---

## 5. Raycasting

Using `Workspace:Raycast` to detect objects in front of the camera or player.

```lua
local Camera = workspace.CurrentCamera
local origin = Camera.CFrame.Position
local direction = Camera.CFrame.LookVector * 500

local result = workspace:Raycast(origin, direction)
if result then
    print("Ray hit instance:", result.Instance:GetFullName())
    print("Hit position:", result.Position)
    print("Normal:", result.Normal)
end
```
