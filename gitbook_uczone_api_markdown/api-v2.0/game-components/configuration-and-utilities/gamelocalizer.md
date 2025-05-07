# 📝GameLocalizer

Table to work with game localization\.
Localization tokens are stored in `resource/localization` folder in `pak01_dir.vpk`

## [](#find)Find

`GameLocalizer.Find(token):` `string`

Name

Type

Description

**token**

`string`

should be in format `#token`

Returns localized string by token or returns empty string if token not found\.

#### [](#example)Example

```
GameLocalizer.Find("#DOTA_AutocastAbility5") -- Autocast Ability Ultimate
```

## [](#findability)FindAbility

`GameLocalizer.FindAbility(ability_name):` `string`

**ability\_name**

Returns localized string by ability name or returns empty string if ability not found\.

#### [](#example-1)Example

```
GameLocalizer.FindAbility("antimage_mana_void") -- Mana Void
```

## [](#finditem)FindItem

`GameLocalizer.FindItem(item_name):` `string`

**item\_name**

Returns localized string by item name or returns empty string if item not found\.

#### [](#example-2)Example

```
GameLocalizer.FindItem("item_blink") -- Blink Dagger
GameLocalizer.FindItem("item_recipe_arcane_blink") -- Recipe: Arcane Blink
```

## [](#findnpc)FindNPC

`GameLocalizer.FindNPC(unit_name):` `string`

**unit\_name**

Returns localized string by unit name or returns empty string if unit not found\.

#### [](#example-3)Example

```
GameLocalizer.FindNPC("npc_dota_hero_necrolyte") -- Necrophos
```

Last updated 19 days ago

