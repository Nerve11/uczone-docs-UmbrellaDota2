# 🦸Hero

Table to work with `CHero`\.

`CHero` extends `CNPC`

## [](#getcurrentxp)GetCurrentXP

`Hero.GetCurrentXP(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

Returns the hero's current XP\.

## [](#getabilitypoints)GetAbilityPoints

`Hero.GetAbilityPoints(hero):` `integer`

Returns the hero's available ability points\.

## [](#getrespawntime)GetRespawnTime

Could be less than current game time if hero is already alive\.

\`Hero\.GetRespawnTime\(hero\):\` \*\*\`number\`\*\*

Returns the game time when the hero will respawn\.

## [](#getrespawntimepenalty)GetRespawnTimePenalty

`Hero.GetRespawnTimePenalty(hero):` `number`

Returns the next respawn time penalty\, e\.g\. buyback\.

## [](#getprimaryattribute)GetPrimaryAttribute

`Hero.GetPrimaryAttribute(hero):` [`Enum.Attributes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Returns the hero's primary attribute type\.

## [](#getstrength)GetStrength

`Hero.GetStrength(hero):` `number`

Returns `white` value of strength\.

## [](#getagility)GetAgility

`Hero.GetAgility(hero):` `number`

Returns `white` value of agility\.

## [](#getintellect)GetIntellect

`Hero.GetIntellect(hero):` `number`

Returns `white` value of intellect\.

## [](#getstrengthtotal)GetStrengthTotal

`Hero.GetStrengthTotal(hero):` `number`

Returns total value of strength\.

## [](#getagilitytotal)GetAgilityTotal

`Hero.GetAgilityTotal(hero):` `number`

Returns total value of agility\.

## [](#getintellecttotal)GetIntellectTotal

`Hero.GetIntellectTotal(hero):` `number`

Returns total value of intellect\.

## [](#getlasthurttime)GetLastHurtTime

`Hero.GetLastHurtTime(hero):` `number`

Returns the time when the hero was last hurt\.

## [](#gethurtamount)GetHurtAmount

`Hero.GetHurtAmount(hero):` `number`

Returns the amount of damage the hero last received\.

## [](#getrecentdamage)GetRecentDamage

`Hero.GetRecentDamage(hero):` `integer`

Returns the damage taken by the hero in the last in ~1 second\.

## [](#getpainfactor)GetPainFactor

`Hero.GetPainFactor(hero):` `number`

Returns the pain factor of the hero\. Not sure what it is\.

## [](#gettargetpainfactor)GetTargetPainFactor

`Hero.GetTargetPainFactor(hero):` `number`

Returns the pain factor of the hero's target\. Not sure what it is\.

## [](#getlifestate)GetLifeState

`Hero.GetLifeState(hero):` `boolean`

Returns `true` if the hero is alive\. Recommended to use `Entity.IsAlive` instead\.

## [](#getplayerid)GetPlayerID

`Hero.GetPlayerID(hero):` `integer`

Returns the ID of the hero player\.

## [](#getreplicatingotherheromodel)GetReplicatingOtherHeroModel

`Hero.GetReplicatingOtherHeroModel(hero):` [`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) \| `nil`

If the hero is an illusion\, Arc's copy\, Meepo clone\, etc\. returns the original hero\, otherwise returns nil\.

## [](#talentislearned)TalentIsLearned

`Hero.TalentIsLearned(hero, talent):` `boolean`

**talent**

[`Enum.TalentTypes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.talenttypes)

Returns `true` if talent is learned\.

#### [](#example)Example

```
TALENT_8 <=> TALENT_7
TALENT_6 <=> TALENT_5
TALENT_4 <=> TALENT_3
TALENT_2 <=> TALENT_1
```

## [](#getfacetabilities)GetFacetAbilities

`Hero.GetFacetAbilities(hero):` [`CAbility[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

Returns facet ability array\.

## [](#getfacetid)GetFacetID

`Hero.GetFacetID(hero):` `integer`

Returns facet id\. Start from 1\.

## [](#getlastmaphackpos)GetLastMaphackPos

`Hero.GetLastMaphackPos(hero):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| `nil`

Returns the last hero pos from maphack\.

Last updated 19 days ago

