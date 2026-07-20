## BasePart

<https://create.roblox.com/docs/reference/engine/classes/BasePart>

**Properties**

### Size

```lua
BasePart.Size: Vector3
```

### Position

```lua
BasePart.Position: Vector3
```

### Transparency

```lua
BasePart.Transparency: number
```

### Color

```lua
BasePart.Color: Color3
```

### Velocity

```lua
BasePart.Velocity: Vector3
```

### AssemblyLinearVelocity

```lua
BasePart.AssemblyLinearVelocity: Vector3
```

### CanCollide

```lua
BasePart.CanCollide: bool
```


## Camera

<https://create.roblox.com/docs/reference/engine/classes/Camera>

**Constructors**

### lookAt

```lua
Camera.lookAt(at: Vector3, lookAt: Vector3)
```

**Properties**

### ViewportSize

```lua
Camera.ViewportSize: Vector2
```

### FieldOfView

```lua
Camera.FieldOfView: number
```

### Position

```lua
Camera.Position: Vector3
```

### CFrame

```lua
Camera.CFrame: CFrame
```


## DataModel

<https://create.roblox.com/docs/reference/engine/classes/DataModel>

**Properties**

### PlaceId

```lua
Instance.PlaceId: number
```

### GameId

```lua
Instance.GameId: number
```

### JobId

```lua
Instance.JobId: string
```

**Methods**

### HttpGet

```lua
function DataModel:HttpGet(url: string, headers: table?): string
```

### HttpPost

```lua
function DataModel:HttpPost(url: string, data: string, contentType: string?, headers: table?): string
```

### GetService

```lua
function DataModel:GetService(name: string): Instance
```

### isLoaded

```lua
function DataModel:isLoaded(): boolean
```

Returns `true` if the game is fully loaded, else `false`.


## HttpService

**Methods**

### JSONEncode

```lua
function HttpService:JSONEncode(tbl: table): string
```

### JSONDecode

```lua
function HttpService:JSONDecode(str: string): table
```

### GenerateGUID

```lua
function HttpService:GenerateGUID(): string
```


## Humanoid

<https://create.roblox.com/docs/reference/engine/classes/Humanoid>

**Properties**

### MaxHealth

```lua
Humanoid.MaxHealth: number
```

### Health

```lua
Humanoid.Health: number
```


## Model

<https://create.roblox.com/docs/reference/engine/classes/Model>

**Properties**

### PrimaryPart

```lua
Model.PrimaryPart: BasePart
```


## Workspace

<https://create.roblox.com/docs/reference/engine/classes/Workspace>

**Properties**

### CurrentCamera

```lua
Workspace.CurrentCamera: Camera
```

**Methods**

### Raycast

```lua
function Workspace:Raycast(origin: Vector3, direction: Vector3, params: RaycastParams?): RaycastResult?
```

Projects a ray from `origin` in the direction of `direction` using optional `RaycastParams`. Returns the first `RaycastResult` hit, or `nil` if no hit.


## Instance

<https://create.roblox.com/docs/reference/engine/classes/Instance>

**Properties**

### Name

```lua
Instance.Name: string
```

### ClassName

```lua
Instance.ClassName: string
```

### Parent

```lua
Instance.Parent: Instance
```

### Address

```lua
Instance.Address: number
```

Hexadecimal number representing the Instance’s memory address.

**Methods**

### FindFirstChildOfClass

```lua
function Instance:FindFirstChildOfClass(name: string): Instance
```

### FindFirstChild

```lua
function Instance:FindFirstChild(name: string): Instance
```

### IsA

```lua
function Instance:IsA(name: string): boolean
```

### GetFullName

```lua
function Instance:GetFullName(): string
```

### GetChildren

```lua
function Instance:GetChildren(): { Instance }
```

### GetAttribute

```lua
function Instance:GetAttribute(name: string): any
```

### GetAttributes

```lua
function Instance:GetAttributes(): { string }
```

### SetAttribute

```lua
function Instance:SetAttribute(name: string, value: any): nil
```

### GetDescendants

```lua
function Instance:GetDescendants(): { Instance }
```

### IsDescendantOf

```lua
function Instance:IsDescendantOf(parent: Instance): boolean
```

### FindFirstChildWhichIsA

```lua
function Instance:FindFirstChildWhichIsA(class: string): Instance
```

### WaitForChild

```lua
function Instance:WaitForChild(name: string): Instance
```


## Mouse

<https://create.roblox.com/docs/reference/engine/classes/Mouse>

**Properties**

### X

```lua
Mouse.X: number
```

### Y

```lua
Mouse.Y: number
```


## Players

<https://create.roblox.com/docs/reference/engine/classes/Players>

**Properties**

### LocalPlayer

```lua
Players.LocalPlayer: Player
```

### GetPlayers

```lua
function Players:GetPlayers(): Table
```

**Events**

### PlayerAdded

```lua
Players.PlayerAdded:Connect(function(player))
```

### PlayerRemoving

```lua
Players.PlayerRemoving:Connect(function(player))
```


## Player

<https://create.roblox.com/docs/reference/engine/classes/Player>

**Properties**

### Character

```lua
Player.Character: Model
```

### Team

```lua
Player.Team: Team
```

### UserId

```lua
Player.UserId: number
```

**Methods**

### GetMouse

```lua
function Player:GetMouse(): Mouse
```


## ValueBase

<https://create.roblox.com/docs/reference/engine/classes/ValueBase>

`ObjectValue`, `Color3Value`, `NumberValue`, `IntValue`, `FloatValue`, `BoolValue`, and `StringValue` all inherit from this class. For simplicity, they do not have separate sub-pages.

**Properties**

### Value

```lua
ValueBase.Value: any
```


## GuiObject

<https://create.roblox.com/docs/reference/engine/classes/GuiObject>

**Properties**

### AbsoluteSize

```lua
GuiObject.AbsoluteSize: Vector2
```

### AbsolutePosition

```lua
GuiObject.AbsolutePosition: Vector2
```


## TextLabel

<https://create.roblox.com/docs/reference/engine/classes/TextLabel>

**Properties**

### Text

```lua
TextLabel.Text: string
```


## MeshPart

<https://create.roblox.com/docs/reference/engine/classes/MeshPart>

**Properties**

### TextureId

```lua
MeshPart.TextureId: string
```

### MeshId

```lua
MeshPart.MeshId: string
```


## UserInputService

```lua
local UserInputService = game:GetService("UserInputService")
```

**Events**

### InputBegan

```lua
 UserInputService.InputBegan:Connect(function(input: InputObject, gameProcessed: boolean))
```

### InputEnded

```lua
UserInputService.InputEnded:Connect(function(input: InputObject, gameProcessed: boolean))
```


## RunService

<https://create.roblox.com/docs/reference/engine/classes/RunService>

The `RunService` service contains methods and events for managing the execution of the game/simulation.

**Events**

### RenderStepped

```lua
RunService.RenderStepped:Connect(function(deltaTime: number))
```

Fires every frame, prior to the frame being rendered. Passes the time elapsed since the last frame (`deltaTime`) as a number.

### Heartbeat

```lua
RunService.Heartbeat:Connect(function(deltaTime: number))
```

Fires every frame, after the physics simulation has completed. Passes the time elapsed since the last frame (`deltaTime`) as a number.

### Stepped

```lua
RunService.Stepped:Connect(function(deltaTime: number))
```

Fires every frame, prior to the physics simulation step. Passes the time elapsed since the last frame (`deltaTime`) as a number.

{% hint style="warning" %}
In the Matcha VM, the `Stepped` event only receives one argument (`deltaTime: number`), unlike the standard Roblox API which receives both `time` and `deltaTime`.
{% endhint %}


## RemoteEvent

<https://create.roblox.com/docs/reference/engine/classes/RemoteEvent>

**Methods**

### FireServer

```lua
RemoteEvent:FireServer(...any)
```

Fires the `RemoteEvent` to the server with the given arguments. *(Added in Hybrid mode - Jul 20 2026).*


## RemoteFunction

<https://create.roblox.com/docs/reference/engine/classes/RemoteFunction>

**Methods**

### InvokeFunction

```lua
RemoteFunction:InvokeFunction(...any): ...any
```

Invokes the `RemoteFunction` on the server and yields until it returns a result. *(Added in Hybrid mode - Jul 20 2026).*

{% hint style="warning" %}
Unlike the standard Roblox `InvokeServer`, Matcha uses `InvokeFunction` to call `RemoteFunction`s externally.
{% endhint %}