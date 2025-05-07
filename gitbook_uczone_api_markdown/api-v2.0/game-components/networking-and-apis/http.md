# 🌐HTTP

Table to work with HTTP requests\.

## [](#request)Request

`HTTP.Request(method, url, [data], callback, [param]):` `boolean`

Name

Type

Description

**method**

`string`

HTTP method

**url**

URL

**data**`[?]`

`{headers:table<string>, cookies:string` \| `table<string>, data:string` \| `table<string>, timeout:number}`

data to send `(default: {})`

**callback**

`fun(tbl: {response: string, code: string, header: string, param: string}):nil`

callback function to call when request is done\. Take 1 argument \- response data table\, see example\.

**param**`[?]`

string parameter to pass to callback function to identify request `(default: "")`

Do HTTP request\. Returns `true` if request was sent successfully\.

#### [](#example)Example

```
-- http_request.lua
local url = "https://reqres.in/api/users/2";

local headers = {
    ["User-Agent"] = "Umbrella/1.0",
    ['Connection'] = 'Keep-Alive',
}

local JSON = require('assets.JSON')
local callback = function(response)
    Log.Write(response["response"]);
    Log.Write(response["code"]);
    Log.Write(response["header"]);
    Log.Write(response["param"]);

    local json = JSON:decode(response["response"]);
    Log.Write(json["data"]["email"]);
end

HTTP.Request("GET", url, { 
		headers = headers,
	}, callback, "reqres_get");
```

Last updated 12 days ago

