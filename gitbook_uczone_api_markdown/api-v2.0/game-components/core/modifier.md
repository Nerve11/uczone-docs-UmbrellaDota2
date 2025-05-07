# ✨Modifier

Table to work with `CModifier`\.
You can get modifiers from `NPC.GetModifier`function\.

## [](#getname)GetName

`Modifier.GetName(modifier):` `string`

Name

Type

Description

**modifier**

[`CModifier`](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier)

modifier to get name of

Returns the name of the modifier\.

## [](#getclass)GetClass

`Modifier.GetClass(modifier):` `string`

Returns the name of the modifier's class\.

## [](#getmodifieraura)GetModifierAura

Deprecated\.

`Modifier.GetModifierAura(modifier):` `string`

modifier to get aura of

Should return the name of the modifier's aura\, but instead\, it returns an empty string in all
the cases I have tested\.

## [](#getserialnumber)GetSerialNumber

`Modifier.GetSerialNumber(modifier):` `integer`

modifier to get serial number of

Should return the serial number of the modifier\, but instead\, it returns 0 in all the cases I
have tested\.

## [](#getstringindex)GetStringIndex

`Modifier.GetStringIndex(modifier):` `integer`

modifier to get string index of

Should return the string index of the modifier\, but instead\, it returns 0 in all the cases I
have tested\.

## [](#getindex)GetIndex

`Modifier.GetIndex(modifier):` `GetIndex`

modifier to get index of

Returns the hero's modifier index\. The index is an incrementable value with each new modifier
the NPC gets

## [](#getcreationtime)GetCreationTime

`Modifier.GetCreationTime(modifier):` `number`

modifier to get creation time of

Returns the game time when the modifier was created\.

## [](#getcreationframe)GetCreationFrame

`Modifier.GetCreationFrame(modifier):` `integer`

modifier to get creation frame of

Returns the frame when the modifier was created\. You could get current frame count from
`GlobalVars.GetFrameCount` function\.

## [](#getlastappliedtime)GetLastAppliedTime

`Modifier.GetLastAppliedTime(modifier):` `number`

modifier to get last applied time of

Returns the game time when the modifier was last applied\. Don't know cases when it can be
different from `GetCreationTime`\.

## [](#getduration)GetDuration

`Modifier.GetDuration(modifier):` `number`

modifier to get duration of

Returns the duration of the modifier\.

## [](#getdietime)GetDieTime

`Modifier.GetDieTime(modifier):` `number`

modifier to get expiration time of

Returns the game time when the modifier will expire\.

## [](#getstackcount)GetStackCount

`Modifier.GetStackCount(modifier):` `integer`

modifier to get stack count of

If there are stacks of the modifier\, it returns the amount of stacks; otherwise\, it returns
0\.

## [](#getaurasearchteam)GetAuraSearchTeam

`Modifier.GetAuraSearchTeam(modifier):` `integer`

modifier to get aura search team of

Returns aura search team of the modifier\.

## [](#getaurasearchtype)GetAuraSearchType

`Modifier.GetAuraSearchType(modifier):` `integer`

modifier to get aura search type of

Returns aura search type of the modifier\.

## [](#getaurasearchflags)GetAuraSearchFlags

`Modifier.GetAuraSearchFlags(modifier):` `integer`

modifier to get aura search flags of

Returns aura search flags of the modifier\.

## [](#getauraradius)GetAuraRadius

`Modifier.GetAuraRadius(modifier):` `number`

modifier to get aura radius of

Returns aura radius of the modifier\.

## [](#getteam)GetTeam

`Modifier.GetTeam(modifier):` [`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

modifier to get team of

Returns team of the modifier\.

## [](#getattributes)GetAttributes

`Modifier.GetAttributes(modifier):` `integer`

modifier to get attributes of

Returns the attributes of the modifier\.

## [](#isaura)IsAura

`Modifier.IsAura(modifier):` `boolean`

modifier to check

Returns `true` if the modifier is an aura\.

## [](#isauraactiveondeath)IsAuraActiveOnDeath

`Modifier.IsAuraActiveOnDeath(modifier):` `boolean`

Returns `true` if the modifier aura active on death\.

## [](#getmarkedfordeletion)GetMarkedForDeletion

`Modifier.GetMarkedForDeletion(modifier):` `boolean`

Returns `true` if the modifier is marked for deletion\.

## [](#getauraisheal)GetAuraIsHeal

`Modifier.GetAuraIsHeal(modifier):` `boolean`

Returns `true` if aura is heal\.

## [](#getprovidedbyaura)GetProvidedByAura

`Modifier.GetProvidedByAura(modifier):` `boolean`

Returns `true` if modifier is provided by an aura\.

## [](#getprevioustick)GetPreviousTick

`Modifier.GetPreviousTick(modifier):` `number`

modifier to get last tick time of

Returns the game time of the last modifier tick \(~0\.033 seconds\)\.

## [](#getthinkinterval)GetThinkInterval

`Modifier.GetThinkInterval(modifier):` `number`

modifier to get think interval of

Returns the modifier's think interval\.

## [](#getthinktimeaccumulator)GetThinkTimeAccumulator

\`Modifier\.GetThinkTimeAccumulator\(modifier\):\` \*\*\`number\`\*\*

modifier to get think time accumulator of

Return the modifier's think interval time accumulator\.

## [](#iscurrentlyinaurarange)IsCurrentlyInAuraRange

`Modifier.IsCurrentlyInAuraRange(modifier):` `boolean`

Returns `true` if is in aura range\.

## [](#getability)GetAbility

`Modifier.GetAbility(modifier):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

modifier to get ability of

Returns the modifier's ability\.

## [](#getauraowner)GetAuraOwner

`Modifier.GetAuraOwner(modifier):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

modifier

Returns the owner of aura

## [](#getparent)GetParent

`Modifier.GetParent(modifier):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Returns the parent of modifier

## [](#getcaster)GetCaster

`Modifier.GetCaster(modifier):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Returns caster of modifier

## [](#getstate)GetState

`Modifier.GetState(modifier):` `number`\, `number`

modifier to get state of

Returns the modifier state masks\. See the example\.

#### [](#example)Example

```
local m_nEnabledStateMask, m_nDisabledStateMask = Modifier.GetState(mod)
local mod_is_hex = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_HEXED & 1) > 0
local mod_is_stun = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_STUNNED & 1) > 0
```

## [](#isdebuff)IsDebuff

`Modifier.IsDebuff(modifier):` `boolean`

Returns `true` if the modifier is a debuff\.

## [](#getfield)GetField

`Modifier.GetField(modifier, fieldName, dbgPrint):` `any`

modifier to get field from

**fieldName**

`string`

field name

**dbgPrint**

`boolean`

print possible errors

Returns value of the field\.

Last updated 12 days ago

