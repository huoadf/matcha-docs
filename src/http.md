{% hint style="info" %}
`httpget` and `httppost` are **synchronous** — they block until the response arrives and return the response body as a string. They never raise an error: an HTTP error status (e.g. 404) returns the server's response body, and a connection failure (e.g. an unreachable host) returns an empty string. They are the global equivalents of `game:HttpGet` / `game:HttpPost`.
{% endhint %}

## httpget

```lua
function httpget(url: string, headers: table?): string
```

Sends a GET request to `url` and returns the response body. Optionally pass a table of request headers.

```lua
local body = httpget("https://example.com/data.json")
if body ~= "" then
    local data = game:GetService("HttpService"):JSONDecode(body)
end
```

## httppost

```lua
function httppost(url: string, body: string, contentType: string?, headers: table?): string
```

Sends a POST request to `url` with `body` and returns the response body. `contentType` defaults to `"application/json"`. Optionally pass a table of request headers as the fourth argument.

```lua
local resp = httppost("https://example.com/api", '{"action":"ping"}', "application/json")
```