# 🔄Angle

Angle metatable

### [](#fields)Fields

Name

Type

Description

**pitch**

`number`

**yaw**

**roll**

## [](#angle)Angle

`Angle([pitch], [yaw], [roll]):` [`Angle`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

**pitch**`[?]`

`(default: 0.0)`

**yaw**`[?]`

**roll**`[?]`

Create a new Angle\.

## [](#tostring)\_\_tostring

`:__tostring():` `string`

## [](#getforward)GetForward

`:GetForward():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward vector from a given Angle\.

## [](#getvectors)GetVectors

`:GetVectors():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)\, [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)\, [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward\, right and up\.

## [](#getyaw)GetYaw

`:GetYaw():` `number`

Returns the yaw\. The same as Angle\.yaw\.

## [](#getroll)GetRoll

`:GetRoll():` `number`

Returns the roll\. The same as Angle\.roll\.

## [](#getpitch)GetPitch

`:GetPitch():` `number`

Returns the pitch\. The same as Angle\.pitch\.

## [](#setyaw)SetYaw

`:SetYaw(value):` `nil`

**value**

Sets the yaw\. The same as Angle\.yaw = value\.

## [](#setroll)SetRoll

`:SetRoll(value):` `nil`

Sets the roll\. The same as Angle\.roll = value\.

## [](#setpitch)SetPitch

`:SetPitch(value):` `nil`

Sets the pitch\. The same as Angle\.pitch = value\.

Last updated 19 days ago

