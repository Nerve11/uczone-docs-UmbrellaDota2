# 🎮Input

Table to work with input system\.

## [](#getworldcursorpos)GetWorldCursorPos

`Input.GetWorldCursorPos():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world cursor position\.

## [](#getcursorpos)GetCursorPos

`Input.GetCursorPos():` `number`\, `number`

Returns screen cursor position \(x\, y\)\. See example\.

#### [](#example)Example

```
local x, y =	Input.GetCursorPos()
```

## [](#iscursorinrect)IsCursorInRect

`Input.IsCursorInRect(x, y, w, h):` `boolean`

Name

Type

Description

**x**

`number`

x position

**y**

**w**

width

**h**

height

Returns `true` if cursor is in rect\.

## [](#iscursorinbounds)IsCursorInBounds

`Input.IsCursorInBounds(x0, y0, x1, y1):` `boolean`

**x0**

**y0**

**x1**

**y1**

Returns `true` if cursor is in bounds\.

## [](#getnearestunittocursor)GetNearestUnitToCursor

Excludes not visible\, illusions and dead units\.

`Input.GetNearestUnitToCursor(teamNum, teamType):` [`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| `nil`

**teamNum**

[`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

team number\. Could be get from `Entity.GetTeamNum`

**teamType**

[`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

team type to search relative to teamNum param

Returns nearest unit to cursor\.

## [](#getnearestherotocursor)GetNearestHeroToCursor

Excludes not visible\, illusions and dead heroes\.

`Input.GetNearestHeroToCursor(teamNum, teamType):` [`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) \| `nil`

Returns nearest hero to cursor\.

## [](#isinputcaptured)IsInputCaptured

`Input.IsInputCaptured():` `boolean`

Returns `true` if input is captured\. e\.g\. opened console\, chat\, shop\.

## [](#iskeydown)IsKeyDown

`Input.IsKeyDown(KeyCode):` `boolean`

**KeyCode**

[`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Returns `true` if key is down\.

## [](#iskeydownonce)IsKeyDownOnce

This function will return \`true\` only once per key press\.

\`Input\.IsKeyDownOnce\(KeyCode\):\` \*\*\`boolean\`\*\*

Return `true` if key is down once\.

Last updated 19 days ago

