# 🎭NPC

Table to work with `CNPC`\.`CNPC` extends `CEntity`

## [](#getownernpc)GetOwnerNPC

`NPC.GetOwnerNPC(npc):` [`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| `nil`

Name

Type

Description

**npc**

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

npc to get owner from

Returns owner of the `CNPC`\. Works for spirit bear\.

## [](#getitem)GetItem

`NPC.GetItem(npc, name, [isReal]):` [`CItem`](https://uczone.gitbook.io/api-v2.0/game-components/core/item) \| `nil`

npc to get item from

**name**

`string`

name of the item

**isReal**`[?]`

`boolean`

if true\, returns only 1\-6 slots and neutral item\, otherwise returns all items \(including backpack and stash\) `(default: true)`

Returns `CItem` by name\.

## [](#hasitem)HasItem

`NPC.HasItem(npc, name, [isReal]):` `boolean`

npc to check

Returns `true` if the `CNPC` has item with specified name\.

## [](#hasmodifier)HasModifier

`NPC.HasModifier(npc, name):` `boolean`

name of the modifier

Returns `true` if the `CNPC` has modifier with specified name\.

## [](#getmodifier)GetModifier

`NPC.GetModifier(npc, name):` [`CModifier`](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) \| `nil`

npc to get modifier from

Returns `CModifier` by name\.

## [](#getmodifiers)GetModifiers

\`poperty\_filter\` doesn\`t filter all modifiers every call\, it uses already prefiltered list\.

`NPC.GetModifiers(npc, [poperty_filter]):` [`CModifier[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier)

npc to get modifiers from

**poperty\_filter**`[?]`

[`Enum.ModifierFunction`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction)

Filter modifiers by specified property `(default: Enum.ModifierFunction.MODIFIER_FUNCTION_INVALID)`

Returns an array of all NPC's `CModifier`s\.

## [](#hasinventoryslotfree)HasInventorySlotFree

`NPC.HasInventorySlotFree(npc, [isReal]):` `boolean`

Returns `true` if the `CNPC` has free inventory slot\.

## [](#hasstate)HasState

`NPC.HasState(npc, state):` `boolean`

**state**

[`Enum.ModifierState`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierstate)

state to check

Returns `true` if the `CNPC` has state\. The best way to check if the `CNPC` is stunned\, silenced\, hexed\, has BKB immune etc\.

## [](#getstatesduration)GetStatesDuration

`NPC.GetStatesDuration(npc, states, [only_active_states]):` `table`

**states**

`integer[]`

states to check

**only\_active\_states**`[?]`

if `true` then check only states that active on unit\, otherwise check all states\. e\.g\. rooted while debuff immune `(default: true)`

Returns table of remaining modifier states duration\. See the example

#### [](#example)Example

```
local states_to_check = {
		[Enum.ModifierState.MODIFIER_STATE_STUNNED] = true,
		[Enum.ModifierState.MODIFIER_STATE_HEXED] = true,
}
local states = NPC.GetStatesDuration(unit, states_to_check)
local hex_duration = states[Enum.ModifierState.MODIFIER_STATE_HEXED]
local stun_duration = states[Enum.ModifierState.MODIFIER_STATE_STUNNED]
```

## [](#iswaitingtospawn)IsWaitingToSpawn

`NPC.IsWaitingToSpawn(npc):` `boolean`

Returns `true` if waiting to spawn\. For example\, creeps are waiting to spawn under the ground near the barracks\.

## [](#isillusion)IsIllusion

`NPC.IsIllusion(npc):` `boolean`

Returns `true` if the `CNPC` is illusion\.

## [](#isvisible)IsVisible

`NPC.IsVisible(npc):` `boolean`

Returns `true` if the `CNPC` is visible to local player\.

## [](#isvisibletoenemies)IsVisibleToEnemies

`NPC.IsVisibleToEnemies(npc):` `boolean`

Returns `true` if the `CNPC` is visible enemies\.

## [](#iscourier)IsCourier

`NPC.IsCourier(npc):` `boolean`

Returns `true` if the `CNPC` is a courier\.

## [](#isranged)IsRanged

`NPC.IsRanged(npc):` `boolean`

Returns `true` if the `CNPC` is a ranged unit\.

## [](#iscreep)IsCreep

`NPC.IsCreep(npc):` `boolean`

Returns `true` if the `CNPC` is a creep\.

## [](#islanecreep)IsLaneCreep

`NPC.IsLaneCreep(npc):` `boolean`

Returns `true` if the `CNPC` is a lane creep\.

## [](#isstructure)IsStructure

`NPC.IsStructure(npc):` `boolean`

Returns `true` if the `CNPC` is a structure\.

## [](#istower)IsTower

`NPC.IsTower(npc):` `boolean`

Returns `true` if the `CNPC` is a tower\.

## [](#getunittype)GetUnitType

`NPC.GetUnitType(npc):` [`Enum.UnitTypeFlags`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags)

Returns unit type flags\.

## [](#isconsideredhero)IsConsideredHero

`NPC.IsConsideredHero(npc):` `boolean`

Returns `true` if it is unit a considered a hero for targeting purposes\.

## [](#isbarracks)IsBarracks

`NPC.IsBarracks(npc):` `boolean`

Returns `true` if the `CNPC` is a barracks\.

## [](#isancient)IsAncient

`NPC.IsAncient(npc):` `boolean`

Returns `true` if the `CNPC` is an ancient creeps\.

## [](#isroshan)IsRoshan

`NPC.IsRoshan(npc):` `boolean`

Returns `true` if the `CNPC` is a Roshan\.

## [](#isneutral)IsNeutral

`NPC.IsNeutral(npc):` `boolean`

Returns `true` if the `CNPC` is a neutral\. Neutral creeps\, ancient creeps\.

## [](#ishero)IsHero

`NPC.IsHero(npc):` `boolean`

Returns `true` if the `CNPC` is a hero\.

## [](#isward)IsWard

`NPC.IsWard(npc):` `boolean`

Returns `true` if the `CNPC` is a ward\.

## [](#ismeepoclone)IsMeepoClone

`NPC.IsMeepoClone(npc):` `boolean`

Returns `true` if the `CNPC` is a meepo clone\.

## [](#isentityinrange)IsEntityInRange

`NPC.IsEntityInRange(npc, npc2, range):` `boolean`

**npc2**

**range**

`number`

range to check

Returns `true` if the `CNPC` in range of other `CNPC`\.

## [](#ispositioninrange)IsPositionInRange

`NPC.IsPositionInRange(npc, pos, range, [hull]):` `boolean`

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

**hull**`[?]`

hull just added to range `(default: 0.0)`

Returns `true` if the `CNPC` in range of position\.

## [](#islinkensprotected)IsLinkensProtected

`NPC.IsLinkensProtected(npc):` `boolean`

Returns `true` if the `CNPC` is protected by Linkens Sphere\.

## [](#ismirrorprotected)IsMirrorProtected

`NPC.IsMirrorProtected(npc):` `boolean`

Returns `true` if the `CNPC` is protected by Mirror Shield\.

## [](#ischannellingability)IsChannellingAbility

Do not work for items\.

`NPC.IsChannellingAbility(npc):` `boolean`

Returns `true` if the `CNPC` is channeling ability\. Black Hole\, Life Drain\, etc\.

## [](#getchannellingability)GetChannellingAbility

`NPC.GetChannellingAbility(npc):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

target npc

Returns the currently channelling `CAbility`\.

## [](#isrunning)IsRunning

`NPC.IsRunning(npc):` `boolean`

Returns `true` if the `CNPC` is running\.

## [](#isattacking)IsAttacking

`NPC.IsAttacking(npc):` `boolean`

Returns `true` if the `CNPC` is attacking\.

## [](#issilenced)IsSilenced

`NPC.IsSilenced(npc):` `boolean`

Returns `true` if the `CNPC` is silenced\.

## [](#isstunned)IsStunned

`NPC.IsStunned(npc):` `boolean`

Returns `true` if the `CNPC` is stunned\.

## [](#hasaegis)HasAegis

`NPC.HasAegis(npc):` `boolean`

Returns `true` if the `CNPC` has aegis\.

## [](#iskillable)IsKillable

`NPC.IsKillable(npc):` `boolean`

Returns `true` if the `CNPC` has killable\. Example: false if affected by Eul\.

## [](#getactivity)GetActivity

`NPC.GetActivity(npc):` [`Enum.GameActivity`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity)

Returns the `CNPC` activity\, such as running\, attacking\, casting\, etc\.

## [](#getanimationinfo)GetAnimationInfo

`NPC.GetAnimationInfo(npc):` `{sequence:integer, cycle:number, name:string, mdl_name:string}`

Returns information about the current animation of the `CNPC`\.

## [](#getattackrange)GetAttackRange

`NPC.GetAttackRange(npc):` `integer`

Returns the base attack range of the `CNPC`\.

## [](#getattackrangebonus)GetAttackRangeBonus

`NPC.GetAttackRangeBonus(npc):` `integer`

Returns the bonus attack range of the `CNPC`\.

## [](#getcastrangebonus)GetCastRangeBonus

`NPC.GetCastRangeBonus(npc):` `integer`

Returns the bonus cast range of the `CNPC`\.

## [](#getphysicalarmorvalue)GetPhysicalArmorValue

`NPC.GetPhysicalArmorValue(npc, [excludeWhiteArmor]):` `number`

**excludeWhiteArmor**`[?]`

exclude white armor `(default: true)`

Returns the physical armor value of the `CNPC`\.

## [](#getphysicaldamagereduction)GetPhysicalDamageReduction

`NPC.GetPhysicalDamageReduction(npc):` `number`

Returns the physical damage reduction value of the `CNPC`\.

## [](#getarmordamagemultiplier)GetArmorDamageMultiplier

`NPC.GetArmorDamageMultiplier(npc):` `number`

Returns the physical damage multiplier value of the `CNPC`\.

## [](#getmagicalarmorvalue)GetMagicalArmorValue

`NPC.GetMagicalArmorValue(npc):` `number`

Returns the magical armor value of the `CNPC`\.

## [](#getmagicalarmordamagemultiplier)GetMagicalArmorDamageMultiplier

`NPC.GetMagicalArmorDamageMultiplier(npc):` `number`

Returns the magical damage multiplier value of the `CNPC`\.

## [](#getincreasedattackspeed)GetIncreasedAttackSpeed

`NPC.GetIncreasedAttackSpeed(npc, [ignore_temp_attack_speed]):` `number`

**ignore\_temp\_attack\_speed**`[?]`

ignore temporary attack speed `(default: false)`

Returns increased attack speed of the `CNPC`\.

## [](#getattackspersecond)GetAttacksPerSecond

`NPC.GetAttacksPerSecond(npc, [ignore_temp_attack_speed]):` `number`

Returns the number of attacks per second that the `CNPC` can deal\.

## [](#getattacktime)GetAttackTime

`NPC.GetAttackTime(npc):` `number`

Returns the amount of time needed for the `CNPC` to perform an attack\.

## [](#getattackspeed)GetAttackSpeed

`NPC.GetAttackSpeed(npc, [ignore_temp_attack_speed]):` `number`

Returns the attack speed of the `CNPC`\.

## [](#getbaseattackspeed)GetBaseAttackSpeed

`NPC.GetBaseAttackSpeed(npc):` `number`

Returns the base attack speed of the `CNPC`\.

## [](#gethullradius)GetHullRadius

`NPC.GetHullRadius(npc):` `number`

Returns the model interaction radius of the `CNPC`\.

## [](#getpaddedcollisionradius)GetPaddedCollisionRadius

`NPC.GetPaddedCollisionRadius(npc):` `number`

`NPC`

Returns the collision hull radius \(including padding\) of this `NPC`\.

## [](#getprojectilecollisionsize)GetProjectileCollisionSize

see: https://dota2\.fandom\.com/wiki/Unit\_Size\#Collision\_Size

`NPC.GetProjectileCollisionSize(npc):` `number`

Returns the collision size of the `CNPC`\. Collision size is the internal size that prevents other units from passing through\.

## [](#getturnrate)GetTurnRate

see: https://dota2\.fandom\.com/wiki/Turn\_rate

`NPC.GetTurnRate(npc):` `number`

Returns the turn rate\, which is the speed at which the `CNPC` can turn\.

## [](#getattackanimpoint)GetAttackAnimPoint

see: https://dota2\.fandom\.com/wiki/Attack\_animation

`NPC.GetAttackAnimPoint(npc):` `number`

Returns the attack animation point\, `nil` if not found\.

## [](#getattackprojectilespeed)GetAttackProjectileSpeed

see: https://dota2\.fandom\.com/wiki/Projectile\_Speed

`NPC.GetAttackProjectileSpeed(npc):` `integer`

Returns the attack projectile speed\, `nil` if not found\.

## [](#isturning)IsTurning

`NPC.IsTurning(npc):` `boolean`

Returns true if the `CNPC` is turning\.

## [](#getanglediff)GetAngleDiff

`NPC.GetAngleDiff(npc):` `integer`

Returns the remaining degree angle needed to complete the turn of the `CNPC`\.

## [](#getphysicalarmormainvalue)GetPhysicalArmorMainValue

`NPC.GetPhysicalArmorMainValue(npc):` `number`

Returns the \(main\) white armor of the `CNPC`\.

## [](#gettimetoface)GetTimeToFace

`NPC.GetTimeToFace(npc, npc):` `number`

source npc

Returns the amount of time needed for the source `CNPC` to face the target `CNPC`\.

## [](#findrotationangle)FindRotationAngle

`NPC.FindRotationAngle(npc, pos):` `number`

position to find the rotation angle

Returns the rotation angle of the `CNPC`\.

## [](#gettimetofaceposition)GetTimeToFacePosition

`NPC.GetTimeToFacePosition(npc, pos):` `number`

target position

Returns the amount of time needed for the source `CNPC` to face a specific position\.

## [](#findfacingnpc)FindFacingNPC

`NPC.FindFacingNPC(npc, ignoreNpc, [team_type], [angle], [distance]):` [`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| `nil`

**ignoreNpc**

ignore npc

**team\_type**`[?]`

[`Enum.TeamType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

team type `(default: TEAM_BOTH)`

**angle**`[?]`

max angle to check `(default: 0.0)`

**distance**`[?]`

max distance to check `(default: 0.0)`

Returns the `CNPC` that the source `CNPC` is currently facing\.

## [](#getbasespeed)GetBaseSpeed

`NPC.GetBaseSpeed(npc):` `integer`

Returns the base move speed of the `CNPC`\.

## [](#getmovespeed)GetMoveSpeed

`NPC.GetMoveSpeed(npc):` `number`

Returns the move speed of the `CNPC`\.

## [](#getmindamage)GetMinDamage

`NPC.GetMinDamage(npc):` `number`

Returns the minumum attack damage of the `CNPC`\.

## [](#getbonusdamage)GetBonusDamage

`NPC.GetBonusDamage(npc):` `number`

Returns the bonus attack damage of the `CNPC`\.

## [](#gettruedamage)GetTrueDamage

`NPC.GetTrueDamage(npc):` `number`

Returns the minumum attack damage \+ bonus damage of the `CNPC`\.

## [](#gettruemaximumdamage)GetTrueMaximumDamage

`NPC.GetTrueMaximumDamage(npc):` `number`

Returns the maximum attack damage \+ bonus damage of the `CNPC`\.

## [](#getitembyindex)GetItemByIndex

`NPC.GetItemByIndex(npc, index):` [`CItem`](https://uczone.gitbook.io/api-v2.0/game-components/core/item) \| `nil`

**index**

`integer`

item index

Returns the `CItem` by index\.

## [](#getabilitybyindex)GetAbilityByIndex

`NPC.GetAbilityByIndex(npc, index):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

ability index

Returns the `CAbility` by index\.

## [](#getabilitybyactivity)GetAbilityByActivity

`NPC.GetAbilityByActivity(npc, activity):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

npc to get ability from

**activity**

[`Enum.GameActivity`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity)

game activity

Returns the `CAbility` by game activity\.

## [](#getability)GetAbility

`NPC.GetAbility(npc, name):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

ability name

Returns the `CAbility` by name\.

## [](#hasability)HasAbility

`NPC.HasAbility(npc, name):` `boolean`

Returns `true` if the `CNPC` has this ability\.

## [](#getmana)GetMana

`NPC.GetMana(npc):` `number`

Returns the current mana of the `CNPC`\.

## [](#getmaxmana)GetMaxMana

`NPC.GetMaxMana(npc):` `number`

Returns the maximum mana of the `CNPC`\.

## [](#getmanaregen)GetManaRegen

`NPC.GetManaRegen(npc):` `number`

Returns the mana regeneration rate of the `CNPC`\.

## [](#gethealthregen)GetHealthRegen

`NPC.GetHealthRegen(npc):` `number`

Returns the health regeneration rate of the `CNPC`\.

## [](#getcurrentlevel)GetCurrentLevel

`NPC.GetCurrentLevel(npc):` `number`

Returns the current level of the `CNPC`\.

## [](#getdaytimevisionrange)GetDayTimeVisionRange

`NPC.GetDayTimeVisionRange(npc):` `integer`

Returns the day\-time vision range of the `CNPC`\.

## [](#getnighttimevisionrange)GetNightTimeVisionRange

`NPC.GetNightTimeVisionRange(npc):` `integer`

Returns the night\-time vision range of the `CNPC`\.

## [](#getunitname)GetUnitName

`NPC.GetUnitName(npc):` `string`

Returns the unit\-name of the `CNPC`\.

## [](#gethealthbaroffset)GetHealthBarOffset

`NPC.GetHealthBarOffset(npc, [checkOverride]):` `integer`

**checkOverride**`[?]`

`bool`

returns override offset if it exists `(default: true)`

Returns the health bar offset of the `CNPC`\.

## [](#getunitnameindex)GetUnitNameIndex

index can change when new unit are added

`NPC.GetUnitNameIndex(npc):` `integer`

Returns unit\-name index of the `CNPC`\.

## [](#getattachment)GetAttachment

`NPC.GetAttachment(npc, name):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

attachment name\. e\.g\. "attach\_hitloc"

Returns the attachment position of the `CNPC` by the name\.

#### [](#example-1)Example

```
-- attachments.txt
attach_hitloc
attach_eye_r
attach_eye_l
attach_mouth
attach_totem
attach_head
attach_tidebringer
attach_tidebringer_2
attach_sword
attach_attack1
attach_weapon
attach_eyes
attach_prop_l
attach_prop_r
attach_light
attach_staff
attach_mouthbase
attach_mouthend
attach_mom_l
attach_mom_r
attach_attack2
attach_fuse
attach_mane
attach_tail
attach_upper_jaw
attach_weapon_core_fx
attach_bow_top
attach_bow_bottom
attach_bow_mid
attach_armor
attach_chimmney
attach_eyeR
attach_eyeL
attach_spine4
attach_spine5
attach_spine6
attach_spine7
attach_spine8
attach_spine9
attach_armlet_1
attach_armlet_2
attach_armlet_3
attach_armlet_4
attach_armlet_5
attach_vanguard_guard_1
attach_vanguard_guard_2
attach_weapon_offhand
attach_vanguard_1
attach_vanguard_2
attach_attack3
attach_attack4
attach_banner
attach_fx
attach_portcullis
attach_gem
```

## [](#getattachmentbyindex)GetAttachmentByIndex

`NPC.GetAttachmentByIndex(npc, index):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

attachment index

Returns the attachment position of the `CNPC` by the specified index\.

## [](#getattachmentindexbyname)GetAttachmentIndexByName

`NPC.GetAttachmentIndexByName(npc, name):` `integer`

Returns the attachment index of the `CNPC` by the name\.

## [](#getbountyxp)GetBountyXP

`NPC.GetBountyXP(npc):` `integer`

Returns the amount of experience points \(XP\) you can earn for killing the `CNPC`\.

## [](#getgoldbountymin)GetGoldBountyMin

`NPC.GetGoldBountyMin(npc):` `integer`

Returns the minimum amount gold you can earn for killing the `CNPC`\.

## [](#getgoldbountymax)GetGoldBountyMax

`NPC.GetGoldBountyMax(npc):` `integer`

Returns the maximum amount gold you can earn for killing the `CNPC`\.

## [](#moveto)MoveTo

`NPC.MoveTo(npc, position, [queue], [show], [callback], [executeFast], [identifier], [force_minimap]):` `nil`

The target NPC\.

**position**

The destination position\.

**queue**`[?]`

Add the order to the Dota queue\. `(default: false)`

**show**`[?]`

Show the order position\. `(default: false)`

**callback**`[?]`

Push the order to the OnPrepareUnitOrders callback\. `(default: false)`

**executeFast**`[?]`

Place the order at the top of the queue\. `(default: false)`

**identifier**`[?]`

The identifier which will be passed to `OnPrepareUnitOrders` callback\. `(default: nil)`

**force\_minimap**`[?]`

If true\, the order will be forced by the minimap if possible\. `(default: true)`

Initiates an order for the `CNPC` to move to a specified position\.

## [](#setzdelta)SetZDelta

`NPC.SetZDelta(npc, z):` `nil`

**z**

Z pos

Sets the Z position of the `CNPC` model\.

## [](#hasscepter)HasScepter

`NPC.HasScepter(npc):` `boolean`

Returns `true` if the `CNPC` has or consumed Aghanim Scepter\.

## [](#hasshard)HasShard

`NPC.HasShard(npc):` `boolean`

Returns `true` if the `CNPC` has or consumed Aghanim Shard\.

## [](#sequenceduration)SequenceDuration

`NPC.SequenceDuration(npc, sequence):` `number`

**sequence**

The sequence index\.

Returns sequence duration of the npc with the specified sequence index\.

## [](#getsecondsperattack)GetSecondsPerAttack

`NPC.GetSecondsPerAttack(npc, bIgnoreTempAttackSpeed):` `number`

**bIgnoreTempAttackSpeed**

Ignore temporary attack speed\.

Returns the seconds per attack of the npc\.

## [](#getbarriers)GetBarriers

`NPC.GetBarriers(npc):` `{physical:{total:number, current:number}, magic:{total:number, current:number}, all:{total:number, current:number}}`

Returns a table with information about the barriers of the `CNPC`\.

## [](#getglow)GetGlow

`NPC.GetGlow(npc):` `{m_bSuppressGlow:boolean, m_bFlashing:boolean, m_bGlowing:boolean, m_iGlowType:integer, r:integer, g:integer, b:integer}`

Returns a table with information about the current glow effect of the `CNPC`\.

## [](#setglow)SetGlow

`NPC.SetGlow(npc, suppress_glow, flashing, glowing, glow_type, r, g, b):` `nil`

**suppress\_glow**

suppress\_glow

**flashing**

flashing

**glowing**

glowing

**glow\_type**

glow type

**r**

r factor

**g**

g factor

**b**

b factor

Sets the `CNPC` glow effect\.

## [](#setcolor)SetColor

`NPC.SetColor(npc, r, g, b):` `nil`

Sets the `CNPC` model color\.

## [](#isinrangeofshop)IsInRangeOfShop

`NPC.IsInRangeOfShop(npc, shop_type, [specific]):` `boolean`

**shop\_type**

[`Enum.ShopType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.shoptype)

Shop type to check\.

**specific**`[?]`

No idea what is that\. `(default: false)`

Checks if the `CNPC` is in range of a shop\.

## [](#getbasespellamp)GetBaseSpellAmp

`NPC.GetBaseSpellAmp(npc):` `number`

Returns the base spell amplification of the `CNPC`\.

## [](#getmodifierproperty)GetModifierProperty

`NPC.GetModifierProperty(npc, property):` `number`

**property**

Property enum\.

Returns the property value for the `CNPC`\.

## [](#iscontrollablebyplayer)IsControllableByPlayer

`NPC.IsControllableByPlayer(npc, playerId):` `boolean`

**playerId**

player id

Returns `true` if npc is controllable by player\.

## [](#getmodifierpropertyhighest)GetModifierPropertyHighest

Fixes the issue when you have multiple Kaya items that actually don't stack\.

\`NPC\.GetModifierPropertyHighest\(npc\, property\):\` \*\*\`number\`\*\*

Returns the hieghest property value for the `CNPC`\.

Last updated 19 days ago

