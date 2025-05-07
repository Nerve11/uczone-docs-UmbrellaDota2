# 🎭NPCs

Table to work with NPC list\.

## [](#count)Count

`NPCs.Count():` `integer`

Return size of NPC list\.

## [](#get)Get

`NPCs.Get(index):` [`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| `nil`

Name

Type

Description

**index**

`integer`

Index of NPC in cheat list\.

Return NPC by index in cheat list\. Not the same as in\-game index\.

## [](#getall)GetAll

`NPCs.GetAll([filter]):` [`CNPC[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

**filter**`[?]`

[`Enum.UnitTypeFlags`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags) \| `fun(npc: CNPC):boolean`

`(default: nil)`

Return all NPCs in cheat list\. Can be filtered by unit type or custom function\.
Unit type filter is a much faster than custom function and can be or'ed to filter multiple types\.

#### [](#example)Example

```
-- filter function to get all structures except towers
for _, v in pairs(NPCs.GetAll(function (npc)
     return NPC.IsStructure(npc) and not NPC.IsTower(npc);
end)) do
     print(NPC.GetUnitName(v))
end

-- get all towers and heroes (x5 times faster than filter function)
for _, v in pairs(NPCs.GetAll(Enum.UnitTypeFlags.TYPE_TOWER | Enum.UnitTypeFlags.TYPE_HERO)) do
		print(NPC.GetUnitName(v))
end
```

## [](#inradius)InRadius

`NPCs.InRadius(pos, radius, teamNum, teamType):` [`CNPC[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

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

Return all NPCs in radius\.

## [](#contains)Contains

`NPCs.Contains(npc):` `boolean`

**npc**

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

NPC to check\.

Check NPC in cheat list\.

Last updated 19 days ago

