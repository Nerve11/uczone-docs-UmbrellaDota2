# 🚚Courier

Table to work with `CCourier`\.`CCourier` extends `CNPC`

## [](#isflyingcourier)IsFlyingCourier

`Courier.IsFlyingCourier(courier):` `boolean`

Name

Type

Description

**courier**

[`CCourier`](https://uczone.gitbook.io/api-v2.0/game-components/core/courier)

The courier to check\.

Returns `true` if the courier is flying\.

## [](#getrespawntime)GetRespawnTime

`Courier.GetRespawnTime(courier):` `number`

Returns the game time when the courier will respawn\.

## [](#getcourierstate)GetCourierState

`Courier.GetCourierState(courier):` [`Enum.CourierState`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.courierstate)

Returns the courier state\.

## [](#getplayerid)GetPlayerID

`Courier.GetPlayerID(courier):` `integer`

Returns owner's player id\.

## [](#getcourierstateentity)GetCourierStateEntity

`Courier.GetCourierStateEntity(courier):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Returns the entity that the courier is currently interacting with\.

Last updated 19 days ago

