# 👤Player

Table to work with `CPlayer`\. `CPlayer` extends `CEntity`

## [](#prepareunitorders)PrepareUnitOrders

`Player.PrepareUnitOrders(player, type, target, pos, ability, issuer, issuer_npc, [queue], [show_effects], [callback], [execute_fast], [identifier], [force_minimap]):` `nil`

Name

Type

Description

**player**

[`CPlayer`](https://uczone.gitbook.io/api-v2.0/game-components/core/player)

The player issuing the order\.

**type**

[`Enum.UnitOrder`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unitorder)

The type of order to be issued\.

**target**

[`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

The target entity\, if applicable\.

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The positional coordinates for the order\.

**ability**

[`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

The ability for order\.

**issuer**

[`Enum.PlayerOrderIssuer`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.playerorderissuer)

The issuer capture mode\.

**issuer\_npc**

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| [`CNPC[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

The specific NPC or group of NPC that will issue the order\.

**queue**`[?]`

`boolean`

If true\, the order will be added to the Dota cast queue\. `(default: false)`

**show\_effects**`[?]`

If true\, visual effects will indicate the position of the order\. `(default: false)`

**callback**`[?]`

If true\, the order will be pushed to the `OnPrepareUnitOrders` callback\. `(default: false)`

**execute\_fast**`[?]`

If true\, the order will bypass internal safety delays for immediate execution\. `(default: false)`

**identifier**`[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback\. `(default: nil)`

**force\_minimap**`[?]`

If true\, the order will be forced by the minimap if possible\. `(default: true)`

Provides ability to execute such game actions as moving\, attacking\, or casting spells etc\.

## [](#holdposition)HoldPosition

`Player.HoldPosition(player, issuer_npc, [queue], [push], [execute_fast], [identifier]):` `nil`

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

The specific NPC that will issue the order\.

**push**`[?]`

If true\, the order will be pushed to the OnPrepareUnitOrders callback\. `(default: false)`

Sends the hold position action\.

## [](#attacktarget)AttackTarget

`Player.AttackTarget(player, issuer_npc, target, [queue], [push], [execute_fast], [identifier], [force_minimap]):` `nil`

The target NPC\.

Sends the attack target position\.

## [](#getplayerid)GetPlayerID

`Player.GetPlayerID(player):` `integer`

The target player\.

Returns the player ID within the current game session\.
If the player ID is not valid\, it will return \-1\.

## [](#getplayerslot)GetPlayerSlot

`Player.GetPlayerSlot(player):` `integer`

Returns the player slot number within the current game session\.

## [](#getplayerteamslot)GetPlayerTeamSlot

`Player.GetPlayerTeamSlot(player):` `integer`

Returns the team slot number assigned to the player within their respective team\.

## [](#getname)GetName

`Player.GetName(player):` `string`\, `string` \| `nil`

Returns the player nickname and his proname

## [](#getproname)GetProName

`Player.GetProName(steamId):` `string`

**steamId**

`integer`

Returns cached player's proname\. Works only in game callbacks

## [](#getplayerdata)GetPlayerData

`Player.GetPlayerData(player):` `{valid:boolean, fullyJoined:boolean, fakeClient:boolean, connectionState:integer, steamid:integer, PlusSubscriber:boolean, MVPLastGame:boolean, PlayerName:string, ProName:string}`

Returns the player data table\.

## [](#getteamdata)GetTeamData

`Player.GetTeamData(player):` `{selected_hero_id:integer, kills:integer, assists:integer, deaths:integer, streak:integer, respawnTime:integer, selected_hero_variant:integer, lane_selection_flags:integer, last_buyback_time:number}`

Returns the player team data table\.
Team data is only available for players on the local team\.

## [](#getneutralstashitems)GetNeutralStashItems

`Player.GetNeutralStashItems(player):` `{item: CItem }[]`

Returns table with `CItem`s available in the neutral stash\.

## [](#getteamplayer)GetTeamPlayer

`Player.GetTeamPlayer(player):` `{reliable_gold:integer, unreliable_gold:integer, starting_position:integer, totalearned_gold:integer, totalearned_xp:integer, shared_gold:integer, hero_kill_gold:integer, creep_kill_gold:integer, neutral_kill_gold:integer, courier_gold:integer, bounty_gold:integer, roshan_gold:integer, building_gold:integer, other_gold:integer, comeback_gold:integer, experimental_gold:integer, experimental2_gold:integer, creepdeny_gold:integer, tp_scrolls_purchased:integer, custom_stats:number, income_gold:integer, ward_kill_gold:integer, ability_gold:integer, networth:integer, deny_count:integer, lasthit_count:integer, lasthit_streak:integer, lasthit_multikill:integer, nearby_creep_death_count:integer, claimed_deny_count:integer, claimed_miss_count:integer, miss_count:integer, possible_hero_selection:integer, meta_level:integer, meta_experience:integer, meta_experience_awarded:integer, buyback_cooldown_time:number, buyback_gold_limit_time:number, buyback_cost_time:number, custom_buyback_cooldown:number, stuns:number, healing:number, tower_Kills:integer, roshan_kills:integer, camera_target:CEntity, override_selection_entity:CEntity, observer_wards_placed:integer, sentry_wards_placed:integer, creeps_stacked:integer, camps_stacked:integer, rune_pickups:integer, gold_spent_on_support:integer, hero_damage:integer, wards_purchased:integer, wards_destroyed:integer, commands_issued:integer, gold_spent_on_consumables:integer, gold_spent_on_items:integer, gold_spent_on_buybacks:integer, gold_lost_to_death:integer, is_new_player:boolean, is_guide_player:boolean, acquired_madstone:integer, current_madstone:integer}`

Returns **Team Player Data** table

## [](#getplayerneutralinfo)GetPlayerNeutralInfo

`Player.GetPlayerNeutralInfo(player):` `nil` \| `{acquired_madstone:integer, current_madstone:integer, trinket_choices:integer[], enhancement_choices:integer[], selected_trinkets:integer[], selected_enhancements:integer[], times_crafted:integer[]}`

Returns info about player's neutral items

## [](#ismuted)IsMuted

`Player.IsMuted(player):` `boolean`

Returns the player mute status\.

## [](#getselectedunits)GetSelectedUnits

`Player.GetSelectedUnits(player):` [`CNPC[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

Returns table of selected units by player\.

## [](#addselectedunit)AddSelectedUnit

`Player.AddSelectedUnit(player, NPC):` `nil`

**NPC**

To select\.

Adds unit to player selection\.

## [](#clearselectedunits)ClearSelectedUnits

`Player.ClearSelectedUnits(player):` `nil`

Clears player selection\.

## [](#getquickbuyinfo)GetQuickBuyInfo

`Player.GetQuickBuyInfo(player):` `{m_quickBuyItems:integer[], m_quickBuyIsPurchasable:boolean[]}`

Returns table with m\_quickBuyItems\(item ids\) and m\_quickBuyIsPurchasable\(table of booleans\)\.

## [](#gettotalgold)GetTotalGold

`Player.GetTotalGold(player):` `integer`

Returns total gold of player\.

## [](#getassignedhero)GetAssignedHero

`Player.GetAssignedHero(player):` [`CHero`](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) \| `nil`

Returns player's assigned hero\.

## [](#getactiveability)GetActiveAbility

`Player.GetActiveAbility(player):` [`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| `nil`

Returns player's active ability\.

Last updated 12 days ago

