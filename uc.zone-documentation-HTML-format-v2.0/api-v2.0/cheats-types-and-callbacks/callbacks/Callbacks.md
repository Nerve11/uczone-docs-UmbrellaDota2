## Callbacks
Callbacks for lua
Scripts should return a table with the following functions.
If the table contains one of the functions below, it will be registered as a callback and will be
called at the appropriate time.

# OnScriptsLoaded
Callbacks.OnScriptsLoaded(): nil
=> Called after all scripts are loaded.

# OnDraw
Callbacks.OnDraw(): nil
=> Called when the game is drawing. Works only in the game.
Recommended to use for drawing only.

# OnFrame
Callbacks.OnFrame(): nil
=> The same as OnDraw, but called in the menu too

# OnUpdate
Callbacks.OnUpdate(): nil
=> Called every game update. Works only in the game.
Recommended to use for logic.

# OnPreHumanizer
Callbacks.OnPreHumanizer(): nil
=> TODO

# OnUpdateEx
Callbacks.OnUpdateEx(): nil
=> Called every game update. Same as OnUpdate but as well called in the menu.
Recommended to use for logic.

# OnEntityCreate
Callbacks.OnEntityCreate(entity): nil
Name      |    Type      |  Description
entity    |    CEntity   |  The entity that was created.
=> Called when a new entity is created.

# OnEntityDestroy
Callbacks.OnEntityDestroy(entity): nil

Name      |    Type      |  Description
entity    |    CEntity   |  The entity that was destroyed.

=> Called when an entity is destroyed.

# OnModifierCreate
Callbacks.OnModifierCreate(entity, modifier): nil
Name      |    Type      |  Description
entity    |    CNPC      |  The entity that has the modifier.
modifier  |    CModifier |  The modifier that was destroyed.

=> Called when a modifier is destroyed.

# OnModifierUpdate
Callbacks.OnModifierUpdate(entity, modifier): nil
Name      |    Type      |  Description
entity    |    CNPC      |  The entity that has the modifier.
modifier  |    CModifier |  The modifier that was updated.

=> Called when a modifier is updated/refreshed.

# OnEntityHurt
!This callback is called only in unsafe mode.

Callbacks.OnEntityHurt(data): nil
Name      |    Type                  |  Description
          | {source:CEntity | nil,   |  
 data     |  target:CEntity | nil,   |  The data that was passed to the function.
          |  ability:CAbility | nil, |
          |  damage:number}          |

=> Called when an entity is hurt.

# OnEntityKilled
!This callback is called only in unsafe mode.

Callbacks.OnEntityKilled(data): nil
Name      |    Type                  |  Description
          | {source:CEntity | nil,   |
 data     |  target:CEntity | nil,   |  The data that was passed to the function.
          |  ability:CAbility | nil} |
=> Called when an entity is killed.

# OnFireEventClient
!This callback is called only in unsafe mode.

`Callbacks.OnFireEventClient(data):` **`nil`**

Name      |    Type                     |  Description
data      |  {name:string, event:Event} |  The data about the event.

=> Called when a game event is fired.

# OnUnitAnimation
Callbacks.OnUnitAnimation(data): nil
Name                     |    Type                  |  Description
data                     |    table                 |  The data about the event.
 .unit                  |     CNPC                 | The unit that played the animation.
 .sequenceVariant       |    number                |  The sequence variant.
 .lag_compensation_time |    number                |  The lag compensation time.
 .playbackRate          |    number                |  The playback rate.
 .castpoint             |    number                |  The cast point.
 .type                  |    integer               |  The type.
 .activity              |    integer               |  The activity.
 .sequence              |    integer               |  The sequence.
 .sequenceName          |    stringr               |  The sequence name.

=> Called when a unit animation is played.

# OnUnitAnimationEnd
Callbacks.OnProjectile(data): nil
Name                     |    Type                  |  Description
data                     |    table                 |  The data about the event.
 .unit                  |     CNPC                 |  The unit that played the animation.
 .snap                  |     boolean              |  The snap.

=> Called when a unit animation ends.

# OnProjectile
Callbacks.OnProjectile(data): nil

| Name                    | Type      | Description                          |
|-------------------------|-----------|--------------------------------------|
| data                    | table     | The data about the event.            |
| .source                 | CNPC      | The source entity.                   |
| .target                 | CNPC      | The target entity.                   |
| .ability                | CAbility  | The ability linked to the projectile.|
| .moveSpeed              | integer   | The move speed.                      |
| .sourceAttachment       | integer   | The source attachment.               |
| .particleSystemHandle   | integer   | The particle system handle.          |
| .dodgeable              | boolean   | The dodgeable.                       |
| .isAttack               | boolean   | The is attack.                       |
| .expireTime             | number    | The expire time.                     |
| .maxImpactTime          | number    | The max impact time.                 |
| .launch_tick            | integer   | The tick the projectile was launched.|
| .colorGemColor          | integer   | The color gem color.                 |
| .fullName               | string    | The full name of projectile.         |
| .name                   | string    | The short name of projectile.        |
| .handle                 | integer   | The handle of projectile.            |
| .target_loc             | Vector    | The location of the target.          |
| .original_move_speed    | integer   | The original move speed.             |

=> Called when new projectile is created.

# OnProjectileLoc
Callbacks.OnProjectileLoc(data): nil

| Name                     | Type         | Description                          |
|--------------------------|--------------|--------------------------------------|
| `data`                   | `table`      | The data about the event.            |
| `.target`                | `CNPC`       | The source entity. *(default: nil)*  |
| `.sourceLoc`            | `Vector`     | The source location.                 |
| `.targetLoc`            | `Vector`     | The target location.                 |
| `.moveSpeed`            | `integer`    | The move speed.                      |
| `.original_move_speed`  | `integer`    | The original move speed.             |
| `.particleSystemHandle` | `integer`    | The particle system handle.          |
| `.dodgeable`            | `boolean`    | The dodgeable.                       |
| `.isAttack`             | `boolean`    | The is attack.                       |
| `.expireTime`           | `number`     | The expire time.                     |
| `.colorGemColor`        | `integer`    | The color gem color.                 |
| `.launchTick`           | `integer`    | The launch tick.                     |
| `.handle`               | `integer`    | The handle of projectile.            |
| `.fullName`             | `string`     | The full name of projectile.         |
| `.name`                 | `string`     | The short name of projectile.        |

=> Called when new projectile loc is created.

# OnLinearProjectileCreate
Callbacks.OnLinearProjectileCreate(data): nil

| Name            | Type      | Description                   |
|-----------------|-----------|-------------------------------|
| data            | `table`   | The data about the event.     |
| .source         | `CNPC`    | The source entity.            |
| .origin         | `Vector`  | The origin.                   |
| .velocity       | `Vector`  | The velocity.                 |
| .particleIndex  | `integer` | The particle index.           |
| .handle         | `integer` | The handle of projectile.     |
| .acceleration   | `Vector`  | The acceleration.             |
| .maxSpeed       | `number`  | The max speed.                |
| .fowRadius      | `number`  | The fow radius.               |
| .distance       | `number`  | The distance.                 |
| .colorGemColor  | `integer` | The color gem color.          |
| .fullName       | `string`  | The full name of projectile.  |
| .name           | `string`  | The short name of projectile. |

=> Called when new linear projectile is created.

# OnLinearProjectileDestroy
Callbacks.OnLinearProjectileDestroy(data): nil

| Name    | Type      | Description                 |
|---------|-----------|-----------------------------|
| data    | table     | The data about the event.   |
| .handle | integer   | The handle of projectile.   |

=> Called when linear projectile is destroyed.

# OnParticleCreate
Callbacks.OnParticleCreate(data): nil

| Name                      | Type                      | Description                              |
|---------------------------|---------------------------|------------------------------------------|
| data                      | table                     | The data about the event.                |
| .index                    | integer                   | The index of particle.                   |
| .entity [?]               | CNPC                      | The entity. (default: nil)               |
| .entity_id                | integer                   | The entity id.                           |
| .entityForModifiers [?]   | CNPC                      | The entity for modifiers. (default: nil) |
| .entity_for_modifiers_id  | integer                   | The entity for modifiers id.             |
| .attachType               | Enum.ParticleAttachment   | The attach type.                         |
| .fullName                 | string                    | The full name of particle.               |
| .name                     | string                    | The short name of particle.              |
| .hash                     | integer                   | The hash of particle.                    |
| .particleNameIndex        | integer                   | The particle name index.                 |

=> Called when new particle is created.

# OnParticleUpdate
Callbacks.OnParticleUpdate(data): nil

| Name          | Type      | Description               |
|---------------|-----------|---------------------------|
| data          | table     | The data about the event. |
| .index        | integer   | The index of particle.    |
| .controlPoint | integer   | The control point.        |
| .position     | Vector    | The position.             |

=> Called when particle is updated.

# OnParticleUpdateFallback
Callbacks.OnParticleUpdateFallback(data): nil

| Name          | Type      | Description               |
|---------------|-----------|---------------------------|
| data          | table     | The data about the event. |
| .index        | integer   | The index of particle.    |
| .controlPoint | integer   | The control point.        |
| .position     | Vector    | The position.             |

=> Called when particle is updated. Alternative version for some particles.

# OnParticleUpdateEntity
Callbacks.OnParticleUpdateEntity(data): nil

| Name              | Type                      | Description               |
|-------------------|---------------------------|---------------------------|
| data              | table                     | The data about the event. |
| .index            | integer                   | The index of particle.    |
| .controlPoint     | integer                   | The control point.        |
| .entity           | CEntity                   | The entity.               |
| .entIdx           | integer                   | The entity id.            |
| .attachType       | Enum.ParticleAttachment   | The attach type.          |
| .attachmentName   | string                    | The attachment name.      |
| .position         | Vector                    | The position.             |
| .includeWearables | boolean                   | Include wearables.        |

=> Called when particle is updated on entity.

# OnParticleDestroy
Callbacks.OnParticleDestroy(data): nil

| Name                | Type    | Description                      |
|---------------------|---------|----------------------------------|
| data                | table   | The data about the event.        |
| .index              | integer | The index of destroyed particle. |
| .destroyImmediately | boolean | Destroy immediately.             |

=> Called when particle is destroyed.

# OnStartSound
Callbacks.OnStartSound(data): nil

| Name        | Type      | Description                         |
|-------------|-----------|-------------------------------------|
| data        | table     | The data about the event.           |
| .source [?] | CEntity   | The source of sound. (default: nil) |
| .hash       | integer   | The hash of sound.                  |
| .guid       | integer   | The guid of sound.                  |
| .seed       | integer   | The seed of sound.                  |
| .name       | string    | The name of sound.                  |
| .position   | Vector    | The position of sound.              |

=> Called when sound is started.

# OnChatEvent
Callbacks.OnChatEvent(data): nil

| Name        | Type    | Description                   |
|-------------|---------|-------------------------------|
| data        | table   | The data about the event.     |
| .type       | integer | The type of chat event.       |
| .value      | integer | The value of chat event.      |
| .value2     | integer | The value2 of chat event.     |
| .value3     | integer | The value3 of chat event.     |
| .playerid_1 | integer | The playerid_1 of chat event. |
| .playerid_2 | integer | The playerid_2 of chat event. |
| .playerid_3 | integer | The playerid_3 of chat event. |
| .playerid_4 | integer | The playerid_4 of chat event. |
| .playerid_5 | integer | The playerid_5 of chat event. |
| .playerid_6 | integer | The playerid_6 of chat event. |

=> Called on chat event.

# OnOverHeadEvent
Callbacks.OnOverHeadEvent(data): nil

| Name |                                        Type                                                  | Description                    |
|------|----------------------------------------------------------------------------------------------|--------------------------------|
| data | {player_source:CPlayer \| nil, player_target:CPlayer \| nil, target_npc:CNPC, value:integer} | The table with the event info. |

=> Called on event above the hero's head.

# OnUnitAddGesture
Callbacks.OnUnitAddGesture(data): nil

| Name             | Type    | Description                                         |
|------------------|---------|-----------------------------------------------------|
| data             | table   | The data about the event.                           |
| .npc [?]         | CNPC    | The unit that is added to a gesture. (default: nil) |
| .sequenceVariant | integer | The sequence variant.                               |
| .playbackRate    | number  | The playback rate.                                  |
| .fadeIn          | number  | The fade in.                                        |
| .fadeOut         | number  | The fade out.                                       |
| .slot            | integer | The slot.                                           |
| .activity        | integer | The activity.                                       |
| .sequenceName    | string  | The sequence name.                                  |

=> Called when a unit is added to a gesture.

# OnPrepareUnitOrders
Callbacks.OnPrepareUnitOrders(data): boolean

| Name          | Type                     | Description                        |
|:--------------|:-------------------------|:-----------------------------------|
| data          | table                    | The data about the event.          |
| .player       | CPlayer                  | The player that issued the order.  |
| .order        | Enum.UnitOrder           | The order type.                    |
| .target [?]   | CEntity                  | The target of the order. (default: |
|               |                          | nil)                               |
| .position     | Vector                   | The position of the order.         |
| .ability [?]  | CAbility                 | The ability of the order. (default:|
|               |                          | nil)                               |
| .orderIssuer  | Enum.PlayerOrderIssuer   | The order issuer.                  |
| .npc          | CNPC                     | The unit of the order.             |
| .queue        | boolean                  | If the order is queued.            |
| .showEffects  | boolean                  | The show effects of the order.     |

=> Called on every player order. Return false to prevent the order from being executed.

# OnGCMessage
Callbacks.OnGCMessage(data): boolean

| Name                  | Type     | Description                           |
|:----------------------|:---------|:--------------------------------------|
| data                  | table    |                                       |
| .msg_type             | number   | The message type.                     |
| .size                 | number   | The size of the message.              |
| .binary_buffer_send   | userdata | The binary buffer of the send         |
|                       |          | message. (default: nil)               |
| .binary_buffer_recv   | userdata | The binary buffer of the recieved     |
|                       |          | message. (default: nil)               |

=> Called when a game coordinator protobuff message is received. Return false to prevent the message
from being sent (doesnt work with recieved messages). For more look at GC table description.

Example:
'''lua
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
'''

# OnSendNetMessage
Callbacks.OnSendNetMessage(data): boolean

| Name           | Type         | Description                         |
|:---------------|:-------------|:------------------------------------|
| data           | table        | The data about the event.           |
| .message_id    | number       | The message id.                     |
| .message_name  | string       | The message name.                   |
| .buffer        | lightuserdata| The encoded buffer of the message.  |
| .size          | number       | The size of the message.            |

=> Called when a net message is sent. Return false to prevent the message from being sent. See example

Example:
'''lua
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
'''

# OnPostReceivedNetMessage
Callbacks.OnPostReceivedNetMessage(data): boolean

| Name          | Type         | Description                         |
|:--------------|:-------------|:------------------------------------|
| data          | table        | The data about the event.           |
| .message_id   | number       | The message id.                     |
| .msg_object   | lightuserdata| The encoded buffer of the message.  |

=> Called when a net message is received. Return false to prevent the message from being recieved

Example:
'''lua
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
'''

# OnGameEnd
Callbacks.OnGameEnd(): nil

=> Called on game end.
Recommended to use for zeroing.

# OnKeyEvent
Callbacks.OnKeyEvent(data): boolean

| Name    | Type              | Description              |
|:--------|:------------------|:-------------------------|
| data    | table             | The data about the event.|
| .key    | Enum.ButtonCode   | The key code.            |
| .event  | Enum.EKeyEvent    | Key event.               |

=> Called on key and mouse input. Return false to prevent the event from being processed.

# OnUnitInventoryUpdated
Callbacks.OnUnitInventoryUpdated(data): nil

| Name | Type | Description              |
|:-----|:-----|:-------------------------|
| data | CNPC | The data about the event.|

=> Called on unit inventory updated.

# OnSetDormant
Callbacks.OnSetDormant(npc, type): nil

| Name | Type               | Description        |
|:-----|:-------------------|:-------------------|
| npc  | CNPC               | The target npc.    |
| type | Enum.DormancyType  | The type of change.|

=> Called on NPC dormancy state changed.

# OnGameRulesStateChange
Callbacks.OnGameRulesStateChange(data): nil

| Name | Type | Description                        |
|:-----|:-----|:-----------------------------------|
| data | {}   | The table with new game state info.|

=> Called on gamestate change.

# OnNpcDying
Callbacks.OnNpcDying(npc): nil

| Name | Type | Description    |
|:-----|:-----|:---------------|
| npc  | CNPC | The target npc.|

=> Called on NPC dying.


===
END FILE

