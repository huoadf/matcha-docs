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