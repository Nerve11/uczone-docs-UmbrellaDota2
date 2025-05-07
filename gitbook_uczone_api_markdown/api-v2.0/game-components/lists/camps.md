# 🐉Camps

Table to work with list of neutral spawners\.

## [](#count)Count

`Camps.Count():` `integer`

Return size of neutral spawner list\.

## [](#get)Get

`Camps.Get(index):` [`CCamp`](https://uczone.gitbook.io/api-v2.0/game-components/core/camp) \| `nil`

Name

Type

Description

**index**

`integer`

Index of neutral spawner in cheat list\.

Return neutral spawner by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`Camps.GetAll():` [`CCamp[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/camp)

Return all neutral spawners in cheat list\.

## [](#inradius)InRadius

`Camps.InRadius(pos, radius):` [`CCamp[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/camp)

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check\.

**radius**

`number`

Radius to check\.

Return all neutral spawners in radius\.

## [](#contains)Contains

`Camps.Contains(camp):` `boolean`

**camp**

[`CCamp`](https://uczone.gitbook.io/api-v2.0/game-components/core/camp)

Neutral spawner to check\.

Check neutral spawner in cheat list\.

Last updated 19 days ago

