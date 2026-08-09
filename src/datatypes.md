## Vector3

<https://create.roblox.com/docs/reference/engine/datatypes/Vector3>

The [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) data type represents a vector in 3D space, typically used as a point in 3D space or the dimensions of a rectangular prism.

**Constructors**

### new

```lua
Vector3.new(x: number, y: number, z: number)
```

Returns a new [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) from the given x, y, and z components.

### zero

```lua
Vector3.zero: Vector3
```

Returns a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) with coordinates (0, 0, 0).

### one

```lua
Vector3.one: Vector3
```

Returns a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) with coordinates (1, 1, 1).

### xAxis

```lua
Vector3.xAxis: Vector3
```

Returns a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) with coordinates (1, 0, 0).

### yAxis

```lua
Vector3.yAxis: Vector3
```

Returns a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) with coordinates (0, 1, 0).

### zAxis

```lua
Vector3.zAxis: Vector3
```

Returns a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3) with coordinates (0, 0, 1).

**Properties**

### X

```lua
Vector3.X: number
```

### Y

```lua
Vector3.Y: number
```

### Z

```lua
Vector3.Z: number
```

### Magnitude

```lua
Vector3.Magnitude: number
```

Returns the length of the vector.

### Unit

```lua
Vector3.Unit: Vector3
```

Returns a vector of length 1 pointing in the same direction as the original vector.

**Operations**

Matcha supports the following mathematical operations on `Vector3` types:

* **Addition / Subtraction**: `Vector3 + Vector3`, `Vector3 - Vector3`
* **Multiplication / Division**: `Vector3 * Vector3`, `Vector3 / Vector3`, `Vector3 * number`, `Vector3 / number`, `number * Vector3`
* **Unary Minus**: `-Vector3`
* **Equality**: `Vector3 == Vector3`

**Methods**

### Abs

```lua
function Vector3:Abs(): Vector3
```

Returns a Vector3 with the absolute value of each component.

### Angle

```lua
function Vector3:Angle(other: Vector3): number
```

Returns the angle between the two vectors in radians.

### Ceil

```lua
function Vector3:Ceil(): Vector3
```

Returns a Vector3 with the components rounded up to the nearest integer.

### Cross

```lua
function Vector3:Cross(other: Vector3): Vector3
```

Returns the cross product of the two vectors.

### Dot

```lua
function Vector3:Dot(other: Vector3): number
```

Returns the dot product of the two vectors.

### Floor

```lua
function Vector3:Floor(): Vector3
```

Returns a Vector3 with the components rounded down to the nearest integer.

### FuzzyEq

```lua
function Vector3:FuzzyEq(other: Vector3, epsilon: number): boolean
```

Returns true if the two vectors are approximately equal within the specified epsilon.

### Lerp

```lua
function Vector3:Lerp(target: Vector3, alpha: number): Vector3
```

Linearly interpolates between the vector and the target vector by alpha.

### Max

```lua
function Vector3:Max(other: Vector3): Vector3
```

Returns a Vector3 where each component is the maximum of the corresponding components in the two vectors.

### Min

```lua
function Vector3:Min(other: Vector3): Vector3
```

Returns a Vector3 where each component is the minimum of the corresponding components in the two vectors.

### Sign

```lua
function Vector3:Sign(): Vector3
```

Returns a Vector3 indicating the sign of each component (-1, 0, or 1).




## CFrame

<https://create.roblox.com/docs/reference/engine/datatypes/CFrame>

The [CFrame](https://create.roblox.com/docs/reference/engine/datatypes/CFrame) (Coordinate Frame) data type describes a position and rotation in 3D space.

**Constructors**

### new

```lua
CFrame.new()
```

Returns an identity CFrame at position (0, 0, 0) with no rotation.

```lua
CFrame.new(x: number, y: number, z: number)
```

Returns a CFrame at position (x, y, z) with no rotation.

```lua
CFrame.new(x: number, y: number, z: number, qx: number, qy: number, qz: number, qw: number)
```

Returns a CFrame with position (x, y, z) and rotation defined by quaternion components (qx, qy, qz, qw).

```lua
CFrame.new(x: number, y: number, z: number, r00: number, r01: number, r02: number, r10: number, r11: number, r12: number, r20: number, r21: number, r22: number)
```

Returns a CFrame with position (x, y, z) and rotation defined by the rotation matrix components.

{% hint style="info" %}
`CFrame.new` expects exactly 0, 3, 6, or 12 arguments.
{% endhint %}

### Angles

```lua
CFrame.Angles(rx: number, ry: number, rz: number)
```

Returns a CFrame with position (0, 0, 0) and rotation defined by the specified Euler angles (in radians).

### fromOrientation

```lua
CFrame.fromOrientation(rx: number, ry: number, rz: number)
```

Returns a CFrame with position (0, 0, 0) and rotation defined by the specified Euler angles (in radians), applied in YXZ order.

**Properties**

### X

```lua
CFrame.X: number
```

The X coordinate of the CFrame's position.

### Y

```lua
CFrame.Y: number
```

The Y coordinate of the CFrame's position.

### Z

```lua
CFrame.Z: number
```

The Z coordinate of the CFrame's position.

### Position

```lua
CFrame.Position: Vector3
```

The position of the CFrame as a [Vector3](https://create.roblox.com/docs/reference/engine/datatypes/Vector3).

### LookVector

```lua
CFrame.LookVector: Vector3
```

The forward-pointing unit vector of the CFrame (the negative Z axis).

### RightVector

```lua
CFrame.RightVector: Vector3
```

The right-pointing unit vector of the CFrame (the X axis).

### UpVector

```lua
CFrame.UpVector: Vector3
```

The upward-pointing unit vector of the CFrame (the Y axis).

**Operations**

Matcha supports the following mathematical operations on `CFrame` types:

* **CFrame Multiplication**: `CFrame * CFrame` composition.
* **Vector Transformation**: `CFrame * Vector3` to transform a point into world space.
* **Equality**: `CFrame == CFrame` (uses reference equality).

**Methods**

### GetComponents

```lua
function CFrame:GetComponents(): (number, number, number, number, number, number, number, number, number, number, number, number)
```

Returns the components of the CFrame: position `x`, `y`, `z` and the 9 rotation matrix components `r00`, `r01`, `r02`, `r10`, `r11`, `r12`, `r20`, `r21`, `r22`.

### Inverse

```lua
function CFrame:Inverse(): CFrame
```

Returns the inverse of this CFrame.

### Lerp

```lua
function CFrame:Lerp(target: CFrame, alpha: number): CFrame
```

Linearly interpolates between this CFrame and the target CFrame by alpha.

### PointToObjectSpace

```lua
function CFrame:PointToObjectSpace(v: Vector3): Vector3
```

Transforms a Vector3 point from world space to the CFrame's local object space.

### PointToWorldSpace

```lua
function CFrame:PointToWorldSpace(v: Vector3): Vector3
```

Transforms a Vector3 point from the CFrame's local object space to world space.

### ToEulerAnglesXYZ

```lua
function CFrame:ToEulerAnglesXYZ(): (number, number, number)
```

Returns the Euler angles (in radians) of this CFrame using XYZ order.

### ToOrientation

```lua
function CFrame:ToOrientation(): (number, number, number)
```

Returns the Euler angles (in radians) of this CFrame using YXZ order.

### VectorToObjectSpace

```lua
function CFrame:VectorToObjectSpace(v: Vector3): Vector3
```

Transforms a Vector3 vector from world space to local object space.

### VectorToWorldSpace

```lua
function CFrame:VectorToWorldSpace(v: Vector3): Vector3
```

Transforms a Vector3 vector from local object space to world space.



## Vector2

<https://create.roblox.com/docs/reference/engine/datatypes/Vector2>

The [Vector2](https://create.roblox.com/docs/reference/engine/datatypes/Vector2) data type represents a 2D value with direction and magnitude. Some applications include GUI elements and 2D mouse positions.

**Constructors**

### new

```lua
Vector2.new(x : number, y : number)
```

Returns a [Vector2](https://create.roblox.com/docs/reference/engine/datatypes/Vector2) from the given x and y components.

**Properties**

### X

```lua
Vector2.X: number
```

### Y

```lua
Vector2.Y: number
```


## Color3

The [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) data type describes a color using red, green, and blue components in the range of 0 to 1. Unlike the [BrickColor](https://create.roblox.com/docs/reference/engine/datatypes/BrickColor) data type which describes named colors, [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) is used for precise coloring of objects on screen through properties like [BasePart.Color](https://create.roblox.com/docs/reference/engine/classes/BasePart#Color).

**Constructors**

### new

```lua
Color3.new(red: number, green: number, blue: number)
```

Returns a [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) with the given red, green, and blue values.

### fromRGB

```lua
Color3.fromRGB(red: number, green: number, blue: number)
```

Returns a [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) from given components within the range of 0 to 255.

### fromHSV

```lua
Color3.fromHSV(hue: number, saturation: number, value: number)
```

Returns a [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) from the given hue, saturation, and value components.

### fromHex

```lua
Color3.fromHex(hex: string)
```

Returns a [Color3](https://create.roblox.com/docs/reference/engine/datatypes/Color3) from a given hex value.

**Properties**

### R

```lua
Color3.R: number
```

### G

```lua
Color3.G: number
```

### B

```lua
Color3.B: number
```


## Ray

The [Ray](https://create.roblox.com/docs/reference/engine/datatypes/Ray) data type represents a ray in 3D space, consisting of an origin and a direction.

**Constructors**

### new

```lua
Ray.new(origin: Vector3, direction: Vector3)
```

Returns a Ray with the given origin and direction.

**Properties**

### Origin

```lua
Ray.Origin: Vector3
```

### Direction

```lua
Ray.Direction: Vector3
```


## UDim

The [UDim](https://create.roblox.com/docs/reference/engine/datatypes/UDim) data type represents a single dimension of a UI coordinate, consisting of a scale (relative size) and an offset (pixel size).

**Constructors**

### new

```lua
UDim.new(scale: number, offset: number)
```

Returns a UDim with the given scale and offset.

**Properties**

### Scale

```lua
UDim.Scale: number
```

### Offset

```lua
UDim.Offset: number
```


## UDim2

The [UDim2](https://create.roblox.com/docs/reference/engine/datatypes/UDim2) data type represents a 2D size or position of a UI element, consisting of two UDims (X and Y).

**Constructors**

### new

```lua
UDim2.new(xScale: number, xOffset: number, yScale: number, yOffset: number)
UDim2.new(x: UDim, y: UDim)
```

Returns a UDim2 with the given components.

### fromOffset

```lua
UDim2.fromOffset(x: number, y: number)
```

Returns a UDim2 with only pixel offset components.

### fromScale

```lua
UDim2.fromScale(x: number, y: number)
```

Returns a UDim2 with only scale components.

**Properties**

### X

```lua
UDim2.X: UDim
```

### Y

```lua
UDim2.Y: UDim
```