# 🌳TempTrees

Table to work with list of temp trees\.

## [](#count)Count

`TempTrees.Count():` `integer`

Return size of temp trees list\.

## [](#get)Get

`TempTrees.Get(index):` [`CTree`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) \| `nil`

Name

Type

Description

**index**

`integer`

Index of temp tree in cheat list\.

Return temp tree by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`TempTrees.GetAll():` [`CTree[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Return all temp trees in cheat list\.

## [](#inradius)InRadius

`TempTrees.InRadius(pos, radius):` [`CTree[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check\.

**radius**

`number`

Radius to check\.

Return all temp trees in radius\.

## [](#contains)Contains

`TempTrees.Contains(tree):` `boolean`

**tree**

[`CTree`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Temp tree to check\.

Check temp tree in cheat list\.

Last updated 19 days ago

