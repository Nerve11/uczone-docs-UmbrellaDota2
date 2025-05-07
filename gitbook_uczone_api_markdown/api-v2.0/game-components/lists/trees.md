# 🌲Trees

Table to work with list of trees\.

## [](#count)Count

`Trees.Count():` `integer`

Return size of tree list\.

## [](#get)Get

`Trees.Get(index):` [`CTree`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) \| `nil`

Name

Type

Description

**index**

`integer`

Index of tree in cheat list\.

Return tree by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`Trees.GetAll():` [`CTree[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Return all trees in cheat list\.

## [](#inradius)InRadius

`Trees.InRadius(pos, radius, [active]):` [`CTree[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check\.

**radius**

`number`

Radius to check\.

**active**`[?]`

`boolean`

Active state to check\. `(default: true)`

Return all trees in radius\.

## [](#contains)Contains

`Trees.Contains(tree):` `boolean`

**tree**

[`CTree`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Tree to check\.

Check tree in cheat list\.

Last updated 19 days ago

