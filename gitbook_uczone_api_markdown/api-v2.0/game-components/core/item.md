# 🔑Item

Table to work with `CItem`\.

`CItem` extends `CAbility`

## [](#iscombinable)IsCombinable

`Item.IsCombinable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](https://uczone.gitbook.io/api-v2.0/game-components/core/item)

Returns `true` if the item is combinable\. I'm not sure if non\-combinable items even exist\.

## [](#ispermanent)IsPermanent

`Item.IsPermanent(item):` `boolean`

Returns `true` if the item is permanent\. I'm not sure what permanent items is\, but for items with stacks this function returns `false`\.

## [](#isstackable)IsStackable

`Item.IsStackable(item):` `boolean`

Returns `true` if the item is stackable\. e\.g tangoes\, wards\, etc\.

## [](#isrecipe)IsRecipe

`Item.IsRecipe(item):` `boolean`

Returns `true` if the item is recipe\.

## [](#getsharability)GetSharability

`Item.GetSharability(item):` [`Enum.ShareAbility`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.shareability)

Returns item's sharability type\.

## [](#isdroppable)IsDroppable

`Item.IsDroppable(item):` `boolean`

Returns `true` if the item is droppable\.

## [](#ispurchasable)IsPurchasable

`Item.IsPurchasable(item):` `boolean`

Returns `true` if the item is purchasable\.

## [](#issellable)IsSellable

`Item.IsSellable(item):` `boolean`

Returns `true` if the item is sellable\.

## [](#requirescharges)RequiresCharges

`Item.RequiresCharges(item):` `boolean`

Returns `true` if the item requires charges\. e\.g\. urn\, vessel etc\.

## [](#iskillable)IsKillable

`Item.IsKillable(item):` `boolean`

Returns `true` if item is destroyable by autoatack\.

## [](#isdisassemblable)IsDisassemblable

`Item.IsDisassemblable(item):` `boolean`

Returns `true` if item is disassemblable\.

## [](#isalertable)IsAlertable

`Item.IsAlertable(item):` `boolean`

Returns `true` if item is alertable\. e\.g\. smoke\, mekansm\, arcane boots etc\.

## [](#getinitialcharges)GetInitialCharges

`Item.GetInitialCharges(item):` `integer`

Returns initial charges of the item\. e\.g\. 3 for bottle\, 1 for dust etc\.

## [](#castsonpickup)CastsOnPickup

`Item.CastsOnPickup(item):` `boolean`

No idea what this function does\.

## [](#getcurrentcharges)GetCurrentCharges

`Item.GetCurrentCharges(item):` `integer`

Returns amount of current charges\.

## [](#getsecondarycharges)GetSecondaryCharges

`Item.GetSecondaryCharges(item):` `integer`

Returns amount of secondary charges\. e\.g\. pack of both type of wards\.

## [](#iscombinelocked)IsCombineLocked

`Item.IsCombineLocked(item):` `boolean`

Returns `true` if item locked for combining\.

## [](#ismarkedforsell)IsMarkedForSell

`Item.IsMarkedForSell(item):` `boolean`

Returns `true` if item is marked for sell\.

## [](#getpurchasetime)GetPurchaseTime

`Item.GetPurchaseTime(item):` `number`

Returns the game time when the item was purchased\. If the item was assembled from other items\, It returns the purchase time of the item that had the lowest
index at the moment of assembling\.

## [](#getassembledtime)GetAssembledTime

`Item.GetAssembledTime(item):` `number`

Returns the game time when the item was assembled\. If the item was not assembled\, returns time when the item was purchased\.

## [](#purchasedwhiledead)PurchasedWhileDead

`Item.PurchasedWhileDead(item):` `boolean`

Returns `true` if item was purchased while dead\.

## [](#canbeusedoutofinventory)CanBeUsedOutOfInventory

`Item.CanBeUsedOutOfInventory(item):` `boolean`

No idea which specific item example could be used out of inventory\.

## [](#isitemenabled)IsItemEnabled

`Item.IsItemEnabled(item):` `boolean`

Returns `false` if item has CD after moving from stash\.

## [](#getenabletime)GetEnableTime

Could be less than current game time if item is already enabled\.

`Item.GetEnableTime(item):` `number`

Returns game time when item will be enabled\.

## [](#getplayerownerid)GetPlayerOwnerID

`Item.GetPlayerOwnerID(item):` `integer`

Returns player ID who owns the item\.

## [](#getcost)GetCost

`Item.GetCost(item):` `integer`

Returns item cost\.

## [](#getstockcount)GetStockCount

Item id can be found in \`assets/data/items\.json\` file in cheat folder\.

\`Item\.GetStockCount\(item\_id\, \[team\]\):\` \*\*\`integer\`\*\*

**item\_id**

`integer`

**team**`[?]`

[`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

\- Optional\. Default is local player's team\. `(default: Enum.TeamNum.TEAM_RADIANT)`

Returns amount of remaining items in shop by item id\.

#### [](#example)Example

```
-- "item_ward_observer": {
--     "ID": "42",
Log.Write("Observers available: " .. Item.GetStockCount(42))
```

Last updated 19 days ago

