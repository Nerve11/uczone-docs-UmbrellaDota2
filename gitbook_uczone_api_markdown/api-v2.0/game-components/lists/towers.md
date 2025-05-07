# 🏰Towers

Table to work with tower list\.

## [](#count)Count

`Towers.Count():` `integer`

Return size of tower list\.

## [](#get)Get

`Towers.Get(index):` [`CTower`](https://uczone.gitbook.io/api-v2.0/game-components/core/tower) \| `nil`

Name

Type

Description

**index**

`integer`

Index of tower in cheat list\.

Return tower by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`Towers.GetAll():` [`CTower[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tower)

Return all towers in cheat list\.

## [](#inradius)InRadius

`Towers.InRadius(pos, radius, teamNum, [teamType]):` [`CTower[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tower)

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check\.

**radius**

`number`

Radius to check\.

**teamNum**

[`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Team number to check\.

**teamType**`[?]`

[`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

Team number to check\. `(default: Enum.TeamType.TEAM_ENEMY)`

Return all towers in radius\.

## [](#contains)Contains

`Towers.Contains(tower):` `boolean`

**tower**

[`CTower`](https://uczone.gitbook.io/api-v2.0/game-components/core/tower)

Tower to check\.

Check tower in cheat list\.

Last updated 19 days ago

