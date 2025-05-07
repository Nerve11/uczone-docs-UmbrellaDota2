# 🌐Game Coordinator

Table to work with Game Coordinator \(GC\)\.

Possible message types and message bodies could be found at [here](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs)
Message type id starts with `k_E` prefix\, for example `k_EMsgGCMatchmakingStatsRequest = 7197;`\.
Message body starts with with `C` prefix instead of "k\_E"\, for example `message CMsgDOTAMatchmakingStatsRequest {}`\.

## [](#sendmessage)SendMessage

`GC.SendMessage(msg, msg_type, msg_size):` `nil`

Name

Type

Description

**msg**

`userdata`

Pointer to protobuf message buffer\.

**msg\_type**

`integer`

Protobuf message type ID\.

**msg\_size**

Size of the protobuf message\.

Sends protobuff message to game coordinator\. Response will be received in `OnGCMessage` callback\.

#### [](#example)Example

```
local protobuf = require('protobuf')
local JSON = require('assets.JSON')
local request = protobuf.encodeFromJSON('CMsgDOTAMatchmakingStatsRequest',
	                JSON:encode({}));
GC.SendMessage( request.binary, 7197, request.size )
```

## [](#getsteamid)GetSteamID

`GC.GetSteamID():` `string`

Returns local player Steam ID as string\.

Last updated 19 days ago

