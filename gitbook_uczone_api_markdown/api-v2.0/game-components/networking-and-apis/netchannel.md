# 📡NetChannel

Table to work with game's net channel\.

## [](#getlatency)GetLatency

`NetChannel.GetLatency([flow]):` `number`

Name

Type

Description

**flow**`[?]`

[`Enum.Flow`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.flow)

flow to get latency of `(default: Enum.Flow.FLOW_OUTGOING)`

Returns the latency/ping of the net channel in seconds\.

## [](#getavglatency)GetAvgLatency

`NetChannel.GetAvgLatency([flow]):` `number`

flow to get average latency of `(default: Enum.Flow.FLOW_OUTGOING)`

Returns the average latency/ping of the net channel in seconds\.

## [](#sendnetmessage)SendNetMessage

You can repeat the same message from OnSendNetMessage if you want to know the format of the message\.

\`NetChannel\.SendNetMessage\(name\, json\):\` \*\*\`nil\`\*\*

**name**

`string`

name of the net message

**json**

json of the net message

Sends a protobuff message to the game server\. [List of messages](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs)\,

#### [](#example)Example

```
-- send_netmsg.lua
-- import json encoder
local JSON = require('assets.JSON');

-- https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs/dota_clientmessages.proto#L395
-- message CDOTAClientMsg_RollDice {
-- 	optional uint32 channel_type = 1;
-- 	optional uint32 roll_min = 2;
-- 	optional uint32 roll_max = 3;
-- }
NetChannel.SendNetMessage("CDOTAClientMsg_RollDice", JSON:encode({
    channel_type = 13,
    roll_min = 11,
    roll_max = 222
}));
```

Last updated 19 days ago

