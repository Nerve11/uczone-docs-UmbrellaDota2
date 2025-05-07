# 🦸Heroes

Table to work with hero list\.

## [](#count)Count

`Heroes.Count():` `integer`

Return size of hero list\.

## [](#get)Get

`Heroes.Get(index):` [`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) \| `nil`

Name

Type

Description

**index**

`integer`

Index of hero in cheat list\.

Return hero by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`Heroes.GetAll():` [`CHero[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

Return all heroes in cheat list\.

## [](#contains)Contains

`Heroes.Contains(hero):` `boolean`

**hero**

[`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

Hero to check\.

Check hero in cheat list\.

## [](#inradius)InRadius

`Heroes.InRadius(pos, radius, teamNum, teamType):` [`CHero[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check\.

**radius**

`number`

Radius to check\.

**teamNum**

[`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Team number to check\.

**teamType**

[`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

Team type to filter by\. Relative to teamNum param\.

Return all heroes in radius\.

## [](#getlocal)GetLocal

`Heroes.GetLocal():` [`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) \| `nil`

Return local hero\.

Last updated 19 days ago

