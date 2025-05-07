# 🚂Steam

Table to with Steam API functions

## [](#setpersonaname)SetPersonaName

`Steam.SetPersonaName(name):` `nil`

Name

Type

Description

**name**

`string`

The name to set

Sets the player name\, stores it on the server and publishes the changes to all friends who
are online\.

## [](#getpersonaname)GetPersonaName

`Steam.GetPersonaName():` `string`

Returns the local players name\. This is the same name as on the users community profile page\.

## [](#getgamelanguage)GetGameLanguage

`Steam.GetGameLanguage():` `string`

Returns the current game language\.

## [](#getprofilepicturebysteamid)GetProfilePictureBySteamId

This function works only if you already got player's user information \(EMsg\_ClientRequestFriendData\)\. That means you should be in the same game with the player or he should be in your friend list\.

`Steam.GetProfilePictureBySteamId(steamID64, [large]):` `integer`

**steamID64**

`integer`

The Steam ID of the player

**large**`[?]`

`boolean`

Whether to get the large profile picture `(default: false)`

Returns the handle of the profile picture of the given Steam ID\.

## [](#getprofilepicturebyaccountid)GetProfilePictureByAccountId

\`Steam\.GetProfilePictureByAccountId\(steamID64\, \[large\]\):\` \*\*\`integer\`\*\*

The account id of the player

Returns the handle of the profile picture of the given account id\.

Last updated 19 days ago

