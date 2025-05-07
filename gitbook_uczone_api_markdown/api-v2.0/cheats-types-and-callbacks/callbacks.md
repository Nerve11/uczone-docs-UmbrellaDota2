# 🔄Callbacks

Callbacks for lua
Scripts should return a table with the following functions\.
If the table contains one of the functions below\, it will be registered as a callback and will be
called at the appropriate time\.

## [](#onscriptsloaded)OnScriptsLoaded

`Callbacks.OnScriptsLoaded():` `nil`

Called after all scripts are loaded\.

## [](#ondraw)OnDraw

`Callbacks.OnDraw():` `nil`

Called when the game is drawing\. Works only in the game\.
Recommended to use for drawing only\.

## [](#onframe)OnFrame

`Callbacks.OnFrame():` `nil`

The same as OnDraw\, but called in the menu too\.

## [](#onupdate)OnUpdate

`Callbacks.OnUpdate():` `nil`

Called every game update\. Works only in the game\.
Recommended to use for logic\.

## [](#onprehumanizer)OnPreHumanizer

`Callbacks.OnPreHumanizer():` `nil`

TODO

## [](#onupdateex)OnUpdateEx

`Callbacks.OnUpdateEx():` `nil`

Called every game update\. Same as OnUpdate but as well called in the menu\.
Recommended to use for logic\.

## [](#onentitycreate)OnEntityCreate

`Callbacks.OnEntityCreate(entity):` `nil`

Name

Type

Description

**entity**

[`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)

The entity that was created\.

Called when a new entity is created\.

## [](#onentitydestroy)OnEntityDestroy

`Callbacks.OnEntityDestroy(entity):` `nil`

The entity that was destroyed\.

Called when an entity is destroyed\.

## [](#onmodifiercreate)OnModifierCreate

`Callbacks.OnModifierCreate(entity, modifier):` `nil`

[`CNPC`](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

The entity that has the modifier\.

**modifier**

[`CModifier`](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier)

The modifier that was created\.

Called when a modifier is created\.

## [](#onmodifierdestroy)OnModifierDestroy

`Callbacks.OnModifierDestroy(entity, modifier):` `nil`

The modifier that was destroyed\.

Called when a modifier is destroyed\.

## [](#onmodifierupdate)OnModifierUpdate

`Callbacks.OnModifierUpdate(entity, modifier):` `nil`

The modifier that was updated\.

Called when a modifier is updated/refreshed\.

## [](#onentityhurt)OnEntityHurt

This callback is called only in unsafe mode\.

`Callbacks.OnEntityHurt(data):` `nil`

**data**

`{source:CEntity` \| `nil, target:CEntity` \| `nil, ability:CAbility` \| `nil, damage:number}`

The data about the event\.

Called when an entity is hurt\.

## [](#onentitykilled)OnEntityKilled

`Callbacks.OnEntityKilled(data):` `nil`

`{source:CEntity` \| `nil, target:CEntity` \| `nil, ability:CAbility` \| `nil}`

Called when an entity is killed\.

## [](#onfireeventclient)OnFireEventClient

\`Callbacks\.OnFireEventClient\(data\):\` \*\*\`nil\`\*\*

`{name:string, event:Event}`

Called when a game event is fired\.

## [](#onunitanimation)OnUnitAnimation

`Callbacks.OnUnitAnimation(data):` `nil`

`table`

\.**unit**

The unit that played the animation\.

\.**sequenceVariant**

`number`

The sequence variant\.

\.**playbackRate**

The playback rate\.

\.**castpoint**

The castpoint\.

\.**type**

`integer`

The type\.

\.**activity**

The activity\.

\.**sequence**

The sequence\.

\.**sequenceName**

`string`

The sequence name\.

\.**lag\_compensation\_time**

The lag compensation time\.

Called when a unit animation is played\.

## [](#onunitanimationend)OnUnitAnimationEnd

`Callbacks.OnUnitAnimationEnd(data):` `nil`

\.**snap**

`boolean`

The snap\.

Called when a unit animation ends\.

## [](#onprojectile)OnProjectile

`Callbacks.OnProjectile(data):` `nil`

\.**source**

The source entity\.

\.**target**

The target entity\.

\.**ability**

[`CAbility`](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

The ability linked to the projectile\.

\.**moveSpeed**

The move speed\.

\.**sourceAttachment**

The source attachment\.

\.**particleSystemHandle**

The particle system handle\.

\.**dodgeable**

The dodgeable\.

\.**isAttack**

The is attack\.

\.**expireTime**

The expire time\.

\.**maxImpactTime**

The max impact time\.

\.**launch\_tick**

The tick the pojectile was launched\.

\.**colorGemColor**

The color gem color\.

\.**fullName**

The full name of projectile\.

\.**name**

The short name of projectile\.

\.**handle**

The handle of projectile\.

\.**target\_loc**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The location of the target\.

\.**original\_move\_speed**

The original move speed\.

Called when new projectile is created\.

## [](#onprojectileloc)OnProjectileLoc

`Callbacks.OnProjectileLoc(data):` `nil`

\.**target**`[?]`

The source entity\. `(default: nil)`

\.**sourceLoc**

The source location\.

\.**targetLoc**

The target location\.

\.**launchTick**

The launch tick\.

Called when new projectile loc is created\.

## [](#onlinearprojectilecreate)OnLinearProjectileCreate

`Callbacks.OnLinearProjectileCreate(data):` `nil`

\.**origin**

The origin\.

\.**velocity**

The velocity\.

\.**particleIndex**

The particle index\.

\.**acceleration**

The acceleration\.

\.**maxSpeed**

The max speed\.

\.**fowRadius**

The fow radius\.

\.**distance**

The distance\.

Called when new linear projectile is created\.

## [](#onlinearprojectiledestroy)OnLinearProjectileDestroy

`Callbacks.OnLinearProjectileDestroy(data):` `nil`

Called when linear projectile is destroyed\.

## [](#onparticlecreate)OnParticleCreate

`Callbacks.OnParticleCreate(data):` `nil`

\.**index**

The index of particle\.

\.**entity**`[?]`

The entity\. `(default: nil)`

\.**entity\_id**

The entity id\.

\.**entityForModifiers**`[?]`

The entity for modifiers\. `(default: nil)`

\.**entity\_for\_modifiers\_id**

The entity for modifiers id\.

\.**attachType**

[`Enum.ParticleAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

The attach type\.

The full name of particle\.

The short name of particle\.

\.**hash**

The hash of particle\.

\.**particleNameIndex**

The particle name index\.

Called when new particle is created\.

## [](#onparticleupdate)OnParticleUpdate

`Callbacks.OnParticleUpdate(data):` `nil`

\.**controlPoint**

The control point\.

\.**position**

The position\.

Called when particle is updated\.

## [](#onparticleupdatefallback)OnParticleUpdateFallback

`Callbacks.OnParticleUpdateFallback(data):` `nil`

Called when particle is updated\. Alternative version for some particles\.

## [](#onparticleupdateentity)OnParticleUpdateEntity

`Callbacks.OnParticleUpdateEntity(data):` `nil`

\.**entity**

The entity\.

\.**entIdx**

\.**attachmentName**

The attachment name\.

\.**includeWearables**

Include wearables\.

Called when particle is updated on entity\.

## [](#onparticledestroy)OnParticleDestroy

`Callbacks.OnParticleDestroy(data):` `nil`

The index of destroyed particle\.

\.**destroyImmediately**

Destroy immediately\.

Called when particle is destroyed\.

## [](#onstartsound)OnStartSound

`Callbacks.OnStartSound(data):` `nil`

\.**source**`[?]`

The source of sound\. `(default: nil)`

The hash of sound\.

\.**guid**

The guid of sound\.

\.**seed**

The seed of sound\.

The name of sound\.

The position of sound\.

Called when sound is started\.

## [](#onchatevent)OnChatEvent

`Callbacks.OnChatEvent(data):` `nil`

The type of chat event\.

\.**value**

The value of chat event\.

\.**value2**

The value2 of chat event\.

\.**value3**

The value3 of chat event\.

\.**playerid\_1**

The playerid\_1 of chat event\.

\.**playerid\_2**

The playerid\_2 of chat event\.

\.**playerid\_3**

The playerid\_3 of chat event\.

\.**playerid\_4**

The playerid\_4 of chat event\.

\.**playerid\_5**

The playerid\_5 of chat event\.

\.**playerid\_6**

The playerid\_6 of chat event\.

Called on chat event\.

## [](#onoverheadevent)OnOverHeadEvent

`Callbacks.OnOverHeadEvent(data):` `nil`

`{player_source:CPlayer` \| `nil, player_target:CPlayer` \| `nil, target_npc:CNPC, value:integer}`

The table with the event info\.

Called on event above the hero's head\.

## [](#onunitaddgesture)OnUnitAddGesture

`Callbacks.OnUnitAddGesture(data):` `nil`

\.**npc**`[?]`

The unit that is added to a gesture\. `(default: nil)`

\.**fadeIn**

The fade in\.

\.**fadeOut**

The fade out\.

\.**slot**

The slot\.

Called when a unit is added to a gesture\.

## [](#onprepareunitorders)OnPrepareUnitOrders

`Callbacks.OnPrepareUnitOrders(data):` `boolean`

\.**player**

[`CPlayer`](https://uczone.gitbook.io/api-v2.0/game-components/core/player)

The player that issued the order\.

\.**order**

[`Enum.UnitOrder`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unitorder)

The order type\.

The target of the order\. `(default: nil)`

The position of the order\.

\.**ability**`[?]`

The ability of the order\. `(default: nil)`

\.**orderIssuer**

[`Enum.PlayerOrderIssuer`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.playerorderissuer)

The order issuer\.

\.**npc**

The unit of the order\.

\.**queue**

If the order is queued\.

\.**showEffects**

The show effects of the order\.

Called on every player order\. Return false to prevent the order from being executed\.

## [](#ongcmessage)OnGCMessage

`Callbacks.OnGCMessage(data):` `boolean`

\.**msg\_type**

The message type\.

\.**size**

The size of the message\.

\.**binary\_buffer\_send**`[?]`

`userdata`

The binary buffer of the send message\. `(default: nil)`

\.**binary\_buffer\_recv**`[?]`

The binary buffer of the recieved message\. `(default: nil)`

Called when a game coordinator protobuff message is received\. Return false to prevent the message
from being sent \(doesnt work with recieved messages\)\. For more look at GC table description\.

#### [](#example)Example

```
-- ongc_message.lua
-- import protobuf and json libraries
local protobuf = require('protobuf');
local JSON = require('assets.JSON');

-- do the stats request
local request = protobuf.encodeFromJSON('CMsgDOTAMatchmakingStatsRequest', JSON:encode({}));
GC.SendMessage( request.binary, 7197, request.size );

return {
    OnGCMessage = function(msg)
        if (msg.msg_type ~= 7198) then
            return true;
        end

        -- decode the response and print it
        local response = protobuf.decodeToJSON('CMsgDOTAMatchmakingStatsResponse', msg.binary_buffer_recv, msg.size);
        Log.Write(response);

        return true;
    end
}
```

## [](#onsendnetmessage)OnSendNetMessage

`Callbacks.OnSendNetMessage(data):` `boolean`

\.**message\_id**

The message id\.

\.**message\_name**

The message name\.

\.**buffer**

`lightuserdata`

The encoded buffer of the message\.

Called when a net message is sent\. Return false to prevent the message from being sent\. See
example

#### [](#example-1)Example

```
-- onsend_netmsg.lua
-- anti-mute script for dota 2
-- redirects all chat messages to console command 'say' or 'say_team'

-- import protobuf and json libraries
local protobuf = require('protobuf');
local JSON = require('assets.JSON');
return {
    OnSendNetMessage = function(msg)
        if msg.message_id ~= 394 then
            return true;
        end

        -- decode protobuf message to json
        local json_message = JSON:decode(protobuf.decodeToJSON("CDOTAClientMsg_ChatMessage", msg.buffer , msg.size));
        if not json_message then
            return true;
        end

        -- message CDOTAClientMsg_ChatMessage {
        --     optional uint32 channel_type = 1;
        --     optional string message_text = 2;
        -- }

        local text_message = json_message.message_text;
        -- skip commands starting with '-'
        if text_message:find("-") == 1 then
            return true;
        end
    
        -- 11 - all chat 
        if (json_message.channel_type == 11) then
            Engine.ExecuteCommand('say "'..text_message..'"');
            return false;
        -- 12 - team chat
        elseif (json_message.channel_type == 12) then
            Engine.ExecuteCommand('say_team "'..text_message..'"');
            return false;
        end
    end
}
```

## [](#onpostreceivednetmessage)OnPostReceivedNetMessage

`Callbacks.OnPostReceivedNetMessage(data):` `boolean`

\.**msg\_object**

Called when a net message is received\. Return false to prevent the message from being recieved

#### [](#example-2)Example

```
-- onrecv_netmsg.lua
local protobuf = require('protobuf')
local JSON = require('assets.JSON')
return {
    OnPostReceivedNetMessage = function(msg)
        if msg.message_id == 612 then -- DOTA_UM_ChatMessage https://github.com/SteamDatabase/GameTracking-Dota2/blob/932a8b002f651262ffda6562b758d8ca97c98297/Protobufs/dota_usermessages.proto#L152
            local json = protobuf.decodeToJSONfromObject(msg.msg_object);
            Log.Write(json)
            local lua_table = JSON:decode(json)
            -- ...
        end
    end
}
```

## [](#ongameend)OnGameEnd

`Callbacks.OnGameEnd():` `nil`

Called on game end\.
Recommended to use for zeroing\.

## [](#onkeyevent)OnKeyEvent

`Callbacks.OnKeyEvent(data):` `boolean`

\.**key**

[`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

The key code\.

\.**event**

[`Enum.EKeyEvent`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.ekeyevent)

Key event\.

Called on key and mouse input\. Return false to prevent the event from being processed\.

## [](#onunitinventoryupdated)OnUnitInventoryUpdated

`Callbacks.OnUnitInventoryUpdated(data):` `nil`

Called on unit inventory updated\.

## [](#onsetdormant)OnSetDormant

`Callbacks.OnSetDormant(npc, type):` `nil`

**npc**

The target npc\.

**type**

[`Enum.DormancyType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.dormancytype)

The type of change\.

Called on NPC dormancy state changed\.

## [](#ongamerulesstatechange)OnGameRulesStateChange

`Callbacks.OnGameRulesStateChange(data):` `nil`

`{}`

The table with new game state info\.

Called on gamestate change\.

## [](#onnpcdying)OnNpcDying

`Callbacks.OnNpcDying(npc):` `nil`

Called on NPC dying\.

Last updated 11 days ago

