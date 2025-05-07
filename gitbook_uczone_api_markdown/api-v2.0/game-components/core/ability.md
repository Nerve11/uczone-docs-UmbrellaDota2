# 🌟Ability

Table to work with `CAbility`\.

`CAbility` extends `CEntity`

## [](#getowner)GetOwner

`Ability.GetOwner(ability):` [`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

Name

Type

Description

**ability**

[`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

Returns the ability owner\.

## [](#ispassive)IsPassive

`Ability.IsPassive(ability):` `boolean`

Returns `true` if the ability is passive\.

## [](#isbasic)IsBasic

`Ability.IsBasic(ability):` `boolean`

Returns `true` if the ability is basic\.

## [](#isultimate)IsUltimate

`Ability.IsUltimate(ability):` `boolean`

Returns `true` if the ability is an ultimate\.

## [](#isattributes)IsAttributes

`Ability.IsAttributes(ability):` `boolean`

Returns `true` if the ability is an attribute or a talent\.

## [](#gettype)GetType

`Ability.GetType(ability):` [`Enum.AbilityTypes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitytypes)

Returns the ability type\.

## [](#getbehavior)GetBehavior

`Ability.GetBehavior(ability):` [`Enum.AbilityBehavior`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitybehavior)

## [](#gettargetteam)GetTargetTeam

`Ability.GetTargetTeam(ability):` [`Enum.TargetTeam`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targetteam)

Returns the target team of this Ability\.

## [](#gettargettype)GetTargetType

`Ability.GetTargetType(ability):` [`Enum.TargetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targettype)

Returns the target type of this Ability\.

## [](#gettargetflags)GetTargetFlags

`Ability.GetTargetFlags(ability):` [`Enum.TargetFlags`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targetflags)

Returns the target flags of this Ability\.

## [](#getdamagetype)GetDamageType

`Ability.GetDamageType(ability):` [`Enum.DamageTypes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.damagetypes)

Returns the damage type of this Ability\.

## [](#getimmunitytype)GetImmunityType

`Ability.GetImmunityType(ability):` [`Enum.ImmunityTypes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.immunitytypes)

Returns the immunity type of this Ability\.

## [](#getdispellabletype)GetDispellableType

`Ability.GetDispellableType(ability):` [`Enum.DispellableTypes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.dispellabletypes)

Returns the dispel type of this Ability\.

## [](#getlevelspecialvaluefor)GetLevelSpecialValueFor

`Ability.GetLevelSpecialValueFor(ability, name, [lvl]):` `number`

**name**

`string`

Special value name\. Can be found in the ability KV file\. \(`assets/data/npc_abilities.json`\)

**lvl**`[?]`

`integer`

Ability level\, if \-1 will automatically get lvl\. `(default: -1)`

WRONG API FIX ME IT MUST BE GetSpecialValueFor\.

## [](#isready)IsReady

`Ability.IsReady(ability):` `boolean`

Returns `true` if the ability is ready to use\.

## [](#secondssincelastuse)SecondsSinceLastUse

`Ability.SecondsSinceLastUse(ability):` `number`

Returns the number of seconds passed from the last usage of the ability\. Will return \-1 if
the ability is not on the cooldown\.

## [](#getdamage)GetDamage

`Ability.GetDamage(ability):` `number`

Returns the ability damage from assets/data/npc\_abilities\.json field\. Will return 0\.0 if the
ability doesn't contain this field\.

## [](#getlevel)GetLevel

`Ability.GetLevel(ability):` `integer`

Returns the current ability level\.

## [](#getcastpoint)GetCastPoint

`Ability.GetCastPoint(ability, [include_modifiers]):` `number`

**include\_modifiers**`[?]`

`boolean`

`(default: true)`

Gets the cast delay of this Ability\.

## [](#getcastpointmodifier)GetCastPointModifier

`Ability.GetCastPointModifier(ability):` `number`

Gets the cast delay modifier of this Ability\.

## [](#iscastable)IsCastable

`Ability.IsCastable(ability, [mana]):` `boolean`

**mana**`[?]`

`number`

`(default: 0.0)`

Returns `true` if the ability is currently castable\. Checks for mana cost\, cooldown\, level\,
and slot for items\.

## [](#ischannelling)IsChannelling

`Ability.IsChannelling(ability):` `boolean`

Returns `true` if the ability is in channeling state\. Example: teleport\, rearm\, powershot
etc\.

## [](#getname)GetName

`Ability.GetName(ability):` `string`

Returns the ability name or empty string\.

## [](#getbasename)GetBaseName

`Ability.GetBaseName(ability):` `string`

Returns the ability base name or empty string\.

## [](#isinnate)IsInnate

`Ability.IsInnate(ability):` `boolean`

Returns `true` if the ability is innate\.

## [](#isinnatepassive)IsInnatePassive

`Ability.IsInnatePassive(ability):` `boolean`

Returns `true` if the ability is passive innate\.

## [](#getmaxlevel)GetMaxLevel

`Ability.GetMaxLevel(ability):` `integer`

Returns ability's max level\.

## [](#isgrantedbyfacet)IsGrantedByFacet

`Ability.IsGrantedByFacet(ability):` `boolean`

Returns `true` when abiliti is granted by facet\.

## [](#canbeexecuted)CanBeExecuted

`Ability.CanBeExecuted(ability):` [`Enum.AbilityCastResult`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitycastresult)

Returns `-1` if ability can be executed\.

## [](#isownersmanaenough)IsOwnersManaEnough

`Ability.IsOwnersManaEnough(ability):` `boolean`

Returns `true` if enough mana for cast\.

## [](#castnotarget)CastNoTarget

`Ability.CastNoTarget(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

**queue**`[?]`

Will add order to the cast queue\. `(default: false)`

**push**`[?]`

Will push order to the OnPrepareUnitOrders callback\. `(default: false)`

**execute\_fast**`[?]`

Will push order to start of the order's list\. `(default: false)`

**identifier**`[?]`

The identifier which will be passed to `OnPrepareUnitOrders` callback\. `(default: nil)`

Casts the ability that doesn't require a target or position\.

## [](#castposition)CastPosition

`Ability.CastPosition(ability, pos, [queue], [push], [execute_fast], [identifier], [force_minimap]):` `nil`

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Order position\.

**force\_minimap**`[?]`

If true\, the order will be forced by the minimap if possible\. `(default: true)`

Casts the ability at a specified position\.

## [](#casttarget)CastTarget

`Ability.CastTarget(ability, target, [queue], [push], [execute_fast], [identifier]):` `nil`

**target**

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

Order target\.

Casts the ability on a specified target\.

## [](#toggle)Toggle

`Ability.Toggle(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

Toggles the ability\. Example: Armlet\.

## [](#togglemod)ToggleMod

`Ability.ToggleMod(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

Toggles the ability modifier\. Example: Frost Arrows\, Medusa's Shield\.

## [](#canbeupgraded)CanBeUpgraded

`Ability.CanBeUpgraded(ability):` [`Enum.AbilityLearnResult`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitylearnresult) \| `nil`

Returns if the ability is upgradable with a specific reason\.

## [](#getindex)GetIndex

`Ability.GetIndex(ability):` `integer`

Returns the index of the ability in the ability owner's list\. The index can be used in
NPC\.GetAbilityByIndex later\.

## [](#getcastrange)GetCastRange

`Ability.GetCastRange(ability):` `number`

Returns the cast range of the ability\.

## [](#ishidden)IsHidden

`Ability.IsHidden(ability):` `boolean`

Returns `true` if ability is hidden\. Example: Zeus's Nimbus before purchasing agh\.

## [](#isactivated)IsActivated

`Ability.IsActivated(ability):` `boolean`

Returns `true` if the ability is in an activated state\.

## [](#getdirtybuttons)GetDirtyButtons

`Ability.GetDirtyButtons(ability):` `integer`

Returns we don't know what :\)\.

## [](#gettogglestate)GetToggleState

`Ability.GetToggleState(ability):` `boolean`

Returns if the ability is toggled\. Example: Medusa's Shield\.

## [](#isinabilityphase)IsInAbilityPhase

`Ability.IsInAbilityPhase(ability):` `boolean`

Returns `true` if the ability is in the cast state\. Examples: Nature's Prophet's Teleport\,
Meepo's Poof\.

## [](#getcooldown)GetCooldown

`Ability.GetCooldown(ability):` `number`

Returns the amount of time before the ability can be cast\.

## [](#getcooldownlength)GetCooldownLength

`Ability.GetCooldownLength(ability):` `number`

Returns the amount of time the ability couldn't be cast after being used\.

## [](#getmanacost)GetManaCost

`Ability.GetManaCost(ability):` `number`

Returns the ability mana cost\.

## [](#getautocaststate)GetAutoCastState

`Ability.GetAutoCastState(ability):` `boolean`

Returns the autocast state of the ability\.

## [](#getaltcaststate)GetAltCastState

`Ability.GetAltCastState(ability):` `boolean`

Returns the alt cast state of the ability\. Example: Doom's Devour\.

## [](#getchannelstarttime)GetChannelStartTime

`Ability.GetChannelStartTime(ability):` `number`

Returns the gametime the channeling of the ability will start\. Requires the ability to be in
the cast state when called\.

## [](#getcaststarttime)GetCastStartTime

`Ability.GetCastStartTime(ability):` `number`

Returns the gametime the ability will be casted\. Requires the ability to be in the cast state
when called\.

## [](#isinindefinatecooldown)IsInIndefinateCooldown

`Ability.IsInIndefinateCooldown(ability):` `boolean`

Returns `true` if the cooldown of the ability is indefinite\.

## [](#isinindefinatecooldown-1)IsInIndefinateCooldown

Returns `true` if the cooldown of the ability is frozen\.

## [](#getoverridecastpoint)GetOverrideCastPoint

`Ability.GetOverrideCastPoint(ability):` `number`

Returns the overridden cast point\. Example: Arcane Blink\.

## [](#isstolen)IsStolen

`Ability.IsStolen(ability):` `boolean`

Returns `true` if the ability is stolen\.

## [](#getcurrentcharges)GetCurrentCharges

`Ability.GetCurrentCharges(ability):` `integer`

Returns the number of charges available\.

## [](#chargerestoretimeremaining)ChargeRestoreTimeRemaining

`Ability.ChargeRestoreTimeRemaining(ability):` `integer`

Returns the remaining time for the next charge to restore\.

## [](#getkeybind)GetKeybind

`Ability.GetKeybind(ability):` `string`

`Ability`

Returns the keybind of the ability\.

Last updated 19 days ago

