# 👾Entity

Table to work with `CEntity`\.

`CEntity` is base class for all entities in the game e\.g\.`CNPC`\, `Hero`\,`CPlayer`\, `CAbility`

## [](#isentity)IsEntity

`Entity.IsEntity(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in entity list\. Search in unordered set\.

## [](#isnpc)IsNPC

`Entity.IsNPC(entity):` `boolean`

Returns `true` if the entity is in NPC list\. Search in unordered set\.

## [](#ishero)IsHero

`Entity.IsHero(entity):` `boolean`

Returns `true` if the entity is in hero list\. Search in unordered set\.

## [](#isplayer)IsPlayer

`Entity.IsPlayer(entity):` `boolean`

Returns `true` if the entity is in player list\. Search in unordered set\.

## [](#isability)IsAbility

`Entity.IsAbility(entity):` `boolean`

Returns `true` if the entity is in ability list\. Search in unordered set\. Item is ability\.

## [](#get)Get

Not the same as Entities\.Get\(index\)\. See example\.

`Entity.Get(index):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

**index**

`integer`

Returns entity by game index\.

#### [](#example)Example

```
-- get_by_index.lua
local hero = Heroes.GetLocal();
local index = Entity.GetIndex(hero);
local entity_by_index = Entity.Get(index);
assert(hero == entity_by_index, "Entity.Get() is broken!"); -- true
```

## [](#getindex)GetIndex

`Entity.GetIndex(entity):` `integer`

Returns game index of entity\.

## [](#getclassname)GetClassName

`Entity.GetClassName(entity):` `string`

Returns the entity's class name\.

## [](#getunitname)GetUnitName

`Entity.GetUnitName(entity):` `string`

Returns the entity's name\.

## [](#getunitdesignername)GetUnitDesignerName

`Entity.GetUnitDesignerName(entity):` `string`

Returns the entity's designerName field\.

## [](#getteamnum)GetTeamNum

`Entity.GetTeamNum(entity):` [`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Returns the entity's team number\.

## [](#issameteam)IsSameTeam

`Entity.IsSameTeam(entity1, entity2):` `boolean`

**entity1**

**entity2**

Returns `true` if the entities are in the same team\.

## [](#getabsorigin)GetAbsOrigin

`Entity.GetAbsOrigin(entity):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the entity's position\.

## [](#getnetorigin)GetNetOrigin

`Entity.GetNetOrigin(entity):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the entity's net position\.

## [](#getrotation)GetRotation

`Entity.GetRotation(entity):` [`Angle`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Returns the entity's rotation\.

#### [](#example-1)Example

```
-- forward_pos.lua
return {
    -- get local hero's forward position and draw a circle around it
    OnUpdate = function ()
        local hero = Heroes.GetLocal();
        local rotation = Entity.GetRotation(hero);
        -- forward_direction is a vector that points 100 units in direction of my hero's rotation
        local forward_direction = rotation:GetForward():Normalized():Scaled(100);
        -- add forward_direction to my hero's position to get the forward position
        local forward_pos = Entity.GetAbsOrigin(hero) + forward_direction;
        -- screen_x and screen_y are the coordinates of forward_pos on the screen
        local screen_x, screen_y, is_on_screen = Renderer.WorldToScreen(forward_pos);
        if is_on_screen then
            -- draw a circle around the position
            Renderer.SetDrawColor(255, 255, 255, 255);
            Renderer.DrawFilledCircle(screen_x, screen_y, 10, 10);
            -- result: https://i.imgur.com/ERf1Pxk.png
        end
    end
}
```

## [](#isalive)IsAlive

`Entity.IsAlive(entity):` `boolean`

Returns `true` if the entity is alive\.

## [](#isdormant)IsDormant

`Entity.IsDormant(entity):` `boolean`

Returns `true` if the entity is not visible to the local player\.

## [](#gethealth)GetHealth

`Entity.GetHealth(entity):` `integer`

Returns the entity's health\.

## [](#getmaxhealth)GetMaxHealth

`Entity.GetMaxHealth(entity):` `integer`

Returns the entity's max health\.

## [](#getowner)GetOwner

`Entity.GetOwner(entity):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Returns the entity's owner or `nil` if the entity has no owner\.\\
e\.g\. for `CPlayer` \-> `npc_dota_hero_ember_spirit` \-> `npc_dota_hero_ember_spirit_fire_remnant`
ownership chain `Entity.GetOwner(remnant)` will return Ember Spirit's entity\.

## [](#ownedby)OwnedBy

`Entity.OwnedBy(entity, owner):` `boolean`

\- entity to check

**owner**

\- owner for comparison

Returns `true` if the entity is owned by another entity\-owner\. It will check the first owner only\.

## [](#recursivegetowner)RecursiveGetOwner

`Entity.RecursiveGetOwner(entity):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Returns the entity's last owner\.\\
e\.g\. for `CPlayer` \-> `npc_dota_hero_ember_spirit` \-> `npc_dota_hero_ember_spirit_fire_remnant`
ownership chain `Entity.GetOwner(remnant)` will return `CPlayer`\.

## [](#recursiveownedby)RecursiveOwnedBy

`Entity.RecursiveOwnedBy(entity, owner):` `boolean`

entity to check

owner for comparison

Returns `true` if the entity is owned by another entity\-owner\. It will check the whole ownership chain\.

## [](#getheroesinradius)GetHeroesInRadius

`Entity.GetHeroesInRadius(entity, radius, [teamType], [skipIllusions]):` [`CHero[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

entity to get position

**radius**

`number`

radius to search around

**teamType**`[?]`

[`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

relative to the entity `(default: TEAM_ENEMY)`

**skipIllusions**`[?]`

`boolean`

`true` if you want to get table without illusions `(default: true)`

Returns an array of all alive and visible heroes in radius of the entity\. Exclude illusion\.

#### [](#example-2)Example

```
local hero = Heroes.GetLocal()
-- get all enemy heroes in 1200 radius
local heroes_around = Entity.GetHeroesInRadius(hero, 1200)
for i = 1, #heroes_around do
	local hero = heroes_around[i];
	Log.Write(NPC.GetUnitName(hero) .. " is near!");
end
```

## [](#getunitsinradius)GetUnitsInRadius

`Entity.GetUnitsInRadius(entity, radius, [teamType], [skipIllusions]):` [`CNPC[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

Returns an array of all alive and visible NPCs in radius of the entity\.

#### [](#example-3)Example

```
local hero = Heroes.GetLocal()
-- get all ally NPCs in 1200 radius
local units_around = Entity.GetUnitsInRadius(hero, 1200, Enum.TeamType.TEAM_FRIEND)
for i = 1, #units_around do
	local unit = units_around[i];
	Log.Write(NPC.GetUnitName(unit) .. " is near!");
end
```

## [](#gettreesinradius)GetTreesInRadius

Active means that tree is not destroyed\.

`Entity.GetTreesInRadius(entity, radius, [active]):` [`CTree[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

**active**`[?]`

`true` if you want to get table with active trees only\, otherwise for inactive trees `(default: true)`

Returns an array of all not temporary trees in radius of the entity\.

#### [](#example-4)Example

```
local hero = Heroes.GetLocal()
-- get all trees in 400 radius
local trees_around = Entity.GetTreesInRadius(hero, 400, true)
for i = 1, #trees_around do
	local tree = trees_around[i];
	Log.Write(Entity.GetClassName(tree) .. " is near!");
end
```

## [](#gettemptreesinradius)GetTempTreesInRadius

Temporary trees are trees planted by abilities or items\.

\`Entity\.GetTempTreesInRadius\(entity\, radius\):\` \[\*\*\`CTree\[\]\`\*\*\]\(Tree\.md\)

Returns an array of all temporary trees in radius of the entity\.

#### [](#example-5)Example

```
local hero = Heroes.GetLocal()
-- get all trees in 400 radius
local trees_around = Entity.GetTempTreesInRadius(hero, 400)
for i = 1, #trees_around do
	local tree = trees_around[i];
	Log.Write(Entity.GetClassName(tree) .. " is near!");
end
```

## [](#iscontrollablebyplayer)IsControllableByPlayer

`Entity.IsControllableByPlayer(entity, playerId):` `boolean`

**playerId**

player id

Returns `true` if entity is controllable by player\.

## [](#getroshanhealth)GetRoshanHealth

`Entity.GetRoshanHealth():` `integer`

Returns Roshan's health\. Onyly works in unsafe mode\.

## [](#getforwardposition)GetForwardPosition

`Entity.GetForwardPosition(entity, distance):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**distance**

distance to move forward

Returns position in front of entity or \(0\,0\,0\) if entity is invalid\.

## [](#getclassid)GetClassID

`Entity.GetClassID(entity):` `integer`

entity to get class id

Returns entity class id\. Could be as a optimized way to check entity type\.

## [](#getfield)GetField

`Entity.GetField(entity, fieldName, dbgPrint):` `any`

entity to get field from

**fieldName**

`string`

field name

**dbgPrint**

print possible errors

Returns value of the field\.

Last updated 19 days ago

