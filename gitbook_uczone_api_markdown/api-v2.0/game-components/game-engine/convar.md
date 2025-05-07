# ⚙️ConVar

Table to work with `CConVars`\.
ConVars are game variable that can be used to retrieve or change some game engine settings\.

## [](#find)Find

`ConVar.Find(name):` [`CConVar`](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) \| `nil`

Name

Type

Description

**name**

`string`

Returns the found ConVar\.

#### [](#example)Example

```
local convar = ConVar.Find("dota_camera_distance")
local camera_distance = ConVar.GetFloat(convar)
```

## [](#getstring)GetString

`ConVar.GetString(convar):` `string`

**convar**

[`CConVar`](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar)

Returns string value of the Convar

## [](#getint)GetInt

`ConVar.GetInt(convar):` `integer`

Returns int value of the Convar

## [](#getfloat)GetFloat

`ConVar.GetFloat(convar):` `number`

Returns float value of the Convar

## [](#getbool)GetBool

`ConVar.GetBool(convar):` `boolean`

Returns boolean value of the Convar

## [](#setstring)SetString

`ConVar.SetString(convar, value):` `nil`

**value**

Assigns new string value to the ConVar

## [](#setint)SetInt

`ConVar.SetInt(convar, value):` `nil`

`integer`

Assigns new int value to the ConVar

## [](#setfloat)SetFloat

`ConVar.SetFloat(convar, value):` `nil`

`number`

Assigns new float value to the ConVar

## [](#setbool)SetBool

`ConVar.SetBool(convar, value):` `nil`

`boolean`

Assigns new boolean value to the ConVar

Last updated 19 days ago

