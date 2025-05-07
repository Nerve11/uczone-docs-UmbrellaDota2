# 📜GameRules

Table to work with GameRules\.

## [](#getservergamestate)GetServerGameState

`GameRules.GetServerGameState():` [`Enum.GameState`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current server game state\.

## [](#getgamestate)GetGameState

`GameRules.GetGameState():` [`Enum.GameState`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current game state\.

## [](#getgamemode)GetGameMode

`GameRules.GetGameMode():` [`Enum.GameMode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamemode)

Returns the current game mode\.

## [](#getpregamestarttime)GetPreGameStartTime

Pregame time is the time before the game starts\, e\.g\. ban phase\, pick time\.

`GameRules.GetPreGameStartTime():` `number`

Returns pregame duration or 0 if now is pregame time\.

## [](#getgamestarttime)GetGameStartTime

Game start time is 0:00 on ingame timer\.

`GameRules.GetGameStartTime():` `number`

Returns game start time duration or 0 if game is not start yet\.

## [](#getgameendtime)GetGameEndTime

`GameRules.GetGameEndTime():` `number`

Returns game end time or 0 if game is not end yet\.

## [](#getgameloadtime)GetGameLoadTime

`GameRules.GetGameLoadTime():` `number`

No idea what this function does\. Returns 0 in all cases what I've tested\.

## [](#getgametime)GetGameTime

Can be used to calculate time in an in\-game timer\. See the example\.

`GameRules.GetGameTime():` `number`

Returns the current game time\. Starts counting from pregame state\.

#### [](#example)Example

```
local game_time = GameRules.GetGameTime();
local ingame_timer = game_time - GameRules.GetGameStartTime();
Log.Write(string.format("Current time: %d:%02d", math.floor(ingame_timer / 60),
math.floor(ingame_timer % 60)))
```

## [](#ispaused)IsPaused

`GameRules.IsPaused():` `boolean`

Returns `true` if game is paused\.

## [](#istemporaryday)IsTemporaryDay

Example: Phoenix's Supernova\.

`GameRules.IsTemporaryDay():` `boolean`

Returns `true` if it's temporary day\.

## [](#istemporarynight)IsTemporaryNight

Example: Luna's Eclipse\.

`GameRules.IsTemporaryNight():` `boolean`

Returns `true` if it's temporary night\.

## [](#isnightstalkernight)IsNightstalkerNight

`GameRules.IsNightstalkerNight():` `boolean`

Returns `true` if it's nightstalker's night\.

## [](#getmatchid)GetMatchID

`GameRules.GetMatchID():` `integer`

Returns current match id\.

## [](#getlobbyid)GetLobbyID

`GameRules.GetLobbyID():` `integer`

Returns current lobby id\.

## [](#getgoodglyphcd)GetGoodGlyphCD

Could be less than current game time if glyph is already available\.

`GameRules.GetGoodGlyphCD():` `number`

Returns game time when next radiant glyph will be available\.

## [](#getbadglyphcd)GetBadGlyphCD

`GameRules.GetBadGlyphCD():` `number`

Returns game time when next dire glyph will be available\.

## [](#getgoodscancd)GetGoodScanCD

Could be less than current game time if scan is already available\.

`GameRules.GetGoodScanCD():` `number`

Returns game time when next radiant scan will be available\.

## [](#getbadscancd)GetBadScanCD

`GameRules.GetBadScanCD():` `number`

Returns game time when next dire scan will be available\.

## [](#getgoodscancharges)GetGoodScanCharges

`GameRules.GetGoodScanCharges():` `integer`

Returns current radiant scan charges\.

## [](#getgoodscancharges-1)GetGoodScanCharges

Returns current dire scan charges\.

## [](#getstockcount)GetStockCount

Item id can be found in \`assets/data/items\.json\` file in cheat folder\.

\`GameRules\.GetStockCount\(item\_id\, \[team\]\):\` \*\*\`integer\`\*\*

Name

Type

Description

**item\_id**

`integer`

**team**`[?]`

[`Enum.TeamNum`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

\- Optional\. Default is local player's team\. `(default: Enum.TeamNum.TEAM_RADIANT)`

Returns amount of remaining items in shop by item id\.

#### [](#example-1)Example

```
-- "item_ward_observer": {
--     "ID": "42",
Log.Write("Observers available: " .. GameRules.GetStockCount(42))
```

## [](#getnextcycletime)GetNextCycleTime

`GameRules.GetNextCycleTime():` `number`\, `boolean`

Return time remaining to the next cycle\.

## [](#getdaytimestart)GetDaytimeStart

`GameRules.GetDaytimeStart():` `number`

Returns day start time\. To work with it use `GameRules.GetTimeOfDay`

## [](#getnighttimestart)GetNighttimeStart

`GameRules.GetNighttimeStart():` `number`

Returns night start time\. To work with it use `GameRules.GetTimeOfDay`

## [](#gettimeofday)GetTimeOfDay

`GameRules.GetTimeOfDay():` `number`

Returns current time of day time\.

## [](#isinbanphase)IsInBanPhase

`GameRules.IsInBanPhase():` `boolean`

Returns `true` if game is in ban phase\.

## [](#getalldraftphase)GetAllDraftPhase

`GameRules.GetAllDraftPhase():` `integer`

Returns index of the current draft phase\.

## [](#isalldraftphaseradiantfirst)IsAllDraftPhaseRadiantFirst

`GameRules.IsAllDraftPhaseRadiantFirst():` `boolean`

Returns `true` if Radiant picks first\.

## [](#getdotatime)GetDOTATime

`GameRules.GetDOTATime([pregame], [negative]):` `number`

**pregame**`[?]`

`boolean`

If `true` includes pregame time\. `(default: false)`

**negative**`[?]`

If `true` includes negative time\. `(default: false)`

Returns the actual DOTA in\-game clock time\.

## [](#getlobbyobjectjson)GetLobbyObjectJson

`GameRules.GetLobbyObjectJson():` `string` \| `nil`

Returns CSODOTALobby protobuf object as JSON string\.

## [](#getbannedheroes)GetBannedHeroes

`GameRules.GetBannedHeroes():` `integer[]` \| `nil`

Returns zero\-based array of banned heroes where index corresponds to the player id\.

## [](#getstatetransitiontime)GetStateTransitionTime

`GameRules.GetStateTransitionTime():` `number`

Returns time remaining between state changes\.

Last updated 19 days ago

