# 🔧Engine

Table to work with game engine\.

## [](#isingame)IsInGame

`Engine.IsInGame():` `boolean`

Returns `true` if the game is in progress\.

## [](#isshopopen)IsShopOpen

`Engine.IsShopOpen():` `boolean`

Returns `true` if the shop is open\.

## [](#setquickbuy)SetQuickBuy

`Engine.SetQuickBuy(item_name, [reset]):` `nil`

Name

Type

Description

**item\_name**

`string`

The name of the item to quick buy\. \(e\.g\. `blink`\, `relic`\)

**reset**`[?]`

`boolean`

Reset the quick buy list\. `(default: true)`

Add item to quick buy list\.

## [](#runscript)RunScript

`Engine.RunScript(script, [contextPanel]):` `boolean`

**script**

The script to run\.

**contextPanel**`[?]`

`string` \| [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

The id of the panel or the panel itself to run the script in\. `(default: "Dashboard")`

Run a JS script in the panorama context\. Return `true` if the script was executed
successfully\. [JS
documentation](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Panorama/Javascript)

#### [](#example)Example

```
-- in dota console, you should see "Hello from Lua!"
Engine.RunScript("$.Msg('Hello from Lua!')");
```

## [](#executecommand)ExecuteCommand

`Engine.ExecuteCommand(command):` `nil`

**command**

The command to execute\.

Execute a console command\.

#### [](#example-1)Example

```
-- in dota chat, you should see "Hello from Lua!"
Engine.ExecuteCommand("say \"Hello from Lua!\"");
```

## [](#playvol)PlayVol

`Engine.PlayVol(sound, [volume]):` `nil`

**sound**

The sound to play\. Could find in `sounds` folder in `pak01_dir.vpk` file\.

**volume**`[?]`

`number`

The volume of the sound\. `(default: 0.1)`

Play a sound with a specific volume\.

#### [](#example-2)Example

```
-- play a sound with a volume of 0.5 (very loud)
Engine.PlayVol("sounds/npc/courier/courier_acknowledge.vsnd_c", 0.5);
```

## [](#createconfig)CreateConfig

`Engine.CreateConfig(config_name, categories):` `nil`

**config\_name**

The name of the config\.

**categories**

`{name: string, hero_ids: integer[], x: number, y: number, width: number, height: number}[]`

Creates a new hero grid config\.

#### [](#example-3)Example

```
Engine.CreateConfig("From lua", {
{
	name = "55%+",
	hero_ids = {1, 2, 3, 4},
	x = 0.0,
	y = 0.0,
	width = 300.0,
	height = 200.0
},
{
	name = "52%+",
	hero_ids = {5, 6},
	x = 350.0,
	y = 0.0,
	width = 300.0,
	height = 200.0
}
});
```

## [](#getcurrentconfigname)GetCurrentConfigName

`Engine.GetCurrentConfigName():` `string`

Returns the current hero grid config name

## [](#setnewgridconfig)SetNewGridConfig

`Engine.SetNewGridConfig(config_name):` `nil`

The name of the config to set

Set the new hero grid config by name

## [](#lookat)LookAt

`Engine.LookAt(x, y):` `nil`

**x**

**y**

Move camera to a specific position\.

## [](#canacceptmatch)CanAcceptMatch

`Engine.CanAcceptMatch():` `boolean`

Returns `true` if the player can accept the match\.

## [](#getgamedirectory)GetGameDirectory

`Engine.GetGameDirectory():` `string`

Returns the current game directory\. \(e\.g\. `dota 2 beta`\)

## [](#getcheatdirectory)GetCheatDirectory

`Engine.GetCheatDirectory():` `string`

Returns the current cheat directory\.

## [](#getlevelname)GetLevelName

`Engine.GetLevelName():` `string`

Returns the current level name\. \(e\.g\. `maps/hero_demo_main.vpk`\)

## [](#getlevelnameshort)GetLevelNameShort

`Engine.GetLevelNameShort():` `string`

Returns the current level name without the extension and folder\. \(e\.g\. `hero_demo_main`\)

## [](#acceptmatch)AcceptMatch

`Engine.AcceptMatch(state):` `nil`

**state**

`integer`

DOTALobbyReadyState

Accept match\.

## [](#consolecolorprintf)ConsoleColorPrintf

`Engine.ConsoleColorPrintf(r, g, b, [a], text):` `nil`

**r**

Red value\.

**g**

Green value\.

**b**

Blue value\.

**a**`[?]`

Alpha value\. `(default: 255)`

**text**

Text to print\.

Print a message to the dota console\.

## [](#getmmr)GetMMR

`Engine.GetMMR():` `integer`

Returns the current MMR\.

## [](#getmmrv2)GetMMRV2

`Engine.GetMMRV2():` `integer`

Returns the current MMR\. Works better than `Engine.GetMMR`\.
Must be called from the game thread\. Ex: OnNetUpdateEx\, OnGCMessage\, not OnFrame or on
initialization\.

## [](#reloadscriptsystem)ReloadScriptSystem

`Engine.ReloadScriptSystem():` `nil`

Executes script system reload\.

## [](#showdotawindow)ShowDotaWindow

`Engine.ShowDotaWindow():` `nil`

Brings the game window to the forefront if it is minimized\.
Use this function to make the game window the topmost window\.

## [](#isinlobby)IsInLobby

`Engine.IsInLobby():` `boolean`

Returns `true` if the player is in a lobby\.

## [](#getbuildversion)GetBuildVersion

`Engine.GetBuildVersion():` `string`

Returns the cheat version\.

## [](#getheroidbyname)GetHeroIDByName

`Engine.GetHeroIDByName(unitName):` `integer` \| `nil`

**unitName**

Can be retrieved from `NPC.GetUnitName`

Returns hero ID by unit name\.

#### [](#example-4)Example

```
local abaddonId = Engine.GetHeroIDByName( "npc_dota_hero_abaddon" )
```

## [](#getdisplaynamebyunitname)GetDisplayNameByUnitName

`Engine.GetDisplayNameByUnitName(unitName):` `string` \| `nil`

Returns hero display name by unit name\.

#### [](#example-5)Example

```
local nevermore_name = Engine.GetDisplayNameByUnitName( "npc_dota_hero_nevermore" )
-- nevermore_name == "Shadow Fiend"
```

## [](#getheronamebyid)GetHeroNameByID

`Engine.GetHeroNameByID(heroID):` `string` \| `nil`

**heroID**

Returns hero name by ID\.

## [](#getuistate)GetUIState

`Engine.GetUIState():` [`Enum.UIState`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.uistate)

Returns current UI state\.

Last updated 19 days ago

