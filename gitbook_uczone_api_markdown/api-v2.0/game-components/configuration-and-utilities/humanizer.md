# 🤖Humanizer

Table to work with humanizer\.

## [](#isinservercamerabounds)IsInServerCameraBounds

`Humanizer.IsInServerCameraBounds(pos):` `boolean`

Name

Type

Description

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

Returns `true` if the world position is in server camera bounds\.

## [](#getservercamerapos)GetServerCameraPos

`Humanizer.GetServerCameraPos():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns server camera position\.

## [](#getorderqueue)GetOrderQueue

`Humanizer.GetOrderQueue():` `{player: CPlayer, orderType: Enum.UnitOrder, targetIndex: integer, position: Vector, abilityIndex: integer, orderIssuer: Enum.PlayerOrderIssuer, unit: CNPC, orderQueueBehavior: integer, showEffects: boolean, triggerCallBack: boolean, isByMiniMap: boolean, addTime: number }[]`

Returns information about the current humanizer order queue\.

## [](#issafetarget)IsSafeTarget

`Humanizer.IsSafeTarget(entity):` `boolean`

**entity**

[`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)

## [](#forceuserorderbyminimap)ForceUserOrderByMinimap

`Humanizer.ForceUserOrderByMinimap():` `nil`

Forces current user order by minimap\. Must be called in OnPrepareUnitOrder

Last updated 19 days ago

