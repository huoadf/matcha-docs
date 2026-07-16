The following snippet will display a red square on the user's screen for 5 seconds.

```lua
local square = Drawing.new("Square")
square.Filled = true
square.Color = Color3.fromRGB(255, 0, 0)
square.Position = Vector2.new(20, 20)
square.Size = Vector2.new(200, 200)
square.Visible = true
square.Corner = 20
wait(5)
square:Remove()
```



## Drawing.new

```lua
Drawing.new(drawingType: string): DrawingObject
```

`drawingType` must be one of the following types:

* Square
* Line
* Circle
* Text
* Triangle
* Image


## DrawingObject

**Methods**

### Remove

```lua
function DrawingObject:Remove(): nil
```

**Base properties**

Shared set of properties across all `DrawingObject` types

### Color

```lua
DrawingObject.Color: Color3
```

### Transparency

```lua
DrawingObject.Transparency: number
```

### Visible

```lua
DrawingObject.Visible: bool
```

### Position

```lua
DrawingObject.Position: Vector2
```

### ZIndex

```lua
DrawingObject.ZIndex: int
```

**Square properties**

### Size

```lua
DrawingObject.Size: Vector2
```

### Filled

```lua
DrawingObject.Filled: bool
```

**Line properties**

### From

```lua
DrawingObject.From: Vector2
```

### To

```lua
DrawingObject.To: Vector2
```

### Thickness

```lua
DrawingObject.Thickness: int
```

**Circle properties**

### Radius

```lua
DrawingObject.Radius: float
```

### NumSides

```lua
DrawingObject.NumSides: int
```

### Thickness

```lua
DrawingObject.Thickness: int
```

**Text properties**

### Text

```lua
DrawingObject.Text: string
```

### Outline

```lua
DrawingObject.Outline: bool
```

### Center

```lua
DrawingObject.Center: bool
```

### Font

```lua
DrawingObject.Font: Font
```

### FontSize

```lua
DrawingObject.FontSize: int
```

**Triangle properties**

### PointA

```lua
DrawingObject.PointA: Vector2
```

### PointB

```lua
DrawingObject.PointB: Vector2
```

### PointC

```lua
DrawingObject.PointC: Vector2
```

**Image properties**

### Data

```lua
DrawingObject.Data: string
```

The raw binary string of the image data (e.g. loaded via `game:HttpGet`).

### Image Size

```lua
DrawingObject.Size: Vector2
```

The width and height of the image (defaults to 50x50).

### Rounding

```lua
DrawingObject.Rounding: number
```

The rounding radius of the image corners (defaults to 0).


## Fonts


```lua
Drawing.Fonts.UI         -- ProggyClean
Drawing.Fonts.System     -- San Francisco
Drawing.Fonts.SystemBold -- SF Bold
Drawing.Fonts.Minecraft  -- Minecraft
Drawing.Fonts.Monospace  -- JetBrains
Drawing.Fonts.Pixel      -- Pixel
Drawing.Fonts.Fortnite   -- Fortnite
Drawing.Fonts.ProximaSoftBold -- Proxima Soft Bold
```


## Example: Basic Player ESP (Boxes & Snaplines)

Here is a complete, well-commented script showing how to use the `Drawing` API, `WorldToScreen`, and `RunService.Heartbeat` to draw 2D bounding boxes and snaplines on other players.

This script runs entirely in the background and cleans up all drawings when stopped.

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local Workspace = game:GetService("Workspace")
local LocalPlayer = Players.LocalPlayer
local Camera = Workspace.CurrentCamera

local espCache = {}

-- Helper to create drawing objects
local function createDrawing(class, properties)
    local draw = Drawing.new(class)
    for prop, val in pairs(properties) do
        draw[prop] = val
    end
    return draw
end

-- Create ESP for a specific player
local function addESP(player)
    if player == LocalPlayer then return end
    
    local esp = {
        Box = createDrawing("Square", {
            Color = Color3.fromRGB(255, 0, 0),
            Thickness = 1.5,
            Filled = false,
            Visible = false
        }),
        Line = createDrawing("Line", {
            Color = Color3.fromRGB(255, 255, 0),
            Thickness = 1,
            Visible = false
        }),
        Text = createDrawing("Text", {
            Color = Color3.fromRGB(255, 255, 255),
            Size = 14,
            Center = true,
            Outline = true,
            Visible = false
        })
    }
    
    espCache[player] = esp
end

-- Clean up ESP for a player
local function removeESP(player)
    local esp = espCache[player]
    if esp then
        esp.Box:Remove()
        esp.Line:Remove()
        esp.Text:Remove()
        espCache[player] = nil
    end
end

-- Update all drawings every physics frame
local connection
connection = RunService.Heartbeat:Connect(function()
    for player, esp in pairs(espCache) do
        local character = player.Character
        local rootPart = character and character:FindFirstChild("HumanoidRootPart")
        local humanoid = character and character:FindFirstChildOfClass("Humanoid")
        
        if rootPart and humanoid and humanoid.Health > 0 then
            -- Projects target player's position to screen
            local screenPos, onScreen = WorldToScreen(rootPart.Position)
            
            if onScreen then
                -- 1. Calculate Bounding Box dimensions based on distance
                local extents = character:GetExtentsSize()
                local height = (Camera.ViewportSize.Y / (screenPos.Y * 2)) * extents.Y * 10
                local width = height * 0.6
                
                esp.Box.Size = Vector2.new(width, height)
                esp.Box.Position = Vector2.new(screenPos.X - width/2, screenPos.Y - height/2)
                esp.Box.Visible = true
                
                -- 2. Draw Snapline from bottom-center of camera viewport to player
                esp.Line.From = Vector2.new(Camera.ViewportSize.X / 2, Camera.ViewportSize.Y)
                esp.Line.To = Vector2.new(screenPos.X, screenPos.Y + height/2)
                esp.Line.Visible = true
                
                -- 3. Draw Player Name & Health text above box
                esp.Text.Text = string.format("%s [%d HP]", player.Name, math.floor(humanoid.Health))
                esp.Text.Position = Vector2.new(screenPos.X, screenPos.Y - height/2 - 18)
                esp.Text.Visible = true
            else
                esp.Box.Visible = false
                esp.Line.Visible = false
                esp.Text.Visible = false
            end
        else
            -- Hide drawings if character is missing or dead
            esp.Box.Visible = false
            esp.Line.Visible = false
            esp.Text.Visible = false
        end
    end
end)

-- Initialize ESP for current players
for _, player in ipairs(Players:GetPlayers()) do
    addESP(player)
end

-- Hook player join/leave events
Players.PlayerAdded:Connect(addESP)
Players.PlayerRemoving:Connect(removeESP)

print("Matcha ESP script loaded! Draw overlays are now active.")
```