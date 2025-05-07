# 🗺️MiniMap

Table to work with in\-game minimap\.

## [](#ping)Ping

`MiniMap.Ping(pos, type):` `nil`

Name

Type

Description

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to ping

**type**

[`Enum.PingType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.pingtype)

ping type

Pings on the minimap\.

## [](#sendline)SendLine

`MiniMap.SendLine(pos, initial, clientside):` `nil`

world position to draw line to

**initial**

`boolean`

start a new line\, otherwise continue the last one

**clientside**

draw only for local player

Draws a line on the minimap\.

## [](#sendline-1)SendLine

`MiniMap.SendLine(x, y, initial, clientside):` `nil`

**x**

`number`

x world position to draw line

**y**

y world position to draw line

## [](#drawcircle)DrawCircle

`MiniMap.DrawCircle(pos, [r], [g], [b], [a], [size]):` `nil`

world position to draw circle

**r**`[?]`

`integer`

red color `(default: 255)`

**g**`[?]`

green color `(default: 255)`

**b**`[?]`

blue color `(default: 255)`

**a**`[?]`

alpha color `(default: 255)`

**size**`[?]`

circle size `(default: 800)`

Draws a circle on the minimap\.

## [](#drawheroicon)DrawHeroIcon

`MiniMap.DrawHeroIcon(unitName, pos, [r], [g], [b], [a], [size]):` `nil`

**unitName**

`string`

unit name to draw icon\. Can get it from `NPC.GetUnitName`

world position to draw icon

icon size `(default: 800)`

Draws a hero icon on the minimap\.

## [](#drawiconbyname)DrawIconByName

`MiniMap.DrawIconByName(iconName, pos, [r], [g], [b], [a], [size]):` `nil`

**iconName**

could get it from game\\dota\\pak01\_dir\.vpk \(scripts\\mod\_textures\.txt\)\.

Draws a icon on the minimap\.

## [](#getmouseposinworld)GetMousePosInWorld

`MiniMap.GetMousePosInWorld():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world position the mouse on the minimap\, if the mouse is not on the minimap\, it will return \(0\,0\,0\)\.

## [](#iscursoronminimap)IsCursorOnMinimap

`MiniMap.IsCursorOnMinimap():` `boolean`

Returns `true` if the mouse is on the minimap\.

## [](#getminimaptoworld)GetMinimapToWorld

`MiniMap.GetMinimapToWorld(ScreenX, ScreenY):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**ScreenX**

**ScreenY**

Returns world position from minimap position\. The same as `GetMousePosInWorld`\, but you can pass any position on screen\, not only mouse position\.

Last updated 19 days ago

