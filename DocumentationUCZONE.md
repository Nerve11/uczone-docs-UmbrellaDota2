# UCZONE API v2.0 - Полная документация

*Сгенерировано из 93 страниц GitBook*

---

# Оглавление

- [Starting Guide](#starting-guide)
- [Cheats Types and Callbacks](#cheats-types-and-callbacks)
  - [Classes - Color](#classes---color)
  - [Classes - Menu System](#classes---menu-system)
  - [Classes - UI Widgets](#classes---ui-widgets)
  - [Classes - Math](#classes---math)
- [Game Components - Entity Lists](#game-components---entity-lists)
- [Game Components - Core Objects](#game-components---core-objects)
- [Game Engine](#game-engine)
- [Networking and APIs](#networking-and-apis)
- [Rendering and Visuals](#rendering-and-visuals)
  - [Rendering - Panorama UI](#rendering---panorama-ui)
- [Configuration and Utilities](#configuration-and-utilities)


================================================================================

## Starting Guide

<!-- Source: https://uczone.gitbook.io/api-v2.0 -->

Copy

# 👉Starting Guide

To execute your script move the `.lua` file into the `%cheat_dir%/scripts` folder.

---

## Callbacks

Most of your code will be executed inside the callbacks. To register the callback function, your script should return a table in the following format:

Copy

```
return {
    CallbackName = FuncHandler,
}
```

Example

Copy

```
-- much more convenient way for big scripts
local script = {}

function script.OnUpdate()
    print("OnUpdate")
end

return script
```

or

Copy

```
return {
    OnUpdate = function() 
        print("OnUpdate")
    end,
}
```

---

## Example Scripts

There is example scripts you can rely on:

Debug Script

Copy

```
---@diagnostic disable: undefined-global, param-type-mismatch, inject-field
local debug = {}

local tab = Menu.Create("General", "Debug", "Debug", "Debug")

local inworld_group = tab:Create("In-World")
local callbacks_group = tab:Create("Callbacks")
local inworld_settings_group = tab:Create("In-World Settings", 1)
local callbacks_settings_group = tab:Create("Callbacks Settings", 2)

--#region UI
local ui = {}

ui.inworld = {}
ui.inworld.global_switch = inworld_group:Switch("In-World Enabled", false)
ui.inworld.name = inworld_group:Switch("Unit Name", false)
ui.inworld.position = inworld_group:Switch("Unit Position", false)
ui.inworld.modifier = inworld_group:Switch("Modifiers", false)
ui.inworld.ability = inworld_group:Switch("Abilities", false)
ui.inworld.item = inworld_group:Switch("Items", false)
ui.inworld.modifier_state = inworld_group:Switch("Modifier State", false)
ui.inworld.modifier_state_duration = inworld_group:Switch("Modifier State Duration", false)

ui.inworld_settings = {}
ui.inworld_settings.hero_only = inworld_settings_group:Switch("Only heroes", true)
ui.inworld_settings.on_draw = inworld_settings_group:Switch("Render in OnDraw \a{primary}fps drop", false)

ui.callbacks = {}
ui.callbacks.modifier = callbacks_group:Switch("Modifier", false)
ui.callbacks.animation = callbacks_group:Switch("Animation", false)
ui.callbacks.add_entity = callbacks_group:Switch("Entity Create/Remove", false)
ui.callbacks.projectile = callbacks_group:Switch("Projectile", false)
ui.callbacks.particle = callbacks_group:Switch("Particle", false)
ui.callbacks.gesture = callbacks_group:Switch("Gesture", false)
ui.callbacks.sound = callbacks_group:Switch("Sound", false)
ui.callbacks.order = callbacks_group:Switch("Unit Order", false)

ui.callbacks_settings = {}
ui.callbacks_settings.divider = callbacks_settings_group:Switch("Add 'divider' in the end of the log message", true)
ui.callbacks_settings.add_more_info = callbacks_settings_group:Switch("More info. Starts with [m] prefix", true)
--#endregion

local font = Render.LoadFont("Arial", 0, 500)

local function add_divider()
    if ui.callbacks_settings.divider:Get() then
        print("+---+---+---+---+---+---+---+")
    end
end

-- we can't modify the original table in callbacks, so we need to copy it to add more info
function table.copy(t)
    local u = { }
    for k, v in pairs(t) do u[k] = v end
    return u
end

--#region Callbacks

--#region Modifier
function debug.OnModifierCreate(ent, mod)
    if not ui.callbacks.modifier:Get() then return end
    print("OnModifierCreate")
    local modifier_name = Modifier.GetName(mod)
    local owner = Ability.GetOwner(Modifier.GetAbility(mod))
    local owner_name = NPC.GetUnitName(owner)
    print(("%s | %s -> %s"):format(modifier_name, owner_name, NPC.GetUnitName(ent)))
    add_divider()
end

function debug.OnModifierDestroy(ent, mod)
    if not ui.callbacks.modifier:Get() then return end
    print("OnModifierDestroy")
    local modifier_name = Modifier.GetName(mod)
    local owner = Ability.GetOwner(Modifier.GetAbility(mod))
    local owner_name = NPC.GetUnitName(owner)
    print(("%s | %s -> %s"):format(modifier_name, owner_name, NPC.GetUnitName(ent)))
    add_divider()
end
--#endregion

--#region Animation
function debug.OnUnitAnimation(a)
    if not ui.callbacks.animation:Get() then return end
    print("OnUnitAnimation")
    if (ui.callbacks_settings.add_more_info:Get() and a.unit and Entity.IsNPC(a.unit)) then
        a = table.copy(a)
        local unit_name = NPC.GetUnitName(a.unit)
        a["[m]unit_name"] = unit_name
    end
    print(a)
    add_divider()
end

function debug.OnUnitAnimationEnd(a)
	if not ui.callbacks.animation:Get() then return end
    print("OnUnitAnimationEnd")
    if (ui.callbacks_settings.add_more_info:Get() and a.unit and Entity.IsNPC(a.unit)) then
        a = table.copy(a)
        local unit_name = NPC.GetUnitName(a.unit)
        a["[m]unit_name"] = unit_name
    end
    print(a)
    add_divider()
end
--#endregion

--#region EntityCreate
function debug.OnEntityCreate(entity)
    if not ui.callbacks.add_entity:Get() then return end

    print('OnEntityCreate')
    -- can't use NPC.GetUnitNameor Abilit.GetName because entity is not fully filled in the first tick
    local type = (function ()
        if Entity.IsAbility(entity) then
            return "Ability"
        elseif Entity.IsNPC(entity) then
            return "NPC"
        elseif Entity.IsPlayer(entity) then
            return "Player"
        else
            return "Entity"
        end
    end)()

    print(("%s | %s | %d"):format(type, Entity.GetClassName(entity), Entity.GetIndex(entity)))
    add_divider()
end

function debug.OnEntityDestroy(entity)
    if not ui.callbacks.add_entity:Get() then return end

	print('OnEntityDestroy')
    local type = (function ()
        if Entity.IsAbility(entity) then
            return "Ability"
        elseif Entity.IsNPC(entity) then
            return "NPC"
        elseif Entity.IsPlayer(entity) then
            return "Player"
        else
            return "Entity"
        end
    end)()

    print(("%s | %s | %d"):format(type, Entity.GetClassName(entity), Entity.GetIndex(entity)))
    add_divider()
end
--#endregion

--#region Projectile
function debug.OnProjectile(proj)
    -- range autoatacks, target abilities
	if not ui.callbacks.projectile:Get() then return end
    print("OnProjectile")
    if ui.callbacks_settings.add_more_info:Get() then
        proj = table.copy(proj)
        if (proj.source and Entity.IsNPC(proj.source)) then
            local unit_name = NPC.GetUnitName(proj.source)
            proj["[m]unit_name"] = unit_name
        end
        if (proj.target and Entity.IsNPC(proj.target)) then
            local unit_name = NPC.GetUnitName(proj.target)
            proj["[m]target_name"] = unit_name
        end
    end
    print(proj)
    add_divider()
end

function debug.OnLinearProjectileCreate(proj)
    -- mirana's arrow
    if not ui.callbacks.projectile:Get() then return end
    print("OnLinearProjectileCreate")
    if ui.callbacks_settings.add_more_info:Get() then
        proj = table.copy(proj)
        if (proj.source and Entity.IsNPC(proj.source)) then
            local unit_name = NPC.GetUnitName(proj.source)
            proj["[m]unit_name"] = unit_name
        end
    end
    print(proj)
    add_divider()
end


function debug.OnProjectileLoc(proj)
    if not ui.callbacks.projectile:Get() then return end

    -- tinker's rockets
	print("OnProjectileLoc")
    print(proj)
    add_divider()
end
--#endregion

--#region Particle
local particle_name_map = {}
function debug.OnParticleCreate(prt)
    if not ui.callbacks.particle:Get() then return end
    
    print("OnParticleCreate")
    if ui.callbacks_settings.add_more_info:Get() then
        prt = table.copy(prt)
        if (prt.entity and Entity.IsNPC(prt.entity)) then
            local unit_name = NPC.GetUnitName(prt.entity)
            prt["[m]entity_name"] = unit_name
        end
        if (prt.entityForModifiers and Entity.IsNPC(prt.entityForModifiers)) then
            local unit_name = NPC.GetUnitName(prt.entityForModifiers)
            prt["[m]entityForModifiers_name"] = unit_name
        end

        particle_name_map[prt.index] = prt.name
    end
    print(prt)
    add_divider()
end

function debug.OnParticleUpdate(prt)
    if not ui.callbacks.particle:Get() then return end

    -- wisp's tentacles spam
    if (prt.controlPoint == 2 and prt.position == Vector(1.0, 1.0, 1.0)) then
		return
	end

    print("OnParticleUpdate")
    if ui.callbacks_settings.add_more_info:Get() then
        prt = table.copy(prt)
        if particle_name_map[prt.index] then
            prt["[m]name"] = particle_name_map[prt.index]
        end
    end
    print(prt)
    add_divider()
end

function debug.OnParticleUpdateEntity(prt)
    if not ui.callbacks.particle:Get() then return end

    print("OnParticleUpdateEntity")
    if ui.callbacks_settings.add_more_info:Get() then
        prt = table.copy(prt)
        if (prt.entity and Entity.IsNPC(prt.entity)) then
            local unit_name = NPC.GetUnitName(prt.entity)
            prt["[m]entity_name"] = unit_name
        end

        if particle_name_map[prt.index] then
            prt["[m]name"] = particle_name_map[prt.index]
        end
    end
    print(prt)
    add_divider()
end

function debug.OnParticleUpdateFallback(prt)
    if not ui.callbacks.particle:Get() then return end

    print("OnParticleUpdateFallback")
    if ui.callbacks_settings.add_more_info:Get() then
        prt = table.copy(prt)
        if particle_name_map[prt.index] then
            prt["[m]name"] = particle_name_map[prt.index]
        end
    end
    print(prt)
    add_divider()
end

function debug.OnParticleDestroy(prt)
    if not ui.callbacks.particle:Get() then return end

    print("OnParticleDestroy")
    if ui.callbacks_settings.add_more_info:Get() then
        prt = table.copy(prt)
        if particle_name_map[prt.index] then
            prt["[m]name"] = particle_name_map[prt.index]
        end
    end
    print(prt)
    add_divider()

    particle_name_map[prt.index] = nil
end
--#endregion

--#region Gesture
function debug.OnUnitAddGesture(a)
    if not ui.callbacks.gesture:Get() then return end

    print("OnUnitAddGesture")
	print(a)
    add_divider()
end
--#endregion

--#region Sound
function debug.OnStartSound(obj)
    if not ui.callbacks.sound:Get() then return end

    
    print("OnStartSound")
    if ui.callbacks_settings.add_more_info:Get() then
        obj = table.copy(obj)
        if (obj.source and Entity.IsNPC(obj.source)) then
            local unit_name = NPC.GetUnitName(obj.source)
            obj["[m]source_name"] = unit_name
        end
    end
    print(obj)
    add_divider()
end
--#endregion

--#region Order
local flipped_order_enum = {}
for i, v in pairs(Enum.UnitOrder) do
    flipped_order_enum[v] = i
end

local flipped_issuer_enum = {}
for i, v in pairs(Enum.PlayerOrderIssuer) do
    flipped_issuer_enum[v] = i
end

function debug.OnPrepareUnitOrders(order)
    if not ui.callbacks.order:Get() then return end

    print("OnPrepareUnitOrders")
    if ui.callbacks_settings.add_more_info:Get() then
        order = table.copy(order)
        if (order.npc and Entity.IsNPC(order.npc)) then
            local unit_name = NPC.GetUnitName(order.npc)
            order["[m]npc_name"] = unit_name
        end
        if (order.target and Entity.IsNPC(order.target)) then
            local unit_name = NPC.GetUnitName(order.target)
            order["[m]target_name"] = unit_name
        end
        if (order.ability and Entity.IsAbility(order.ability)) then
            local ability_name = Ability.GetName(order.ability)
            order["[m]ability_name"] = ability_name
        end

        if (order.order) then
            local order_name = flipped_order_enum[order.order]
            if order_name then
                order["[m]order_name"] = order_name
            end
        end
    end

	print(order)
    add_divider()
end
--#endregion

--#endregion

local text_color <const> = Color(255, 255, 255, 255)
local font_size <const> = 14
local line_height <const> = 18

local floor = math.floor

local flipped_modstate_enum = {}
for i, v in pairs(Enum.ModifierState) do
    flipped_modstate_enum[v] = i
end

local function inworld_processing()
    if not ui.inworld.global_switch:Get() then return end

    local render_names = ui.inworld.name:Get()
    local render_position = ui.inworld.position:Get()
    local render_modifiers = ui.inworld.modifier:Get()
    local render_abilities = ui.inworld.ability:Get()
    local render_items = ui.inworld.item:Get()
    local render_modifier_state = ui.inworld.modifier_state:Get()
    local render_modifier_state_duration = ui.inworld.modifier_state_duration:Get()

    local list = ui.inworld_settings.hero_only:Get() and Heroes.GetAll() or NPCs.GetAll()
    for i, unit in pairs(list) do
        if unit then
            local pos = Entity.GetAbsOrigin(unit)
            local screen_pos, is_visible = pos:ToScreen()
            if not is_visible then
                goto continue
            end
            if render_names then
                local text = ("%s | %s | %d"):format(
                    Entity.GetClassName(unit),
                    Entity.GetClassName(unit),
                    Entity.GetIndex(unit)
                )
                Render.Text(font, font_size, text, screen_pos, text_color)
                screen_pos = screen_pos + Vec2(0, line_height)
            end
            if render_position then
                local text = ("%d, %d, %d"):format(
                    floor(pos.x),
                    floor(pos.y),
                    floor(pos.z)
                )
                Render.Text(font, font_size, text, screen_pos, text_color)
                screen_pos = screen_pos + Vec2(0, line_height)
            end
            if render_modifiers then
                local modifiers = NPC.GetModifiers(unit)
                if modifiers then
                    for _, mod in pairs(modifiers) do
                        local text = Modifier.GetName(mod)
                        Render.Text(font, font_size, text, screen_pos, text_color)
                        screen_pos = screen_pos + Vec2(0, line_height)
                    end
                end
            end
            if render_abilities then
                for i = 0, 25 do
                    local ab = NPC.GetAbilityByIndex(unit, i)
                    if ab then
                        local text = ("%d: %s"):format(i, Ability.GetName(ab))
                        Render.Text(font, font_size, text, screen_pos, text_color)
                        screen_pos = screen_pos + Vec2(0, line_height)
                    end
                end
            end
            if render_items then
                for i = 0, 20 do
                    local item = NPC.GetItemByIndex(unit, i)
                    if item then
                        local text = ("%d: %s"):format(i, Ability.GetName(item))
                        Render.Text(font, font_size, text, screen_pos, text_color)
                        screen_pos = screen_pos + Vec2(0, line_height)
                    end
                end
            end
            if render_modifier_state then
                for state_name, state_value in pairs(Enum.ModifierState) do
                    local has_state = NPC.HasState(unit, state_value)
                    if (has_state) then
                        local text = state_name
                        Render.Text(font, font_size, text, screen_pos, text_color)
                        screen_pos = screen_pos + Vec2(0, line_height)
                    end
                end
            end
            if render_modifier_state_duration then
                local payload = {}
                for i = 0, Enum.ModifierState.MODIFIER_STATE_LAST, 1 do
                    payload[i] = true
                end

                local states = NPC.GetStatesDuration(unit, payload, false)
                for mod_state, duration in pairs(states) do
                    if (duration > 0.0) then
                        local name = flipped_modstate_enum[mod_state]
                        if (name) then
                            local text = ("%s: %.2f"):format(name, duration)
                            Render.Text(font, font_size, text, screen_pos, text_color)
                            screen_pos = screen_pos + Vec2(0, line_height)
                        end
                    end
                end
            end
        end
        ::continue::
    end
end

function debug.OnDraw()
    if not ui.inworld_settings.on_draw:Get() then
        return
    end

    inworld_processing()
end

function debug.OnUpdate()
    if ui.inworld_settings.on_draw:Get() then
        return
    end

    inworld_processing()
end

return debug
```

Example

---

## Debugging

You can use `print` or `log` function to print messages to the console and `%cheat_dir%/debug.log` file.
This is useful for debugging your scripts.

This functions will automaticly stringify your tables

Example

## Useful Links

Here are some useful links:

* [Lua 5.4 Manual](https://www.lua.org/manual/5.4/)
* [VS Code Umbrella Extention](https://marketplace.visualstudio.com/items?itemName=ILKA.umbrella-vscode)

[NextCallbacks](/api-v2.0/cheats-types-and-callbacks/callbacks)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Cheats Types and Callbacks

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/callbacks -->

Copy

# 🔄Callbacks

Callbacks for lua Scripts should return a table with the following functions. If the table contains one of the functions below, it will be registered as a callback and will be called at the appropriate time.

## OnScriptsLoaded

`Callbacks.OnScriptsLoaded():` `nil`

Called after all scripts are loaded.

## OnDraw

`Callbacks.OnDraw():` `nil`

Called when the game is drawing. Works only in the game.
Recommended to use for drawing only.

## OnFrame

`Callbacks.OnFrame():` `nil`

The same as OnDraw, but called in the menu too.

## OnUpdate

`Callbacks.OnUpdate():` `nil`

Called every game update. Works only in the game.
Recommended to use for logic.

## OnPreHumanizer

`Callbacks.OnPreHumanizer():` `nil`

TODO

## OnUpdateEx

`Callbacks.OnUpdateEx():` `nil`

Called every game update. Same as OnUpdate but as well called in the menu.
Recommended to use for logic.

## OnEntityCreate

`Callbacks.OnEntityCreate(entity):` `nil`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

The entity that was created.

Called when a new entity is created.

## OnNpcSpawned

`Callbacks.OnNpcSpawned(npc):` `nil`

Name

Type

Description

**npc**

`CNpc`

The npc that was created.

Called when a npc is spawned. Unlike OnAddEntity, the entity is fully initialized here.

## OnEntityDestroy

`Callbacks.OnEntityDestroy(entity):` `nil`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

The entity that was destroyed.

Called when an entity is destroyed.

## OnModifierCreate

`Callbacks.OnModifierCreate(entity, modifier):` `nil`

Name

Type

Description

**entity**

[`CNPC`](/api-v2.0/game-components/core/npc)

The entity that has the modifier.

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

The modifier that was created.

Called when a modifier is created.

## OnModifierDestroy

`Callbacks.OnModifierDestroy(entity, modifier):` `nil`

Name

Type

Description

**entity**

[`CNPC`](/api-v2.0/game-components/core/npc)

The entity that has the modifier.

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

The modifier that was destroyed.

Called when a modifier is destroyed.

## OnModifierUpdate

`Callbacks.OnModifierUpdate(entity, modifier):` `nil`

Name

Type

Description

**entity**

[`CNPC`](/api-v2.0/game-components/core/npc)

The entity that has the modifier.

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

The modifier that was updated.

Called when a modifier is updated/refreshed.

## OnEntityHurt

This callback is called only in unsafe mode.

`Callbacks.OnEntityHurt(data):` `nil`

Name

Type

Description

**data**

`{source:CEntity` | `nil, target:CEntity` | `nil, ability:CAbility` | `nil, damage:number}`

The data about the event.

Called when an entity is hurt.

## OnEntityKilled

This callback is called only in unsafe mode.

`Callbacks.OnEntityKilled(data):` `nil`

Name

Type

Description

**data**

`{source:CEntity` | `nil, target:CEntity` | `nil, ability:CAbility` | `nil}`

The data about the event.

Called when an entity is killed.

## OnFireEventClient

This callback is called only in unsafe mode.

`Callbacks.OnFireEventClient(data):` \*\*`nil`\*\*

Name

Type

Description

**data**

`{name:string, event:Event}`

The data about the event.

Called when a game event is fired.

## OnUnitAnimation

`Callbacks.OnUnitAnimation(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**unit**

[`CNPC`](/api-v2.0/game-components/core/npc)

The unit that played the animation.

.**sequenceVariant**

`number`

The sequence variant.

.**playbackRate**

`number`

The playback rate.

.**castpoint**

`number`

The castpoint.

.**type**

`integer`

The type.

.**activity**

`integer`

The activity.

.**sequence**

`integer`

The sequence.

.**sequenceName**

`string`

The sequence name.

.**lag\_compensation\_time**

`number`

The lag compensation time.

Called when a unit animation is played.

## OnUnitAnimationEnd

`Callbacks.OnUnitAnimationEnd(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**unit**

[`CNPC`](/api-v2.0/game-components/core/npc)

The unit that played the animation.

.**snap**

`boolean`

The snap.

Called when a unit animation ends.

## OnProjectile

`Callbacks.OnProjectile(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**source**

[`CNPC`](/api-v2.0/game-components/core/npc)

The source entity.

.**target**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target entity.

.**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

The ability linked to the projectile.

.**moveSpeed**

`integer`

The move speed.

.**sourceAttachment**

`integer`

The source attachment.

.**particleSystemHandle**

`integer`

The particle system handle.

.**dodgeable**

`boolean`

The dodgeable.

.**isAttack**

`boolean`

The is attack.

.**expireTime**

`number`

The expire time.

.**maxImpactTime**

`number`

The max impact time.

.**launch\_tick**

`integer`

The tick the pojectile was launched.

.**colorGemColor**

`integer`

The color gem color.

.**fullName**

`string`

The full name of projectile.

.**name**

`string`

The short name of projectile.

.**handle**

`integer`

The handle of projectile.

.**target\_loc**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The location of the target.

.**original\_move\_speed**

`integer`

The original move speed.

Called when new projectile is created.

## OnProjectileLoc

`Callbacks.OnProjectileLoc(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**target** `[?]`

[`CNPC`](/api-v2.0/game-components/core/npc)

The source entity. `(default: nil)`

.**sourceLoc**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The source location.

.**targetLoc**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The target location.

.**moveSpeed**

`integer`

The move speed.

.**original\_move\_speed**

`integer`

The original move speed.

.**particleSystemHandle**

`integer`

The particle system handle.

.**dodgeable**

`boolean`

The dodgeable.

.**isAttack**

`boolean`

The is attack.

.**expireTime**

`number`

The expire time.

.**colorGemColor**

`integer`

The color gem color.

.**launchTick**

`integer`

The launch tick.

.**handle**

`integer`

The handle of projectile.

.**fullName**

`string`

The full name of projectile.

.**name**

`string`

The short name of projectile.

Called when new projectile loc is created.

## OnLinearProjectileCreate

`Callbacks.OnLinearProjectileCreate(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**source**

[`CNPC`](/api-v2.0/game-components/core/npc)

The source entity.

.**origin**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The origin.

.**velocity**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The velocity.

.**particleIndex**

`integer`

The particle index.

.**handle**

`integer`

The handle of projectile.

.**acceleration**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The acceleration.

.**maxSpeed**

`number`

The max speed.

.**fowRadius**

`number`

The fow radius.

.**distance**

`number`

The distance.

.**colorGemColor**

`integer`

The color gem color.

.**fullName**

`string`

The full name of projectile.

.**name**

`string`

The short name of projectile.

Called when new linear projectile is created.

## OnLinearProjectileDestroy

`Callbacks.OnLinearProjectileDestroy(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**handle**

`integer`

The handle of projectile.

Called when linear projectile is destroyed.

## OnParticleCreate

`Callbacks.OnParticleCreate(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**index**

`integer`

The index of particle.

.**entity** `[?]`

[`CNPC`](/api-v2.0/game-components/core/npc)

The entity. `(default: nil)`

.**entity\_id**

`integer`

The entity id.

.**entityForModifiers** `[?]`

[`CNPC`](/api-v2.0/game-components/core/npc)

The entity for modifiers. `(default: nil)`

.**entity\_for\_modifiers\_id**

`integer`

The entity for modifiers id.

.**attachType**

[`Enum.ParticleAttachment`](/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

The attach type.

.**fullName**

`string`

The full name of particle.

.**name**

`string`

The short name of particle.

.**hash**

`integer`

The hash of particle.

.**particleNameIndex**

`integer`

The particle name index.

Called when new particle is created.

## OnParticleUpdate

`Callbacks.OnParticleUpdate(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**index**

`integer`

The index of particle.

.**controlPoint**

`integer`

The control point.

.**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The position.

Called when particle is updated.

## OnParticleUpdateFallback

`Callbacks.OnParticleUpdateFallback(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**index**

`integer`

The index of particle.

.**controlPoint**

`integer`

The control point.

.**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The position.

Called when particle is updated. Alternative version for some particles.

## OnParticleUpdateEntity

`Callbacks.OnParticleUpdateEntity(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**index**

`integer`

The index of particle.

.**controlPoint**

`integer`

The control point.

.**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

The entity.

.**entIdx**

`integer`

The entity id.

.**attachType**

[`Enum.ParticleAttachment`](/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

The attach type.

.**attachmentName**

`string`

The attachment name.

.**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The position.

.**includeWearables**

`boolean`

Include wearables.

Called when particle is updated on entity.

## OnParticleDestroy

`Callbacks.OnParticleDestroy(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**index**

`integer`

The index of destroyed particle.

.**destroyImmediately**

`boolean`

Destroy immediately.

Called when particle is destroyed.

## OnStartSound

`Callbacks.OnStartSound(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**source** `[?]`

[`CEntity`](/api-v2.0/game-components/core/entity)

The source of sound. `(default: nil)`

.**hash**

`integer`

The hash of sound.

.**guid**

`integer`

The guid of sound.

.**seed**

`integer`

The seed of sound.

.**name**

`string`

The name of sound.

.**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The position of sound.

Called when sound is started.

## OnSpeak

`Callbacks.OnSpeak(data):` `boolean`

Name

Type

Description

**data**

`table`

The data about the event.

.**source**

[`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

The unit who speak.

.**name**

`string`

The name of the sound.

Called every time unit/announcer talk. You could return false to prevent the sound from being played.

## OnChatEvent

`Callbacks.OnChatEvent(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**type**

`integer`

The type of chat event.

.**value**

`integer`

The value of chat event.

.**value2**

`integer`

The value2 of chat event.

.**value3**

`integer`

The value3 of chat event.

.**playerid\_1**

`integer`

The playerid\_1 of chat event.

.**playerid\_2**

`integer`

The playerid\_2 of chat event.

.**playerid\_3**

`integer`

The playerid\_3 of chat event.

.**playerid\_4**

`integer`

The playerid\_4 of chat event.

.**playerid\_5**

`integer`

The playerid\_5 of chat event.

.**playerid\_6**

`integer`

The playerid\_6 of chat event.

Called on chat event.

## OnOverHeadEvent

`Callbacks.OnOverHeadEvent(data):` `nil`

Name

Type

Description

**data**

`{player_source:CPlayer` | `nil, player_target:CPlayer` | `nil, target_npc:CNPC, value:integer}`

The table with the event info.

Called on event above the hero's head.

## OnUnitAddGesture

`Callbacks.OnUnitAddGesture(data):` `nil`

Name

Type

Description

**data**

`table`

The data about the event.

.**npc** `[?]`

[`CNPC`](/api-v2.0/game-components/core/npc)

The unit that is added to a gesture. `(default: nil)`

.**sequenceVariant**

`integer`

The sequence variant.

.**playbackRate**

`number`

The playback rate.

.**fadeIn**

`number`

The fade in.

.**fadeOut**

`number`

The fade out.

.**slot**

`integer`

The slot.

.**activity**

`integer`

The activity.

.**sequenceName**

`string`

The sequence name.

Called when a unit is added to a gesture.

## OnPrepareUnitOrders

`Callbacks.OnPrepareUnitOrders(data):` `boolean`

Name

Type

Description

**data**

`table`

The data about the event.

.**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The player that issued the order.

.**order**

[`Enum.UnitOrder`](/api-v2.0/cheats-types-and-callbacks/enums#enum.unitorder)

The order type.

.**target** `[?]`

[`CEntity`](/api-v2.0/game-components/core/entity)

The target of the order. `(default: nil)`

.**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The position of the order.

.**ability** `[?]`

[`CAbility`](/api-v2.0/game-components/core/ability)

The ability of the order. `(default: nil)`

.**orderIssuer**

[`Enum.PlayerOrderIssuer`](/api-v2.0/cheats-types-and-callbacks/enums#enum.playerorderissuer)

The order issuer.

.**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The unit of the order.

.**queue**

`boolean`

If the order is queued.

.**showEffects**

`boolean`

The show effects of the order.

Called on every player order. Return false to prevent the order from being executed.

## OnGCMessage

`Callbacks.OnGCMessage(data):` `boolean`

Name

Type

Description

**data**

`table`

.**msg\_type**

`number`

The message type.

.**size**

`number`

The size of the message.

.**binary\_buffer\_send** `[?]`

`userdata`

The binary buffer of the send message. `(default: nil)`

.**binary\_buffer\_recv** `[?]`

`userdata`

The binary buffer of the recieved message. `(default: nil)`

Called when a game coordinator protobuff message is received. Return false to prevent the message
from being sent (doesnt work with recieved messages). For more look at GC table description.

#### Example

## OnSendNetMessage

`Callbacks.OnSendNetMessage(data):` `boolean`

Name

Type

Description

**data**

`table`

The data about the event.

.**message\_id**

`number`

The message id.

.**message\_name**

`string`

The message name.

.**buffer**

`lightuserdata`

The encoded buffer of the message.

.**size**

`number`

The size of the message.

Called when a net message is sent. Return false to prevent the message from being sent. See
example

#### Example

## OnPostReceivedNetMessage

`Callbacks.OnPostReceivedNetMessage(data):` `boolean`

Name

Type

Description

**data**

`table`

The data about the event.

.**message\_id**

`number`

The message id.

.**msg\_object**

`lightuserdata`

The encoded buffer of the message.

Called when a net message is received. Return false to prevent the message from being recieved

#### Example

## OnGameEnd

`Callbacks.OnGameEnd():` `nil`

Called on game end.
Recommended to use for zeroing.

## OnKeyEvent

`Callbacks.OnKeyEvent(data):` `boolean`

Name

Type

Description

**data**

`table`

The data about the event.

.**key**

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

The key code.

.**event**

[`Enum.EKeyEvent`](/api-v2.0/cheats-types-and-callbacks/enums#enum.ekeyevent)

Key event.

Called on key and mouse input. Return false to prevent the event from being processed.

## OnUnitInventoryUpdated

`Callbacks.OnUnitInventoryUpdated(data):` `nil`

Name

Type

Description

**data**

[`CNPC`](/api-v2.0/game-components/core/npc)

The data about the event.

Called on unit inventory updated.

## OnSetDormant

`Callbacks.OnSetDormant(npc, type):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target npc.

**type**

[`Enum.DormancyType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.dormancytype)

The type of change.

Called on NPC dormancy state changed.

## OnGameRulesStateChange

`Callbacks.OnGameRulesStateChange(data):` `nil`

Name

Type

Description

**data**

`{}`

The table with new game state info.

Called on gamestate change.

## OnNpcDying

`Callbacks.OnNpcDying(npc):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target npc.

Called on NPC dying.

[PreviousStarting Guide](/api-v2.0)[NextEnums](/api-v2.0/cheats-types-and-callbacks/enums)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums -->

Copy

# 📊Enums

## Enum.ShopType

Key

Value

`DOTA_SHOP_HOME`

0

`DOTA_SHOP_SIDE`

1

`DOTA_SHOP_SECRET`

2

`DOTA_SHOP_GROUND`

3

`DOTA_SHOP_SIDE2`

4

`DOTA_SHOP_SECRET2`

5

`DOTA_SHOP_CUSTOM`

6

`DOTA_SHOP_NEUTRALS`

7

`DOTA_SHOP_NONE`

8

## Enum.AbilityTypes

Key

Value

`ABILITY_TYPE_BASIC`

0

`ABILITY_TYPE_ULTIMATE`

1

`ABILITY_TYPE_ATTRIBUTES`

2

`ABILITY_TYPE_HIDDEN`

3

## Enum.AbilityBehavior

Key

Value

`DOTA_ABILITY_BEHAVIOR_NONE`

0

`DOTA_ABILITY_BEHAVIOR_HIDDEN`

1

`DOTA_ABILITY_BEHAVIOR_PASSIVE`

2

`DOTA_ABILITY_BEHAVIOR_NO_TARGET`

4

`DOTA_ABILITY_BEHAVIOR_UNIT_TARGET`

8

`DOTA_ABILITY_BEHAVIOR_POINT`

16

`DOTA_ABILITY_BEHAVIOR_AOE`

32

`DOTA_ABILITY_BEHAVIOR_NOT_LEARNABLE`

64

`DOTA_ABILITY_BEHAVIOR_CHANNELLED`

128

`DOTA_ABILITY_BEHAVIOR_ITEM`

256

`DOTA_ABILITY_BEHAVIOR_TOGGLE`

512

`DOTA_ABILITY_BEHAVIOR_DIRECTIONAL`

1024

`DOTA_ABILITY_BEHAVIOR_IMMEDIATE`

2048

`DOTA_ABILITY_BEHAVIOR_AUTOCAST`

4096

`DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET`

8192

`DOTA_ABILITY_BEHAVIOR_OPTIONAL_POINT`

16384

`DOTA_ABILITY_BEHAVIOR_OPTIONAL_NO_TARGET`

32768

`DOTA_ABILITY_BEHAVIOR_AURA`

65536

`DOTA_ABILITY_BEHAVIOR_ATTACK`

131072

`DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT`

262144

`DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES`

524288

`DOTA_ABILITY_BEHAVIOR_UNRESTRICTED`

1048576

`DOTA_ABILITY_BEHAVIOR_IGNORE_PSEUDO_QUEUE`

2097152

`DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL`

4194304

`DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT`

8388608

`DOTA_ABILITY_BEHAVIOR_DONT_ALERT_TARGET`

16777216

`DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK`

33554432

`DOTA_ABILITY_BEHAVIOR_NORMAL_WHEN_STOLEN`

67108864

`DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING`

134217728

`DOTA_ABILITY_BEHAVIOR_RUNE_TARGET`

268435456

`DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_CHANNEL`

536870912

`DOTA_ABILITY_BEHAVIOR_VECTOR_TARGETING`

1073741824

`DOTA_ABILITY_BEHAVIOR_LAST_RESORT_POINT`

2147483648

`DOTA_ABILITY_BEHAVIOR_CAN_SELF_CAST`

4294967296

`DOTA_ABILITY_BEHAVIOR_SHOW_IN_GUIDES`

8589934592

`DOTA_ABILITY_BEHAVIOR_UNLOCKED_BY_EFFECT_INDEX`

17179869184

`DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE`

34359738368

`DOTA_ABILITY_BEHAVIOR_FREE_DRAW_TARGETING`

68719476736

`DOTA_ABILITY_BEHAVIOR_IGNORE_SILENCE`

137438953472

`DOTA_ABILITY_BEHAVIOR_IGNORE_MUTED`

549755813888

`DOTA_ABILITY_BEHAVIOR_ALT_CASTABLE`

1099511627776

`DOTA_ABILITY_BEHAVIOR_SKIP_FOR_KEYBINDS`

4398046511104

## Enum.TargetTeam

Key

Value

`DOTA_UNIT_TARGET_TEAM_NONE`

0

`DOTA_UNIT_TARGET_TEAM_FRIENDLY`

1

`DOTA_UNIT_TARGET_TEAM_ENEMY`

2

`DOTA_UNIT_TARGET_TEAM_CUSTOM`

4

`DOTA_UNIT_TARGET_TEAM_BOTH`

3

## Enum.TargetType

Key

Value

`DOTA_UNIT_TARGET_NONE`

0

`DOTA_UNIT_TARGET_HERO`

1

`DOTA_UNIT_TARGET_CREEP`

2

`DOTA_UNIT_TARGET_BUILDING`

4

`DOTA_UNIT_TARGET_COURIER`

16

`DOTA_UNIT_TARGET_OTHER`

32

`DOTA_UNIT_TARGET_TREE`

64

`DOTA_UNIT_TARGET_CUSTOM`

128

`DOTA_UNIT_TARGET_SELF`

256

`DOTA_UNIT_TARGET_BASIC`

18

`DOTA_UNIT_TARGET_ALL`

55

`DOTA_UNIT_TARGET_HEROES_AND_CREEPS`

19

## Enum.TargetFlags

Key

Value

`DOTA_UNIT_TARGET_FLAG_NONE`

0

`DOTA_UNIT_TARGET_FLAG_RANGED_ONLY`

2

`DOTA_UNIT_TARGET_FLAG_MELEE_ONLY`

4

`DOTA_UNIT_TARGET_FLAG_DEAD`

8

`DOTA_UNIT_TARGET_FLAG_MAGIC_IMMUNE_ENEMIES`

16

`DOTA_UNIT_TARGET_FLAG_NOT_MAGIC_IMMUNE_ALLIES`

32

`DOTA_UNIT_TARGET_FLAG_INVULNERABLE`

64

`DOTA_UNIT_TARGET_FLAG_FOW_VISIBLE`

128

`DOTA_UNIT_TARGET_FLAG_NO_INVIS`

256

`DOTA_UNIT_TARGET_FLAG_NOT_ANCIENTS`

512

`DOTA_UNIT_TARGET_FLAG_PLAYER_CONTROLLED`

1024

`DOTA_UNIT_TARGET_FLAG_NOT_DOMINATED`

2048

`DOTA_UNIT_TARGET_FLAG_NOT_SUMMONED`

4096

`DOTA_UNIT_TARGET_FLAG_NOT_ILLUSIONS`

8192

`DOTA_UNIT_TARGET_FLAG_NOT_ATTACK_IMMUNE`

16384

`DOTA_UNIT_TARGET_FLAG_MANA_ONLY`

32768

`DOTA_UNIT_TARGET_FLAG_CHECK_DISABLE_HELP`

65536

`DOTA_UNIT_TARGET_FLAG_NOT_CREEP_HERO`

131072

`DOTA_UNIT_TARGET_FLAG_OUT_OF_WORLD`

262144

`DOTA_UNIT_TARGET_FLAG_NOT_NIGHTMARED`

524288

`DOTA_UNIT_TARGET_FLAG_PREFER_ENEMIES`

1048576

`DOTA_UNIT_TARGET_FLAG_RESPECT_OBSTRUCTIONS`

2097152

## Enum.DamageTypes

Key

Value

`DAMAGE_TYPE_NONE`

0

`DAMAGE_TYPE_PHYSICAL`

1

`DAMAGE_TYPE_MAGICAL`

2

`DAMAGE_TYPE_PURE`

4

`DAMAGE_TYPE_HP_REMOVAL`

8

`DAMAGE_TYPE_ALL`

7

## Enum.TalentTypes

Key

Value

`TALENT_1`

1

`TALENT_2`

2

`TALENT_3`

4

`TALENT_4`

8

`TALENT_5`

16

`TALENT_6`

32

`TALENT_7`

64

`TALENT_8`

128

## Enum.ImmunityTypes

Key

Value

`SPELL_IMMUNITY_NONE`

0

`SPELL_IMMUNITY_ALLIES_YES`

1

`SPELL_IMMUNITY_ALLIES_NO`

2

`SPELL_IMMUNITY_ENEMIES_YES`

3

`SPELL_IMMUNITY_ENEMIES_NO`

4

`SPELL_IMMUNITY_ALLIES_YES_ENEMIES_NO`

5

## Enum.DispellableTypes

Key

Value

`SPELL_DISPELLABLE_NONE`

0

`SPELL_DISPELLABLE_YES_STRONG`

1

`SPELL_DISPELLABLE_YES`

2

`SPELL_DISPELLABLE_NO`

3

## Enum.TeamType

Key

Value

`TEAM_ENEMY`

0

`TEAM_FRIEND`

1

`TEAM_BOTH`

2

## Enum.ECampType

Key

Value

`ECampType_SMALL`

0

`ECampType_MEDIUM`

1

`ECampType_LARGE`

2

`ECampType_ANCIENT`

3

## Enum.EKeyEvent

Key

Value

`EKeyEvent_SCROLL_DOWN`

0

`EKeyEvent_SCROLL_UP`

1

`EKeyEvent_KEY_DOWN`

2

`EKeyEvent_KEY_UP`

3

## Enum.CourierState

Key

Value

`COURIER_STATE_INIT`

4294967295

`COURIER_STATE_IDLE`

0

`COURIER_STATE_AT_BASE`

1

`COURIER_STATE_MOVING`

2

`COURIER_STATE_DELIVERING_ITEMS`

3

`COURIER_STATE_RETURNING_TO_BASE`

4

`COURIER_STATE_DEAD`

5

`COURIER_STATE_GOING_TO_SECRET_SHOP`

6

`COURIER_STATE_AT_SECRET_SHOP`

7

`COURIER_NUM_STATES`

8

## Enum.RuneType

Key

Value

`DOTA_RUNE_INVALID`

4294967295

`DOTA_RUNE_DOUBLEDAMAGE`

0

`DOTA_RUNE_HASTE`

1

`DOTA_RUNE_ILLUSION`

2

`DOTA_RUNE_INVISIBILITY`

3

`DOTA_RUNE_REGENERATION`

4

`DOTA_RUNE_BOUNTY`

5

`DOTA_RUNE_ARCANE`

6

`DOTA_RUNE_WATER`

7

`DOTA_RUNE_XP`

8

`DOTA_RUNE_SHIELD`

9

`DOTA_RUNE_COUNT`

10

## Enum.ModifierState

Key

Value

`MODIFIER_STATE_ROOTED`

0

`MODIFIER_STATE_DISARMED`

1

`MODIFIER_STATE_ATTACK_IMMUNE`

2

`MODIFIER_STATE_SILENCED`

3

`MODIFIER_STATE_MUTED`

4

`MODIFIER_STATE_STUNNED`

5

`MODIFIER_STATE_HEXED`

6

`MODIFIER_STATE_INVISIBLE`

7

`MODIFIER_STATE_INVULNERABLE`

8

`MODIFIER_STATE_MAGIC_IMMUNE`

9

`MODIFIER_STATE_PROVIDES_VISION`

10

`MODIFIER_STATE_NIGHTMARED`

11

`MODIFIER_STATE_BLOCK_DISABLED`

12

`MODIFIER_STATE_EVADE_DISABLED`

13

`MODIFIER_STATE_UNSELECTABLE`

14

`MODIFIER_STATE_CANNOT_TARGET_ENEMIES`

15

`MODIFIER_STATE_CANNOT_TARGET_BUILDINGS`

16

`MODIFIER_STATE_CANNOT_MISS`

17

`MODIFIER_STATE_SPECIALLY_DENIABLE`

18

`MODIFIER_STATE_FROZEN`

19

`MODIFIER_STATE_COMMAND_RESTRICTED`

20

`MODIFIER_STATE_NOT_ON_MINIMAP`

21

`MODIFIER_STATE_LOW_ATTACK_PRIORITY`

22

`MODIFIER_STATE_NO_HEALTH_BAR`

23

`MODIFIER_STATE_NO_HEALTH_BAR_FOR_ENEMIES`

24

`MODIFIER_STATE_NO_HEALTH_BAR_FOR_OTHER_PLAYERS`

25

`MODIFIER_STATE_FLYING`

26

`MODIFIER_STATE_NO_UNIT_COLLISION`

27

`MODIFIER_STATE_NO_TEAM_MOVE_TO`

28

`MODIFIER_STATE_NO_TEAM_SELECT`

29

`MODIFIER_STATE_PASSIVES_DISABLED`

30

`MODIFIER_STATE_DOMINATED`

31

`MODIFIER_STATE_BLIND`

32

`MODIFIER_STATE_OUT_OF_GAME`

33

`MODIFIER_STATE_FAKE_ALLY`

34

`MODIFIER_STATE_FLYING_FOR_PATHING_PURPOSES_ONLY`

35

`MODIFIER_STATE_TRUESIGHT_IMMUNE`

36

`MODIFIER_STATE_UNTARGETABLE`

37

`MODIFIER_STATE_UNTARGETABLE_ALLIED`

38

`MODIFIER_STATE_UNTARGETABLE_ENEMY`

39

`MODIFIER_STATE_UNTARGETABLE_SELF`

40

`MODIFIER_STATE_IGNORING_MOVE_AND_ATTACK_ORDERS`

41

`MODIFIER_STATE_ALLOW_PATHING_THROUGH_TREES`

42

`MODIFIER_STATE_NOT_ON_MINIMAP_FOR_ENEMIES`

43

`MODIFIER_STATE_UNSLOWABLE`

44

`MODIFIER_STATE_TETHERED`

45

`MODIFIER_STATE_IGNORING_STOP_ORDERS`

46

`MODIFIER_STATE_FEARED`

47

`MODIFIER_STATE_TAUNTED`

48

`MODIFIER_STATE_CANNOT_BE_MOTION_CONTROLLED`

49

`MODIFIER_STATE_FORCED_FLYING_VISION`

50

`MODIFIER_STATE_ATTACK_ALLIES`

51

`MODIFIER_STATE_ALLOW_PATHING_THROUGH_CLIFFS`

52

`MODIFIER_STATE_ALLOW_PATHING_THROUGH_FISSURE`

53

`MODIFIER_STATE_SPECIALLY_UNDENIABLE`

54

`MODIFIER_STATE_ALLOW_PATHING_THROUGH_OBSTRUCTIONS`

55

`MODIFIER_STATE_DEBUFF_IMMUNE`

56

`MODIFIER_STATE_NEUTRALS_DONT_ATTACK`

63

`MODIFIER_STATE_ALLOW_PATHING_THROUGH_BASE_BLOCKER`

57

`MODIFIER_STATE_IGNORING_MOVE_ORDERS`

58

`MODIFIER_STATE_ATTACKS_ARE_MELEE`

59

`MODIFIER_STATE_CAN_USE_BACKPACK_ITEMS`

60

`MODIFIER_STATE_CASTS_IGNORE_CHANNELING`

61

`MODIFIER_STATE_ATTACKS_DONT_REVEAL`

62

`MODIFIER_STATE_LAST`

64

## Enum.GameActivity

Key

Value

`ACT_DOTA_IDLE`

1500

`ACT_DOTA_IDLE_RARE`

1501

`ACT_DOTA_RUN`

1502

`ACT_DOTA_ATTACK`

1503

`ACT_DOTA_ATTACK2`

1504

`ACT_DOTA_ATTACK_EVENT`

1505

`ACT_DOTA_DIE`

1506

`ACT_DOTA_FLINCH`

1507

`ACT_DOTA_FLAIL`

1508

`ACT_DOTA_DISABLED`

1509

`ACT_DOTA_CAST_ABILITY_1`

1510

`ACT_DOTA_CAST_ABILITY_2`

1511

`ACT_DOTA_CAST_ABILITY_3`

1512

`ACT_DOTA_CAST_ABILITY_4`

1513

`ACT_DOTA_CAST_ABILITY_5`

1514

`ACT_DOTA_CAST_ABILITY_6`

1515

`ACT_DOTA_OVERRIDE_ABILITY_1`

1516

`ACT_DOTA_OVERRIDE_ABILITY_2`

1517

`ACT_DOTA_OVERRIDE_ABILITY_3`

1518

`ACT_DOTA_OVERRIDE_ABILITY_4`

1519

`ACT_DOTA_CHANNEL_ABILITY_1`

1520

`ACT_DOTA_CHANNEL_ABILITY_2`

1521

`ACT_DOTA_CHANNEL_ABILITY_3`

1522

`ACT_DOTA_CHANNEL_ABILITY_4`

1523

`ACT_DOTA_CHANNEL_ABILITY_5`

1524

`ACT_DOTA_CHANNEL_ABILITY_6`

1525

`ACT_DOTA_CHANNEL_END_ABILITY_1`

1526

`ACT_DOTA_CHANNEL_END_ABILITY_2`

1527

`ACT_DOTA_CHANNEL_END_ABILITY_3`

1528

`ACT_DOTA_CHANNEL_END_ABILITY_4`

1529

`ACT_DOTA_CHANNEL_END_ABILITY_5`

1530

`ACT_DOTA_CHANNEL_END_ABILITY_6`

1531

`ACT_DOTA_CONSTANT_LAYER`

1532

`ACT_DOTA_CAPTURE`

1533

`ACT_DOTA_SPAWN`

1534

`ACT_DOTA_KILLTAUNT`

1535

`ACT_DOTA_TAUNT`

1536

`ACT_DOTA_THIRST`

1537

`ACT_DOTA_CAST_DRAGONBREATH`

1538

`ACT_DOTA_ECHO_SLAM`

1539

`ACT_DOTA_CAST_ABILITY_1_END`

1540

`ACT_DOTA_CAST_ABILITY_2_END`

1541

`ACT_DOTA_CAST_ABILITY_3_END`

1542

`ACT_DOTA_CAST_ABILITY_4_END`

1543

`ACT_MIRANA_LEAP_END`

1544

`ACT_WAVEFORM_START`

1545

`ACT_WAVEFORM_END`

1546

`ACT_DOTA_CAST_ABILITY_ROT`

1547

`ACT_DOTA_DIE_SPECIAL`

1548

`ACT_DOTA_RATTLETRAP_BATTERYASSAULT`

1549

`ACT_DOTA_RATTLETRAP_POWERCOGS`

1550

`ACT_DOTA_RATTLETRAP_HOOKSHOT_START`

1551

`ACT_DOTA_RATTLETRAP_HOOKSHOT_LOOP`

1552

`ACT_DOTA_RATTLETRAP_HOOKSHOT_END`

1553

`ACT_STORM_SPIRIT_OVERLOAD_RUN_OVERRIDE`

1554

`ACT_DOTA_TINKER_REARM1`

1555

`ACT_DOTA_TINKER_REARM2`

1556

`ACT_DOTA_TINKER_REARM3`

1557

`ACT_TINY_AVALANCHE`

1558

`ACT_TINY_TOSS`

1559

`ACT_TINY_GROWL`

1560

`ACT_DOTA_WEAVERBUG_ATTACH`

1561

`ACT_DOTA_CAST_WILD_AXES_END`

1562

`ACT_DOTA_CAST_LIFE_BREAK_START`

1563

`ACT_DOTA_CAST_LIFE_BREAK_END`

1564

`ACT_DOTA_NIGHTSTALKER_TRANSITION`

1565

`ACT_DOTA_LIFESTEALER_RAGE`

1566

`ACT_DOTA_LIFESTEALER_OPEN_WOUNDS`

1567

`ACT_DOTA_SAND_KING_BURROW_IN`

1568

`ACT_DOTA_SAND_KING_BURROW_OUT`

1569

`ACT_DOTA_EARTHSHAKER_TOTEM_ATTACK`

1570

`ACT_DOTA_WHEEL_LAYER`

1571

`ACT_DOTA_ALCHEMIST_CHEMICAL_RAGE_START`

1572

`ACT_DOTA_ALCHEMIST_CONCOCTION`

1573

`ACT_DOTA_JAKIRO_LIQUIDFIRE_START`

1574

`ACT_DOTA_JAKIRO_LIQUIDFIRE_LOOP`

1575

`ACT_DOTA_LIFESTEALER_INFEST`

1576

`ACT_DOTA_LIFESTEALER_INFEST_END`

1577

`ACT_DOTA_LASSO_LOOP`

1578

`ACT_DOTA_ALCHEMIST_CONCOCTION_THROW`

1579

`ACT_DOTA_ALCHEMIST_CHEMICAL_RAGE_END`

1580

`ACT_DOTA_CAST_COLD_SNAP`

1581

`ACT_DOTA_CAST_GHOST_WALK`

1582

`ACT_DOTA_CAST_TORNADO`

1583

`ACT_DOTA_CAST_EMP`

1584

`ACT_DOTA_CAST_ALACRITY`

1585

`ACT_DOTA_CAST_CHAOS_METEOR`

1586

`ACT_DOTA_CAST_SUN_STRIKE`

1587

`ACT_DOTA_CAST_FORGE_SPIRIT`

1588

`ACT_DOTA_CAST_ICE_WALL`

1589

`ACT_DOTA_CAST_DEAFENING_BLAST`

1590

`ACT_DOTA_VICTORY`

1591

`ACT_DOTA_DEFEAT`

1592

`ACT_DOTA_SPIRIT_BREAKER_CHARGE_POSE`

1593

`ACT_DOTA_SPIRIT_BREAKER_CHARGE_END`

1594

`ACT_DOTA_TELEPORT`

1595

`ACT_DOTA_TELEPORT_END`

1596

`ACT_DOTA_CAST_REFRACTION`

1597

`ACT_DOTA_CAST_ABILITY_7`

1598

`ACT_DOTA_CANCEL_SIREN_SONG`

1599

`ACT_DOTA_CHANNEL_ABILITY_7`

1600

`ACT_DOTA_LOADOUT`

1601

`ACT_DOTA_FORCESTAFF_END`

1602

`ACT_DOTA_POOF_END`

1603

`ACT_DOTA_SLARK_POUNCE`

1604

`ACT_DOTA_MAGNUS_SKEWER_START`

1605

`ACT_DOTA_MAGNUS_SKEWER_END`

1606

`ACT_DOTA_MEDUSA_STONE_GAZE`

1607

`ACT_DOTA_RELAX_START`

1608

`ACT_DOTA_RELAX_LOOP`

1609

`ACT_DOTA_RELAX_END`

1610

`ACT_DOTA_CENTAUR_STAMPEDE`

1611

`ACT_DOTA_BELLYACHE_START`

1612

`ACT_DOTA_BELLYACHE_LOOP`

1613

`ACT_DOTA_BELLYACHE_END`

1614

`ACT_DOTA_ROQUELAIRE_LAND`

1615

`ACT_DOTA_ROQUELAIRE_LAND_IDLE`

1616

`ACT_DOTA_GREEVIL_CAST`

1617

`ACT_DOTA_GREEVIL_OVERRIDE_ABILITY`

1618

`ACT_DOTA_GREEVIL_HOOK_START`

1619

`ACT_DOTA_GREEVIL_HOOK_END`

1620

`ACT_DOTA_GREEVIL_BLINK_BONE`

1621

`ACT_DOTA_IDLE_SLEEPING`

1622

`ACT_DOTA_INTRO`

1623

`ACT_DOTA_GESTURE_POINT`

1624

`ACT_DOTA_GESTURE_ACCENT`

1625

`ACT_DOTA_SLEEPING_END`

1626

`ACT_DOTA_AMBUSH`

1627

`ACT_DOTA_ITEM_LOOK`

1628

`ACT_DOTA_STARTLE`

1629

`ACT_DOTA_FRUSTRATION`

1630

`ACT_DOTA_TELEPORT_REACT`

1631

`ACT_DOTA_TELEPORT_END_REACT`

1632

`ACT_DOTA_SHRUG`

1633

`ACT_DOTA_RELAX_LOOP_END`

1634

`ACT_DOTA_PRESENT_ITEM`

1635

`ACT_DOTA_IDLE_IMPATIENT`

1636

`ACT_DOTA_SHARPEN_WEAPON`

1637

`ACT_DOTA_SHARPEN_WEAPON_OUT`

1638

`ACT_DOTA_IDLE_SLEEPING_END`

1639

`ACT_DOTA_BRIDGE_DESTROY`

1640

`ACT_DOTA_TAUNT_SNIPER`

1641

`ACT_DOTA_DEATH_BY_SNIPER`

1642

`ACT_DOTA_LOOK_AROUND`

1643

`ACT_DOTA_CAGED_CREEP_RAGE`

1644

`ACT_DOTA_CAGED_CREEP_RAGE_OUT`

1645

`ACT_DOTA_CAGED_CREEP_SMASH`

1646

`ACT_DOTA_CAGED_CREEP_SMASH_OUT`

1647

`ACT_DOTA_IDLE_IMPATIENT_SWORD_TAP`

1648

`ACT_DOTA_INTRO_LOOP`

1649

`ACT_DOTA_BRIDGE_THREAT`

1650

`ACT_DOTA_DAGON`

1651

`ACT_DOTA_CAST_ABILITY_2_ES_ROLL_START`

1652

`ACT_DOTA_CAST_ABILITY_2_ES_ROLL`

1653

`ACT_DOTA_CAST_ABILITY_2_ES_ROLL_END`

1654

`ACT_DOTA_NIAN_PIN_START`

1655

`ACT_DOTA_NIAN_PIN_LOOP`

1656

`ACT_DOTA_NIAN_PIN_END`

1657

`ACT_DOTA_LEAP_STUN`

1658

`ACT_DOTA_LEAP_SWIPE`

1659

`ACT_DOTA_NIAN_INTRO_LEAP`

1660

`ACT_DOTA_AREA_DENY`

1661

`ACT_DOTA_NIAN_PIN_TO_STUN`

1662

`ACT_DOTA_RAZE_1`

1663

`ACT_DOTA_RAZE_2`

1664

`ACT_DOTA_RAZE_3`

1665

`ACT_DOTA_UNDYING_DECAY`

1666

`ACT_DOTA_UNDYING_SOUL_RIP`

1667

`ACT_DOTA_UNDYING_TOMBSTONE`

1668

`ACT_DOTA_WHIRLING_AXES_RANGED`

1669

`ACT_DOTA_SHALLOW_GRAVE`

1670

`ACT_DOTA_COLD_FEET`

1671

`ACT_DOTA_ICE_VORTEX`

1672

`ACT_DOTA_CHILLING_TOUCH`

1673

`ACT_DOTA_ENFEEBLE`

1674

`ACT_DOTA_FATAL_BONDS`

1675

`ACT_DOTA_MIDNIGHT_PULSE`

1676

`ACT_DOTA_ANCESTRAL_SPIRIT`

1677

`ACT_DOTA_THUNDER_STRIKE`

1678

`ACT_DOTA_KINETIC_FIELD`

1679

`ACT_DOTA_STATIC_STORM`

1680

`ACT_DOTA_MINI_TAUNT`

1681

`ACT_DOTA_ARCTIC_BURN_END`

1682

`ACT_DOTA_LOADOUT_RARE`

1683

`ACT_DOTA_SWIM`

1684

`ACT_DOTA_FLEE`

1685

`ACT_DOTA_TROT`

1686

`ACT_DOTA_SHAKE`

1687

`ACT_DOTA_SWIM_IDLE`

1688

`ACT_DOTA_WAIT_IDLE`

1689

`ACT_DOTA_GREET`

1690

`ACT_DOTA_TELEPORT_COOP_START`

1691

`ACT_DOTA_TELEPORT_COOP_WAIT`

1692

`ACT_DOTA_TELEPORT_COOP_END`

1693

`ACT_DOTA_TELEPORT_COOP_EXIT`

1694

`ACT_DOTA_SHOPKEEPER_PET_INTERACT`

1695

`ACT_DOTA_ITEM_PICKUP`

1696

`ACT_DOTA_ITEM_DROP`

1697

`ACT_DOTA_CAPTURE_PET`

1698

`ACT_DOTA_PET_WARD_OBSERVER`

1699

`ACT_DOTA_PET_WARD_SENTRY`

1700

`ACT_DOTA_PET_LEVEL`

1701

`ACT_DOTA_CAST_BURROW_END`

1702

`ACT_DOTA_LIFESTEALER_ASSIMILATE`

1703

`ACT_DOTA_LIFESTEALER_EJECT`

1704

`ACT_DOTA_ATTACK_EVENT_BASH`

1705

`ACT_DOTA_CAPTURE_RARE`

1706

`ACT_DOTA_AW_MAGNETIC_FIELD`

1707

`ACT_DOTA_CAST_GHOST_SHIP`

1708

`ACT_DOTA_FXANIM`

1709

`ACT_DOTA_VICTORY_START`

1710

`ACT_DOTA_DEFEAT_START`

1711

`ACT_DOTA_DP_SPIRIT_SIPHON`

1712

`ACT_DOTA_TRICKS_END`

1713

`ACT_DOTA_ES_STONE_CALLER`

1714

`ACT_DOTA_MK_STRIKE`

1715

`ACT_DOTA_VERSUS`

1716

`ACT_DOTA_CAPTURE_CARD`

1717

`ACT_DOTA_MK_SPRING_SOAR`

1718

`ACT_DOTA_MK_SPRING_END`

1719

`ACT_DOTA_MK_TREE_SOAR`

1720

`ACT_DOTA_MK_TREE_END`

1721

`ACT_DOTA_MK_FUR_ARMY`

1722

`ACT_DOTA_MK_SPRING_CAST`

1723

`ACT_DOTA_NECRO_GHOST_SHROUD`

1724

`ACT_DOTA_OVERRIDE_ARCANA`

1725

`ACT_DOTA_SLIDE`

1726

`ACT_DOTA_SLIDE_LOOP`

1727

`ACT_DOTA_GENERIC_CHANNEL_1`

1728

`ACT_DOTA_GS_SOUL_CHAIN`

1729

`ACT_DOTA_GS_INK_CREATURE`

1730

`ACT_DOTA_TRANSITION`

1731

`ACT_DOTA_BLINK_DAGGER`

1732

`ACT_DOTA_BLINK_DAGGER_END`

1733

`ACT_DOTA_CUSTOM_TOWER_ATTACK`

1734

`ACT_DOTA_CUSTOM_TOWER_IDLE`

1735

`ACT_DOTA_CUSTOM_TOWER_DIE`

1736

`ACT_DOTA_CAST_COLD_SNAP_ORB`

1737

`ACT_DOTA_CAST_GHOST_WALK_ORB`

1738

`ACT_DOTA_CAST_TORNADO_ORB`

1739

`ACT_DOTA_CAST_EMP_ORB`

1740

`ACT_DOTA_CAST_ALACRITY_ORB`

1741

`ACT_DOTA_CAST_CHAOS_METEOR_ORB`

1742

`ACT_DOTA_CAST_SUN_STRIKE_ORB`

1743

`ACT_DOTA_CAST_FORGE_SPIRIT_ORB`

1744

`ACT_DOTA_CAST_ICE_WALL_ORB`

1745

`ACT_DOTA_CAST_DEAFENING_BLAST_ORB`

1746

`ACT_DOTA_NOTICE`

1747

`ACT_DOTA_CAST_ABILITY_2_ALLY`

1748

`ACT_DOTA_SHUFFLE_L`

1749

`ACT_DOTA_SHUFFLE_R`

1750

`ACT_DOTA_OVERRIDE_LOADOUT`

1751

`ACT_DOTA_TAUNT_SPECIAL`

1752

`ACT_DOTA_TELEPORT_START`

1753

`ACT_DOTA_GENERIC_CHANNEL_1_START`

1754

`ACT_DOTA_CUSTOM_TOWER_IDLE_RARE`

1755

`ACT_DOTA_CUSTOM_TOWER_TAUNT`

1756

`ACT_DOTA_CUSTOM_TOWER_HIGH_FIVE`

1757

`ACT_DOTA_ATTACK_SPECIAL`

1758

`ACT_DOTA_TRANSITION_IDLE`

1759

`ACT_DOTA_PIERCE_THE_VEIL`

1760

`ACT_DOTA_RUN_RARE`

1761

`ACT_DOTA_VIPER_DIVE`

1762

`ACT_DOTA_VIPER_DIVE_END`

1763

`ACT_DOTA_MK_STRIKE_END`

1764

## Enum.Attributes

Key

Value

`DOTA_ATTRIBUTE_STRENGTH`

0

`DOTA_ATTRIBUTE_AGILITY`

1

`DOTA_ATTRIBUTE_INTELLECT`

2

`DOTA_ATTRIBUTE_ALL`

3

`DOTA_ATTRIBUTE_MAX`

4

`DOTA_ATTRIBUTE_INVALID`

4294967295

## Enum.UnitTypeFlags

Key

Value

`TYPE_HERO`

`TYPE_CONSIDERED_HERO`

`TYPE_TOWER`

`TYPE_STRUCTURE`

`TYPE_ANCIENT`

`TYPE_BARRACKS`

`TYPE_CREEP`

`TYPE_COURIER`

`TYPE_SHOP`

`TYPE_LANE_CREEP`

`TYPE_WARD`

`TYPE_ROSHAN`

## Enum.UnitOrder

Key

Value

`DOTA_UNIT_ORDER_NONE`

0

`DOTA_UNIT_ORDER_MOVE_TO_POSITION`

1

`DOTA_UNIT_ORDER_MOVE_TO_TARGET`

2

`DOTA_UNIT_ORDER_ATTACK_MOVE`

3

`DOTA_UNIT_ORDER_ATTACK_TARGET`

4

`DOTA_UNIT_ORDER_CAST_POSITION`

5

`DOTA_UNIT_ORDER_CAST_TARGET`

6

`DOTA_UNIT_ORDER_CAST_TARGET_TREE`

7

`DOTA_UNIT_ORDER_CAST_NO_TARGET`

8

`DOTA_UNIT_ORDER_CAST_TOGGLE`

9

`DOTA_UNIT_ORDER_HOLD_POSITION`

10

`DOTA_UNIT_ORDER_TRAIN_ABILITY`

11

`DOTA_UNIT_ORDER_DROP_ITEM`

12

`DOTA_UNIT_ORDER_GIVE_ITEM`

13

`DOTA_UNIT_ORDER_PICKUP_ITEM`

14

`DOTA_UNIT_ORDER_PICKUP_RUNE`

15

`DOTA_UNIT_ORDER_PURCHASE_ITEM`

16

`DOTA_UNIT_ORDER_SELL_ITEM`

17

`DOTA_UNIT_ORDER_DISASSEMBLE_ITEM`

18

`DOTA_UNIT_ORDER_MOVE_ITEM`

19

`DOTA_UNIT_ORDER_CAST_TOGGLE_AUTO`

20

`DOTA_UNIT_ORDER_STOP`

21

`DOTA_UNIT_ORDER_TAUNT`

22

`DOTA_UNIT_ORDER_BUYBACK`

23

`DOTA_UNIT_ORDER_GLYPH`

24

`DOTA_UNIT_ORDER_EJECT_ITEM_FROM_STASH`

25

`DOTA_UNIT_ORDER_CAST_RUNE`

26

`DOTA_UNIT_ORDER_PING_ABILITY`

27

`DOTA_UNIT_ORDER_MOVE_TO_DIRECTION`

28

`DOTA_UNIT_ORDER_PATROL`

29

`DOTA_UNIT_ORDER_VECTOR_TARGET_POSITION`

30

`DOTA_UNIT_ORDER_RADAR`

31

`DOTA_UNIT_ORDER_SET_ITEM_COMBINE_LOCK`

32

`DOTA_UNIT_ORDER_CONTINUE`

33

`DOTA_UNIT_ORDER_VECTOR_TARGET_CANCELED`

34

`DOTA_UNIT_ORDER_CAST_RIVER_PAINT`

35

`DOTA_UNIT_ORDER_PREGAME_ADJUST_ITEM_ASSIGNMENT`

36

`DOTA_UNIT_ORDER_DROP_ITEM_AT_FOUNTAIN`

37

`DOTA_UNIT_ORDER_TAKE_ITEM_FROM_NEUTRAL_ITEM_STASH`

38

`DOTA_UNIT_ORDER_MOVE_RELATIVE`

39

`DOTA_UNIT_ORDER_CAST_TOGGLE_ALT`

40

`DOTA_UNIT_ORDER_CONSUME_ITEM`

41

## Enum.PlayerOrderIssuer

Key

Value

`DOTA_ORDER_ISSUER_SELECTED_UNITS`

0

`DOTA_ORDER_ISSUER_CURRENT_UNIT_ONLY`

1

`DOTA_ORDER_ISSUER_HERO_ONLY`

2

`DOTA_ORDER_ISSUER_PASSED_UNIT_ONLY`

3

## Enum.GameState

Key

Value

`DOTA_GAMERULES_STATE_INIT`

0

`DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD`

1

`DOTA_GAMERULES_STATE_HERO_SELECTION`

2

`DOTA_GAMERULES_STATE_STRATEGY_TIME`

3

`DOTA_GAMERULES_STATE_PRE_GAME`

4

`DOTA_GAMERULES_STATE_GAME_IN_PROGRESS`

5

`DOTA_GAMERULES_STATE_POST_GAME`

6

`DOTA_GAMERULES_STATE_DISCONNECT`

7

`DOTA_GAMERULES_STATE_TEAM_SHOWCASE`

8

`DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP`

9

`DOTA_GAMERULES_STATE_WAIT_FOR_MAP_TO_LOAD`

10

`DOTA_GAMERULES_STATE_LAST`

13

## Enum.GameMode

Key

Value

`DOTA_GAMEMODE_NONE`

0

`DOTA_GAMEMODE_AP`

1

`DOTA_GAMEMODE_CM`

2

`DOTA_GAMEMODE_RD`

3

`DOTA_GAMEMODE_SD`

4

`DOTA_GAMEMODE_AR`

5

`DOTA_GAMEMODE_INTRO`

6

`DOTA_GAMEMODE_HW`

7

`DOTA_GAMEMODE_REVERSE_CM`

8

`DOTA_GAMEMODE_XMAS`

9

`DOTA_GAMEMODE_TUTORIAL`

10

`DOTA_GAMEMODE_MO`

11

`DOTA_GAMEMODE_LP`

12

`DOTA_GAMEMODE_POOL1`

13

`DOTA_GAMEMODE_FH`

14

`DOTA_GAMEMODE_CUSTOM`

15

`DOTA_GAMEMODE_CD`

16

`DOTA_GAMEMODE_BD`

17

`DOTA_GAMEMODE_ABILITY_DRAFT`

18

`DOTA_GAMEMODE_1V1MID`

21

`DOTA_GAMEMODE_ALL_DRAFT`

22

`DOTA_GAMEMODE_TURBO`

23

`DOTA_GAMEMODE_MUTATION`

24

`DOTA_GAMEMODE_COACHES_CHALLENGE`

25

## Enum.Flow

Key

Value

`FLOW_OUTGOING`

0

`FLOW_INCOMING`

1

`MAX_FLOWS`

2

## Enum.ParticleAttachment

Key

Value

`PATTACH_INVALID`

4294967295

`PATTACH_ABSORIGIN`

0

`PATTACH_ABSORIGIN_FOLLOW`

1

`PATTACH_CUSTOMORIGIN`

2

`PATTACH_CUSTOMORIGIN_FOLLOW`

3

`PATTACH_POINT`

4

`PATTACH_POINT_FOLLOW`

5

`PATTACH_EYES_FOLLOW`

6

`PATTACH_OVERHEAD_FOLLOW`

7

`PATTACH_WORLDORIGIN`

8

`PATTACH_ROOTBONE_FOLLOW`

9

`PATTACH_RENDERORIGIN_FOLLOW`

10

`PATTACH_MAIN_VIEW`

11

`PATTACH_WATERWAKE`

12

`PATTACH_CENTER_FOLLOW`

13

`PATTACH_CUSTOM_GAME_STATE_1`

14

`PATTACH_HEALTHBAR`

15

`MAX_PATTACH_TYPES`

16

## Enum.ButtonCode

Key

Value

`BUTTON_CODE_INVALID`

`BUTTON_CODE_NONE`

`KEY_FIRST`

`KEY_NONE`

`KEY_0`

`KEY_1`

`KEY_2`

`KEY_3`

`KEY_4`

`KEY_5`

`KEY_6`

`KEY_7`

`KEY_8`

`KEY_9`

`KEY_A`

`KEY_B`

`KEY_C`

`KEY_D`

`KEY_E`

`KEY_F`

`KEY_G`

`KEY_H`

`KEY_I`

`KEY_J`

`KEY_K`

`KEY_L`

`KEY_M`

`KEY_N`

`KEY_O`

`KEY_P`

`KEY_Q`

`KEY_R`

`KEY_S`

`KEY_T`

`KEY_U`

`KEY_V`

`KEY_W`

`KEY_X`

`KEY_Y`

`KEY_Z`

`KEY_PAD_0`

`KEY_PAD_1`

`KEY_PAD_2`

`KEY_PAD_3`

`KEY_PAD_4`

`KEY_PAD_5`

`KEY_PAD_6`

`KEY_PAD_7`

`KEY_PAD_8`

`KEY_PAD_9`

`KEY_PAD_DIVIDE`

`KEY_PAD_MULTIPLY`

`KEY_PAD_MINUS`

`KEY_PAD_PLUS`

`KEY_PAD_ENTER`

`KEY_PAD_DECIMAL`

`KEY_LBRACKET`

`KEY_RBRACKET`

`KEY_SEMICOLON`

`KEY_APOSTROPHE`

`KEY_BACKQUOTE`

`KEY_COMMA`

`KEY_PERIOD`

`KEY_SLASH`

`KEY_BACKSLASH`

`KEY_MINUS`

`KEY_EQUAL`

`KEY_ENTER`

`KEY_SPACE`

`KEY_BACKSPACE`

`KEY_TAB`

`KEY_CAPSLOCK`

`KEY_NUMLOCK`

`KEY_ESCAPE`

`KEY_SCROLLLOCK`

`KEY_INSERT`

`KEY_DELETE`

`KEY_HOME`

`KEY_END`

`KEY_PAGEUP`

`KEY_PAGEDOWN`

`KEY_BREAK`

`KEY_LSHIFT`

`KEY_RSHIFT`

`KEY_LALT`

`KEY_RALT`

`KEY_LCONTROL`

`KEY_RCONTROL`

`KEY_LWIN`

`KEY_RWIN`

`KEY_APP`

`KEY_UP`

`KEY_LEFT`

`KEY_DOWN`

`KEY_RIGHT`

`KEY_F1`

`KEY_F2`

`KEY_F3`

`KEY_F4`

`KEY_F5`

`KEY_F6`

`KEY_F7`

`KEY_F8`

`KEY_F9`

`KEY_F10`

`KEY_F11`

`KEY_F12`

`KEY_F13`

`KEY_F14`

`KEY_F15`

`KEY_F16`

`KEY_F17`

`KEY_F18`

`KEY_F19`

`KEY_F20`

`KEY_F21`

`KEY_F22`

`KEY_F23`

`KEY_F24`

`KEY_CAPSLOCKTOGGLE`

`KEY_NUMLOCKTOGGLE`

`KEY_SCROLLLOCKTOGGLE`

`KEY_MOUSE1`

`KEY_MOUSE2`

`KEY_MOUSE3`

`KEY_MOUSE4`

`KEY_MOUSE5`

`KEY_MWHEELUP`

`KEY_MWHEELDOWN`

## Enum.FontCreate

Key

Value

`FONTFLAG_NONE`

0

`FONTFLAG_ITALIC`

1

`FONTFLAG_UNDERLINE`

2

`FONTFLAG_STRIKEOUT`

4

`FONTFLAG_SYMBOL`

8

`FONTFLAG_ANTIALIAS`

16

`FONTFLAG_GAUSSIANBLUR`

32

`FONTFLAG_ROTARY`

64

`FONTFLAG_DROPSHADOW`

128

`FONTFLAG_ADDITIVE`

256

`FONTFLAG_OUTLINE`

512

`FONTFLAG_CUSTOM`

1024

`FONTFLAG_BITMAP`

2048

## Enum.FontWeight

Key

Value

`THIN`

`ULTRALIGHT`

`LIGHT`

`NORMAL`

`MEDIUM`

`SEMIBOLD`

`BOLD`

`EXTRABOLD`

`HEAVY`

## Enum.WidgetType

Key

Value

`MenuFirstTab`

`MenuSection`

`MenuSecondTab`

`MenuThirdTab`

`MenuGroup`

`MenuSwitch`

`MenuBind`

`MenuSliderFloat`

`MenuSliderInt`

`MenuColorPicker`

`MenuButton`

`MenuComboBox`

`MenuMultiComboBox`

`MenuGearAttachment`

`MenuInputBox`

`MenuMultiSelect`

`MenuSearch`

`MenuThemePicker`

`MenuLabel`

`MenuCustomBind`

`MenuTypesCount`

`MenuTypeInvalid`

## Enum.GroupSide

## Enum.PingType

Key

Value

`PINGTYPE_INFO`

0

`PINGTYPE_WARNING`

1

`PINGTYPE_LOCATION`

2

`PINGTYPE_DANGER`

3

`PINGTYPE_ATTACK`

4

`PINGTYPE_ENEMY_VISION`

5

`PINGTYPE_OWN_VISION`

6

`PINGTYPE_LIKE`

7

## Enum.DotaChatMessage

Key

Value

`CHAT_MESSAGE_INVALID`

-1

`CHAT_MESSAGE_HERO_KILL`

0

`CHAT_MESSAGE_HERO_DENY`

1

`CHAT_MESSAGE_BARRACKS_KILL`

2

`CHAT_MESSAGE_TOWER_KILL`

3

`CHAT_MESSAGE_TOWER_DENY`

4

`CHAT_MESSAGE_FIRSTBLOOD`

5

`CHAT_MESSAGE_STREAK_KILL`

6

`CHAT_MESSAGE_BUYBACK`

7

`CHAT_MESSAGE_AEGIS`

8

`CHAT_MESSAGE_ROSHAN_KILL`

9

`CHAT_MESSAGE_COURIER_LOST`

10

`CHAT_MESSAGE_COURIER_RESPAWNED`

11

`CHAT_MESSAGE_GLYPH_USED`

12

`CHAT_MESSAGE_ITEM_PURCHASE`

13

`CHAT_MESSAGE_CONNECT`

14

`CHAT_MESSAGE_DISCONNECT`

15

`CHAT_MESSAGE_DISCONNECT_WAIT_FOR_RECONNECT`

16

`CHAT_MESSAGE_DISCONNECT_TIME_REMAINING`

17

`CHAT_MESSAGE_DISCONNECT_TIME_REMAINING_PLURAL`

18

`CHAT_MESSAGE_RECONNECT`

19

`CHAT_MESSAGE_PLAYER_LEFT`

20

`CHAT_MESSAGE_SAFE_TO_LEAVE`

21

`CHAT_MESSAGE_RUNE_PICKUP`

22

`CHAT_MESSAGE_RUNE_BOTTLE`

23

`CHAT_MESSAGE_INTHEBAG`

24

`CHAT_MESSAGE_SECRETSHOP`

25

`CHAT_MESSAGE_ITEM_AUTOPURCHASED`

26

`CHAT_MESSAGE_ITEMS_COMBINED`

27

`CHAT_MESSAGE_SUPER_CREEPS`

28

`CHAT_MESSAGE_CANT_USE_ACTION_ITEM`

29

`CHAT_MESSAGE_CANTPAUSE`

31

`CHAT_MESSAGE_NOPAUSESLEFT`

32

`CHAT_MESSAGE_CANTPAUSEYET`

33

`CHAT_MESSAGE_PAUSED`

34

`CHAT_MESSAGE_UNPAUSE_COUNTDOWN`

35

`CHAT_MESSAGE_UNPAUSED`

36

`CHAT_MESSAGE_AUTO_UNPAUSED`

37

`CHAT_MESSAGE_YOUPAUSED`

38

`CHAT_MESSAGE_CANTUNPAUSETEAM`

39

`CHAT_MESSAGE_VOICE_TEXT_BANNED`

41

`CHAT_MESSAGE_SPECTATORS_WATCHING_THIS_GAME`

42

`CHAT_MESSAGE_REPORT_REMINDER`

43

`CHAT_MESSAGE_ECON_ITEM`

44

`CHAT_MESSAGE_TAUNT`

45

`CHAT_MESSAGE_RANDOM`

46

`CHAT_MESSAGE_RD_TURN`

47

`CHAT_MESSAGE_DROP_RATE_BONUS`

49

`CHAT_MESSAGE_NO_BATTLE_POINTS`

50

`CHAT_MESSAGE_DENIED_AEGIS`

51

`CHAT_MESSAGE_INFORMATIONAL`

52

`CHAT_MESSAGE_AEGIS_STOLEN`

53

`CHAT_MESSAGE_ROSHAN_CANDY`

54

`CHAT_MESSAGE_ITEM_GIFTED`

55

`CHAT_MESSAGE_HERO_KILL_WITH_GREEVIL`

56

`CHAT_MESSAGE_HOLDOUT_TOWER_DESTROYED`

57

`CHAT_MESSAGE_HOLDOUT_WALL_DESTROYED`

58

`CHAT_MESSAGE_HOLDOUT_WALL_FINISHED`

59

`CHAT_MESSAGE_PLAYER_LEFT_LIMITED_HERO`

62

`CHAT_MESSAGE_ABANDON_LIMITED_HERO_EXPLANATION`

63

`CHAT_MESSAGE_DISCONNECT_LIMITED_HERO`

64

`CHAT_MESSAGE_LOW_PRIORITY_COMPLETED_EXPLANATION`

65

`CHAT_MESSAGE_RECRUITMENT_DROP_RATE_BONUS`

66

`CHAT_MESSAGE_FROSTIVUS_SHINING_BOOSTER_ACTIVE`

67

`CHAT_MESSAGE_PLAYER_LEFT_AFK`

73

`CHAT_MESSAGE_PLAYER_LEFT_DISCONNECTED_TOO_LONG`

74

`CHAT_MESSAGE_PLAYER_ABANDONED`

75

`CHAT_MESSAGE_PLAYER_ABANDONED_AFK`

76

`CHAT_MESSAGE_PLAYER_ABANDONED_DISCONNECTED_TOO_LONG`

77

`CHAT_MESSAGE_WILL_NOT_BE_SCORED`

78

`CHAT_MESSAGE_WILL_NOT_BE_SCORED_RANKED`

79

`CHAT_MESSAGE_WILL_NOT_BE_SCORED_NETWORK`

80

`CHAT_MESSAGE_WILL_NOT_BE_SCORED_NETWORK_RANKED`

81

`CHAT_MESSAGE_CAN_QUIT_WITHOUT_ABANDON`

82

`CHAT_MESSAGE_RANKED_GAME_STILL_SCORED_LEAVERS_GET_LOSS`

83

`CHAT_MESSAGE_ABANDON_RANKED_BEFORE_FIRST_BLOOD_PARTY`

84

`CHAT_MESSAGE_COMPENDIUM_LEVEL`

85

`CHAT_MESSAGE_VICTORY_PREDICTION_STREAK`

86

`CHAT_MESSAGE_ASSASSIN_ANNOUNCE`

87

`CHAT_MESSAGE_ASSASSIN_SUCCESS`

88

`CHAT_MESSAGE_ASSASSIN_DENIED`

89

`CHAT_MESSAGE_VICTORY_PREDICTION_SINGLE_USER_CONFIRM`

90

`CHAT_MESSAGE_EFFIGY_KILL`

91

`CHAT_MESSAGE_VOICE_TEXT_BANNED_OVERFLOW`

92

`CHAT_MESSAGE_YEAR_BEAST_KILLED`

93

`CHAT_MESSAGE_PAUSE_COUNTDOWN`

94

`CHAT_MESSAGE_COINS_WAGERED`

95

`CHAT_MESSAGE_HERO_NOMINATED_BAN`

96

`CHAT_MESSAGE_HERO_BANNED`

97

`CHAT_MESSAGE_HERO_BAN_COUNT`

98

`CHAT_MESSAGE_RIVER_PAINTED`

99

`CHAT_MESSAGE_SCAN_USED`

100

`CHAT_MESSAGE_SHRINE_KILLED`

101

`CHAT_MESSAGE_WAGER_TOKEN_SPENT`

102

`CHAT_MESSAGE_RANK_WAGER`

103

`CHAT_MESSAGE_NEW_PLAYER_REMINDER`

104

`CHAT_MESSAGE_OBSERVER_WARD_KILLED`

105

`CHAT_MESSAGE_SENTRY_WARD_KILLED`

106

`CHAT_MESSAGE_ITEM_PLACED_IN_NEUTRAL_STASH`

107

`CHAT_MESSAGE_HERO_CHOICE_INVALID`

108

`CHAT_MESSAGE_BOUNTY`

109

`CHAT_MESSAGE_ABILITY_DRAFT_START`

110

`CHAT_MESSAGE_HERO_FOUND_CANDY`

111

`CHAT_MESSAGE_ABILITY_DRAFT_RANDOMED`

112

`CHAT_MESSAGE_PRIVATE_COACH_CONNECTED`

113

`CHAT_MESSAGE_CANT_PAUSE_TOO_EARLY`

115

`CHAT_MESSAGE_HERO_KILL_WITH_PENGUIN`

116

`CHAT_MESSAGE_MINIBOSS_KILL`

117

`CHAT_MESSAGE_PLAYER_IN_GAME_BAN_TEXT`

118

`CHAT_MESSAGE_BANNER_PLANTED`

119

## Enum.AbilityLearnResult

Key

Value

`ABILITY_CAN_BE_UPGRADED`

0

`ABILITY_CANNOT_BE_UPGRADED_NOT_UPGRADABLE`

1

`ABILITY_CANNOT_BE_UPGRADED_AT_MAX`

2

`ABILITY_CANNOT_BE_UPGRADED_REQUIRES_LEVEL`

3

`ABILITY_NOT_LEARNABLE`

4

## Enum.AbilityCastResult

Key

Value

`READY`

`NOT_LEARNED`

`NO_MANA`

`ABILITY_CD`

`PASSIVE`

`HIDDEN`

`ITEM_CD`

## Enum.ModifierFunction

Key

Value

`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE`

0

`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_TARGET`

1

`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_PROC`

2

`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_POST_CRIT`

3

`MODIFIER_PROPERTY_BASEATTACK_BONUSDAMAGE`

4

`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_PHYSICAL`

5

`MODIFIER_PROPERTY_PROCATTACK_CONVERT_PHYSICAL_TO_MAGICAL`

6

`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_MAGICAL`

7

`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_PURE`

8

`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_MAGICAL_TARGET`

9

`MODIFIER_PROPERTY_PROCATTACK_FEEDBACK`

10

`MODIFIER_PROPERTY_OVERRIDE_ATTACK_DAMAGE`

11

`MODIFIER_PROPERTY_PRE_ATTACK`

12

`MODIFIER_PROPERTY_INVISIBILITY_LEVEL`

13

`MODIFIER_PROPERTY_INVISIBILITY_ATTACK_BEHAVIOR_EXCEPTION`

14

`MODIFIER_PROPERTY_PERSISTENT_INVISIBILITY`

15

`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT`

16

`MODIFIER_PROPERTY_MOVESPEED_BASE_OVERRIDE`

17

`MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE`

20

`MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE_UNIQUE`

21

`MODIFIER_PROPERTY_MOVESPEED_BONUS_UNIQUE`

22

`MODIFIER_PROPERTY_MOVESPEED_BONUS_UNIQUE_2`

23

`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT_UNIQUE`

24

`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT_UNIQUE_2`

25

`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE`

26

`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE_MIN`

27

`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE_MAX`

28

`MODIFIER_PROPERTY_IGNORE_MOVESPEED_LIMIT`

29

`MODIFIER_PROPERTY_MOVESPEED_LIMIT`

30

`MODIFIER_PROPERTY_ATTACKSPEED_BASE_OVERRIDE`

31

`MODIFIER_PROPERTY_FIXED_ATTACK_RATE`

32

`MODIFIER_PROPERTY_ATTACKSPEED_BONUS_CONSTANT`

33

`MODIFIER_PROPERTY_IGNORE_ATTACKSPEED_LIMIT`

34

`MODIFIER_PROPERTY_COOLDOWN_REDUCTION_CONSTANT`

35

`MODIFIER_PROPERTY_MANACOST_REDUCTION_CONSTANT`

36

`MODIFIER_PROPERTY_HEALTHCOST_REDUCTION_CONSTANT`

37

`MODIFIER_PROPERTY_BASE_ATTACK_TIME_CONSTANT`

38

`MODIFIER_PROPERTY_BASE_ATTACK_TIME_CONSTANT_ADJUST`

39

`MODIFIER_PROPERTY_BASE_ATTACK_TIME_PERCENTAGE`

40

`MODIFIER_PROPERTY_ATTACK_POINT_CONSTANT`

41

`MODIFIER_PROPERTY_BONUSDAMAGEOUTGOING_PERCENTAGE`

42

`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE`

43

`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_ILLUSION`

44

`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_ILLUSION_AMPLIFY`

45

`MODIFIER_PROPERTY_TOTALDAMAGEOUTGOING_PERCENTAGE`

46

`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_CREEP`

47

`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE`

48

`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_UNIQUE`

49

`MODIFIER_PROPERTY_HEAL_AMPLIFY_PERCENTAGE_SOURCE`

51

`MODIFIER_PROPERTY_HEAL_AMPLIFY_PERCENTAGE_TARGET`

52

`MODIFIER_PROPERTY_HP_REGEN_AMPLIFY_PERCENTAGE`

53

`MODIFIER_PROPERTY_LIFESTEAL_AMPLIFY_PERCENTAGE`

54

`MODIFIER_PROPERTY_SPELL_LIFESTEAL_AMPLIFY_PERCENTAGE`

55

`MODIFIER_PROPERTY_MP_REGEN_AMPLIFY_PERCENTAGE`

57

`MODIFIER_PROPERTY_MANA_DRAIN_AMPLIFY_PERCENTAGE`

59

`MODIFIER_PROPERTY_MP_RESTORE_AMPLIFY_PERCENTAGE`

60

`MODIFIER_PROPERTY_BASEDAMAGEOUTGOING_PERCENTAGE`

61

`MODIFIER_PROPERTY_BASEDAMAGEOUTGOING_PERCENTAGE_UNIQUE`

62

`MODIFIER_PROPERTY_INCOMING_DAMAGE_PERCENTAGE`

63

`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_PERCENTAGE`

64

`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT`

65

`MODIFIER_PROPERTY_INCOMING_SPELL_DAMAGE_CONSTANT`

66

`MODIFIER_PROPERTY_EVASION_CONSTANT`

67

`MODIFIER_PROPERTY_NEGATIVE_EVASION_CONSTANT`

68

`MODIFIER_PROPERTY_STATUS_RESISTANCE`

69

`MODIFIER_PROPERTY_STATUS_RESISTANCE_STACKING`

70

`MODIFIER_PROPERTY_STATUS_RESISTANCE_CASTER`

71

`MODIFIER_PROPERTY_AVOID_DAMAGE`

72

`MODIFIER_PROPERTY_AVOID_SPELL`

73

`MODIFIER_PROPERTY_MISS_PERCENTAGE`

74

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BASE_PERCENTAGE`

75

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_TOTAL_PERCENTAGE`

76

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS`

77

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_UNIQUE`

78

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_UNIQUE_ACTIVE`

79

`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_POST`

80

`MODIFIER_PROPERTY_MIN_PHYSICAL_ARMOR`

81

`MODIFIER_PROPERTY_IGNORE_PHYSICAL_ARMOR`

82

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BASE_REDUCTION`

83

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_DIRECT_MODIFICATION`

84

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS`

85

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS_ILLUSIONS`

86

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS_UNIQUE`

87

`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_DECREPIFY_UNIQUE`

88

`MODIFIER_PROPERTY_BASE_MANA_REGEN`

89

`MODIFIER_PROPERTY_MANA_REGEN_CONSTANT`

90

`MODIFIER_PROPERTY_MANA_REGEN_CONSTANT_UNIQUE`

91

`MODIFIER_PROPERTY_MANA_REGEN_TOTAL_PERCENTAGE`

92

`MODIFIER_PROPERTY_HEALTH_REGEN_CONSTANT`

93

`MODIFIER_PROPERTY_HEALTH_REGEN_PERCENTAGE`

94

`MODIFIER_PROPERTY_HEALTH_REGEN_PERCENTAGE_UNIQUE`

95

`MODIFIER_PROPERTY_HEALTH_BONUS`

96

`MODIFIER_PROPERTY_MANA_BONUS`

97

`MODIFIER_PROPERTY_EXTRA_STRENGTH_BONUS`

98

`MODIFIER_PROPERTY_EXTRA_HEALTH_BONUS`

99

`MODIFIER_PROPERTY_EXTRA_MANA_BONUS`

100

`MODIFIER_PROPERTY_EXTRA_MANA_BONUS_PERCENTAGE`

101

`MODIFIER_PROPERTY_EXTRA_HEALTH_PERCENTAGE`

102

`MODIFIER_PROPERTY_EXTRA_MANA_PERCENTAGE`

103

`MODIFIER_PROPERTY_STATS_STRENGTH_BONUS`

104

`MODIFIER_PROPERTY_STATS_AGILITY_BONUS`

105

`MODIFIER_PROPERTY_STATS_INTELLECT_BONUS`

106

`MODIFIER_PROPERTY_STATS_STRENGTH_BONUS_PERCENTAGE`

107

`MODIFIER_PROPERTY_STATS_AGILITY_BONUS_PERCENTAGE`

108

`MODIFIER_PROPERTY_STATS_INTELLECT_BONUS_PERCENTAGE`

109

`MODIFIER_PROPERTY_CAST_RANGE_BONUS`

110

`MODIFIER_PROPERTY_CAST_RANGE_BONUS_PERCENTAGE`

111

`MODIFIER_PROPERTY_CAST_RANGE_BONUS_TARGET`

112

`MODIFIER_PROPERTY_CAST_RANGE_BONUS_STACKING`

113

`MODIFIER_PROPERTY_ATTACK_RANGE_BASE_OVERRIDE`

114

`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS`

115

`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS_UNIQUE`

116

`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS_PERCENTAGE`

117

`MODIFIER_PROPERTY_MAX_ATTACK_RANGE`

118

`MODIFIER_PROPERTY_PROJECTILE_SPEED_BONUS`

119

`MODIFIER_PROPERTY_PROJECTILE_SPEED_BONUS_PERCENTAGE`

120

`MODIFIER_PROPERTY_PROJECTILE_NAME`

121

`MODIFIER_PROPERTY_REINCARNATION`

122

`MODIFIER_PROPERTY_REINCARNATION_SUPPRESS_FX`

123

`MODIFIER_PROPERTY_RESPAWNTIME`

124

`MODIFIER_PROPERTY_RESPAWNTIME_PERCENTAGE`

125

`MODIFIER_PROPERTY_RESPAWNTIME_STACKING`

126

`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE`

127

`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE_ONGOING`

128

`MODIFIER_PROPERTY_CASTTIME_PERCENTAGE`

129

`MODIFIER_PROPERTY_ATTACK_ANIM_TIME_PERCENTAGE`

130

`MODIFIER_PROPERTY_MANACOST_PERCENTAGE`

131

`MODIFIER_PROPERTY_MANACOST_PERCENTAGE_STACKING`

132

`MODIFIER_PROPERTY_HEALTHCOST_PERCENTAGE`

133

`MODIFIER_PROPERTY_HEALTHCOST_PERCENTAGE_STACKING`

134

`MODIFIER_PROPERTY_DEATHGOLDCOST`

135

`MODIFIER_PROPERTY_PERCENTAGE_DEATHGOLDCOST`

136

`MODIFIER_PROPERTY_EXP_RATE_BOOST`

137

`MODIFIER_PROPERTY_GOLD_RATE_BOOST`

138

`MODIFIER_PROPERTY_PREATTACK_CRITICALSTRIKE`

139

`MODIFIER_PROPERTY_PREATTACK_TARGET_CRITICALSTRIKE`

140

`MODIFIER_PROPERTY_MAGICAL_CONSTANT_BLOCK`

141

`MODIFIER_PROPERTY_PHYSICAL_CONSTANT_BLOCK`

142

`MODIFIER_PROPERTY_PHYSICAL_CONSTANT_BLOCK_SPECIAL`

143

`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK_UNAVOIDABLE_PRE_ARMOR`

145

`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK`

146

`MODIFIER_PROPERTY_OVERRIDE_ANIMATION`

147

`MODIFIER_PROPERTY_OVERRIDE_ANIMATION_RATE`

148

`MODIFIER_PROPERTY_ABSORB_SPELL`

149

`MODIFIER_PROPERTY_REFLECT_SPELL`

150

`MODIFIER_PROPERTY_DISABLE_AUTOATTACK`

151

`MODIFIER_PROPERTY_BONUS_DAY_VISION`

152

`MODIFIER_PROPERTY_BONUS_DAY_VISION_PERCENTAGE`

153

`MODIFIER_PROPERTY_BONUS_NIGHT_VISION`

154

`MODIFIER_PROPERTY_BONUS_NIGHT_VISION_UNIQUE`

155

`MODIFIER_PROPERTY_BONUS_VISION_PERCENTAGE`

156

`MODIFIER_PROPERTY_FIXED_DAY_VISION`

157

`MODIFIER_PROPERTY_FIXED_NIGHT_VISION`

158

`MODIFIER_PROPERTY_MIN_HEALTH`

159

`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PHYSICAL`

161

`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_MAGICAL`

162

`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PURE`

163

`MODIFIER_PROPERTY_IS_ILLUSION`

164

`MODIFIER_PROPERTY_ILLUSION_LABEL`

165

`MODIFIER_PROPERTY_STRONG_ILLUSION`

166

`MODIFIER_PROPERTY_SUPER_ILLUSION`

167

`MODIFIER_PROPERTY_SUPER_ILLUSION_WITH_ULTIMATE`

168

`MODIFIER_PROPERTY_XP_DURING_DEATH`

169

`MODIFIER_PROPERTY_TURN_RATE_PERCENTAGE`

170

`MODIFIER_PROPERTY_TURN_RATE_OVERRIDE`

171

`MODIFIER_PROPERTY_DISABLE_HEALING`

172

`MODIFIER_PROPERTY_ALWAYS_ALLOW_ATTACK`

174

`MODIFIER_PROPERTY_ALWAYS_ETHEREAL_ATTACK`

175

`MODIFIER_PROPERTY_OVERRIDE_ATTACK_MAGICAL`

176

`MODIFIER_PROPERTY_UNIT_STATS_NEEDS_REFRESH`

177

`MODIFIER_PROPERTY_BOUNTY_CREEP_MULTIPLIER`

178

`MODIFIER_PROPERTY_BOUNTY_OTHER_MULTIPLIER`

179

`MODIFIER_PROPERTY_UNIT_DISALLOW_UPGRADING`

180

`MODIFIER_PROPERTY_DODGE_PROJECTILE`

181

`MODIFIER_PROPERTY_TRIGGER_COSMETIC_AND_END_ATTACK`

182

`MODIFIER_PROPERTY_MAX_DEBUFF_DURATION`

183

`MODIFIER_PROPERTY_PRIMARY_STAT_DAMAGE_MULTIPLIER`

184

`MODIFIER_PROPERTY_PREATTACK_DEADLY_BLOW`

185

`MODIFIER_PROPERTY_ALWAYS_AUTOATTACK_WHILE_HOLD_POSITION`

186

`MODIFIER_EVENT_ON_SPELL_TARGET_READY`

191

`MODIFIER_EVENT_ON_ATTACK_RECORD`

192

`MODIFIER_EVENT_ON_ATTACK_START`

193

`MODIFIER_EVENT_ON_ATTACK`

194

`MODIFIER_EVENT_ON_ATTACK_LANDED`

195

`MODIFIER_EVENT_ON_ATTACK_FAIL`

196

`MODIFIER_EVENT_ON_ATTACK_ALLIED`

197

`MODIFIER_EVENT_ON_PROJECTILE_DODGE`

198

`MODIFIER_EVENT_ON_ORDER`

199

`MODIFIER_EVENT_ON_UNIT_MOVED`

200

`MODIFIER_EVENT_ON_ABILITY_START`

201

`MODIFIER_EVENT_ON_ABILITY_EXECUTED`

202

`MODIFIER_EVENT_ON_ABILITY_FULLY_CAST`

203

`MODIFIER_EVENT_ON_BREAK_INVISIBILITY`

204

`MODIFIER_EVENT_ON_ABILITY_END_CHANNEL`

205

`MODIFIER_EVENT_ON_PROCESS_UPGRADE`

206

`MODIFIER_EVENT_ON_REFRESH`

207

`MODIFIER_EVENT_ON_TAKEDAMAGE`

208

`MODIFIER_EVENT_ON_DEATH_PREVENTED`

209

`MODIFIER_EVENT_ON_STATE_CHANGED`

210

`MODIFIER_EVENT_ON_ORB_EFFECT`

211

`MODIFIER_EVENT_ON_PROCESS_CLEAVE`

212

`MODIFIER_EVENT_ON_DAMAGE_CALCULATED`

213

`MODIFIER_EVENT_ON_MAGIC_DAMAGE_CALCULATED`

214

`MODIFIER_EVENT_ON_ATTACKED`

215

`MODIFIER_EVENT_ON_DEATH`

216

`MODIFIER_EVENT_ON_DEATH_COMPLETED`

217

`MODIFIER_EVENT_ON_RESPAWN`

218

`MODIFIER_EVENT_ON_SPENT_MANA`

219

`MODIFIER_EVENT_ON_SPENT_HEALTH`

220

`MODIFIER_EVENT_ON_TELEPORTING`

221

`MODIFIER_EVENT_ON_TELEPORTED`

222

`MODIFIER_EVENT_ON_SET_LOCATION`

223

`MODIFIER_EVENT_ON_HEALTH_GAINED`

224

`MODIFIER_EVENT_ON_MANA_GAINED`

225

`MODIFIER_EVENT_ON_TAKEDAMAGE_KILLCREDIT`

226

`MODIFIER_EVENT_ON_HERO_KILLED`

227

`MODIFIER_EVENT_ON_HEAL_RECEIVED`

228

`MODIFIER_EVENT_ON_BUILDING_KILLED`

229

`MODIFIER_EVENT_ON_MODEL_CHANGED`

230

`MODIFIER_EVENT_ON_MODIFIER_ADDED`

231

`MODIFIER_EVENT_ON_MODIFIER_REMOVED`

232

`MODIFIER_PROPERTY_TOOLTIP`

233

`MODIFIER_PROPERTY_MODEL_CHANGE`

234

`MODIFIER_PROPERTY_MODEL_SCALE`

235

`MODIFIER_PROPERTY_MODEL_SCALE_ANIMATE_TIME`

236

`MODIFIER_PROPERTY_MODEL_SCALE_USE_IN_OUT_EASE`

237

`MODIFIER_PROPERTY_MODEL_SCALE_CONSTANT`

238

`MODIFIER_PROPERTY_IS_SCEPTER`

239

`MODIFIER_PROPERTY_IS_SHARD`

240

`MODIFIER_PROPERTY_RADAR_COOLDOWN_REDUCTION`

241

`MODIFIER_PROPERTY_TRANSLATE_ACTIVITY_MODIFIERS`

242

`MODIFIER_PROPERTY_TRANSLATE_ATTACK_SOUND`

243

`MODIFIER_PROPERTY_LIFETIME_FRACTION`

244

`MODIFIER_PROPERTY_PROVIDES_FOW_POSITION`

245

`MODIFIER_PROPERTY_SPELLS_REQUIRE_HP`

246

`MODIFIER_PROPERTY_CONVERT_MANA_COST_TO_HEALTH_COST`

247

`MODIFIER_PROPERTY_FORCE_DRAW_MINIMAP`

248

`MODIFIER_PROPERTY_DISABLE_TURNING`

249

`MODIFIER_PROPERTY_IGNORE_CAST_ANGLE`

250

`MODIFIER_PROPERTY_CHANGE_ABILITY_VALUE`

251

`MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL`

252

`MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL_VALUE`

253

`MODIFIER_PROPERTY_ABILITY_LAYOUT`

254

`MODIFIER_EVENT_ON_DOMINATED`

255

`MODIFIER_EVENT_ON_KILL`

256

`MODIFIER_EVENT_ON_ASSIST`

257

`MODIFIER_PROPERTY_TEMPEST_DOUBLE`

258

`MODIFIER_PROPERTY_PRESERVE_PARTICLES_ON_MODEL_CHANGE`

259

`MODIFIER_EVENT_ON_ATTACK_FINISHED`

260

`MODIFIER_PROPERTY_IGNORE_COOLDOWN`

261

`MODIFIER_PROPERTY_CAN_ATTACK_TREES`

262

`MODIFIER_PROPERTY_VISUAL_Z_DELTA`

263

`MODIFIER_PROPERTY_VISUAL_Z_SPEED_BASE_OVERRIDE`

264

`MODIFIER_PROPERTY_INCOMING_DAMAGE_ILLUSION`

265

`MODIFIER_PROPERTY_DONT_GIVE_VISION_OF_ATTACKER`

266

`MODIFIER_PROPERTY_TOOLTIP2`

267

`MODIFIER_EVENT_ON_ATTACK_RECORD_DESTROY`

268

`MODIFIER_EVENT_ON_PROJECTILE_OBSTRUCTION_HIT`

269

`MODIFIER_PROPERTY_SUPPRESS_TELEPORT`

270

`MODIFIER_EVENT_ON_ATTACK_CANCELLED`

271

`MODIFIER_PROPERTY_SUPPRESS_CLEAVE`

272

`MODIFIER_PROPERTY_BOT_ATTACK_SCORE_BONUS`

273

`MODIFIER_PROPERTY_ATTACKSPEED_REDUCTION_PERCENTAGE`

274

`MODIFIER_PROPERTY_MOVESPEED_REDUCTION_PERCENTAGE`

275

`MODIFIER_PROPERTY_ATTACK_WHILE_MOVING_TARGET`

276

`MODIFIER_PROPERTY_ATTACKSPEED_PERCENTAGE`

277

`MODIFIER_EVENT_ON_ATTEMPT_PROJECTILE_DODGE`

278

`MODIFIER_EVENT_ON_PREDEBUFF_APPLIED`

279

`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE_STACKING`

280

`MODIFIER_PROPERTY_SPELL_REDIRECT_TARGET`

281

`MODIFIER_PROPERTY_TURN_RATE_CONSTANT`

282

`MODIFIER_PROPERTY_PACK_RAT`

283

`MODIFIER_PROPERTY_PHYSICALDAMAGEOUTGOING_PERCENTAGE`

284

`MODIFIER_PROPERTY_KNOCKBACK_AMPLIFICATION_PERCENTAGE`

285

`MODIFIER_PROPERTY_HEALTHBAR_PIPS`

286

`MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT`

287

`MODIFIER_EVENT_SPELL_APPLIED_SUCCESSFULLY`

288

`MODIFIER_PROPERTY_AVOID_DAMAGE_AFTER_REDUCTIONS`

289

`MODIFIER_PROPERTY_FAIL_ATTACK`

290

`MODIFIER_PROPERTY_PREREDUCE_INCOMING_DAMAGE_MULT`

291

`MODIFIER_PROPERTY_SUPPRESS_FULLSCREEN_DEATH_FX`

292

`MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT_POST`

293

`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_MULTIPLICATIVE`

294

`MODIFIER_PROPERTY_TICK_GOLD_MULTIPLIER`

295

`MODIFIER_PROPERTY_SLOW_RESISTANCE_UNIQUE`

296

`MODIFIER_PROPERTY_SLOW_RESISTANCE_STACKING`

297

`MODIFIER_PROPERTY_AOE_BONUS_PERCENTAGE`

299

`MODIFIER_PROPERTY_PROJECTILE_SPEED`

300

`MODIFIER_PROPERTY_PROJECTILE_SPEED_TARGET`

301

`MODIFIER_PROPERTY_BECOME_STRENGTH`

302

`MODIFIER_PROPERTY_BECOME_AGILITY`

303

`MODIFIER_PROPERTY_BECOME_INTELLIGENCE`

304

`MODIFIER_PROPERTY_BECOME_UNIVERSAL`

305

`MODIFIER_EVENT_ON_FORCE_PROC_MAGIC_STICK`

306

`MODIFIER_EVENT_ON_DAMAGE_HPLOSS`

307

`MODIFIER_PROPERTY_SHARE_XPRUNE`

308

`MODIFIER_PROPERTY_NO_FREE_TP_SCROLL_ON_DEATH`

310

`MODIFIER_PROPERTY_HAS_BONUS_NEUTRAL_ITEM_CHOICE`

311

`MODIFIER_PROPERTY_FORCE_MAX_HEALTH`

313

`MODIFIER_PROPERTY_FORCE_MAX_MANA`

314

`MODIFIER_PROPERTY_AOE_BONUS_CONSTANT`

315

`MODIFIER_PROPERTY_AOE_BONUS_CONSTANT_STACKING`

316

`MODIFIER_EVENT_ON_TAKEDAMAGE_POST_UNAVOIDABLE_BLOCK`

317

`MODIFIER_EVENT_ON_MUTE_DAMAGE_ABILITIES`

318

`MODIFIER_PROPERTY_SUPPRESS_CRIT`

319

`MODIFIER_PROPERTY_ABILITY_POINTS`

320

`MODIFIER_PROPERTY_BUYBACK_PENALTY_PERCENT`

321

`MODIFIER_PROPERTY_ITEM_SELLBACK_COST`

322

`MODIFIER_PROPERTY_DISASSEMBLE_ANYTHING`

323

`MODIFIER_PROPERTY_FIXED_MANA_REGEN`

324

`MODIFIER_PROPERTY_BONUS_UPHILL_MISS_CHANCE`

325

`MODIFIER_PROPERTY_CREEP_DENY_PERCENT`

326

`MODIFIER_PROPERTY_ATTACKSPEED_ABSOLUTE_MAX`

327

`MODIFIER_PROPERTY_FOW_TEAM`

328

`MODIFIER_EVENT_ON_HERO_BEGIN_DYING`

329

`MODIFIER_PROPERTY_BONUS_LOTUS_HEAL`

330

`MODIFIER_PROPERTY_BASE_HP_REGEN_PER_STR_BONUS_PERCENTAGE`

331

`MODIFIER_PROPERTY_BASE_ARMOR_PER_AGI_BONUS_PERCENTAGE`

332

`MODIFIER_PROPERTY_BASE_MP_REGEN_PER_INT_BONUS_PERCENTAGE`

333

`MODIFIER_PROPERTY_BASE_MRES_PER_INT_BONUS_PERCENTAGE`

334

`MODIFIER_EVENT_ON_DAY_STARTED`

335

`MODIFIER_PROPERTY_CREATE_BONUS_ILLUSION_CHANCE`

337

`MODIFIER_PROPERTY_CREATE_BONUS_ILLUSION_COUNT`

338

`MODIFIER_PROPERTY_PSEUDORANDOM_BONUS`

339

`MODIFIER_PROPERTY_ATTACK_HEIGHT_BONUS`

340

`MODIFIER_PROPERTY_SKIP_ATTACK_REGULATOR`

341

`MODIFIER_PROPERTY_MISS_PERCENTAGE_TARGET`

342

`MODIFIER_PROPERTY_ADDITIONAL_NEUTRAL_ITEM_DROPS`

343

`MODIFIER_PROPERTY_KILL_STREAK_BONUS_GOLD_PERCENTAGE`

344

`MODIFIER_PROPERTY_HP_REGEN_MULTIPLIER_PRE_AMPLIFICATION`

345

`MODIFIER_PROPERTY_HEROFACET_OVERRIDE`

346

`MODIFIER_EVENT_ON_TREE_CUT_DOWN`

347

`MODIFIER_EVENT_ON_CLEAVE_ATTACK_LANDED`

348

`MODIFIER_PROPERTY_MIN_ATTRIBUTE_LEVEL`

349

`MODIFIER_PROPERTY_TIER_TOKEN_REROLL`

350

`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK_STACKING`

352

`MODIFIER_PROPERTY_INVENTORY_SLOT_RESTRICTED`

353

`MODIFIER_EVENT_ON_TIER_TOKEN_REROLLED`

354

`MODIFIER_PROPERTY_REDIRECT_SPELL`

355

`MODIFIER_PROPERTY_BASEATTACK_POSTBONUS`

356

`MODIFIER_EVENT_ON_FOW_TEAM_CHANGED`

357

`MODIFIER_PROPERTY_SUPPRESS_ATTACK_PROCS`

358

`MODIFIER_EVENT_ON_ABILITY_TOGGLED`

359

`MODIFIER_FUNCTION_LAST`

378

`MODIFIER_FUNCTION_INVALID`

65535

## Enum.DrunkenBrawlerState

Key

Value

`DRUNKEN_BRAWLER_STATE_EARTH`

0

`DRUNKEN_BRAWLER_STATE_STORM`

1

`DRUNKEN_BRAWLER_STATE_FIRE`

2

## Enum.OverHeadAlert

Key

Value

`OVERHEAD_ALERT_GOLD`

0

`OVERHEAD_ALERT_DENY`

1

`OVERHEAD_ALERT_CRITICAL`

2

`OVERHEAD_ALERT_XP`

3

`OVERHEAD_ALERT_BONUS_SPELL_DAMAGE`

4

`OVERHEAD_ALERT_MISS`

5

`OVERHEAD_ALERT_DAMAGE`

6

`OVERHEAD_ALERT_EVADE`

7

`OVERHEAD_ALERT_BLOCK`

8

`OVERHEAD_ALERT_BONUS_POISON_DAMAGE`

9

`OVERHEAD_ALERT_HEAL`

10

`OVERHEAD_ALERT_MANA_ADD`

11

`OVERHEAD_ALERT_MANA_LOSS`

12

`OVERHEAD_ALERT_MAGICAL_BLOCK`

16

`OVERHEAD_ALERT_INCOMING_DAMAGE`

17

`OVERHEAD_ALERT_OUTGOING_DAMAGE`

18

`OVERHEAD_ALERT_DISABLE_RESIST`

19

`OVERHEAD_ALERT_DEATH`

20

`OVERHEAD_ALERT_BLOCKED`

21

`OVERHEAD_ALERT_ITEM_RECEIVED`

22

`OVERHEAD_ALERT_SHARD`

23

`OVERHEAD_ALERT_DEADLY_BLOW`

24

## Enum.ShareAbility

Key

Value

`ITEM_FULLY_SHAREABLE`

0

`ITEM_PARTIALLY_SHAREABLE`

1

`ITEM_NOT_SHAREABLE`

2

## Enum.TeamNum

Key

Value

`TEAM_NONE`

`TEAM_DIRE`

`TEAM_RADIANT`

`TEAM_NEUTRAL`

## Enum.UIState

Key

Value

`DOTA_GAME_UI_STATE_INVALID`

`DOTA_GAME_UI_STATE_LOADING_SCREEN`

`DOTA_GAME_UI_DOTA_INGAME`

`DOTA_GAME_UI_STATE_DASHBOARD`

## Enum.DormancyType

Key

Value

`ENTITY_NOT_DORMANT`

0

`ENTITY_DORMANT`

1

`ENTITY_SUSPENDED`

2

## Enum.ECourierState

Key

Value

`k_eIdle`

0

`k_eGoToShop`

2

`k_eGoToUnit`

3

`k_eManual`

4

## Enum.DrawFlags

Key

Value

`None`

`Closed`

`RoundCornersTopLeft`

`RoundCornersTopRight`

`RoundCornersBottomLeft`

`RoundCornersBottomRight`

`RoundCornersNone`

`RoundCornersTop`

`RoundCornersBottom`

`RoundCornersLeft`

`RoundCornersRight`

`RoundCornersAll`

`RoundCornersDefault_`

`RoundCornersMask_`

`ShadowCutOutShapeBackground`

[PreviousCallbacks](/api-v2.0/cheats-types-and-callbacks/callbacks)[NextClasses](/api-v2.0/cheats-types-and-callbacks/classes)

Last updated 6 months ago


--------------------------------------------------------------------------------

### Classes - Color

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color -->

Copy

# 🎨Color

Color metatable

### Fields

Name

Type

Description

**r**

`number`

red

**g**

`number`

green

**b**

`number`

blue

**a**

`number`

alpha

## Color

`Color([r], [g], [b], [a]):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**r** `[?]`

`number`

`(default: 255)`

**g** `[?]`

`number`

`(default: 255)`

**b** `[?]`

`number`

`(default: 255)`

**a** `[?]`

`number`

`(default: 255)`

Create a new Color.

## Color

`Color(hex):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**hex**

`string`

Hex string. Do not use "#" symbol.

Create a new Color from hex string.

## AsFraction

`:AsFraction(r, g, b, a):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**r**

`number`

New R color range as a percentage in the range [0.0, 1.0]

**g**

`number`

New G color range as a percentage in the range [0.0, 1.0]

**b**

`number`

New B color range as a percentage in the range [0.0, 1.0]

**a**

`number`

New A color range as a percentage in the range [0.0, 1.0]

Overwrites the color's ranges using the fraction values. Returns itself.

## AsInt

`:AsInt(value):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**value**

`number`

int color value

Overwrites the color's ranges converting the int value to RGBA values. Returns
itself.

## AsHsv

`:AsHsv(h, s, v, a):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**h**

`number`

Hue color range [0.0, 1.0]

**s**

`number`

Saturation color range [0.0, 1.0]

**v**

`number`

Value color range [0.0, 1.0]

**a**

`number`

Alpha color range [0.0, 1.0]

Overwrites the color's ranges converting the HSV to RGBA values. Returns itself.

## AsHsl

`:AsHsl(h, s, l, a):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**h**

`number`

Hue color range [0.0, 1.0]

**s**

`number`

Saturation color range [0.0, 1.0]

**l**

`number`

Lightness color range [0.0, 1.0]

**a**

`number`

Alpha color range [0.0, 1.0]

Overwrites the color's ranges converting the HSL to RGBA values. Returns itself.

## ToFraction

`:ToFraction():` `number`, `number`, `number`, `number`

Returns the r, g, b, and a ranges of the color as a percentage in the range of
[0.0, 1.0].

## ToInt

`:ToInt():` `number`

Returns the int value representing the color.

## ToHsv

`:ToHsv():` `number`, `number`, `number`

Returns the HSV representation of the color.

## ToHsl

`:ToHsl():` `number`, `number`, `number`

Returns the ToHsl representation of the color.

## ToHex

`:ToHex():` `string`

Returns the hex string representing the color.

## Lerp

`:Lerp(other, weight):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**other**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color to interpolate to

**weight**

`number`

A value between 0 and 1 that indicates the weight of **other**

Returns the linearly interpolated color between two colors by the specified weight.

## Grayscale

`:Grayscale(weight):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**weight**

`number`

A value between 0 and 1 that indicates the weight of **grayscale**

Returns the grayscaled color.

## AlphaModulate

`:AlphaModulate(alpha):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**alpha**

`number`

Alpha color range [0.0, 1.0]

Returns the alpha modulated color.

## Clone

`:Clone():` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Creates and returns a copy of the color object.

## Unpack

`:Unpack():` `number`, `number`, `number`, `number`

Returns the r, g, b, and a values of the color. Note that these fields can be
accessed by indexing r, g, b, and a.

## \_\_tostring

`:__tostring():` `string`

Returns hex string representing the color.

[PreviousClasses](/api-v2.0/cheats-types-and-callbacks/classes)[NextMenu](/api-v2.0/cheats-types-and-callbacks/classes/menu)

Last updated 8 months ago


--------------------------------------------------------------------------------

### Classes - Menu System

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu -->

Copy

# 📋Menu

Table to work with Menu.

## Find

`Menu.Find(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName, widgetName, attachmentName, widgetInGearName):` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [`CMenuColorPicker`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [`CMenuButton`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) | [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [`CMenuMultiSelect`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | `nil`

Name

Type

Description

**firstTabName**

`string`

**sectionName**

`string`

**secondTabName**

`string`

**thirdTabName**

`string`

**groupTabName**

`string`

**widgetName**

`string`

**attachmentName**

`string`

**widgetInGearName**

`string`

Returns menu item.

## Create

`Menu.Create(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName):` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

Name

Type

Description

**firstTabName**

`string`

**sectionName**

`string`

**secondTabName**

`string`

**thirdTabName**

`string`

**groupTabName**

`string`

Creates tab/section/group. Returns menu item.

## Style

`Menu.Style(styleColor):` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Name

Type

Description

**styleColor**

`string`

Creates tab/section/group. Returns color of specified style var or table of all style colors
depends on param.

## Opened

`Menu.Opened():` `boolean`

Returns current menu open state.

## VisualsIsEnabled

`Menu.VisualsIsEnabled():` `boolean`

Returns current visuals enabled state.

## Alpha

`Menu.Alpha():` `number`

Returns current menu alpha.

## Pos

`Menu.Pos():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu pos.

## Size

`Menu.Size():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu size.

## Scale

`Menu.Scale():` `integer`

Returns current menu scale percentage.

## AnimDuration

`Menu.AnimDuration():` `number`

Returns current menu animation duration.

[PreviousColor](/api-v2.0/cheats-types-and-callbacks/classes/color)[NextCTabSection](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection -->

Copy

# CTabSection

CTabSection metatable

## Name

`:Name():` `string`

Returns tab's name.

## Parent

`:Parent():` [`CFirstTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab)

Returns tab's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## Create

`:Create(sectionName):` [`CSecondTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)

Name

Type

Description

**sectionName**

`string`

Creates new `CSecondTab`.

## Find

`:Find(sectionName):` [`CSecondTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab) | `nil`

Name

Type

Description

**sectionName**

`string`

Finds the `CSecondTab` by name.

[PreviousMenu](/api-v2.0/cheats-types-and-callbacks/classes/menu)[NextCFirstTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab -->

Copy

# CFirstTab

CFirstTab metatable

## Name

`:Name():` `string`

Returns tab's name.

## Parent

`:Parent():` `nil`

Returns parent. It's `nil` for CFirstTab.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## Create

`:Create(sectionName):` [`CTabSection`](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

Name

Type

Description

**sectionName**

`string`

Creates new `CTabSection`.

## Find

`:Find(sectionName):` [`CTabSection`](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection) | `nil`

Name

Type

Description

**sectionName**

`string`

Finds the `CTabSection` by name.

[PreviousCTabSection](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)[NextCSecondTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab -->

Copy

# CSecondTab

CSecondTab metatable

## Name

`:Name():` `string`

Returns tab's name.

## Parent

`:Parent():` [`CTabSection`](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

Returns tab's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## Create

`:Create(tabName):` [`CThirdTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Name

Type

Description

**tabName**

`string`

Creates new `CThirdTab`.

## Find

`:Find(tabName):` [`CThirdTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab) | `nil`

Name

Type

Description

**tabName**

`string`

Finds the `CThirdTab` by name.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets tab's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## LinkHero

`:LinkHero(heroId, attribute):` `nil`

Name

Type

Description

**heroId**

`integer`

See `Engine.GetHeroIDByName`

**attribute**

[`Enum.Attributes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Links tab to hero and attribute.

[PreviousCFirstTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab)[NextCThirdTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab -->

Copy

# CThirdTab

CThirdTab metatable

## Name

`:Name():` `string`

Returns tab's name.

## Parent

`:Parent():` [`CSecondTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)

Returns tab's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## Create

`:Create(groupName, [side]):` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

Name

Type

Description

**groupName**

`string`

**side** `[?]`

[`Enum.GroupSide`](/api-v2.0/cheats-types-and-callbacks/enums#enum.groupside)

`(default: Enum.GroupSide.Default)`

Creates new `CMenuGroup`.

## Find

`:Find(groupName):` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | `nil`

Name

Type

Description

**groupName**

`string`

Finds the `CMenuGroup` by name.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets third tab's visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets tab's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

[PreviousCSecondTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)[NextCMenuGroup](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup -->

Copy

# CMenuGroup

CMenuGroup metatable

## Name

`:Name():` `string`

Returns group's name.

## Parent

`:Parent():` [`CThirdTab`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Returns group's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## Find

`:Find(widgetName):` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [`CMenuColorPicker`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [`CMenuButton`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) | [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [`CMenuMultiSelect`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | `nil`

Name

Type

Description

**widgetName**

`string`

Finds the widget by name.

## Switch

`:Switch(switchName, [defaultValue], [imageIcon]):` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

Name

Type

Description

**switchName**

`string`

**defaultValue** `[?]`

`boolean`

`(default: false)`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuSwitch`.

## Bind

`:Bind(bindName, [defaultValue], [imageIcon]):` [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Name

Type

Description

**bindName**

`string`

**defaultValue** `[?]`

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

`(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuBind`.

## Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

Name

Type

Description

**sliderName**

`string`

**minValue**

`integer`

**maxValue**

`integer`

**defaultValue**

`integer`

**format** `[?]`

`string` | `fun(value: integer):string`

Format string or function to format value. See example. `(default: "%d")`

Creates new `CMenuSliderInt` or `CMenuSliderFloat` depents on arg types.
`minValue`, `maxValue` and `defaultValue` should be integer to create `CMenuSliderInt`.

#### Example

## Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

Name

Type

Description

**sliderName**

`string`

**minValue**

`number`

**maxValue**

`number`

**defaultValue**

`number`

**format** `[?]`

`string` | `fun(value: number):string`

Format string or function to format value. See example. `(default: "%f")`

Creates new `CMenuSliderFloat`.

#### Example

## ColorPicker

`:ColorPicker(colorPickerName, color, [imageIcon]):` [`CMenuColorPicker`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

Name

Type

Description

**colorPickerName**

`string`

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuColorPicker`.

## Button

`:Button(buttonName, callback, [altStyle], [widthPercent]):` [`CMenuButton`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)

Name

Type

Description

**buttonName**

`string`

**callback**

`function`

`func(this: CMenuButton):nil` function to call on button click.

**altStyle** `[?]`

`boolean`

Use alternative button style. `(default: false)`

**widthPercent** `[?]`

`number`

Button width in percents. [0.0, 1.0] `(default: 1.0)`

Creates new `CMenuButton`.

#### Example

## Combo

`:Combo(comboName, items, [defaultValue]):` [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

Name

Type

Description

**comboName**

`string`

**items**

`string[]`

**defaultValue** `[?]`

`integer`

Index of default item. (starts from 0) `(default: 0)`

Creates new `CMenuComboBox`.

## MultiCombo

`:MultiCombo(multiComboName, items, enabledItems):` [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

Name

Type

Description

**multiComboName**

`string`

**items**

`string[]`

**enabledItems**

`string[]`

table of enabled items

Creates new `CMenuMultiComboBox`.

#### Example

## MultiSelect

`:MultiSelect(multiSelectName, items, [expanded]):` [`CMenuMultiSelect`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

Name

Type

Description

**multiSelectName**

`string`

**items**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See example.

**expanded** `[?]`

`boolean`

false if you want to create MultiSelect in collapsed state. `(default: false)`

Creates new `CMenuMultiSelect`.

#### Example

## Input

`:Input(inputName, defaultValue, [imageIcon]):` [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

Name

Type

Description

**inputName**

`string`

**defaultValue**

`string`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuInputBox`.

## Label

`:Label(labelText, [imageIcon]):` [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

Name

Type

Description

**labelText**

`string`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuLabel`.

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets group's disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets group's visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## SearchHidden

`:SearchHidden(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets group's search state. Depends on argument.

#### Example

## SearchHidden

`:SearchHidden():` `boolean`

#### Example

[PreviousCThirdTab](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)[NextWidgets](/api-v2.0/cheats-types-and-callbacks/classes/widgets)

Last updated 2 months ago


--------------------------------------------------------------------------------

### Classes - UI Widgets

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets -->

Copy

# 🧩Widgets

[CMenuSwitch](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)[CMenuSliderFloat](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)[CMenuSliderInt](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)[CMenuButton](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)[CMenuColorPicker](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)[CMenuColorPickerAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)[CMenuComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)[CMenuGearAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)[CMenuInputBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)[CMenuMultiComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)[CMenuMultiSelect](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)[CMenuBind](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)[CMenuLabel](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

[PreviousCMenuGroup](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)[NextCMenuSwitch](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch -->

Copy

# CMenuSwitch

CMenuSwitch metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` `boolean`

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

`boolean`

Sets widget's value.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuSwitch):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuSwitch):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousWidgets](/api-v2.0/cheats-types-and-callbacks/classes/widgets)[NextCMenuSliderFloat](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat -->

Copy

# CMenuSliderFloat

CMenuSliderFloat metatable.

## Update

`:Update(minValue, maxValue, defaultValue):` `nil`

Name

Type

Description

**minValue**

`number`

**maxValue**

`number`

**defaultValue**

`number`

Updates the slider values.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` `number`

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

`number`

Sets widget's value.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuSliderFloat):nil`

function to be called on widget change.\

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuSliderFloat):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousCMenuSwitch](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)[NextCMenuSliderInt](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint -->

Copy

# CMenuSliderInt

CMenuSliderInt metatable.

## Update

`:Update(minValue, maxValue, defaultValue):` `nil`

Name

Type

Description

**minValue**

`integer`

**maxValue**

`integer`

**defaultValue**

`integer`

Updates the slider values.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` `integer`

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

`integer`

Sets widget's value.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuSliderInt):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuSliderInt):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousCMenuSliderFloat](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)[NextCMenuButton](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton -->

Copy

# CMenuButton

CMenuButton metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuButton):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuButton):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

[PreviousCMenuSliderInt](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)[NextCMenuColorPicker](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker -->

Copy

# CMenuColorPicker

CMenuColorPicker metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Sets widget's value.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuColorPicker):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuColorPicker):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## HideAlphaBar

`:HideAlphaBar(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets alpha bar state. Depends on argument.

#### Example

## HideAlphaBar

`:HideAlphaBar():` `boolean`

#### Example

[PreviousCMenuButton](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)[NextCMenuColorPickerAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment -->

Copy

# CMenuColorPickerAttachment

CMenuColorPickerAttachment metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) | [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Get

`:Get():` [`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Sets widget's value.

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuColorPickerAttachment):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuColorPickerAttachment):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

[PreviousCMenuColorPicker](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)[NextCMenuComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox -->

Copy

# CMenuComboBox

CMenuComboBox metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Update

`:Update(items, [defaultValue]):` `nil`

Name

Type

Description

**items**

`string[]`

**defaultValue** `[?]`

`integer`

Index of default item. (starts from 0) `(default: 0)`

Update the combo box values.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` `integer`

Returns index of the selected item. It starts from 0.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

`integer`

Sets widget's value.

## List

`:List():` `string[]`

Returns array of the items.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuComboBox):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuComboBox):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousCMenuColorPickerAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)[NextCMenuGearAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment -->

Copy

# CMenuGearAttachment

CMenuGearAttachment metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` \*\*`nil`\*\*

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## Find

`:Find(widgetName):` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [`CMenuColorPicker`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [`CMenuMultiSelect`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | `nil`

Name

Type

Description

**widgetName**

`string`

Finds the widget by name.

## Switch

`:Switch(switchName, [defaultValue], [imageIcon]):` [`CMenuSwitch`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

Name

Type

Description

**switchName**

`string`

**defaultValue** `[?]`

`boolean`

`(default: false)`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuSwitch`.

## Bind

`:Bind(bindName, [defaultValue], [imageIcon]):` [`CMenuBind`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Name

Type

Description

**bindName**

`string`

**defaultValue** `[?]`

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

`(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuBind`.

## Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderInt`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

Name

Type

Description

**sliderName**

`string`

**minValue**

`integer`

**maxValue**

`integer`

**defaultValue**

`integer`

**format** `[?]`

`string` | `fun(value: integer):string`

Format string or function to format value. See example. `(default: "%d")`

Creates new `CMenuSliderInt` or `CMenuSliderFloat` depents on arg types.
`minValue`, `maxValue` and `defaultValue` should be integer to create `CMenuSliderInt`.

#### Example

## Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderFloat`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

Name

Type

Description

**sliderName**

`string`

**minValue**

`number`

**maxValue**

`number`

**defaultValue**

`number`

**format** `[?]`

`string` | `fun(value: number):string`

Format string or function to format value. See example. `(default: "%f")`

Creates new `CMenuSliderFloat`.

#### Example

## ColorPicker

`:ColorPicker(colorPickerName, color, [imageIcon]):` [`CMenuColorPicker`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

Name

Type

Description

**colorPickerName**

`string`

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuColorPicker`.

## Combo

`:Combo(comboName, items, [defaultValue]):` [`CMenuComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

Name

Type

Description

**comboName**

`string`

**items**

`string[]`

**defaultValue** `[?]`

`integer`

Index of default item. (starts from 0) `(default: 0)`

Creates new `CMenuComboBox`.

## MultiCombo

`:MultiCombo(multiComboName, items, enabledItems):` [`CMenuMultiComboBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

Name

Type

Description

**multiComboName**

`string`

**items**

`string[]`

**enabledItems**

`string[]`

table of enabled items

Creates new `CMenuMultiComboBox`.

#### Example

## MultiSelect

`:MultiSelect(multiSelectName, items, [expanded]):` [`CMenuMultiSelect`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

Name

Type

Description

**multiSelectName**

`string`

**items**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See example.

**expanded** `[?]`

`boolean`

false if you want to create MultiSelect in collapsed state. `(default: false)`

Creates new `CMenuMultiSelect`.

#### Example

## Input

`:Input(inputName, [defaultValue], [imageIcon]):` [`CMenuInputBox`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

Name

Type

Description

**inputName**

`string`

**defaultValue** `[?]`

`string`

`(default: "")`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuInputBox`.

## Label

`:Label(labelText, [imageIcon]):` [`CMenuLabel`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

Name

Type

Description

**labelText**

`string`

**imageIcon** `[?]`

`string`

Path to image or FontAwesome icon unicode. `(default: "")`

Creates new `CMenuLabel`.

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

[PreviousCMenuComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)[NextCMenuInputBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox -->

Copy

# CMenuInputBox

CMenuInputBox metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get():` `string`

Returns widget's value.

## Set

`:Set(value):` `nil`

Name

Type

Description

**value**

`string`

Sets widget's value.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuInputBox):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuInputBox):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousCMenuGearAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)[NextCMenuMultiComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox -->

Copy

# CMenuMultiComboBox

CMenuMultiComboBox metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Update

`:Update(items, enabledItems):` `nil`

Name

Type

Description

**items**

`string[]`

**enabledItems**

`string[]`

table of enabled items

Updates the multicombo values.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get(itemId):` `boolean`

Name

Type

Description

**itemId**

`string`

Returns enable state of the item in combo box.

## Set

`:Set(enabledItems):` `nil`

Name

Type

Description

**enabledItems**

`string[]`

A table of enabled items; other items will be disabled.

Sets a new value for the item by itemId or sets a new list of enabled items

## Set

`:Set(itemId, value):` `nil`

Name

Type

Description

**itemId**

`string`

**value**

`boolean`

## List

`:List():` `string[]`

Returns array of itemIds.

## ListEnabled

`:ListEnabled():` `string[]`

Returns array of enabled itemIds.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuMultiComboBox):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuMultiComboBox):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

[PreviousCMenuInputBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)[NextCMenuMultiSelect](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect -->

Copy

# CMenuMultiSelect

CMenuMultiSelect metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Update

`:Update(items, [expanded], [saveToConfig]):` `nil`

Name

Type

Description

**items**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See `CMenuGroup:MultiSelect`.

**expanded** `[?]`

`boolean`

false if you want to create MultiSelect in collapsed state. `(default: false)`

**saveToConfig** `[?]`

`boolean`

true if you want to save to config `(default: false)`

Updates the multiselect values.

## OneItemSelection

`:OneItemSelection(newState):` `boolean`

Name

Type

Description

**newState**

`boolean`

Gets or sets one item selection state. One item selection allows only one item to be
selected. Depends on the argument.

## OneItemSelection

`:OneItemSelection():` `boolean`

## DragAllowed

`:DragAllowed(newState):` `boolean`

Name

Type

Description

**newState**

`boolean`

Gets or sets drag allowed state. Drag allows items to be ordered by cursor.
Depends on the argument.

## DragAllowed

`:DragAllowed():` `boolean`

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get(itemId):` `boolean`

Name

Type

Description

**itemId**

`string`

Returns enable state of the item in multiselect.

## Set

`:Set(enabledItems):` `nil`

Name

Type

Description

**enabledItems**

`string[]`

A table of enabled items; other items will be disabled.

Sets a new value for the item by itemId or sets a new list of enabled items

## Set

`:Set(itemId, value):` `nil`

Name

Type

Description

**itemId**

`string`

**value**

`boolean`

## List

`:List():` `string[]`

Returns array of itemIds.

## ListEnabled

`:ListEnabled():` `string[]`

Returns array of enabled itemIds.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuMultiSelect):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuMultiSelect):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## UpdateBackgroundColors

`:UpdateBackgroundColors(colors):` `nil`

Name

Type

Description

**colors**

`table<string>`

Table with background colors.

Updates widget's background colors.

## UpdateImageColors

`:UpdateImageColors(colors):` `nil`

Name

Type

Description

**colors**

`table<string>`

Table with image colors.

Updates widget's image colors.

## UpdateToolTips

`:UpdateToolTips(colors):` `nil`

Name

Type

Description

**colors**

`table<string>`

Table with new tooltips

Updates widget's tooltips

[PreviousCMenuMultiComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)[NextCMenuBind](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind -->

Copy

# CMenuBind

CMenuBind metatable.

## Name

`:Name():` `string`

Returns widget's name.

## Parent

`:Parent():` [`CMenuGroup`](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## Type

`:Type():` [`Enum.WidgetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget's type.

## Open

`:Open():` `nil`

Opens parent tabs.

## ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

**newText**

`string`

Changes text in the widget. The path to the widget is not affected.
May be used for dynamic text customization or recolor.

## ToolTip

`:ToolTip(newText):` `string`

Name

Type

Description

**newText**

`string`

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.
Depends on the argument.

## ToolTip

`:ToolTip():` `string`

## Visible

`:Visible(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets visible state. Depends on argument.

#### Example

## Visible

`:Visible():` `boolean`

#### Example

## Disabled

`:Disabled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets disabled state. Depends on argument.

#### Example

## Disabled

`:Disabled():` `boolean`

#### Example

## Unsafe

`:Unsafe(value):` `nil`

Name

Type

Description

**value**

`boolean`

Gets or sets unsafe state. Unsafe widgets have warning sign.
Depends on argument.

## Unsafe

`:Unsafe():` `boolean`

## Get

`:Get([idx]):` [`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Name

Type

Description

**idx** `[?]`

`0` | `1`

index of the button to get value from `(default: 0)`

Returns widget's value. To get both of the buttons use `Buttons` method.

## Set

`:Set(key1, [key2]):` `nil`

Name

Type

Description

**key1**

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

primary button code

**key2** `[?]`

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

secondary button code `(default: Enum.ButtonCode.KEY_NONE)`

Sets widget's value.

## Buttons

`:Buttons():` [`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode), [`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Returns widget's buttons value.

## IsDown

`:IsDown():` `boolean`

Returns `true` when the key or both keys is down.

## IsPressed

`:IsPressed():` `boolean`

Returns `true` when the key or both keys is pressed for the first time.

## IsToggled

`:IsToggled():` `boolean`

Bind stores it's toggle state and switches it when the key is pressed. This method
returns this state.

## SetToggled

`:SetToggled(value):` `nil`

Name

Type

Description

**value**

`boolean`

Sets the toggle state manually.

## Image

`:Image(imagePath, [offset]):` `nil`

Name

Type

Description

**imagePath**

`string`

Path to the image.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets widget's image.

## ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset. `(default: {0.0, 0.0})`

Sets tab's image by already created handle.

## Icon

`:Icon(icon, [offset]):` `nil`

Name

Type

Description

**icon**

`string`

icon unicode.

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional icon offset. `(default: {0.0, 0.0})`

Sets widget's icon.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### Example

## SetCallback

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` \*\*`nil`\*\*

Name

Type

Description

**callback**

`fun(this: CMenuBind):nil`

function to be called on widget change.

**forceCall** `[?]`

`boolean`

true if you want to call callback on widget creation. `(default: false)`

Sets widget's on change callback.

## UnsetCallback

`:UnsetCallback(callback):` `nil`

Name

Type

Description

**callback**

`fun(this: CMenuBind):nil`

function to be removed from widget's callbacks.

Removes widget's on change callback.

## ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color.

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Name

Type

Description

**name**

`string`

Name of the attachment.

**gearIcon** `[?]`

`string`

Gear FontAwesome icon. `(default: "\uf013")`

**useSmallFont** `[?]`

`boolean`

Use small font for gear icon. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget.

## Properties

`:Properties([name], [value], [markAsToggle]):` `nil`

Name

Type

Description

**name** `[?]`

`string`

Overridden name to display in bind list. `(default: nil)`

**value** `[?]`

`string`

Overridden value to display alongside the name in the bind list. This can be used to provide additional context about the bind. `(default: nil)`

**markAsToggle** `[?]`

`boolean`

Indicates whether the bind should be marked as a toggle, which is particularly useful if the bind's functionality includes toggling states. Recommended to be used in conjunction with the IsToggled(). `(default: false)`

Updates the properties of a widget for display in the bind list.

## ShowInBindIsland

`:ShowInBindIsland(newStatus):` `boolean`

Name

Type

Description

**newStatus**

`boolean`

Gets or sets the visibility of the bind in the bind island.

## ShowInBindIsland

`:ShowInBindIsland():` `boolean`

## MouseBinding

`:MouseBinding(newStatus):` `boolean`

Name

Type

Description

**newStatus**

`boolean`

Gets or sets the ability to bind the mouse button.

## MouseBinding

`:MouseBinding():` `boolean`

[PreviousCMenuMultiSelect](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)[NextCMenuLabel](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

Last updated 5 months ago


--------------------------------------------------------------------------------

### Classes - Math

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math -->

Copy

# 🔢Math

[🌐Vector](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)[🔄Angle](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)[🔢Vec2](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)[🔀Vertex](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

[PreviousCMenuLabel](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)[NextVector](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector -->

Copy

# 🌐Vector

Vector metatable

### Fields

Name

Type

Description

**x**

`number`

**y**

`number`

**z**

`number`

## Vector

`Vector([x], [y], [z]):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**x** `[?]`

`number`

`(default: 0.0)`

**y** `[?]`

`number`

`(default: 0.0)`

**z** `[?]`

`number`

`(default: 0.0)`

Create a new Vector.

## \_\_tostring

`:__tostring():` `string`

## \_\_add

Overload for operator +

`:__add(other):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_sub

Overload for operator -

`:__sub(other):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_div

Overload for operator /

`:__div(other):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_mul

Overload for operator \*

`:__mul(other):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_eq

Overload for operator ==

`:\_\_eq(other):` \*\*`boolean`\*\*

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

## Distance

`:Distance(other):` `number`

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Computes the distance from this vector to other.

## Distance2D

`:Distance2D(other):` `number`

Name

Type

Description

**other**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Computes the distance from this vector to other ignoring Z axis.

## Normalized

`:Normalized():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns this vector with a length of 1.
When normalized, a vector keeps the same direction but its length is 1.0.
Note that the current vector is unchanged and a new normalized vector is returned. If you want to normalize the current vector, use `Vector:Normalize` function.

## Normalize

`:Normalize():` `nil`

Makes this vector have a length of 1.
When normalized, a vector keeps the same direction but its length is 1.0.
Note that this function will change the current vector. If you want to keep the current vector unchanged, use `Vector:Normalized` function.

## Dot

`:Dot(vector):` `number`

Name

Type

Description

**vector**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Dot Product of two vectors.
The dot product is a float value equal to the magnitudes of the two vectors multiplied together and then multiplied by the cosine of the angle between them.
For normalized vectors Dot returns 1 if they point in exactly the same direction, -1 if they point in completely opposite directions and zero if the vectors are perpendicular.
[More](https://medium.com/@r.w.overdijk/unity-vector3-dot-what-11feb258052e)

## Dot2D

`:Dot2D(vector):` `number`

Name

Type

Description

**vector**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Dot Product of two vectors ignoring Z axis.

## Scaled

`:Scaled(scale):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**scale**

`number`

Returns this vector multiplied by the given number. The same as `Vector * number`.

## Scale

`:Scale(scale):` `nil`

Name

Type

Description

**scale**

`number`

Multiplies this vector by the given number. The same as `Vector = Vector * number`.

## Length

`:Length():` `number`

Returns the length of this vector.
The length of the vector is `math.sqrt(x*x+y*y+z*z)`.
If you only need to compare length of some vectors, you can compare squared magnitudes of them using LengthSqr (computing squared length is faster).

## LengthSqr

`:LengthSqr():` `number`

Returns the squared length of this vector.
This method is faster than Length because it avoids computing a square root. Use this method if you need to compare vectors.

## Length2D

`:Length2D():` `number`

Returns the length of this vector ignoring Z axis.

## Length2DSqr

`:Length2DSqr():` `number`

Returns the squared length of this vector ignoring Z axis.
This method is faster than Length2D because it avoids computing a square root. Use this method if you need to compare vectors.

## Rotated

`:Rotated(angle):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**angle**

`number` | [`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Returns the new vector rotated counterclockwise by the given angle in the XY-plane, leaving the Z-axis unaffected.

## Rotate

`:Rotate(angle):` `nil`

Name

Type

Description

**angle**

`number` | [`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Rotates this vector counterclockwise by the given angle in the XY-plane, leaving the Z-axis unaffected.

## Lerp

`:Lerp(b, t):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**b**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

end value, returned when t = 1

**t**

`number`

value used to interpolate between a and b.

Returns linearly interpolated vector between two vectors.
The value returned equals **a + (b - a) \* t** (which can also be written **a \* (1-t) + b\*t**).
When `t = 0`, **a:Lerp(b, t)** returns `a`.
When `t = 1`, **a:Lerp(b, t)** returns `b`.
When `t = 0.5`, **a:Lerp(b, t)** returns the point midway between `a` and `b`.

## Cross

`:Cross(vector):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**vector**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns cross product of two vectors.
[More](https://docs.unity3d.com/ScriptReference/Vector3.Cross.html)
[Visualization](https://www.youtube.com/watch?v=kz92vvioeng)

## MoveForward

`:MoveForward(angle, distance):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**angle**

[`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

**distance**

`number`

distance to move

Moves vector forward by a specified distance in the direction defined by a given Angle.

#### Example

## ToAngle

`:ToAngle():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Converts Vector to Angle. See
https://github.com/ValveSoftware/source-sdk-2013/blob/0565403b153dfcde602f6f58d8f4d13483696a13/src/mathlib/mathlib\_base.cpp#L535

## ToScreen

`:ToScreen():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2), `boolean`

Converts Vector to screen coordinate

## Get

`:Get():` `number`, `number`, `number`

Returns x, y and z of this vector.

## GetX

`:GetX():` `number`

Returns x of this vector. The same as Vector.x.

## GetY

`:GetY():` `number`

Returns y of this vector. The same as Vector.y.

## GetZ

`:GetZ():` `number`

Returns z of this vector. The same as Vector.z.

## SetX

`:SetX(value):` `nil`

Name

Type

Description

**value**

`number`

Sets x. The same as Vector.x = value.

## SetY

`:SetY(value):` `nil`

Name

Type

Description

**value**

`number`

Sets y. The same as Vector.y = value.

## SetZ

`:SetZ(value):` `nil`

Name

Type

Description

**value**

`number`

Sets z. The same as Vector.z = value.

[PreviousMath](/api-v2.0/cheats-types-and-callbacks/classes/math)[NextAngle](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle -->

Copy

# 🔄Angle

Angle metatable

### Fields

Name

Type

Description

**pitch**

`number`

**yaw**

`number`

**roll**

`number`

## Angle

`Angle([pitch], [yaw], [roll]):` [`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Name

Type

Description

**pitch** `[?]`

`number`

`(default: 0.0)`

**yaw** `[?]`

`number`

`(default: 0.0)`

**roll** `[?]`

`number`

`(default: 0.0)`

Create a new Angle.

## \_\_tostring

`:__tostring():` `string`

## GetForward

`:GetForward():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward vector from a given Angle.

## GetVectors

`:GetVectors():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector), [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector), [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward, right and up.

## GetYaw

`:GetYaw():` `number`

Returns the yaw. The same as Angle.yaw.

## GetRoll

`:GetRoll():` `number`

Returns the roll. The same as Angle.roll.

## GetPitch

`:GetPitch():` `number`

Returns the pitch. The same as Angle.pitch.

## SetYaw

`:SetYaw(value):` `nil`

Name

Type

Description

**value**

`number`

Sets the yaw. The same as Angle.yaw = value.

## SetRoll

`:SetRoll(value):` `nil`

Name

Type

Description

**value**

`number`

Sets the roll. The same as Angle.roll = value.

## SetPitch

`:SetPitch(value):` `nil`

Name

Type

Description

**value**

`number`

Sets the pitch. The same as Angle.pitch = value.

[PreviousVector](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)[NextVec2](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2 -->

Copy

# 🔢Vec2

Vec2 metatable

### Fields

Name

Type

Description

**x**

`number`

**y**

`number`

## Vec2

`Vec2(x, y):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Name

Type

Description

**x**

`number`

**y**

`number`

Create a new Vec2.

## Vec2

`Vec2():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Create a new Vec2(0,0).

## \_\_tostring

`:__tostring():` `string`

## \_\_add

Overload for operator +

`:__add(other):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Name

Type

Description

**other**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_sub

Overload for operator -

`:__sub(other):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Name

Type

Description

**other**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## \_\_div

Overload for operator /

`:\_\_div(other):` [\*\*`Vec2`\*\*](Vec2.md)

Name

Type

Description

**other**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | `number`

## Length

`:Length():` `number`

Returns the length of the vector.

## Get

`:Get():` `number`, `number`

Returns x, y of this vector.

## GetX

`:GetX():` `number`

Returns x of this vector. The same as Vec2.x.

## GetY

`:GetY():` `number`

Returns y of this vector. The same as Vec2.y.

## SetX

`:SetX(value):` `nil`

Name

Type

Description

**value**

`number`

Sets x. The same as Vec2.x = value.

## SetY

`:SetY(value):` `nil`

Name

Type

Description

**value**

`number`

Sets y. The same as Vec2.y = value.

[PreviousAngle](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)[NextVertex](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex -->

Copy

# 🔀Vertex

Vertex metatable

### Fields

Name

Type

Description

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

screen pos

**uv**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

texture uv

## Vertex

`Vertex(pos, uv):` [`Vertex`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

Name

Type

Description

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

**uv**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Create a new Vertex.

## Vertex

`Vertex(posx, posy, uvx, uvy):` [`Vertex`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

Name

Type

Description

**posx**

`number`

**posy**

`number`

**uvx**

`number`

**uvy**

`number`

Create a new Vertex(0,0).

## \_\_tostring

`:__tostring():` `string`

## \_\_add

Overload for operator +

`:__add(other):` [`Vertex`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

Name

Type

Description

**other**

[`Vertex`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex) | `number`

## \_\_sub

Overload for operator -

`:\_\_sub(other):` [\*\*`Vertex`\*\*](Vertex.md)

Name

Type

Description

**other**

[`Vertex`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex) | `number`

[PreviousVec2](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)[NextLists](/api-v2.0/game-components/lists)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Game Components - Entity Lists

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists -->

Copy

# 📃Lists

[🔮Abilities](/api-v2.0/game-components/lists/abilities)[🚚Couriers](/api-v2.0/game-components/lists/couriers)[🛠️CustomEntities](/api-v2.0/game-components/lists/customentities)[👾Entities](/api-v2.0/game-components/lists/entities)[🦸Heroes](/api-v2.0/game-components/lists/heroes)[🎭NPCs](/api-v2.0/game-components/lists/npcs)[🐉Camps](/api-v2.0/game-components/lists/camps)[👥Players](/api-v2.0/game-components/lists/players)[🔮Runes](/api-v2.0/game-components/lists/runes)[🌳TempTrees](/api-v2.0/game-components/lists/temptrees)[🏰Towers](/api-v2.0/game-components/lists/towers)[🌲Trees](/api-v2.0/game-components/lists/trees)[🎁Physical Items](/api-v2.0/game-components/lists/physicalitems)[✨Modifiers](/api-v2.0/game-components/lists/modifiers)[🚀LinearProjectiles](/api-v2.0/game-components/lists/linearprojectiles)

[PreviousVertex](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)[NextAbilities](/api-v2.0/game-components/lists/abilities)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/abilities -->

Copy

# 🔮Abilities

Table to work with ability list.

## Count

`Abilities.Count():` `integer`

Return size of ability list.

## Get

`Abilities.Get(index):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**index**

`integer`

Index of ability in cheat list.

Return ability by index in cheat list. Not the same as in-game index.

## GetAll

`Abilities.GetAll():` [`CAbility[]`](/api-v2.0/game-components/core/ability)

Return all abilities in cheat list.

## Contains

`Abilities.Contains(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Ability to check.

Check ability in cheat list.

[PreviousLists](/api-v2.0/game-components/lists)[NextCouriers](/api-v2.0/game-components/lists/couriers)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/couriers -->

Copy

# 🚚Couriers

Table to work with courier list.

## Count

`Couriers.Count():` `integer`

Return size of courier list.

## Get

`Couriers.Get(index):` [`CCourier`](/api-v2.0/game-components/core/courier) | `nil`

Name

Type

Description

**index**

`integer`

Index of courier in cheat list.

Return courier by index in cheat list. Not the same as in-game index.

## GetAll

`Couriers.GetAll():` [`CCourier[]`](/api-v2.0/game-components/core/courier)

Return all couriers in cheat list.

## Contains

`Couriers.Contains(courier):` `boolean`

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

Courier to check.

Check courier in cheat list.

## GetLocal

`Couriers.GetLocal():` [`CCourier`](/api-v2.0/game-components/core/courier) | `nil`

Return local courier.

[PreviousAbilities](/api-v2.0/game-components/lists/abilities)[NextCustomEntities](/api-v2.0/game-components/lists/customentities)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/customentities -->

Copy

# 🛠️CustomEntities

Table to work with specific abilities.

## GetSpiritBear

`CustomEntities.GetSpiritBear(spiritBear):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**spiritBear**

[`CAbility`](/api-v2.0/game-components/core/ability)

The Spirit Bear ability.

Accept the Spirit Bear ability and return linked Bear.

## GetVengeIllusion

`CustomEntities.GetVengeIllusion(commandAura):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**commandAura**

[`CAbility`](/api-v2.0/game-components/core/ability)

The Command Aura ability.

Accept the Vengeful Spirit's Command Aura ability and return scepter linked illusion.

## GetTetheredUnit

`CustomEntities.GetTetheredUnit(tether):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**tether**

[`CAbility`](/api-v2.0/game-components/core/ability)

The Tether ability.

Accept the Wisp's Tether ability and return linked unit.

## GetTempestDouble

`CustomEntities.GetTempestDouble(tempestDouble):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**tempestDouble**

[`CAbility`](/api-v2.0/game-components/core/ability)

The Tempest Double ability.

Accept the Arc Warden's Tempest Double ability and return linked clone.

## GetMeepoIndex

`CustomEntities.GetMeepoIndex(dividedWeStand):` `integer` | `nil`

Name

Type

Description

**dividedWeStand**

[`CAbility`](/api-v2.0/game-components/core/ability)

The Divided We Stand ability.

Accept the Meepo's Divided We Stand ability and return index of Meepo.

[PreviousCouriers](/api-v2.0/game-components/lists/couriers)[NextEntities](/api-v2.0/game-components/lists/entities)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/entities -->

Copy

# 👾Entities

Table to work with entity list.

## GetAll

`Entities.GetAll():` [`CEntity[]`](/api-v2.0/game-components/core/entity)

Get all entities on the map.

## Contains

`Entities.Contains(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Entity to check.

Check entity in cheat list.

[PreviousCustomEntities](/api-v2.0/game-components/lists/customentities)[NextHeroes](/api-v2.0/game-components/lists/heroes)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/heroes -->

Copy

# 🦸Heroes

Table to work with hero list.

## Count

`Heroes.Count():` `integer`

Return size of hero list.

## Get

`Heroes.Get(index):` [`CHero`](/api-v2.0/game-components/core/hero) | `nil`

Name

Type

Description

**index**

`integer`

Index of hero in cheat list.

Return hero by index in cheat list. Not the same as in-game index.

## GetAll

`Heroes.GetAll():` [`CHero[]`](/api-v2.0/game-components/core/hero)

Return all heroes in cheat list.

## Contains

`Heroes.Contains(hero):` `boolean`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Hero to check.

Check hero in cheat list.

## InRadius

`Heroes.InRadius(pos, radius, teamNum, teamType, [omitIllusions], [omitDormant]):` [`CHero[]`](/api-v2.0/game-components/core/hero)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

**teamNum**

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Team number to check.

**teamType**

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

Team type to filter by. Relative to teamNum param.

**omitIllusions** `[?]`

`boolean`

`true` if you want to get table without illusions `(default: false)`

**omitDormant** `[?]`

`boolean`

`true` if you want to get table without dormant units `(default: true)`

Return all heroes in radius.

## GetLocal

`Heroes.GetLocal():` [`CHero`](/api-v2.0/game-components/core/hero) | `nil`

Return local hero.

[PreviousEntities](/api-v2.0/game-components/lists/entities)[NextNPCs](/api-v2.0/game-components/lists/npcs)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/npcs -->

Copy

# 🎭NPCs

Table to work with NPC list.

## Count

`NPCs.Count():` `integer`

Return size of NPC list.

## Get

`NPCs.Get(index):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**index**

`integer`

Index of NPC in cheat list.

Return NPC by index in cheat list. Not the same as in-game index.

## GetAll

`NPCs.GetAll([filter]):` [`CNPC[]`](/api-v2.0/game-components/core/npc)

Name

Type

Description

**filter** `[?]`

[`Enum.UnitTypeFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags) | `fun(npc: CNPC):boolean`

`(default: nil)`

Return all NPCs in cheat list. Can be filtered by unit type or custom function.
Unit type filter is a much faster than custom function and can be or'ed to filter multiple types.

#### Example

Copy

```
-- filter function to get all structures except towers
for _, v in pairs(NPCs.GetAll(function (npc)
     return NPC.IsStructure(npc) and not NPC.IsTower(npc);
end)) do
     print(NPC.GetUnitName(v))
end

-- get all towers and heroes (x5 times faster than filter function)
for _, v in pairs(NPCs.GetAll(Enum.UnitTypeFlags.TYPE_TOWER | Enum.UnitTypeFlags.TYPE_HERO)) do
		print(NPC.GetUnitName(v))
end
```

## GetInScreen

`NPCs.GetInScreen([filter], [skipDormant]):` `{entity:CNPC, position:Vec2}[]`

Name

Type

Description

**filter** `[?]`

[`Enum.UnitTypeFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags) | `nil`

`(default: nil)`

**skipDormant** `[?]`

`boolean`

`true` if you want to get table without dormant units `(default: true)`

Return all NPCs in cheat list that visible on your screen. Can be filtered by unit type argument.

## InRadius

`NPCs.InRadius(pos, radius, teamNum, teamType, [omitIllusions], [omitDormant]):` [`CNPC[]`](/api-v2.0/game-components/core/npc)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

**teamNum**

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Team number to check.

**teamType**

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

Team type to filter by. Relative to teamNum param.

**omitIllusions** `[?]`

`boolean`

`true` if you want to get table without illusions `(default: false)`

**omitDormant** `[?]`

`boolean`

`true` if you want to get table without dormant units `(default: true)`

Return all NPCs in radius.

## Contains

`NPCs.Contains(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

NPC to check.

Check NPC in cheat list.

[PreviousHeroes](/api-v2.0/game-components/lists/heroes)[NextCamps](/api-v2.0/game-components/lists/camps)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/camps -->

Copy

# 🐉Camps

Table to work with list of neutral spawners.

## Count

`Camps.Count():` `integer`

Return size of neutral spawner list.

## Get

`Camps.Get(index):` [`CCamp`](/api-v2.0/game-components/core/camp) | `nil`

Name

Type

Description

**index**

`integer`

Index of neutral spawner in cheat list.

Return neutral spawner by index in cheat list. Not the same as in-game index.

## GetAll

`Camps.GetAll():` [`CCamp[]`](/api-v2.0/game-components/core/camp)

Return all neutral spawners in cheat list.

## InRadius

`Camps.InRadius(pos, radius):` [`CCamp[]`](/api-v2.0/game-components/core/camp)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

Return all neutral spawners in radius.

## Contains

`Camps.Contains(camp):` `boolean`

Name

Type

Description

**camp**

[`CCamp`](/api-v2.0/game-components/core/camp)

Neutral spawner to check.

Check neutral spawner in cheat list.

[PreviousNPCs](/api-v2.0/game-components/lists/npcs)[NextPlayers](/api-v2.0/game-components/lists/players)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/players -->

Copy

# 👥Players

Table to work with player list.

## Count

`Players.Count():` `integer`

Return size of player list.

## Get

`Players.Get(index):` [`CPlayer`](/api-v2.0/game-components/core/player) | `nil`

Name

Type

Description

**index**

`integer`

Index of player in cheat list.

Return player by index in cheat list. Not the same as in-game index.

## GetAll

`Players.GetAll():` [`CPlayer[]`](/api-v2.0/game-components/core/player)

Return all players in cheat list.

## Contains

`Players.Contains(player):` `boolean`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

Player to check.

Check player in cheat list.

## GetLocal

`Players.GetLocal():` [`CPlayer`](/api-v2.0/game-components/core/player)

Return local player.

[PreviousCamps](/api-v2.0/game-components/lists/camps)[NextRunes](/api-v2.0/game-components/lists/runes)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/runes -->

Copy

# 🔮Runes

Table to work with rune list.

## Count

`Runes.Count():` `integer`

Return size of rune list.

## Get

`Runes.Get(index):` [`CRune`](/api-v2.0/game-components/core/rune) | `nil`

Name

Type

Description

**index**

`integer`

Index of rune in cheat list.

Return rune by index in cheat list. Not the same as in-game index.

## GetAll

`Runes.GetAll():` [`CRune[]`](/api-v2.0/game-components/core/rune)

Return all runes in cheat list.

## Contains

`Runes.Contains(rune):` `boolean`

Name

Type

Description

**rune**

[`CRune`](/api-v2.0/game-components/core/rune)

Rune to check.

Check rune in cheat list.

[PreviousPlayers](/api-v2.0/game-components/lists/players)[NextTempTrees](/api-v2.0/game-components/lists/temptrees)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/temptrees -->

Copy

# 🌳TempTrees

Table to work with list of temp trees.

## Count

`TempTrees.Count():` `integer`

Return size of temp trees list.

## Get

`TempTrees.Get(index):` [`CTree`](/api-v2.0/game-components/core/tree) | `nil`

Name

Type

Description

**index**

`integer`

Index of temp tree in cheat list.

Return temp tree by index in cheat list. Not the same as in-game index.

## GetAll

`TempTrees.GetAll():` [`CTree[]`](/api-v2.0/game-components/core/tree)

Return all temp trees in cheat list.

## InRadius

`TempTrees.InRadius(pos, radius):` [`CTree[]`](/api-v2.0/game-components/core/tree)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

Return all temp trees in radius.

## Contains

`TempTrees.Contains(tree):` `boolean`

Name

Type

Description

**tree**

[`CTree`](/api-v2.0/game-components/core/tree)

Temp tree to check.

Check temp tree in cheat list.

[PreviousRunes](/api-v2.0/game-components/lists/runes)[NextTowers](/api-v2.0/game-components/lists/towers)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/towers -->

Copy

# 🏰Towers

Table to work with tower list.

## Count

`Towers.Count():` `integer`

Return size of tower list.

## Get

`Towers.Get(index):` [`CTower`](/api-v2.0/game-components/core/tower) | `nil`

Name

Type

Description

**index**

`integer`

Index of tower in cheat list.

Return tower by index in cheat list. Not the same as in-game index.

## GetAll

`Towers.GetAll():` [`CTower[]`](/api-v2.0/game-components/core/tower)

Return all towers in cheat list.

## InRadius

`Towers.InRadius(pos, radius, teamNum, [teamType]):` [`CTower[]`](/api-v2.0/game-components/core/tower)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

**teamNum**

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Team number to check.

**teamType** `[?]`

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

Team number to check. `(default: Enum.TeamType.TEAM_ENEMY)`

Return all towers in radius.

## Contains

`Towers.Contains(tower):` `boolean`

Name

Type

Description

**tower**

[`CTower`](/api-v2.0/game-components/core/tower)

Tower to check.

Check tower in cheat list.

[PreviousTempTrees](/api-v2.0/game-components/lists/temptrees)[NextTrees](/api-v2.0/game-components/lists/trees)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/trees -->

Copy

# 🌲Trees

Table to work with list of trees.

## Count

`Trees.Count():` `integer`

Return size of tree list.

## Get

`Trees.Get(index):` [`CTree`](/api-v2.0/game-components/core/tree) | `nil`

Name

Type

Description

**index**

`integer`

Index of tree in cheat list.

Return tree by index in cheat list. Not the same as in-game index.

## GetAll

`Trees.GetAll():` [`CTree[]`](/api-v2.0/game-components/core/tree)

Return all trees in cheat list.

## InRadius

`Trees.InRadius(pos, radius, [active]):` [`CTree[]`](/api-v2.0/game-components/core/tree)

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Position to check.

**radius**

`number`

Radius to check.

**active** `[?]`

`boolean`

Active state to check. `(default: true)`

Return all trees in radius.

## Contains

`Trees.Contains(tree):` `boolean`

Name

Type

Description

**tree**

[`CTree`](/api-v2.0/game-components/core/tree)

Tree to check.

Check tree in cheat list.

[PreviousTowers](/api-v2.0/game-components/lists/towers)[NextPhysical Items](/api-v2.0/game-components/lists/physicalitems)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/physicalitems -->

Copy

# 🎁Physical Items

Table to work with list of phisical items.

## Count

`PhysicalItems.Count():` `integer`

Return size of physical item list.

## Get

`PhysicalItems.Get(index):` [`CPhysicalItem`](/api-v2.0/game-components/core/physicalitem) | `nil`

Name

Type

Description

**index**

`integer`

Index of physical item in cheat list.

Return physical item by index in cheat list. Not the same as in-game index.

## GetAll

`PhysicalItems.GetAll():` [`CPhysicalItem[]`](/api-v2.0/game-components/core/physicalitem)

Return all physical items in cheat list.

## Contains

`PhysicalItems.Contains(physical):` `boolean`

Name

Type

Description

**physical**

[`CPhysicalItem`](/api-v2.0/game-components/core/physicalitem)

item Physical item to check.

Check physical item in cheat list.

[PreviousTrees](/api-v2.0/game-components/lists/trees)[NextModifiers](/api-v2.0/game-components/lists/modifiers)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/modifiers -->

Copy

# ✨Modifiers

Table to work with list of modifiers.

## Count

`Modifiers.Count():` `integer`

Returns size of modifiers list.

## Get

`Modifiers.Get(index):` [`CModifier`](/api-v2.0/game-components/core/modifier) | `nil`

Name

Type

Description

**index**

`integer`

Index of temp tree in cheat list.

Returns modifiers by index in cheat list. Not the same as in-game index.

## GetAll

`Modifiers.GetAll():` [`CModifier[]`](/api-v2.0/game-components/core/modifier)

Returns all modifiers in cheat list.

## Contains

`Modifiers.Contains(tree):` `boolean`

Name

Type

Description

**tree**

[`CModifier`](/api-v2.0/game-components/core/modifier)

Temp tree to check.

Checks if modifiers is in list.

[PreviousPhysical Items](/api-v2.0/game-components/lists/physicalitems)[NextLinearProjectiles](/api-v2.0/game-components/lists/linearprojectiles)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/linearprojectiles -->

Copy

# 🚀LinearProjectiles

Table to work linear projectiles.

## GetAll

`LinearProjectiles.GetAll():` `{handle: integer, max_speed: number, max_dist: number, start_position: Vector, position: Vector, velocity: Vector, original_velocity: Vector, acceleration: Vector, fow_radius: number, source: CEntity}[]`

Returns the 1-based indexed table with all existing projectiles. See example.

#### Example

Copy

```
-- linearprojectiles_getall.lua
return {
    OnUpdate = function ()
        local linears = LinearProjectiles.GetAll();
        if (not linears) then return end;
        
        for i, projectile in pairs(linears) do
            Log.Write("+++++++++++++++++++++++")
            Log.Write(projectile['max_dist']);
            Log.Write(projectile['handle']);
            Log.Write(projectile['position']);
            Log.Write(projectile['velocity']);
            Log.Write(projectile['start_position']);
            Log.Write(projectile['max_speed']);
            Log.Write("+++++++++++++++++++++++")
        end
    end
}
```

[PreviousModifiers](/api-v2.0/game-components/lists/modifiers)[NextCore](/api-v2.0/game-components/core)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Game Components - Core Objects

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core -->

Copy

# 🔧Core

[👤Player](/api-v2.0/game-components/core/player)[✨Modifier](/api-v2.0/game-components/core/modifier)[👾Entity](/api-v2.0/game-components/core/entity)[🎭NPC](/api-v2.0/game-components/core/npc)[🦸Hero](/api-v2.0/game-components/core/hero)[🌟Ability](/api-v2.0/game-components/core/ability)[🔑Item](/api-v2.0/game-components/core/item)[🔮Rune](/api-v2.0/game-components/core/rune)[🏰Tower](/api-v2.0/game-components/core/tower)[🌳Tree](/api-v2.0/game-components/core/tree)[🔱Vambrace](/api-v2.0/game-components/core/vambrace)[🐉Camp](/api-v2.0/game-components/core/camp)[🍾Bottle](/api-v2.0/game-components/core/bottle)[🚚Courier](/api-v2.0/game-components/core/courier)[🍻DrunkenBrawler](/api-v2.0/game-components/core/drunkenbrawler)[📦PhysicalItem](/api-v2.0/game-components/core/physicalitem)[👟PowerTreads](/api-v2.0/game-components/core/powertreads)[🪙TierToken](/api-v2.0/game-components/core/tiertoken)

[PreviousLinearProjectiles](/api-v2.0/game-components/lists/linearprojectiles)[NextPlayer](/api-v2.0/game-components/core/player)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/player -->

Copy

# 👤Player

Table to work with `CPlayer`. `CPlayer` extends `CEntity`

## PrepareUnitOrders

`Player.PrepareUnitOrders(player, type, target, pos, ability, issuer, issuer_npc, [queue], [show_effects], [callback], [execute_fast], [identifier], [force_minimap]):` `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The player issuing the order.

**type**

[`Enum.UnitOrder`](/api-v2.0/cheats-types-and-callbacks/enums#enum.unitorder)

The type of order to be issued.

**target**

[`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

The target entity, if applicable.

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The positional coordinates for the order.

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

The ability for order.

**issuer**

[`Enum.PlayerOrderIssuer`](/api-v2.0/cheats-types-and-callbacks/enums#enum.playerorderissuer)

The issuer capture mode.

**issuer\_npc**

[`CNPC`](/api-v2.0/game-components/core/npc) | [`CNPC[]`](/api-v2.0/game-components/core/npc)

The specific NPC or group of NPC that will issue the order.

**queue** `[?]`

`boolean`

If true, the order will be added to the Dota cast queue. `(default: false)`

**show\_effects** `[?]`

`boolean`

If true, visual effects will indicate the position of the order. `(default: false)`

**callback** `[?]`

`boolean`

If true, the order will be pushed to the `OnPrepareUnitOrders` callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

If true, the order will bypass internal safety delays for immediate execution. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

**force\_minimap** `[?]`

`boolean`

If true, the order will be forced by the minimap if possible. `(default: true)`

Provides ability to execute such game actions as moving, attacking, or casting spells etc.

## HoldPosition

`Player.HoldPosition(player, issuer_npc, [queue], [push], [execute_fast], [identifier]):` `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The player issuing the order.

**issuer\_npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The specific NPC that will issue the order.

**queue** `[?]`

`boolean`

If true, the order will be added to the Dota cast queue. `(default: false)`

**push** `[?]`

`boolean`

If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

If true, the order will bypass internal safety delays for immediate execution. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

Sends the hold position action.

## AttackTarget

`Player.AttackTarget(player, issuer_npc, target, [queue], [push], [execute_fast], [identifier], [force_minimap]):` `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The player issuing the order.

**issuer\_npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The specific NPC that will issue the order.

**target**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**queue** `[?]`

`boolean`

If true, the order will be added to the Dota cast queue. `(default: false)`

**push** `[?]`

`boolean`

If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

If true, the order will bypass internal safety delays for immediate execution. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

**force\_minimap** `[?]`

`boolean`

If true, the order will be forced by the minimap if possible. `(default: true)`

Sends the attack target position.

## GetPlayerID

`Player.GetPlayerID(player):` `integer`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player ID within the current game session.
If the player ID is not valid, it will return -1.

## GetPlayerSlot

`Player.GetPlayerSlot(player):` `integer`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player slot number within the current game session.

## GetPlayerTeamSlot

`Player.GetPlayerTeamSlot(player):` `integer`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the team slot number assigned to the player within their respective team.

## GetName

`Player.GetName(player):` `string`, `string` | `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player nickname and his proname

## GetProName

`Player.GetProName(steamId):` `string`

Name

Type

Description

**steamId**

`integer`

Returns cached player's proname. Works only in game callbacks

## GetPlayerData

`Player.GetPlayerData(player):` `{valid:boolean, fullyJoined:boolean, fakeClient:boolean, connectionState:integer, steamid:integer, PlusSubscriber:boolean, MVPLastGame:boolean, PlayerName:string, ProName:string}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player data table.

## GetTeamData

`Player.GetTeamData(player):` `{selected_hero_id:integer, kills:integer, assists:integer, deaths:integer, streak:integer, respawnTime:integer, selected_hero_variant:integer, lane_selection_flags:integer, last_buyback_time:number}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player team data table.
Team data is only available for players on the local team.

## GetNeutralStashItems

`Player.GetNeutralStashItems(player):` `{item: CItem }[]`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns table with `CItem`s available in the neutral stash.

## GetTeamPlayer

`Player.GetTeamPlayer(player):` `{reliable_gold:integer, unreliable_gold:integer, starting_position:integer, totalearned_gold:integer, totalearned_xp:integer, shared_gold:integer, hero_kill_gold:integer, creep_kill_gold:integer, neutral_kill_gold:integer, courier_gold:integer, bounty_gold:integer, roshan_gold:integer, building_gold:integer, other_gold:integer, comeback_gold:integer, experimental_gold:integer, experimental2_gold:integer, creepdeny_gold:integer, tp_scrolls_purchased:integer, custom_stats:number, income_gold:integer, ward_kill_gold:integer, ability_gold:integer, networth:integer, deny_count:integer, lasthit_count:integer, lasthit_streak:integer, lasthit_multikill:integer, nearby_creep_death_count:integer, claimed_deny_count:integer, claimed_miss_count:integer, miss_count:integer, possible_hero_selection:integer, meta_level:integer, meta_experience:integer, meta_experience_awarded:integer, buyback_cooldown_time:number, buyback_gold_limit_time:number, buyback_cost_time:number, custom_buyback_cooldown:number, stuns:number, healing:number, tower_Kills:integer, roshan_kills:integer, camera_target:CEntity, override_selection_entity:CEntity, observer_wards_placed:integer, sentry_wards_placed:integer, creeps_stacked:integer, camps_stacked:integer, rune_pickups:integer, gold_spent_on_support:integer, hero_damage:integer, wards_purchased:integer, wards_destroyed:integer, commands_issued:integer, gold_spent_on_consumables:integer, gold_spent_on_items:integer, gold_spent_on_buybacks:integer, gold_lost_to_death:integer, is_new_player:boolean, is_guide_player:boolean, acquired_madstone:integer, current_madstone:integer}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns **Team Player Data** table

## GetPlayerNeutralInfo

`Player.GetPlayerNeutralInfo(player):` `nil` | `{acquired_madstone:integer, current_madstone:integer, trinket_choices:integer[], enhancement_choices:integer[], selected_trinkets:integer[], selected_enhancements:integer[], times_crafted:integer[]}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns info about player's neutral items

## IsMuted

`Player.IsMuted(player):` `boolean`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns the player mute status.

## GetSelectedUnits

`Player.GetSelectedUnits(player):` [`CNPC[]`](/api-v2.0/game-components/core/npc)

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns table of selected units by player.

## AddSelectedUnit

`Player.AddSelectedUnit(player, NPC):` `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

**NPC**

[`CNPC`](/api-v2.0/game-components/core/npc)

To select.

Adds unit to player selection.

## ClearSelectedUnits

`Player.ClearSelectedUnits(player):` `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Clears player selection.

## GetQuickBuyInfo

`Player.GetQuickBuyInfo(player):` `{m_quickBuyItems:integer[], m_quickBuyIsPurchasable:boolean[]}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns table with m\_quickBuyItems(item ids) and m\_quickBuyIsPurchasable(table of booleans).

## GetCourierControllerInfo

`Player.GetCourierControllerInfo(player):` `{state:integer, shop:integer}`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns table with m\_CourierController structure

## GetTotalGold

`Player.GetTotalGold(player):` `integer`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns total gold of player.

## GetAssignedHero

`Player.GetAssignedHero(player):` [`CHero`](/api-v2.0/game-components/core/hero) | `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns player's assigned hero.

## GetActiveAbility

`Player.GetActiveAbility(player):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**player**

[`CPlayer`](/api-v2.0/game-components/core/player)

The target player.

Returns player's active ability.

[PreviousCore](/api-v2.0/game-components/core)[NextModifier](/api-v2.0/game-components/core/modifier)

Last updated 6 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/modifier -->

Copy

# ✨Modifier

Table to work with `CModifier`. You can get modifiers from `NPC.GetModifier`function.

## GetName

`Modifier.GetName(modifier):` `string`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get name of

Returns the name of the modifier.

## GetClass

`Modifier.GetClass(modifier):` `string`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

Returns the name of the modifier's class.

## GetModifierAura

Deprecated.

`Modifier.GetModifierAura(modifier):` `string`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get aura of

Should return the name of the modifier's aura, but instead, it returns an empty string in all
the cases I have tested.

## GetSerialNumber

Deprecated.

`Modifier.GetSerialNumber(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get serial number of

Should return the serial number of the modifier, but instead, it returns 0 in all the cases I
have tested.

## GetStringIndex

Deprecated.

`Modifier.GetStringIndex(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get string index of

Should return the string index of the modifier, but instead, it returns 0 in all the cases I
have tested.

## GetIndex

`Modifier.GetIndex(modifier):` `GetIndex`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get index of

Returns the hero's modifier index. The index is an incrementable value with each new modifier
the NPC gets

## GetCreationTime

`Modifier.GetCreationTime(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get creation time of

Returns the game time when the modifier was created.

## GetCreationFrame

`Modifier.GetCreationFrame(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get creation frame of

Returns the frame when the modifier was created. You could get current frame count from
`GlobalVars.GetFrameCount` function.

## GetLastAppliedTime

`Modifier.GetLastAppliedTime(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get last applied time of

Returns the game time when the modifier was last applied. Don't know cases when it can be
different from `GetCreationTime`.

## GetDuration

`Modifier.GetDuration(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get duration of

Returns the duration of the modifier.

## GetDieTime

`Modifier.GetDieTime(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get expiration time of

Returns the game time when the modifier will expire.

## GetStackCount

`Modifier.GetStackCount(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get stack count of

If there are stacks of the modifier, it returns the amount of stacks; otherwise, it returns
0.

## GetAuraSearchTeam

Deprecated.

`Modifier.GetAuraSearchTeam(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get aura search team of

Returns aura search team of the modifier.

## GetAuraSearchType

Deprecated.

`Modifier.GetAuraSearchType(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get aura search type of

Returns aura search type of the modifier.

## GetAuraSearchFlags

Deprecated.

`Modifier.GetAuraSearchFlags(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get aura search flags of

Returns aura search flags of the modifier.

## GetAuraRadius

Deprecated.

`Modifier.GetAuraRadius(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get aura radius of

Returns aura radius of the modifier.

## GetTeam

`Modifier.GetTeam(modifier):` [`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get team of

Returns team of the modifier.

## GetAttributes

Deprecated.

`Modifier.GetAttributes(modifier):` `integer`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get attributes of

Returns the attributes of the modifier.

## IsAura

Deprecated.

`Modifier.IsAura(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if the modifier is an aura.

## IsAuraActiveOnDeath

Deprecated.

`Modifier.IsAuraActiveOnDeath(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if the modifier aura active on death.

## GetMarkedForDeletion

Deprecated.

`Modifier.GetMarkedForDeletion(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if the modifier is marked for deletion.

## GetAuraIsHeal

Deprecated.

`Modifier.GetAuraIsHeal(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if aura is heal.

## GetProvidedByAura

`Modifier.GetProvidedByAura(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if modifier is provided by an aura.

## GetPreviousTick

`Modifier.GetPreviousTick(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get last tick time of

Returns the game time of the last modifier tick (~0.033 seconds).

## GetThinkInterval

Deprecated.

`Modifier.GetThinkInterval(modifier):` `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get think interval of

Returns the modifier's think interval.

## GetThinkTimeAccumulator

Deprecated.

`Modifier.GetThinkTimeAccumulator(modifier):` \*\*`number`\*\*

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get think time accumulator of

Return the modifier's think interval time accumulator.

## IsCurrentlyInAuraRange

`Modifier.IsCurrentlyInAuraRange(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if is in aura range.

## GetAbility

`Modifier.GetAbility(modifier):` [`CAbility`](/api-v2.0/game-components/core/ability)

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get ability of

Returns the modifier's ability.

## GetAuraOwner

`Modifier.GetAuraOwner(modifier):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier

Returns the owner of aura

## GetParent

`Modifier.GetParent(modifier):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier

Returns the parent of modifier

## GetCaster

`Modifier.GetCaster(modifier):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier

Returns caster of modifier

## GetState

`Modifier.GetState(modifier):` `number`, `number`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get state of

Returns the modifier state masks. See the example.

#### Example

## IsDebuff

`Modifier.IsDebuff(modifier):` `boolean`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to check

Returns `true` if the modifier is a debuff.

## GetField

`Modifier.GetField(modifier, fieldName, [dbgPrint]):` `any`

Name

Type

Description

**modifier**

[`CModifier`](/api-v2.0/game-components/core/modifier)

modifier to get field from

**fieldName**

`string`

field name

**dbgPrint** `[?]`

`boolean`

print possible errors `(default: false)`

Returns value of the field.

[PreviousPlayer](/api-v2.0/game-components/core/player)[NextEntity](/api-v2.0/game-components/core/entity)

Last updated 1 month ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/entity -->

Copy

# 👾Entity

Table to work with `CEntity`.

`CEntity` is base class for all entities in the game e.g. `CNPC`, `Hero`, `CPlayer`, `CAbility`

## IsEntity

`Entity.IsEntity(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in entity list. Search in unordered set.

## IsNPC

`Entity.IsNPC(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in NPC list. Search in unordered set.

## IsHero

`Entity.IsHero(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in hero list. Search in unordered set.

## IsPlayer

`Entity.IsPlayer(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in player list. Search in unordered set.

## IsAbility

`Entity.IsAbility(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is in ability list. Search in unordered set. Item is ability.

## Get

Not the same as Entities.Get(index). See example.

`Entity.Get(index):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**index**

`integer`

Returns entity by game index.

#### Example

## GetIndex

`Entity.GetIndex(entity):` `integer`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns game index of entity.

## GetClassName

`Entity.GetClassName(entity):` `string`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's class name.

## GetUnitName

`Entity.GetUnitName(entity):` `string`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's name.

## GetUnitDesignerName

`Entity.GetUnitDesignerName(entity):` `string`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's designerName field.

## GetTeamNum

`Entity.GetTeamNum(entity):` [`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's team number.

## IsSameTeam

`Entity.IsSameTeam(entity1, entity2):` `boolean`

Name

Type

Description

**entity1**

[`CEntity`](/api-v2.0/game-components/core/entity)

**entity2**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entities are in the same team.

## GetAbsOrigin

`Entity.GetAbsOrigin(entity):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's position.

## GetNetOrigin

`Entity.GetNetOrigin(entity):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's net position.

## GetRotation

`Entity.GetRotation(entity):` [`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's rotation.

#### Example

## IsAlive

`Entity.IsAlive(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is alive.

## IsDormant

`Entity.IsDormant(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns `true` if the entity is not visible to the local player.

## GetHealth

`Entity.GetHealth(entity):` `integer`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's health.

## GetMaxHealth

`Entity.GetMaxHealth(entity):` `integer`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's max health.

## GetOwner

`Entity.GetOwner(entity):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's owner or `nil` if the entity has no owner.\ e.g. for `CPlayer` -> `npc_dota_hero_ember_spirit` -> `npc_dota_hero_ember_spirit_fire_remnant`
ownership chain `Entity.GetOwner(remnant)` will return Ember Spirit's entity.

## OwnedBy

`Entity.OwnedBy(entity, owner):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

- entity to check

**owner**

[`CEntity`](/api-v2.0/game-components/core/entity)

- owner for comparison

Returns `true` if the entity is owned by another entity-owner. It will check the first owner only.

## RecursiveGetOwner

`Entity.RecursiveGetOwner(entity):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns the entity's last owner.\ e.g. for `CPlayer` -> `npc_dota_hero_ember_spirit` -> `npc_dota_hero_ember_spirit_fire_remnant`
ownership chain `Entity.GetOwner(remnant)` will return `CPlayer`.

## RecursiveOwnedBy

`Entity.RecursiveOwnedBy(entity, owner):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to check

**owner**

[`CEntity`](/api-v2.0/game-components/core/entity)

owner for comparison

Returns `true` if the entity is owned by another entity-owner. It will check the whole ownership chain.

## GetHeroesInRadius

`Entity.GetHeroesInRadius(entity, radius, [teamType], [omitIllusions], [omitDormant]):` [`CHero[]`](/api-v2.0/game-components/core/hero)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get position

**radius**

`number`

radius to search around

**teamType** `[?]`

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

relative to the entity `(default: TEAM_ENEMY)`

**omitIllusions** `[?]`

`boolean`

`true` if you want to get table without illusions `(default: false)`

**omitDormant** `[?]`

`boolean`

`true` if you want to get table without dormant units `(default: true)`

Returns an array of all alive and visible heroes in radius of the entity. Exclude illusion.

#### Example

## GetUnitsInRadius

`Entity.GetUnitsInRadius(entity, radius, [teamType], [omitIllusions], [omitDormant]):` [`CNPC[]`](/api-v2.0/game-components/core/npc)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get position

**radius**

`number`

radius to search around

**teamType** `[?]`

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

relative to the entity `(default: TEAM_ENEMY)`

**omitIllusions** `[?]`

`boolean`

`true` if you want to get table without illusions `(default: false)`

**omitDormant** `[?]`

`boolean`

`true` if you want to get table without dormant units `(default: true)`

Returns an array of all alive and visible NPCs in radius of the entity.

#### Example

## GetTreesInRadius

Active means that tree is not destroyed.

`Entity.GetTreesInRadius(entity, radius, [active]):` [`CTree[]`](/api-v2.0/game-components/core/tree)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get position

**radius**

`number`

radius to search around

**active** `[?]`

`boolean`

`true` if you want to get table with active trees only, otherwise for inactive trees `(default: true)`

Returns an array of all not temporary trees in radius of the entity.

#### Example

## GetTempTreesInRadius

Temporary trees are trees planted by abilities or items.

`Entity.GetTempTreesInRadius(entity, radius):` [\*\*`CTree[]`\*\*](Tree.md)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get position

**radius**

`number`

radius to search around

Returns an array of all temporary trees in radius of the entity.

#### Example

## IsControllableByPlayer

`Entity.IsControllableByPlayer(entity, playerId):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to check

**playerId**

`integer`

player id

Returns `true` if entity is controllable by player.

## GetRoshanHealth

`Entity.GetRoshanHealth():` `integer`

Returns Roshan's health. Onyly works in unsafe mode.

## GetForwardPosition

`Entity.GetForwardPosition(entity, distance):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get position

**distance**

`number`

distance to move forward

Returns position in front of entity or (0,0,0) if entity is invalid.

## GetClassID

`Entity.GetClassID(entity):` `integer`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get class id

Returns entity class id. Could be as a optimized way to check entity type.

## GetField

`Entity.GetField(entity, fieldName, [dbgPrint]):` `any`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

entity to get field from

**fieldName**

`string`

field name

**dbgPrint** `[?]`

`boolean`

print possible errors `(default: false)`

Returns value of the field.

[PreviousModifier](/api-v2.0/game-components/core/modifier)[NextNPC](/api-v2.0/game-components/core/npc)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/npc -->

Copy

# 🎭NPC

Table to work with `CNPC`. `CNPC` extends `CEntity`

## GetOwnerNPC

`NPC.GetOwnerNPC(npc):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to get owner from

Returns owner of the `CNPC`. Works for spirit bear.

## GetItem

`NPC.GetItem(npc, name, [isReal]):` [`CItem`](/api-v2.0/game-components/core/item) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to get item from

**name**

`string`

name of the item

**isReal** `[?]`

`boolean`

if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)`

Returns `CItem` by name.

## HasItem

`NPC.HasItem(npc, name, [isReal]):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**name**

`string`

name of the item

**isReal** `[?]`

`boolean`

if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)`

Returns `true` if the `CNPC` has item with specified name.

## HasModifier

`NPC.HasModifier(npc, name):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**name**

`string`

name of the modifier

Returns `true` if the `CNPC` has modifier with specified name.

## GetModifier

`NPC.GetModifier(npc, name):` [`CModifier`](/api-v2.0/game-components/core/modifier) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to get modifier from

**name**

`string`

name of the modifier

Returns `CModifier` by name.

## GetModifiers

`poperty\_filter` doesn`t filter all modifiers every call, it uses already prefiltered list. {% endhint %} `

NPC.GetModifiers(npc, [poperty\_filter]): `[<mark style="color:purple">**`CModifier[]`\*\*](Modifier.md)

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to get modifiers from

**poperty\_filter** `[?]`

[`Enum.ModifierFunction`](/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction)

Filter modifiers by specified property `(default: Enum.ModifierFunction.MODIFIER_FUNCTION_INVALID)`

Returns an array of all NPC's `CModifier`s.

## HasInventorySlotFree

`NPC.HasInventorySlotFree(npc, [isReal]):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**isReal** `[?]`

`boolean`

if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)`

Returns `true` if the `CNPC` has free inventory slot.

## HasState

`NPC.HasState(npc, state):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**state**

[`Enum.ModifierState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierstate)

state to check

Returns `true` if the `CNPC` has state. The best way to check if the `CNPC` is stunned, silenced, hexed, has BKB immune etc.

## GetStatesDuration

`NPC.GetStatesDuration(npc, states, [only_active_states]):` `table`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**states**

`integer[]`

states to check

**only\_active\_states** `[?]`

`boolean`

if `true` then check only states that active on unit, otherwise check all states. e.g. rooted while debuff immune `(default: true)`

Returns table of remaining modifier states duration. See the example

#### Example

## IsWaitingToSpawn

`NPC.IsWaitingToSpawn(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if waiting to spawn. For example, creeps are waiting to spawn under the ground near the barracks.

## IsIllusion

`NPC.IsIllusion(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is illusion.

## IsVisible

`NPC.IsVisible(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is visible to local player.

## IsVisibleToEnemies

`NPC.IsVisibleToEnemies(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is visible enemies.

## IsCourier

`NPC.IsCourier(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a courier.

## IsRanged

`NPC.IsRanged(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a ranged unit.

## IsCreep

`NPC.IsCreep(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a creep.

## IsLaneCreep

`NPC.IsLaneCreep(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a lane creep.

## IsStructure

`NPC.IsStructure(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a structure.

## IsTower

`NPC.IsTower(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a tower.

## GetUnitType

`NPC.GetUnitType(npc):` [`Enum.UnitTypeFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags)

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns unit type flags.

## IsConsideredHero

`NPC.IsConsideredHero(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if it is unit a considered a hero for targeting purposes.

## IsBarracks

`NPC.IsBarracks(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a barracks.

## IsAncient

`NPC.IsAncient(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is an ancient creeps.

## IsRoshan

`NPC.IsRoshan(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a Roshan.

## IsNeutral

`NPC.IsNeutral(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a neutral. Neutral creeps, ancient creeps.

## IsHero

`NPC.IsHero(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a hero.

## IsWard

`NPC.IsWard(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a ward.

## IsMeepoClone

`NPC.IsMeepoClone(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is a meepo clone.

## IsEntityInRange

`NPC.IsEntityInRange(npc, npc2, range):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**npc2**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**range**

`number`

range to check

Returns `true` if the `CNPC` in range of other `CNPC`.

## IsPositionInRange

`NPC.IsPositionInRange(npc, pos, range, [hull]):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

**range**

`number`

range to check

**hull** `[?]`

`number`

hull just added to range `(default: 0.0)`

Returns `true` if the `CNPC` in range of position.

## IsLinkensProtected

`NPC.IsLinkensProtected(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is protected by Linkens Sphere.

## IsMirrorProtected

`NPC.IsMirrorProtected(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is protected by Mirror Shield.

## IsChannellingAbility

Do not work for items.

`NPC.IsChannellingAbility(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

Returns `true` if the `CNPC` is channeling ability. Black Hole, Life Drain, etc.

## GetChannellingAbility

`NPC.GetChannellingAbility(npc):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the currently channelling `CAbility`.

## IsRunning

`NPC.IsRunning(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` is running.

## IsAttacking

`NPC.IsAttacking(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` is attacking.

## IsSilenced

`NPC.IsSilenced(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` is silenced.

## IsStunned

`NPC.IsStunned(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` is stunned.

## HasAegis

`NPC.HasAegis(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` has aegis.

## IsKillable

`NPC.IsKillable(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns `true` if the `CNPC` has killable. Example: false if affected by Eul.

## GetActivity

`NPC.GetActivity(npc):` [`Enum.GameActivity`](/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity)

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the `CNPC` activity, such as running, attacking, casting, etc.

## GetAnimationInfo

`NPC.GetAnimationInfo(npc):` `{sequence:integer, cycle:number, name:string, mdl_name:string}`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns information about the current animation of the `CNPC`.

## GetAttackRange

`NPC.GetAttackRange(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the base attack range of the `CNPC`.

## GetAttackRangeBonus

`NPC.GetAttackRangeBonus(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the bonus attack range of the `CNPC`.

## GetCastRangeBonus

`NPC.GetCastRangeBonus(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the bonus cast range of the `CNPC`.

## GetPhysicalArmorValue

`NPC.GetPhysicalArmorValue(npc, [excludeWhiteArmor]):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**excludeWhiteArmor** `[?]`

`boolean`

exclude white armor `(default: true)`

Returns the physical armor value of the `CNPC`.

## GetPhysicalDamageReduction

`NPC.GetPhysicalDamageReduction(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the physical damage reduction value of the `CNPC`.

## GetArmorDamageMultiplier

`NPC.GetArmorDamageMultiplier(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the physical damage multiplier value of the `CNPC`.

## GetMagicalArmorValue

`NPC.GetMagicalArmorValue(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the magical armor value of the `CNPC`.

## GetMagicalArmorDamageMultiplier

`NPC.GetMagicalArmorDamageMultiplier(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the magical damage multiplier value of the `CNPC`.

## GetIncreasedAttackSpeed

`NPC.GetIncreasedAttackSpeed(npc, [ignore_temp_attack_speed]):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**ignore\_temp\_attack\_speed** `[?]`

`boolean`

ignore temporary attack speed `(default: false)`

Returns increased attack speed of the `CNPC`.

## GetAttacksPerSecond

`NPC.GetAttacksPerSecond(npc, [ignore_temp_attack_speed]):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**ignore\_temp\_attack\_speed** `[?]`

`boolean`

ignore temporary attack speed `(default: false)`

Returns the number of attacks per second that the `CNPC` can deal.

## GetAttackTime

`NPC.GetAttackTime(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the amount of time needed for the `CNPC` to perform an attack.

## GetAttackSpeed

`NPC.GetAttackSpeed(npc, [ignore_temp_attack_speed]):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**ignore\_temp\_attack\_speed** `[?]`

`boolean`

ignore temporary attack speed `(default: false)`

Returns the attack speed of the `CNPC`.

## GetBaseAttackSpeed

`NPC.GetBaseAttackSpeed(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the base attack speed of the `CNPC`.

## GetHullRadius

`NPC.GetHullRadius(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the model interaction radius of the `CNPC`.

## GetPaddedCollisionRadius

`NPC.GetPaddedCollisionRadius(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the collision hull radius (including padding) of this `NPC`.

## GetCollisionPadding

`NPC.GetCollisionPadding(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the collision including padding of this `NPC`.

## GetPaddedCollisionRadius

`NPC.GetPaddedCollisionRadius(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the ring radius of this `NPC`.

## GetProjectileCollisionSize

see: https://dota2.fandom.com/wiki/Unit\_Size#Collision\_Size

`NPC.GetProjectileCollisionSize(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the collision size of the `CNPC`. Collision size is the internal size that prevents other units from passing through.

## GetTurnRate

see: https://dota2.fandom.com/wiki/Turn\_rate

`NPC.GetTurnRate(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the turn rate, which is the speed at which the `CNPC` can turn.

## GetAttackAnimPoint

see: https://dota2.fandom.com/wiki/Attack\_animation

`NPC.GetAttackAnimPoint(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the attack animation point, `nil` if not found.

## GetAttackProjectileSpeed

see: https://dota2.fandom.com/wiki/Projectile\_Speed

`NPC.GetAttackProjectileSpeed(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the attack projectile speed, `nil` if not found.

## IsTurning

`NPC.IsTurning(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns true if the `CNPC` is turning.

## GetAngleDiff

doesn't work for creeps

`NPC.GetAngleDiff(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the remaining degree angle needed to complete the turn of the `CNPC`.

## GetPhysicalArmorMainValue

`NPC.GetPhysicalArmorMainValue(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the (main) white armor of the `CNPC`.

## GetTimeToFace

`NPC.GetTimeToFace(npc, target):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

source npc

**target**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the amount of time needed for the source `CNPC` to face the target `CNPC`.

## FindRotationAngle

`NPC.FindRotationAngle(npc, pos):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

source npc

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to find the rotation angle

Returns the rotation angle of the `CNPC`.

## GetTimeToFacePosition

`NPC.GetTimeToFacePosition(npc, pos):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

source npc

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

target position

Returns the amount of time needed for the source `CNPC` to face a specific position.

## FindFacingNPC

`NPC.FindFacingNPC(npc, ignoreNpc, [team_type], [angle], [distance]):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

source npc

**ignoreNpc**

[`CNPC`](/api-v2.0/game-components/core/npc)

ignore npc

**team\_type** `[?]`

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

team type `(default: TEAM_BOTH)`

**angle** `[?]`

`number`

max angle to check `(default: 0.0)`

**distance** `[?]`

`number`

max distance to check `(default: 0.0)`

Returns the `CNPC` that the source `CNPC` is currently facing.

## GetBaseSpeed

`NPC.GetBaseSpeed(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the base move speed of the `CNPC`.

## GetMoveSpeed

`NPC.GetMoveSpeed(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the move speed of the `CNPC`.

## GetMinDamage

`NPC.GetMinDamage(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the minumum attack damage of the `CNPC`.

## GetBonusDamage

`NPC.GetBonusDamage(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the bonus attack damage of the `CNPC`.

## GetTrueDamage

`NPC.GetTrueDamage(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the minumum attack damage + bonus damage of the `CNPC`.

## GetTrueMaximumDamage

`NPC.GetTrueMaximumDamage(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the maximum attack damage + bonus damage of the `CNPC`.

## GetItemByIndex

`NPC.GetItemByIndex(npc, index):` [`CItem`](/api-v2.0/game-components/core/item) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**index**

`integer`

item index

Returns the `CItem` by index.

## GetAbilityByIndex

`NPC.GetAbilityByIndex(npc, index):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**index**

`integer`

ability index

Returns the `CAbility` by index.

## GetAbilityByActivity

`NPC.GetAbilityByActivity(npc, activity):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to get ability from

**activity**

[`Enum.GameActivity`](/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity)

game activity

Returns the `CAbility` by game activity.

## GetAbility

`NPC.GetAbility(npc, name):` [`CAbility`](/api-v2.0/game-components/core/ability) | `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**name**

`string`

ability name

Returns the `CAbility` by name.

## HasAbility

`NPC.HasAbility(npc, name):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**name**

`string`

ability name

Returns `true` if the `CNPC` has this ability.

## GetMana

`NPC.GetMana(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the current mana of the `CNPC`.

## GetMaxMana

`NPC.GetMaxMana(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the maximum mana of the `CNPC`.

## GetManaRegen

`NPC.GetManaRegen(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the mana regeneration rate of the `CNPC`.

## GetHealthRegen

`NPC.GetHealthRegen(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the health regeneration rate of the `CNPC`.

## CalculateHealthRegen

Works for creeps but really slow.

`NPC.CalculateHealthRegen(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Iterate over all modifiers and returns the health regeneration rate of the `CNPC`.

## GetCurrentLevel

`NPC.GetCurrentLevel(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the current level of the `CNPC`.

## GetDayTimeVisionRange

`NPC.GetDayTimeVisionRange(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the day-time vision range of the `CNPC`.

## GetNightTimeVisionRange

`NPC.GetNightTimeVisionRange(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the night-time vision range of the `CNPC`.

## GetUnitName

`NPC.GetUnitName(npc):` `string`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the unit-name of the `CNPC`.

## GetHealthBarOffset

`NPC.GetHealthBarOffset(npc, [checkOverride]):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**checkOverride** `[?]`

`boolean`

returns override offset if it exists `(default: true)`

Returns the health bar offset of the `CNPC`.

## GetUnitNameIndex

index can change when new unit are added

`NPC.GetUnitNameIndex(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns unit-name index of the `CNPC`.

## GetAttachment

`NPC.GetAttachment(npc, name):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**name**

`string`

attachment name. e.g. "attach\_hitloc"

Returns the attachment position of the `CNPC` by the name.

#### Example

## GetAttachmentByIndex

`NPC.GetAttachmentByIndex(npc, index):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**index**

`integer`

attachment index

Returns the attachment position of the `CNPC` by the specified index.

## GetAttachmentIndexByName

`NPC.GetAttachmentIndexByName(npc, name):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

**name**

`string`

attachment name. e.g. "attach\_hitloc"

Returns the attachment index of the `CNPC` by the name.

## GetBountyXP

`NPC.GetBountyXP(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the amount of experience points (XP) you can earn for killing the `CNPC`.

## GetGoldBountyMin

`NPC.GetGoldBountyMin(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the minimum amount gold you can earn for killing the `CNPC`.

## GetGoldBountyMax

`NPC.GetGoldBountyMax(npc):` `integer`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

target npc

Returns the maximum amount gold you can earn for killing the `CNPC`.

## MoveTo

`NPC.MoveTo(npc, position, [queue], [show], [callback], [executeFast], [identifier], [force_minimap]):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The destination position.

**queue** `[?]`

`boolean`

Add the order to the Dota queue. `(default: false)`

**show** `[?]`

`boolean`

Show the order position. `(default: false)`

**callback** `[?]`

`boolean`

Push the order to the OnPrepareUnitOrders callback. `(default: false)`

**executeFast** `[?]`

`boolean`

Place the order at the top of the queue. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

**force\_minimap** `[?]`

`boolean`

If true, the order will be forced by the minimap if possible. `(default: true)`

Initiates an order for the `CNPC` to move to a specified position.

## SetZDelta

`NPC.SetZDelta(npc, z):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**z**

`number`

Z pos

Sets the Z position of the `CNPC` model.

## HasScepter

`NPC.HasScepter(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

Returns `true` if the `CNPC` has or consumed Aghanim Scepter.

## HasShard

`NPC.HasShard(npc):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

Returns `true` if the `CNPC` has or consumed Aghanim Shard.

## SequenceDuration

`NPC.SequenceDuration(npc, sequence):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**sequence**

`integer`

The sequence index.

Returns sequence duration of the npc with the specified sequence index.

## GetSecondsPerAttack

`NPC.GetSecondsPerAttack(npc, bIgnoreTempAttackSpeed):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**bIgnoreTempAttackSpeed**

`boolean`

Ignore temporary attack speed.

Returns the seconds per attack of the npc.

## GetBarriers

`NPC.GetBarriers(npc):` `{physical:{total:number, current:number}, magic:{total:number, current:number}, all:{total:number, current:number}}`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

Returns a table with information about the barriers of the `CNPC`.

## GetGlow

`NPC.GetGlow(npc):` `{m_bSuppressGlow:boolean, m_bFlashing:boolean, m_bGlowing:boolean, m_iGlowType:integer, r:integer, g:integer, b:integer}`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

Returns a table with information about the current glow effect of the `CNPC`.

## SetGlow

`NPC.SetGlow(npc, suppress_glow, flashing, glowing, glow_type, r, g, b):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**suppress\_glow**

`boolean`

suppress\_glow

**flashing**

`boolean`

flashing

**glowing**

`boolean`

glowing

**glow\_type**

`integer`

glow type

**r**

`integer`

r factor

**g**

`integer`

g factor

**b**

`integer`

b factor

Sets the `CNPC` glow effect.

## SetColor

`NPC.SetColor(npc, r, g, b):` `nil`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**r**

`integer`

r factor

**g**

`integer`

g factor

**b**

`integer`

b factor

Sets the `CNPC` model color.

## IsInRangeOfShop

`NPC.IsInRangeOfShop(npc, shop_type, [specific]):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**shop\_type**

[`Enum.ShopType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.shoptype)

Shop type to check.

**specific** `[?]`

`boolean`

No idea what is that. `(default: false)`

Checks if the `CNPC` is in range of a shop.

## GetBaseSpellAmp

`NPC.GetBaseSpellAmp(npc):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

Returns the base spell amplification of the `CNPC`.

## GetModifierProperty

`NPC.GetModifierProperty(npc, property):` `number`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**property**

[`Enum.ModifierFunction`](/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction)

Property enum.

Returns the property value for the `CNPC`.

## IsControllableByPlayer

`NPC.IsControllableByPlayer(npc, playerId):` `boolean`

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

npc to check

**playerId**

`integer`

player id

Returns `true` if npc is controllable by player.

## GetModifierPropertyHighest

Fixes the issue when you have multiple Kaya items that actually don't stack.

`NPC.GetModifierPropertyHighest(npc, property):` \*\*`number`\*\*

Name

Type

Description

**npc**

[`CNPC`](/api-v2.0/game-components/core/npc)

The target NPC.

**property**

[`Enum.ModifierFunction`](/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction)

Property enum.

Returns the hieghest property value for the `CNPC`.

[PreviousEntity](/api-v2.0/game-components/core/entity)[NextHero](/api-v2.0/game-components/core/hero)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/hero -->

Copy

# 🦸Hero

Table to work with `CHero`.

`CHero` extends `CNPC`

## GetCurrentXP

`Hero.GetCurrentXP(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the hero's current XP.

## GetAbilityPoints

`Hero.GetAbilityPoints(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the hero's available ability points.

## GetRespawnTime

Could be less than current game time if hero is already alive.

`Hero.GetRespawnTime(hero):` \*\*`number`\*\*

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the game time when the hero will respawn.

## GetRespawnTimePenalty

`Hero.GetRespawnTimePenalty(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the next respawn time penalty, e.g. buyback.

## GetPrimaryAttribute

`Hero.GetPrimaryAttribute(hero):` [`Enum.Attributes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the hero's primary attribute type.

## GetStrength

`Hero.GetStrength(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns `white` value of strength.

## GetAgility

`Hero.GetAgility(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns `white` value of agility.

## GetIntellect

`Hero.GetIntellect(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns `white` value of intellect.

## GetStrengthTotal

`Hero.GetStrengthTotal(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns total value of strength.

## GetAgilityTotal

`Hero.GetAgilityTotal(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns total value of agility.

## GetIntellectTotal

`Hero.GetIntellectTotal(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns total value of intellect.

## GetLastHurtTime

`Hero.GetLastHurtTime(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the time when the hero was last hurt.

## GetHurtAmount

`Hero.GetHurtAmount(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the amount of damage the hero last received.

## GetRecentDamage

`Hero.GetRecentDamage(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the damage taken by the hero in the last in ~1 second.

## GetPainFactor

`Hero.GetPainFactor(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the pain factor of the hero. Not sure what it is.

## GetTargetPainFactor

`Hero.GetTargetPainFactor(hero):` `number`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the pain factor of the hero's target. Not sure what it is.

## GetLifeState

`Hero.GetLifeState(hero):` `boolean`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns `true` if the hero is alive. Recommended to use `Entity.IsAlive` instead.

## GetPlayerID

`Hero.GetPlayerID(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the ID of the hero player.

## GetReplicatingOtherHeroModel

`Hero.GetReplicatingOtherHeroModel(hero):` [`CHero`](/api-v2.0/game-components/core/hero) | `nil`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

If the hero is an illusion, Arc's copy, Meepo clone, etc. returns the original hero, otherwise returns nil.

## TalentIsLearned

`Hero.TalentIsLearned(hero, talent):` `boolean`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

**talent**

[`Enum.TalentTypes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.talenttypes)

Returns `true` if talent is learned.

#### Example

## GetFacetAbilities

`Hero.GetFacetAbilities(hero):` [`CAbility[]`](/api-v2.0/game-components/core/ability)

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns facet ability array.

## GetFacetID

`Hero.GetFacetID(hero):` `integer`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns facet id. Start from 1.

## GetLastMaphackPos

`Hero.GetLastMaphackPos(hero):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | `nil`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the last hero pos from maphack.

## GetLastVisibleTime

`Hero.GetLastVisibleTime(hero):` `float` | `nil`

Name

Type

Description

**hero**

[`CHero`](/api-v2.0/game-components/core/hero)

Returns the last visible time from VBE.

[PreviousNPC](/api-v2.0/game-components/core/npc)[NextAbility](/api-v2.0/game-components/core/ability)

Last updated 1 month ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/ability -->

Copy

# 🌟Ability

Table to work with `CAbility`.

`CAbility` extends `CEntity`

## GetOwner

`Ability.GetOwner(ability):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability owner.

## IsBasic

`Ability.IsBasic(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is basic.

## IsUltimate

`Ability.IsUltimate(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is an ultimate.

## IsAttributes

`Ability.IsAttributes(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is an attribute or a talent.

## GetType

`Ability.GetType(ability):` [`Enum.AbilityTypes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitytypes)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability type.

## GetBehavior

`Ability.GetBehavior(ability, [from_static_data]):` [`Enum.AbilityBehavior`](/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitybehavior)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns the ability type.

## IsPassive

`Ability.IsPassive(ability, [from_static_data]):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns `true` if the ability is passive.

## GetTargetTeam

`Ability.GetTargetTeam(ability, [from_static_data]):` [`Enum.TargetTeam`](/api-v2.0/cheats-types-and-callbacks/enums#enum.targetteam)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns the target team of this Ability.

## GetTargetType

`Ability.GetTargetType(ability, [from_static_data]):` [`Enum.TargetType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.targettype)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns the target type of this Ability.

## GetTargetFlags

`Ability.GetTargetFlags(ability):` [`Enum.TargetFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.targetflags)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the target flags of this Ability.

## GetDamageType

`Ability.GetDamageType(ability):` [`Enum.DamageTypes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.damagetypes)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the damage type of this Ability.

## GetImmunityType

`Ability.GetImmunityType(ability, [from_static_data]):` [`Enum.ImmunityTypes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.immunitytypes)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns the immunity type of this Ability.

## GetDispellableType

`Ability.GetDispellableType(ability, [from_static_data]):` [`Enum.DispellableTypes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.dispellabletypes)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**from\_static\_data** `[?]`

`boolean`

if `true` will check from ability static data `(default: false)`

Returns the dispel type of this Ability.

## GetLevelSpecialValueFor

`Ability.GetLevelSpecialValueFor(ability, name, [lvl]):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**name**

`string`

Special value name. Can be found in the ability KV file. (`assets/data/npc_abilities.json`)

**lvl** `[?]`

`integer`

Ability level, if -1 will automatically get lvl. `(default: -1)`

WRONG API FIX ME IT MUST BE GetSpecialValueFor.

## IsReady

`Ability.IsReady(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is ready to use.

## SecondsSinceLastUse

`Ability.SecondsSinceLastUse(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the number of seconds passed from the last usage of the ability. Will return -1 if
the ability is not on the cooldown.

## GetDamage

`Ability.GetDamage(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability damage from assets/data/npc\_abilities.json field. Will return 0.0 if the
ability doesn't contain this field.

## GetLevel

`Ability.GetLevel(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the current ability level.

## GetCastPoint

`Ability.GetCastPoint(ability, [include_modifiers]):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**include\_modifiers** `[?]`

`boolean`

`(default: true)`

Gets the cast delay of this Ability.

## GetCastPointModifier

`Ability.GetCastPointModifier(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Gets the cast delay modifier of this Ability.

## IsCastable

`Ability.IsCastable(ability, [mana]):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**mana** `[?]`

`number`

`(default: 0.0)`

Returns `true` if the ability is currently castable. Checks for mana cost, cooldown, level,
and slot for items.

## IsChannelling

`Ability.IsChannelling(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is in channeling state. Example: teleport, rearm, powershot
etc.

## GetName

`Ability.GetName(ability):` `string`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability name or empty string.

## GetBaseName

`Ability.GetBaseName(ability):` `string`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability base name or empty string.

## IsInnate

`Ability.IsInnate(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is innate.

## IsInnatePassive

`Ability.IsInnatePassive(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is passive innate.

## GetMaxLevel

`Ability.GetMaxLevel(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns ability's max level.

## IsGrantedByFacet

`Ability.IsGrantedByFacet(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` when abiliti is granted by facet.

## CanBeExecuted

`Ability.CanBeExecuted(ability):` [`Enum.AbilityCastResult`](/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitycastresult)

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `-1` if ability can be executed.

## IsOwnersManaEnough

`Ability.IsOwnersManaEnough(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if enough mana for cast.

## CastNoTarget

`Ability.CastNoTarget(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**queue** `[?]`

`boolean`

Will add order to the cast queue. `(default: false)`

**push** `[?]`

`boolean`

Will push order to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

Will push order to start of the order's list. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

Casts the ability that doesn't require a target or position.

## CastPosition

`Ability.CastPosition(ability, pos, [queue], [push], [execute_fast], [identifier], [force_minimap]):` `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Order position.

**queue** `[?]`

`boolean`

Will add order to the cast queue. `(default: false)`

**push** `[?]`

`boolean`

Will push order to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

Will push order to start of the order's list. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

**force\_minimap** `[?]`

`boolean`

If true, the order will be forced by the minimap if possible. `(default: true)`

Casts the ability at a specified position.

## CastTarget

`Ability.CastTarget(ability, target, [queue], [push], [execute_fast], [identifier]):` `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**target**

[`CNPC`](/api-v2.0/game-components/core/npc)

Order target.

**queue** `[?]`

`boolean`

Will add order to the cast queue. `(default: false)`

**push** `[?]`

`boolean`

Will push order to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

Will push order to start of the order's list. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

Casts the ability on a specified target.

## Toggle

`Ability.Toggle(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**queue** `[?]`

`boolean`

Will add order to the cast queue. `(default: false)`

**push** `[?]`

`boolean`

Will push order to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

Will push order to start of the order's list. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

Toggles the ability. Example: Armlet.

## ToggleMod

`Ability.ToggleMod(ability, [queue], [push], [execute_fast], [identifier]):` `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

**queue** `[?]`

`boolean`

Will add order to the cast queue. `(default: false)`

**push** `[?]`

`boolean`

Will push order to the OnPrepareUnitOrders callback. `(default: false)`

**execute\_fast** `[?]`

`boolean`

Will push order to start of the order's list. `(default: false)`

**identifier** `[?]`

`string`

The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`

Toggles the ability modifier. Example: Frost Arrows, Medusa's Shield.

## GetDefaultName

`Ability.GetDefaultName(ability_name):` `string` | `nil`

Name

Type

Description

**ability\_name**

`string`

Returns the default ability icon name from items\_game.txt

## CanBeUpgraded

`Ability.CanBeUpgraded(ability):` [`Enum.AbilityLearnResult`](/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitylearnresult) | `nil`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns if the ability is upgradable with a specific reason.

## GetAbilityID

`Ability.GetAbilityID(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns ability id

## GetIndex

`Ability.GetIndex(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the index of the ability in the ability owner's list. The index can be used in
NPC.GetAbilityByIndex later.

## GetCastRange

`Ability.GetCastRange(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the cast range of the ability.

## IsHidden

`Ability.IsHidden(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if ability is hidden. Example: Zeus's Nimbus before purchasing agh.

## IsActivated

`Ability.IsActivated(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is in an activated state.

## GetDirtyButtons

`Ability.GetDirtyButtons(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns we don't know what :).

## GetToggleState

`Ability.GetToggleState(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns if the ability is toggled. Example: Medusa's Shield.

## IsInAbilityPhase

`Ability.IsInAbilityPhase(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is in the cast state. Examples: Nature's Prophet's Teleport,
Meepo's Poof.

## GetCooldown

`Ability.GetCooldown(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the amount of time before the ability can be cast.

## GetCooldownLength

`Ability.GetCooldownLength(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the amount of time the ability couldn't be cast after being used.

## GetManaCost

`Ability.GetManaCost(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the ability mana cost.

## GetAutoCastState

`Ability.GetAutoCastState(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the autocast state of the ability.

## GetAltCastState

`Ability.GetAltCastState(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the alt cast state of the ability. Example: Doom's Devour.

## GetChannelStartTime

`Ability.GetChannelStartTime(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the gametime the channeling of the ability will start. Requires the ability to be in
the cast state when called.

## GetCastStartTime

`Ability.GetCastStartTime(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the gametime the ability will be casted. Requires the ability to be in the cast state
when called.

## IsInIndefinateCooldown

`Ability.IsInIndefinateCooldown(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the cooldown of the ability is indefinite.

## IsInIndefinateCooldown

`Ability.IsInIndefinateCooldown(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the cooldown of the ability is frozen.

## GetOverrideCastPoint

`Ability.GetOverrideCastPoint(ability):` `number`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the overridden cast point. Example: Arcane Blink.

## IsStolen

`Ability.IsStolen(ability):` `boolean`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns `true` if the ability is stolen.

## GetCurrentCharges

`Ability.GetCurrentCharges(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the number of charges available.

## ChargeRestoreTimeRemaining

`Ability.ChargeRestoreTimeRemaining(ability):` `integer`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the remaining time for the next charge to restore.

## GetKeybind

`Ability.GetKeybind(ability):` `string`

Name

Type

Description

**ability**

[`CAbility`](/api-v2.0/game-components/core/ability)

Returns the keybind of the ability.

[PreviousHero](/api-v2.0/game-components/core/hero)[NextItem](/api-v2.0/game-components/core/item)

Last updated 1 month ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/item -->

Copy

# 🔑Item

Table to work with `CItem`.

`CItem` extends `CAbility`

## IsCombinable

`Item.IsCombinable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is combinable. I'm not sure if non-combinable items even exist.

## IsPermanent

`Item.IsPermanent(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is permanent. I'm not sure what permanent items is, but for items with stacks this function returns `false`.

## IsStackable

`Item.IsStackable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is stackable. e.g tangoes, wards, etc.

## IsRecipe

`Item.IsRecipe(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is recipe.

## GetSharability

`Item.GetSharability(item):` [`Enum.ShareAbility`](/api-v2.0/cheats-types-and-callbacks/enums#enum.shareability)

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns item's sharability type.

## IsDroppable

`Item.IsDroppable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is droppable.

## IsPurchasable

`Item.IsPurchasable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is purchasable.

## IsSellable

`Item.IsSellable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item is sellable.

## RequiresCharges

`Item.RequiresCharges(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if the item requires charges. e.g. urn, vessel etc.

## IsKillable

`Item.IsKillable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item is destroyable by autoatack.

## IsDisassemblable

`Item.IsDisassemblable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item is disassemblable.

## IsAlertable

`Item.IsAlertable(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item is alertable. e.g. smoke, mekansm, arcane boots etc.

## GetInitialCharges

`Item.GetInitialCharges(item):` `integer`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns initial charges of the item. e.g. 3 for bottle, 1 for dust etc.

## CastsOnPickup

`Item.CastsOnPickup(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

No idea what this function does.

## GetCurrentCharges

`Item.GetCurrentCharges(item):` `integer`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns amount of current charges.

## GetSecondaryCharges

`Item.GetSecondaryCharges(item):` `integer`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns amount of secondary charges. e.g. pack of both type of wards.

## IsCombineLocked

`Item.IsCombineLocked(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item locked for combining.

## IsMarkedForSell

`Item.IsMarkedForSell(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item is marked for sell.

## GetPurchaseTime

`Item.GetPurchaseTime(item):` `number`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns the game time when the item was purchased. If the item was assembled from other items, It returns the purchase time of the item that had the lowest
index at the moment of assembling.

## GetAssembledTime

`Item.GetAssembledTime(item):` `number`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns the game time when the item was assembled. If the item was not assembled, returns time when the item was purchased.

## PurchasedWhileDead

`Item.PurchasedWhileDead(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `true` if item was purchased while dead.

## CanBeUsedOutOfInventory

`Item.CanBeUsedOutOfInventory(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

No idea which specific item example could be used out of inventory.

## IsItemEnabled

`Item.IsItemEnabled(item):` `boolean`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns `false` if item has CD after moving from stash.

## GetEnableTime

Could be less than current game time if item is already enabled.

`Item.GetEnableTime(item):` `number`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns game time when item will be enabled.

## GetPlayerOwnerID

`Item.GetPlayerOwnerID(item):` `integer`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns player ID who owns the item.

## GetCost

`Item.GetCost(item):` `integer`

Name

Type

Description

**item**

[`CItem`](/api-v2.0/game-components/core/item)

Returns item cost.

## GetStockCount

Item id can be found in `assets/data/items.json` file in cheat folder.

`Item.GetStockCount(item\_id, [team]):` \*\*`integer`\*\*

Name

Type

Description

**item\_id**

`integer`

**team** `[?]`

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

- Optional. Default is local player's team. `(default: Enum.TeamNum.TEAM_RADIANT)`

Returns amount of remaining items in shop by item id.

#### Example

[PreviousAbility](/api-v2.0/game-components/core/ability)[NextRune](/api-v2.0/game-components/core/rune)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/rune -->

Copy

# 🔮Rune

Table to work with `CRune`.`CRune` extends `CEntity`

## GetRuneType

`Rune.GetRuneType(rune):` [`Enum.RuneType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.runetype)

Name

Type

Description

**rune**

[`CRune`](/api-v2.0/game-components/core/rune)

Returns `Enum.RuneType` the rune type.

[PreviousItem](/api-v2.0/game-components/core/item)[NextTower](/api-v2.0/game-components/core/tower)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tower -->

Copy

# 🏰Tower

Table to work with `CTower`.`CTower` extends `CNPC`

## GetAttackTarget

`Tower.GetAttackTarget(tower):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**tower**

[`CTower`](/api-v2.0/game-components/core/tower)

Returns `CNPC` that is attacked by the tower now.

[PreviousRune](/api-v2.0/game-components/core/rune)[NextTree](/api-v2.0/game-components/core/tree)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tree -->

Copy

# 🌳Tree

Table to work with `CTree`.`CTree` extends `CEntity`

## IsActive

`Tree.IsActive(tree):` `boolean`

Name

Type

Description

**tree**

[`CTree`](/api-v2.0/game-components/core/tree)

Returns if the tree is not cut.

[PreviousTower](/api-v2.0/game-components/core/tower)[NextVambrace](/api-v2.0/game-components/core/vambrace)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace -->

Copy

# 🔱Vambrace

Table to work with `CVambrace`.`CVambrace` extends `CItem`

## GetStats

`Vambrace.GetStats(vambrace):` [`Enum.Attributes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Name

Type

Description

**vambrace**

[`CVambrace`](/api-v2.0/game-components/core/vambrace)

Returns selected `Enum.Attributes` attribute.

[PreviousTree](/api-v2.0/game-components/core/tree)[NextCamp](/api-v2.0/game-components/core/camp)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/camp -->

Copy

# 🐉Camp

Table to work with `CCamp`.`CCamp` extends `CEntity`

## GetType

`Camp.GetType(camp):` `integer`

Name

Type

Description

**camp**

[`CCamp`](/api-v2.0/game-components/core/camp)

The camp to check.

Returns the camp type.

## GetCampBox

`Camp.GetCampBox(camp):` `{min:Vector, max:Vector}`

Name

Type

Description

**camp**

[`CCamp`](/api-v2.0/game-components/core/camp)

The camp to check.

Returns camp box as a table with **min** and **max** fields(**Vector**).

[PreviousVambrace](/api-v2.0/game-components/core/vambrace)[NextBottle](/api-v2.0/game-components/core/bottle)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/bottle -->

Copy

# 🍾Bottle

Table to work with `CBottle`.

`CBottle` extends `CItem`

## GetRuneType

`Bottle.GetRuneType(bottle):` [`Enum.RuneType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.runetype)

Name

Type

Description

**bottle**

[`CBottle`](/api-v2.0/game-components/core/bottle)

Returns the rune inside the bottle.

[PreviousCamp](/api-v2.0/game-components/core/camp)[NextCourier](/api-v2.0/game-components/core/courier)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/courier -->

Copy

# 🚚Courier

Table to work with `CCourier`.`CCourier` extends `CNPC`

## IsFlyingCourier

`Courier.IsFlyingCourier(courier):` `boolean`

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

The courier to check.

Returns `true` if the courier is flying.

## GetRespawnTime

`Courier.GetRespawnTime(courier):` `number`

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

The courier to check.

Returns the game time when the courier will respawn.

## GetCourierState

`Courier.GetCourierState(courier):` [`Enum.CourierState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.courierstate)

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

The courier to check.

Returns the courier state.

## GetPlayerID

`Courier.GetPlayerID(courier):` `integer`

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

The courier to check.

Returns owner's player id.

## GetCourierStateEntity

`Courier.GetCourierStateEntity(courier):` [`CEntity`](/api-v2.0/game-components/core/entity) | `nil`

Name

Type

Description

**courier**

[`CCourier`](/api-v2.0/game-components/core/courier)

The courier to check.

Returns the entity that the courier is currently interacting with.

[PreviousBottle](/api-v2.0/game-components/core/bottle)[NextDrunkenBrawler](/api-v2.0/game-components/core/drunkenbrawler)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler -->

Copy

# 🍻DrunkenBrawler

Table to work with `CDrunkenBrawler`.`CDrunkenBrawler` extends `CAbility`

## GetState

`DrunkenBrawler.GetState(ability):` [`Enum.DrunkenBrawlerState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drunkenbrawlerstate)

Name

Type

Description

**ability**

[`CDrunkenBrawler`](/api-v2.0/game-components/core/drunkenbrawler)

Returns the state of the CDrunkenBrawler ability.

[PreviousCourier](/api-v2.0/game-components/core/courier)[NextPhysicalItem](/api-v2.0/game-components/core/physicalitem)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem -->

Copy

# 📦PhysicalItem

Table to work with `CPhysicalItem`.`CPhysicalItem` extends `CEntity`

## GetItem

`PhysicalItem.GetItem(physical_item):` [`CItem`](/api-v2.0/game-components/core/item) | `nil`

Name

Type

Description

**physical\_item**

[`CPhysicalItem`](/api-v2.0/game-components/core/physicalitem)

Returns `CItem` object from `CPhysicalItem`.

[PreviousDrunkenBrawler](/api-v2.0/game-components/core/drunkenbrawler)[NextPowerTreads](/api-v2.0/game-components/core/powertreads)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads -->

Copy

# 👟PowerTreads

Table to work with `CPowerTreads`.`CTower` extends `CItem`

## GetStats

`PowerTreads.GetStats(power_tread):` [`Enum.Attributes`](/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Name

Type

Description

**power\_tread**

[`CPowerTreads`](/api-v2.0/game-components/core/powertreads)

Returns selected `Enum.Attributes` attribute.

[PreviousPhysicalItem](/api-v2.0/game-components/core/physicalitem)[NextTierToken](/api-v2.0/game-components/core/tiertoken)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken -->

Copy

# 🪙TierToken

Table to work with `CTierToken`.`CTierToken` extends `CItem`

## GetChoices

`TierToken.GetChoices(tier_token):` `integer[]`

Name

Type

Description

**tier\_token**

[`CTierToken`](/api-v2.0/game-components/core/tiertoken)

The `TierToken` to get the choices from.

Returns the choices (ability ids) of the `CTierToken`.

[PreviousPowerTreads](/api-v2.0/game-components/core/powertreads)[NextGame Engine](/api-v2.0/game-components/game-engine)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Game Engine

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine -->

Copy

# 🛠️Game Engine

[🔧Engine](/api-v2.0/game-components/game-engine/engine)[🎉Event](/api-v2.0/game-components/game-engine/event)[📜GameRules](/api-v2.0/game-components/game-engine/gamerules)[🌍GlobalVars](/api-v2.0/game-components/game-engine/globalvars)[🧭GridNav](/api-v2.0/game-components/game-engine/gridnav)[🎮Input](/api-v2.0/game-components/game-engine/input)[🌍World](/api-v2.0/game-components/game-engine/world)[🌫️FogOfWar](/api-v2.0/game-components/game-engine/fogofwar)[⚙️ConVar](/api-v2.0/game-components/game-engine/convar)

[PreviousTierToken](/api-v2.0/game-components/core/tiertoken)[NextEngine](/api-v2.0/game-components/game-engine/engine)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/engine -->

Copy

# 🔧Engine

Table to work with game engine.

## IsInGame

`Engine.IsInGame():` `boolean`

Returns `true` if the game is in progress.

## IsShopOpen

`Engine.IsShopOpen():` `boolean`

Returns `true` if the shop is open.

## SetQuickBuy

`Engine.SetQuickBuy(item_name, [reset]):` `nil`

Name

Type

Description

**item\_name**

`string`

The name of the item to quick buy. (e.g. `blink`, `relic`)

**reset** `[?]`

`boolean`

Reset the quick buy list. `(default: true)`

Add item to quick buy list.

## RunScript

`Engine.RunScript(script, [contextPanel]):` `boolean`

Name

Type

Description

**script**

`string`

The script to run.

**contextPanel** `[?]`

`string` | [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

The id of the panel or the panel itself to run the script in. `(default: "Dashboard")`

Run a JS script in the panorama context. Return `true` if the script was executed
successfully. [JS
documentation](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Panorama/Javascript)

#### Example

## ExecuteCommand

`Engine.ExecuteCommand(command):` `nil`

Name

Type

Description

**command**

`string`

The command to execute.

Execute a console command.

#### Example

## PlayVol

`Engine.PlayVol(sound, [volume]):` `nil`

Name

Type

Description

**sound**

`string`

The sound to play. Could find in `sounds` folder in `pak01_dir.vpk` file.

**volume** `[?]`

`number`

The volume of the sound. `(default: 0.1)`

Play a sound with a specific volume.

#### Example

## CreateConfig

`Engine.CreateConfig(config_name, categories):` `nil`

Name

Type

Description

**config\_name**

`string`

The name of the config.

**categories**

`{name: string, hero_ids: integer[], x: number, y: number, width: number, height: number}[]`

Creates a new hero grid config.

#### Example

## GetCurrentConfigName

`Engine.GetCurrentConfigName():` `string`

Returns the current hero grid config name

## SetNewGridConfig

`Engine.SetNewGridConfig(config_name):` `nil`

Name

Type

Description

**config\_name**

`string`

The name of the config to set

Set the new hero grid config by name

## LookAt

`Engine.LookAt(x, y):` `nil`

Name

Type

Description

**x**

`number`

**y**

`number`

Move camera to a specific position.

## CanAcceptMatch

`Engine.CanAcceptMatch():` `boolean`

Returns `true` if the player can accept the match.

## GetGameDirectory

`Engine.GetGameDirectory():` `string`

Returns the current game directory. (e.g. `dota 2 beta`)

## GetCheatDirectory

`Engine.GetCheatDirectory():` `string`

Returns the current cheat directory.

## GetLevelName

`Engine.GetLevelName():` `string`

Returns the current level name. (e.g. `maps/hero_demo_main.vpk`)

## GetLevelNameShort

`Engine.GetLevelNameShort():` `string`

Returns the current level name without the extension and folder. (e.g. `hero_demo_main`)

## AcceptMatch

`Engine.AcceptMatch(state):` `nil`

Name

Type

Description

**state**

`integer`

DOTALobbyReadyState

Accept match.

## ConsoleColorPrintf

`Engine.ConsoleColorPrintf(r, g, b, [a], text):` `nil`

Name

Type

Description

**r**

`integer`

Red value.

**g**

`integer`

Green value.

**b**

`integer`

Blue value.

**a** `[?]`

`integer`

Alpha value. `(default: 255)`

**text**

`string`

Text to print.

Print a message to the dota console.

## GetMMR

`Engine.GetMMR():` `integer`

Returns the current MMR.

## GetMMRV2

`Engine.GetMMRV2():` `integer`

Returns the current MMR. Works better than `Engine.GetMMR`.
Must be called from the game thread. Ex: OnNetUpdateEx, OnGCMessage, not OnFrame or on
initialization.

## ReloadScriptSystem

`Engine.ReloadScriptSystem():` `nil`

Executes script system reload.

## ShowDotaWindow

`Engine.ShowDotaWindow():` `nil`

Brings the game window to the forefront if it is minimized.
Use this function to make the game window the topmost window.

## IsInLobby

`Engine.IsInLobby():` `boolean`

Returns `true` if the player is in a lobby.

## GetBuildVersion

`Engine.GetBuildVersion():` `string`

Returns the cheat version.

## GetHeroIDByName

`Engine.GetHeroIDByName(unitName):` `integer` | `nil`

Name

Type

Description

**unitName**

`string`

Can be retrieved from `NPC.GetUnitName`

Returns hero ID by unit name.

#### Example

## GetDisplayNameByUnitName

`Engine.GetDisplayNameByUnitName(unitName):` `string` | `nil`

Name

Type

Description

**unitName**

`string`

Can be retrieved from `NPC.GetUnitName`

Returns hero display name by unit name.

#### Example

## GetHeroNameByID

`Engine.GetHeroNameByID(heroID):` `string` | `nil`

Name

Type

Description

**heroID**

`integer`

Returns hero name by ID.

## GetUIState

`Engine.GetUIState():` [`Enum.UIState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.uistate)

Returns current UI state.

[PreviousGame Engine](/api-v2.0/game-components/game-engine)[NextEvent](/api-v2.0/game-components/game-engine/event)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event -->

Copy

# 🎉Event

Table to work with game events.

When you install events, you send the subscribe message to the server, which is potentially unsafe.
Therefore, you won't be able to install new listeners when you have unsafe features disabled in the Settings -> Security tab.

The list of events can be found in the "pak01\_dir.vpk" under "resource/game.gameevents."

## AddListener

`Event.AddListener(name):` `nil`

Name

Type

Description

**name**

`string`

Event name

Installs an event listener for the desired event.

## IsReliable

`Event.IsReliable(event):` `boolean`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

Checks if the event is reliable.

## IsLocal

`Event.IsLocal(event):` `boolean`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

Checks if the event is local or networked.

## IsEmpty

`Event.IsEmpty(event):` `boolean`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

Checks if the event is empty.

## GetBool

`Event.GetBool(event, field):` `boolean`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

**field**

`string`

Field name

Returns the boolean value of the specified event field.

## GetInt

`Event.GetInt(event, field):` `integer`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

**field**

`string`

Field name

Returns the integer value of the specified event field.

## GetUint64

`Event.GetUint64(event, field):` `integer`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

**field**

`string`

Field name

Returns the uint64 value of the specified event field.

## GetFloat

`Event.GetFloat(event, field):` `number`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

**field**

`string`

Field name

Returns the floating value of the specified event field.

## GetString

`Event.GetString(event, field):` `string`

Name

Type

Description

**event**

[`CEvent`](/api-v2.0/game-components/game-engine/event)

**field**

`string`

Field name

Returns the string value of the specified event field.

[PreviousEngine](/api-v2.0/game-components/game-engine/engine)[NextGameRules](/api-v2.0/game-components/game-engine/gamerules)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gamerules -->

Copy

# 📜GameRules

Table to work with GameRules.

## GetServerGameState

`GameRules.GetServerGameState():` [`Enum.GameState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current server game state.

## GetGameState

`GameRules.GetGameState():` [`Enum.GameState`](/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current game state.

## GetGameMode

`GameRules.GetGameMode():` [`Enum.GameMode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.gamemode)

Returns the current game mode.

## GetPreGameStartTime

Pregame time is the time before the game starts, e.g. ban phase, pick time.

`GameRules.GetPreGameStartTime():` `number`

Returns pregame duration or 0 if now is pregame time.

## GetGameStartTime

Game start time is 0:00 on ingame timer.

`GameRules.GetGameStartTime():` `number`

Returns game start time duration or 0 if game is not start yet.

## GetGameEndTime

`GameRules.GetGameEndTime():` `number`

Returns game end time or 0 if game is not end yet.

## GetGameLoadTime

`GameRules.GetGameLoadTime():` `number`

No idea what this function does. Returns 0 in all cases what I've tested.

## GetGameTime

Can be used to calculate time in an in-game timer. See the example.

`GameRules.GetGameTime():` `number`

Returns the current game time. Starts counting from pregame state.

#### Example

## IsPaused

`GameRules.IsPaused():` `boolean`

Returns `true` if game is paused.

## IsTemporaryDay

Example: Phoenix's Supernova.

`GameRules.IsTemporaryDay():` `boolean`

Returns `true` if it's temporary day.

## IsTemporaryNight

Example: Luna's Eclipse.

`GameRules.IsTemporaryNight():` `boolean`

Returns `true` if it's temporary night.

## IsNightstalkerNight

`GameRules.IsNightstalkerNight():` `boolean`

Returns `true` if it's nightstalker's night.

## GetMatchID

`GameRules.GetMatchID():` `integer`

Returns current match id.

## GetLobbyID

`GameRules.GetLobbyID():` `integer`

Returns current lobby id.

## GetGoodGlyphCD

Could be less than current game time if glyph is already available.

`GameRules.GetGoodGlyphCD():` `number`

Returns game time when next radiant glyph will be available.

## GetBadGlyphCD

Could be less than current game time if glyph is already available.

`GameRules.GetBadGlyphCD():` `number`

Returns game time when next dire glyph will be available.

## GetGoodScanCD

Could be less than current game time if scan is already available.

`GameRules.GetGoodScanCD():` `number`

Returns game time when next radiant scan will be available.

## GetBadScanCD

Could be less than current game time if scan is already available.

`GameRules.GetBadScanCD():` `number`

Returns game time when next dire scan will be available.

## GetGoodScanCharges

`GameRules.GetGoodScanCharges():` `integer`

Returns current radiant scan charges.

## GetGoodScanCharges

`GameRules.GetGoodScanCharges():` `integer`

Returns current dire scan charges.

## GetStockCount

Item id can be found in `assets/data/items.json` file in cheat folder.

`GameRules.GetStockCount(item\_id, [team]):` \*\*`integer`\*\*

Name

Type

Description

**item\_id**

`integer`

**team** `[?]`

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

- Optional. Default is local player's team. `(default: Enum.TeamNum.TEAM_RADIANT)`

Returns amount of remaining items in shop by item id.

#### Example

## GetNextCycleTime

`GameRules.GetNextCycleTime():` `number`, `boolean`

Return time remaining to the next cycle.

## GetDaytimeStart

`GameRules.GetDaytimeStart():` `number`

Returns day start time. To work with it use `GameRules.GetTimeOfDay`

## GetNighttimeStart

`GameRules.GetNighttimeStart():` `number`

Returns night start time. To work with it use `GameRules.GetTimeOfDay`

## GetTimeOfDay

`GameRules.GetTimeOfDay():` `number`

Returns current time of day time.

## IsInBanPhase

`GameRules.IsInBanPhase():` `boolean`

Returns `true` if game is in ban phase.

## GetAllDraftPhase

`GameRules.GetAllDraftPhase():` `integer`

Returns index of the current draft phase.

## IsAllDraftPhaseRadiantFirst

`GameRules.IsAllDraftPhaseRadiantFirst():` `boolean`

Returns `true` if Radiant picks first.

## GetDOTATime

`GameRules.GetDOTATime([pregame], [negative]):` `number`

Name

Type

Description

**pregame** `[?]`

`boolean`

If `true` includes pregame time. `(default: false)`

**negative** `[?]`

`boolean`

If `true` includes negative time. `(default: false)`

Returns the actual DOTA in-game clock time.

## GetLobbyObjectJson

`GameRules.GetLobbyObjectJson():` `string` | `nil`

Returns CSODOTALobby protobuf object as JSON string.

## GetBannedHeroes

`GameRules.GetBannedHeroes():` `integer[]` | `nil`

Returns zero-based array of banned heroes where index corresponds to the player id.

## GetStateTransitionTime

`GameRules.GetStateTransitionTime():` `number`

Returns time remaining between state changes.

[PreviousEvent](/api-v2.0/game-components/game-engine/event)[NextGlobalVars](/api-v2.0/game-components/game-engine/globalvars)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/globalvars -->

Copy

# 🌍GlobalVars

Talbe to work with game's global variables.

## GetFrameCount

`GlobalVars.GetFrameCount():` `integer`

Returns absolute frame counter. Continues to increase even if game is paused.

## GetAbsFrameTime

`GlobalVars.GetAbsFrameTime():` `number`

Returns absolute frame time.

## GetAbsFrameTimeDev

`GlobalVars.GetAbsFrameTimeDev():` `number`

Returns absolute frame time. No idea what's the difference between this and `GetAbsFrameTime`.

## GetMapName

`GlobalVars.GetMapName():` `string`

Returns full name of the current map. For example, "maps/dota.vpk" or "maps/hero\_demo\_main.vpk".

## GetMapGroupName

`GlobalVars.GetMapGroupName():` `string`

Returns short name of the current map. For example, "dota" or "hero\_demo\_main".

## GetCurTime

`GlobalVars.GetCurTime():` `number`

TODO

## GetServerTick

`GlobalVars.GetServerTick():` `integer`

TODO

## GetIntervalPerTick

`GlobalVars.GetIntervalPerTick():` `number`

TODO

[PreviousGameRules](/api-v2.0/game-components/game-engine/gamerules)[NextGridNav](/api-v2.0/game-components/game-engine/gridnav)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gridnav -->

Copy

# 🧭GridNav

Table to work with in-game navigation API.

## CreateNpcMap

You should always call `GridNav.ReleaseNpcMap` after you done with your build pathing

`GridNav.CreateNpcMap([excluded\_npcs], [includeTempTrees], [customCollisionSizes]):` [\*\*`GridNavNpcMap`\*\*](GridNavNpcMap.md)

Name

Type

Description

**excluded\_npcs** `[?]`

[`CEntity[]`](/api-v2.0/game-components/core/entity) | `nil`

table with npc to exclude from the map. for example you want to exclude local hero if you build path from local hero position `(default: nil)`

**includeTempTrees** `[?]`

`boolean`

`true` if you want include temp trees to the map e.g. furion's 1st spell, iron branch `(default: true)`

**customCollisionSizes** `[?]`

`table` | `nil`

table where key is entity userdata and value is {left, top, right, bottom} offsets from entity position `(default: nil)`

Creates a new `GridNavNpcMap`

## ReleaseNpcMap

`GridNav.ReleaseNpcMap(npc_map):` `nil`

Name

Type

Description

**npc\_map**

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md)

map to release to release

Releases allocated memory for `GridNavNpcMap`

## IsTraversable

`GridNav.IsTraversable(pos, [flag]):` `boolean`, `integer`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

**flag** `[?]`

`number`

flag to check `(default: 1)`

Returns `true` if the world position is traversable.

## BuildPath

`GridNav.BuildPath(start, end_, [ignoreTrees], [npc_map]):` [`Vector[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**start**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to start

**end\_**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to end

**ignoreTrees** `[?]`

`boolean`

`true` if you want to exclude static trees from the pathing `(default: false)`

**npc\_map** `[?]`

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) | `nil`

map with the npc's positions which works as additional mask for terrain map `(default: nil)`

Build path from start to end. Returns an array with builded positions.

#### Example

## IsTraversableFromTo

`GridNav.IsTraversableFromTo(start, end_, [ignoreTrees], [npc_map]):` `boolean`

Name

Type

Description

**start**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to start

**end\_**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to end

**ignoreTrees** `[?]`

`boolean`

`true` if you want to exclude static trees from the pathing `(default: false)`

**npc\_map** `[?]`

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) | `nil`

map with the npc's positions which works as additional mask for terrain map `(default: nil)`

Lite version of GridNav.BuildPath function which just cheking if the path is exists.

## DebugRender

`GridNav.DebugRender([grid_range], [npc_map], [render_cell_flags]):` `boolean`

Name

Type

Description

**grid\_range** `[?]`

`integer`

grid radius in "cell units" from Vector(0,0,0) `(default: 50)`

**npc\_map** `[?]`

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) | `nil`

map with the npc's positions which works as additional mask for terrain map `(default: nil)`

**render\_cell\_flags** `[?]`

`boolean`

render the flags value for each not approachable cell (don't think you ever want to see this numbers, so ignore this arg) `(default: false)`

Debug render of current GridNav with GridNavNpcMap (if provided)

[PreviousGlobalVars](/api-v2.0/game-components/game-engine/globalvars)[NextInput](/api-v2.0/game-components/game-engine/input)

Last updated 6 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/input -->

Copy

# 🎮Input

Table to work with input system.

## GetWorldCursorPos

`Input.GetWorldCursorPos():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world cursor position.

## GetCursorPos

`Input.GetCursorPos():` `number`, `number`

Returns screen cursor position (x, y). See example.

#### Example

Copy

```
local x, y =	Input.GetCursorPos()
```

## IsCursorInRect

`Input.IsCursorInRect(x, y, w, h):` `boolean`

Name

Type

Description

**x**

`number`

x position

**y**

`number`

**w**

`number`

width

**h**

`number`

height

Returns `true` if cursor is in rect.

## IsCursorInBounds

`Input.IsCursorInBounds(x0, y0, x1, y1):` `boolean`

Name

Type

Description

**x0**

`number`

**y0**

`number`

**x1**

`number`

**y1**

`number`

Returns `true` if cursor is in bounds.

## GetNearestUnitToCursor

Excludes not visible, illusions and dead units.

`Input.GetNearestUnitToCursor(teamNum, teamType):` [`CNPC`](/api-v2.0/game-components/core/npc) | `nil`

Name

Type

Description

**teamNum**

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

team number. Could be get from `Entity.GetTeamNum`

**teamType**

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

team type to search relative to teamNum param

Returns nearest unit to cursor.

## GetNearestHeroToCursor

Excludes not visible, illusions and dead heroes.

`Input.GetNearestHeroToCursor(teamNum, teamType):` [`CHero`](/api-v2.0/game-components/core/hero) | `nil`

Name

Type

Description

**teamNum**

[`Enum.TeamNum`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

team number. Could be get from `Entity.GetTeamNum`

**teamType**

[`Enum.TeamType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype)

team type to search relative to teamNum param

Returns nearest hero to cursor.

## IsInputCaptured

`Input.IsInputCaptured():` `boolean`

Returns `true` if input is captured. e.g. opened console, chat, shop.

## IsKeyDown

`Input.IsKeyDown(KeyCode):` `boolean`

Name

Type

Description

**KeyCode**

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Returns `true` if key is down.

## IsKeyDownOnce

This function will return `true` only once per key press.

`Input.IsKeyDownOnce(KeyCode):` \*\*`boolean`\*\*

Name

Type

Description

**KeyCode**

[`Enum.ButtonCode`](/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Return `true` if key is down once.

[PreviousGridNav](/api-v2.0/game-components/game-engine/gridnav)[NextWorld](/api-v2.0/game-components/game-engine/world)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/world -->

Copy

# 🌍World

Table containing functions for interacting with the world.

## GetGroundZ

`World.GetGroundZ(x, y):` `number`

Name

Type

Description

**x**

`number`

The X position to get the ground Z from.

**y**

`number`

The Y position to get the ground Z from.

Returns the ground Z at the given position.

[PreviousInput](/api-v2.0/game-components/game-engine/input)[NextFogOfWar](/api-v2.0/game-components/game-engine/fogofwar)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/fogofwar -->

Copy

# 🌫️FogOfWar

Table to work with FogOfWar API.

## IsPointVisible

`FogOfWar.IsPointVisible(pos):` `boolean`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

Returns `true` if the world position is visible.

[PreviousWorld](/api-v2.0/game-components/game-engine/world)[NextConVar](/api-v2.0/game-components/game-engine/convar)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar -->

Copy

# ⚙️ConVar

Table to work with `CConVars`.
ConVars are game variable that can be used to retrieve or change some game engine settings.

## Find

`ConVar.Find(name):` [`CConVar`](/api-v2.0/game-components/game-engine/convar) | `nil`

Name

Type

Description

**name**

`string`

Returns the found ConVar.

#### Example

Copy

```
local convar = ConVar.Find("dota_camera_distance")
local camera_distance = ConVar.GetFloat(convar)
```

## GetString

`ConVar.GetString(convar):` `string`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

Returns string value of the Convar

## GetInt

`ConVar.GetInt(convar):` `integer`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

Returns int value of the Convar

## GetFloat

`ConVar.GetFloat(convar):` `number`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

Returns float value of the Convar

## GetBool

`ConVar.GetBool(convar):` `boolean`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

Returns boolean value of the Convar

## SetString

`ConVar.SetString(convar, value):` `nil`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

**value**

`string`

Assigns new string value to the ConVar

## SetInt

`ConVar.SetInt(convar, value):` `nil`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

**value**

`integer`

Assigns new int value to the ConVar

## SetFloat

`ConVar.SetFloat(convar, value):` `nil`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

**value**

`number`

Assigns new float value to the ConVar

## SetBool

`ConVar.SetBool(convar, value):` `nil`

Name

Type

Description

**convar**

[`CConVar`](/api-v2.0/game-components/game-engine/convar)

**value**

`boolean`

Assigns new boolean value to the ConVar

[PreviousFogOfWar](/api-v2.0/game-components/game-engine/fogofwar)[NextNetworking & APIs](/api-v2.0/game-components/networking-and-apis)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Networking and APIs

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis -->

Copy

# 🌐Networking & APIs

[💬Chat](/api-v2.0/game-components/networking-and-apis/chatapi)[🌐HTTP](/api-v2.0/game-components/networking-and-apis/http)[🚂Steam](/api-v2.0/game-components/networking-and-apis/steamapi)[📡NetChannel](/api-v2.0/game-components/networking-and-apis/netchannel)[🌐Game Coordinator](/api-v2.0/game-components/networking-and-apis/gc)

[PreviousConVar](/api-v2.0/game-components/game-engine/convar)[NextChat](/api-v2.0/game-components/networking-and-apis/chatapi)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi -->

Copy

# 💬Chat

Table to work with chat.

## GetChannels

`Chat.GetChannels():` `string[]`

Returns an array of channel names.

## Print

`Chat.Print(channel, text):` `nil`

Name

Type

Description

**channel**

`string`

The channel name to say the message in.

**text**

`string`

The message to say.

Print a message in a channel. This message will not be sent to the server.

## Say

`Chat.Say(channel, text):` `nil`

Name

Type

Description

**channel**

`string`

The channel name to say the message in.

**text**

`string`

The message to say.

Say a message in a channel.

## Flip

`Chat.Flip(channel):` `nil`

Name

Type

Description

**channel**

`string`

The channel name to flip the coin in.

Flip the coin in a channel.

## Roll

`Chat.Roll(channel, [min], [max]):` `nil`

Name

Type

Description

**channel**

`string`

The channel name to roll the dice in.

**min** `[?]`

`number`

The minimum number to roll. `(default: 0)`

**max** `[?]`

`number`

The maximum number to roll. `(default: 100)`

Roll a dice in a channel.

[PreviousNetworking & APIs](/api-v2.0/game-components/networking-and-apis)[NextHTTP](/api-v2.0/game-components/networking-and-apis/http)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http -->

Copy

# 🌐HTTP

Table to work with HTTP requests.

## Request

`HTTP.Request(method, url, [data], callback, [param]):` `boolean`

Name

Type

Description

**method**

`string`

HTTP method

**url**

`string`

URL

**data** `[?]`

`{headers:table<string>, cookies:string` | `table<string>, data:string` | `table<string>, timeout:number}`

data to send `(default: {})`

**callback**

`fun(tbl: {response: string, code: string, header: string, param: string}):nil`

callback function to call when request is done. Take 1 argument - response data table, see example.

**param** `[?]`

`string`

string parameter to pass to callback function to identify request `(default: "")`

Do HTTP request. Returns `true` if request was sent successfully.

#### Example

Copy

```
-- http_request.lua
local url = "https://reqres.in/api/users/2";

local headers = {
    ["User-Agent"] = "Umbrella/1.0",
    ['Connection'] = 'Keep-Alive',
}

local JSON = require('assets.JSON')
local callback = function(response)
    Log.Write(response["response"]);
    Log.Write(response["code"]);
    Log.Write(response["header"]);
    Log.Write(response["param"]);

    local json = JSON:decode(response["response"]);
    Log.Write(json["data"]["email"]);
end

HTTP.Request("GET", url, { 
		headers = headers,
	}, callback, "reqres_get");
```

[PreviousChat](/api-v2.0/game-components/networking-and-apis/chatapi)[NextSteam](/api-v2.0/game-components/networking-and-apis/steamapi)

Last updated 7 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi -->

Copy

# 🚂Steam

Table to with Steam API functions

## SetPersonaName

`Steam.SetPersonaName(name):` `nil`

Name

Type

Description

**name**

`string`

The name to set

Sets the player name, stores it on the server and publishes the changes to all friends who
are online.

## GetPersonaName

`Steam.GetPersonaName():` `string`

Returns the local players name. This is the same name as on the users community profile page.

## GetGameLanguage

`Steam.GetGameLanguage():` `string`

Returns the current game language.

## GetProfilePictureBySteamId

This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.

`Steam.GetProfilePictureBySteamId(steamID64, [large]):` `integer`

Name

Type

Description

**steamID64**

`integer`

The Steam ID of the player

**large** `[?]`

`boolean`

Whether to get the large profile picture `(default: false)`

Returns the handle of the profile picture of the given Steam ID.

## GetProfilePictureByAccountId

This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.

`Steam.GetProfilePictureByAccountId(steamID64, [large]):` \*\*`integer`\*\*

Name

Type

Description

**steamID64**

`integer`

The account id of the player

**large** `[?]`

`boolean`

Whether to get the large profile picture `(default: false)`

Returns the handle of the profile picture of the given account id.

[PreviousHTTP](/api-v2.0/game-components/networking-and-apis/http)[NextNetChannel](/api-v2.0/game-components/networking-and-apis/netchannel)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel -->

Copy

# 📡NetChannel

Table to work with game's net channel.

## GetLatency

`NetChannel.GetLatency([flow]):` `number`

Name

Type

Description

**flow** `[?]`

[`Enum.Flow`](/api-v2.0/cheats-types-and-callbacks/enums#enum.flow)

flow to get latency of `(default: Enum.Flow.FLOW_OUTGOING)`

Returns the latency/ping of the net channel in seconds.

## GetAvgLatency

`NetChannel.GetAvgLatency([flow]):` `number`

Name

Type

Description

**flow** `[?]`

[`Enum.Flow`](/api-v2.0/cheats-types-and-callbacks/enums#enum.flow)

flow to get average latency of `(default: Enum.Flow.FLOW_OUTGOING)`

Returns the average latency/ping of the net channel in seconds.

## SendNetMessage

You can repeat the same message from OnSendNetMessage if you want to know the format of the message.

`NetChannel.SendNetMessage(name, json):` \*\*`nil`\*\*

Name

Type

Description

**name**

`string`

name of the net message

**json**

`string`

json of the net message

Sends a protobuff message to the game server. [List of messages](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs),

#### Example

[PreviousSteam](/api-v2.0/game-components/networking-and-apis/steamapi)[NextGame Coordinator](/api-v2.0/game-components/networking-and-apis/gc)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/gc -->

Copy

# 🌐Game Coordinator

Table to work with Game Coordinator (GC).

Possible message types and message bodies could be found at [here](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs)
Message type id starts with `k_E` prefix, for example `k_EMsgGCMatchmakingStatsRequest = 7197;`.
Message body starts with with `C` prefix instead of "k\_E", for example `message CMsgDOTAMatchmakingStatsRequest {}`.

## SendMessage

`GC.SendMessage(msg, msg_type, msg_size):` `nil`

Name

Type

Description

**msg**

`userdata`

Pointer to protobuf message buffer.

**msg\_type**

`integer`

Protobuf message type ID.

**msg\_size**

`integer`

Size of the protobuf message.

Sends protobuff message to game coordinator. Response will be received in `OnGCMessage` callback.

#### Example

Copy

```
local protobuf = require('protobuf')
local JSON = require('assets.JSON')
local request = protobuf.encodeFromJSON('CMsgDOTAMatchmakingStatsRequest',
	                JSON:encode({}));
GC.SendMessage( request.binary, 7197, request.size )
```

## GetSteamID

`GC.GetSteamID():` `string`

Returns local player Steam ID as string.

[PreviousNetChannel](/api-v2.0/game-components/networking-and-apis/netchannel)[NextRendering & Visuals](/api-v2.0/game-components/rendering-and-visuals)

Last updated 8 months ago


--------------------------------------------------------------------------------

## Rendering and Visuals

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals -->

Copy

# 🎨Rendering & Visuals

[✨Particle](/api-v2.0/game-components/rendering-and-visuals/particle)[🖌️Renderer](/api-v2.0/game-components/rendering-and-visuals/renderv1)[🎨Render](/api-v2.0/game-components/rendering-and-visuals/renderv2)[🗺️MiniMap](/api-v2.0/game-components/rendering-and-visuals/minimap)[🖼️Panorama](/api-v2.0/game-components/rendering-and-visuals/panorama)

[PreviousGame Coordinator](/api-v2.0/game-components/networking-and-apis/gc)[NextParticle](/api-v2.0/game-components/rendering-and-visuals/particle)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle -->

Copy

# ✨Particle

Table to work with particles.

## Create

`Particle.Create(particle, [attach_type], [entity]):` `integer`

Name

Type

Description

**particle**

`string`

Particle path

**attach\_type** `[?]`

[`Enum.ParticleAttachment`](/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

attach\_type Attach type `(default: Enum.ParticleAttachment.PATTACH_WORLDORIGIN)`

**entity** `[?]`

[`CEntity`](/api-v2.0/game-components/core/entity)

Entity to own of the particle. If not specified, the local hero will be used. `(default: Players.GetLocal())`

Creates a particle and returns its index.

## SetControlPoint

`Particle.SetControlPoint(particle_index, control_point, value):` `nil`

Name

Type

Description

**particle\_index**

`integer`

Particle index

**control\_point**

`integer`

Control point

**value**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Control point value

Sets the control point value of a particle.

## SetShouldDraw

`Particle.SetShouldDraw(particle_index, value):` `nil`

Name

Type

Description

**particle\_index**

`integer`

Particle index

**value**

`bool`

set value

Enables or disables the drawing of a particle.

## SetControlPointEnt

`Particle.SetControlPointEnt(particle_index, control_point, entity, attach_type, attach_name, position, lock_orientation):` `nil`

Name

Type

Description

**particle\_index**

`integer`

Particle index

**control\_point**

`integer`

Control point

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Entity to attach

**attach\_type**

[`Enum.ParticleAttachment`](/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

Attach type

**attach\_name**

`string` | `nil`

Attach name. See `NPC.GetAttachment` function

**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Control point position

**lock\_orientation**

`boolean`

Lock orientation. No idea what it does

Sets the control point entity value of a particle.

## SetParticleControlTransform

`Particle.SetParticleControlTransform(particle_index, control_point, position, angle):` `nil`

Name

Type

Description

**particle\_index**

`integer`

Particle index

**control\_point**

`integer`

Control point

**position**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Control point position

**angle**

[`Angle`](/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Control point angle

Sets the control point's position and angle.

## Destroy

`Particle.Destroy(particle_index):` `nil`

Name

Type

Description

**particle\_index**

`integer`

Particle index

Destroys the particle by index.

[PreviousRendering & Visuals](/api-v2.0/game-components/rendering-and-visuals)[NextRenderer](/api-v2.0/game-components/rendering-and-visuals/renderv1)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1 -->

Copy

# 🖌️Renderer

Table to work with renderer.

## SetDrawColor

`Renderer.SetDrawColor([r], [g], [b], [a]):` `nil`

Name

Type

Description

**r** `[?]`

`integer`

Red color. `(default: 255)`

**g** `[?]`

`integer`

Green color. `(default: 255)`

**b** `[?]`

`integer`

Blue color. `(default: 255)`

**a** `[?]`

`integer`

Alpha color. `(default: 255)`

Sets the color of the renderer.

## DrawLine

`Renderer.DrawLine(x0, y0, x1, y1):` `nil`

Name

Type

Description

**x0**

`integer`

X coordinate of the first point.

**y0**

`integer`

Y coordinate of the first point.

**x1**

`integer`

X coordinate of the second point.

**y1**

`integer`

Y coordinate of the second point.

Draws a line.

## DrawPolyLine

`Renderer.DrawPolyLine(points):` `nil`

Name

Type

Description

**points**

`table`

Table of points.

Draws a polyline.

## DrawPolyLineFilled

`Renderer.DrawPolyLineFilled(points):` `nil`

Name

Type

Description

**points**

`table`

Table of points.

Draws a filled polyline.

## DrawFilledRect

`Renderer.DrawFilledRect(x, y, w, h):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the rectangle.

**y**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

Draws a filled rectangle.

## DrawOutlineRect

`Renderer.DrawOutlineRect(x, y, w, h):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the rectangle.

**y**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

Draws an outlined rectangle.

## DrawOutlineCircle

`Renderer.DrawOutlineCircle(x, y, r, s):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the circle.

**y**

`integer`

Y coordinate of the circle.

**r**

`integer`

Radius of the circle.

**s**

`integer`

Segments of the circle.

Draws an outlined circle.

## DrawFilledCircle

`Renderer.DrawFilledCircle(x, y, r):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the circle.

**y**

`integer`

Y coordinate of the circle.

**r**

`integer`

Radius of the circle.

Draws a filled circle.

## DrawOutlineRoundedRect

`Renderer.DrawOutlineRoundedRect(x, y, w, h, radius):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the rectangle.

**y**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

**radius**

`integer`

Radius of the rectangle.

Draws an outlined rounded rectangle.

## DrawFilledRoundedRect

`Renderer.DrawFilledRoundedRect(x, y, w, h, radius):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the rectangle.

**y**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

**radius**

`integer`

Radius of the rectangle.

Draws a filled rounded rectangle.

## DrawOutlineTriangle

`Renderer.DrawOutlineTriangle(points):` `nil`

Name

Type

Description

**points**

`table`

Table of points.

Draws an outlined triangle.

## DrawFilledTriangle

`Renderer.DrawFilledTriangle(points):` `nil`

Name

Type

Description

**points**

`table`

Table of points.

Draws a filled triangle.

## DrawTexturedPolygon

`Renderer.DrawTexturedPolygon(points, texture):` `nil`

Name

Type

Description

**points**

`table`

Table of points.

**texture**

`integer`

Texture handle.

Draws a textured polygon.

## LoadFont

`Renderer.LoadFont(name, size, flags, weight):` `integer`

Name

Type

Description

**name**

`string`

Name of the font.

**size**

`integer`

Size of the font.

**flags**

`integer`

Font flags.

**weight**

`integer`

Font weight.

Loads a font.

## DrawText

`Renderer.DrawText(font, x, y, text):` `nil`

Name

Type

Description

**font**

`integer`

Font handle.

**x**

`integer`

X coordinate of the text.

**y**

`integer`

Y coordinate of the text.

**text**

`string`

Text to draw.

Draws a text.

## WorldToScreen

`Renderer.WorldToScreen(pos):` `integer`, `integer`, `boolean`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

World coordinates.

Converts world coordinates to screen coordinates. Returns x, y and visible.

## GetScreenSize

`Renderer.GetScreenSize():` `integer`, `integer`

Returns screen size.

## GetTextSize

`Renderer.GetTextSize(font, text):` `integer`, `integer`

Name

Type

Description

**font**

`integer`

Font handle.

**text**

`string`

Text to measure.

Returns text size.

## LoadImage

`Renderer.LoadImage(path):` `integer`

Name

Type

Description

**path**

`string`

Path to the image.

Loads an image. Returns image handle.

## DrawImage

`Renderer.DrawImage(handle, x, y, w, h):` `nil`

Name

Type

Description

**handle**

`integer`

Image handle.

**x**

`integer`

X coordinate of the image.

**y**

`integer`

Y coordinate of the image.

**w**

`integer`

Width of the image.

**h**

`integer`

Height of the image.

Draws an image.

## DrawImageCentered

`Renderer.DrawImageCentered(handle, x, y, w, h):` `nil`

Name

Type

Description

**handle**

`integer`

Image handle.

**x**

`integer`

X coordinate of the image.

**y**

`integer`

Y coordinate of the image.

**w**

`integer`

Width of the image.

**h**

`integer`

Height of the image.

Draws an image centered.

## GetImageSize

`Renderer.GetImageSize(handle):` `integer`, `integer`

Name

Type

Description

**handle**

`integer`

Image handle.

Returns image size.

## DrawFilledRectFade

`Renderer.DrawFilledRectFade(x0, y0, x1, y1, alpha0, alpha1, bHorizontal):` `nil`

Name

Type

Description

**x0**

`integer`

X coordinate of the rectangle.

**y0**

`integer`

Y coordinate of the rectangle.

**x1**

`integer`

X coordinate of the rectangle.

**y1**

`integer`

Y coordinate of the rectangle.

**alpha0**

`integer`

Alpha of the first point.

**alpha1**

`integer`

Alpha of the second point.

**bHorizontal**

`boolean`

Horizontal fade.

Draws a filled rectangle with fade.

## DrawFilledGradRect

`Renderer.DrawFilledGradRect(x0, y0, x1, y1, r, g, b, a, r2, g2, b2, a2, bHorizontal):` `nil`

Name

Type

Description

**x0**

`integer`

X coordinate of the rectangle.

**y0**

`integer`

Y coordinate of the rectangle.

**x1**

`integer`

X coordinate of the rectangle.

**y1**

`integer`

Y coordinate of the rectangle.

**r**

`integer`

Red color of the first point.

**g**

`integer`

Green color of the first point.

**b**

`integer`

Blue color of the first point.

**a**

`integer`

Alpha color of the first point.

**r2**

`integer`

Red color of the second point.

**g2**

`integer`

Green color of the second point.

**b2**

`integer`

Blue color of the second point.

**a2**

`integer`

Alpha color of the second point.

**bHorizontal**

`boolean`

Horizontal gradient.

Draws a filled gradient rectangle.

## DrawGlow

`Renderer.DrawGlow(x0, y0, w, h, thickness, obj_rounding):` `nil`

Name

Type

Description

**x0**

`integer`

X coordinate of the rectangle.

**y0**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

**thickness**

`integer`

Thickness of the glow.

**obj\_rounding**

`integer`

Rounding of the glow.

Draws a glow.

## DrawBlur

`Renderer.DrawBlur(x0, y0, w, h, strength, rounding, alpha):` `nil`

Name

Type

Description

**x0**

`number`

X coordinate of the rectangle.

**y0**

`number`

Y coordinate of the rectangle.

**w**

`number`

Width of the rectangle.

**h**

`number`

Height of the rectangle.

**strength**

`number`

Strength of the blur.

**rounding**

`number`

Rounding of the blur.

**alpha**

`number`

Alpha of the blur.

Draws a blur.

## PushClip

`Renderer.PushClip(x, y, w, h, intersect):` `nil`

Name

Type

Description

**x**

`integer`

X coordinate of the rectangle.

**y**

`integer`

Y coordinate of the rectangle.

**w**

`integer`

Width of the rectangle.

**h**

`integer`

Height of the rectangle.

**intersect**

`boolean`

Intersect with the previous clip.

Pushes a clip rect.

## PopClip

`Renderer.PopClip():` `nil`

Pops a clip rect.

## DrawCenteredNotification

`Renderer.DrawCenteredNotification(text, duration):` `nil`

Name

Type

Description

**text**

`string`

Text to draw.

**duration**

`number`

Duration of the notification.

Draws a centered notification.

[PreviousParticle](/api-v2.0/game-components/rendering-and-visuals/particle)[NextRender](/api-v2.0/game-components/rendering-and-visuals/renderv2)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2 -->

Copy

# 🎨Render

Table to work with render v2.

## FilledRect

`Render.FilledRect(start, end_, color, [rounding], [flags]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the rectangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the rectangle.

**rounding** `[?]`

`number`

The rounding radius of the rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

Draws a filled rectangle.

## Rect

`Render.Rect(start, end_, color, [rounding], [flags], [thickness]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the rectangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the rectangle's border.

**rounding** `[?]`

`number`

The rounding radius of the rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

**thickness** `[?]`

`number`

The thickness of the rectangle's border. `(default: 1.0)`

Draws an unfilled rectangle.

## RoundedProgressRect

`Render.RoundedProgressRect(start, end_, color, percent, rounding, [thickness]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the rectangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the rectangle.

**percent**

`number`

The percentage of the rectangle to fill [0..1].

**rounding**

`number`

The rounding radius of the rectangle corners.

**thickness** `[?]`

`number`

The thickness of the rectangle's border. `(default: 1.0)`

Draw a progress rectangle.

## Line

`Render.Line(start, end_, color, [thickness]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the line.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the line.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the line.

**thickness** `[?]`

`number`

The thickness of the line. `(default: 1.0)`

Draws a line between two points.

## PolyLine

`Render.PolyLine(points, color, [thickness]):` `nil`

Name

Type

Description

**points**

[`Vec2[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

A table of Vec2 points to connect with lines.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the polyline.

**thickness** `[?]`

`number`

The thickness of the polyline. `(default: 1.0)`

Draws a series of connected lines (polyline).

## Circle

`Render.Circle(pos, radius, color, [thickness], [startDeg], [percentage], [rounded], [segments]):` `nil`

Name

Type

Description

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center position of the circle.

**radius**

`number`

The radius of the circle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the circle.

**thickness** `[?]`

`number`

The thickness of the circle's outline. `(default: 1.0)`

**startDeg** `[?]`

`number`

The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)`

**percentage** `[?]`

`number`

The percentage of the circle to draw, in the range [0.0-1.0]. `(default: 1.0)`

**rounded** `[?]`

`boolean`

Whether the circle is rounded. `(default: false)`

**segments** `[?]`

`integer`

The number of segments used for drawing the circle. `(default: 32)`

Draws a circle.

## FilledCircle

`Render.FilledCircle(pos, radius, color, [startDeg], [percentage], [segments]):` `nil`

Name

Type

Description

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center position of the circle.

**radius**

`number`

The radius of the circle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the circle.

**startDeg** `[?]`

`number`

The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)`

**percentage** `[?]`

`number`

The percentage of the circle to draw, in the range [0.0-1.0]. `(default: 1.0)`

**segments** `[?]`

`integer`

The number of segments used for drawing the circle. `(default: 32)`

Draws a filled circle.

## CircleGradient

`Render.CircleGradient(pos, radius, colorOuter, colorInner, [startDeg], [percentage]):` `nil`

Name

Type

Description

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center position of the circle.

**radius**

`number`

The radius of the circle.

**colorOuter**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The outer color of the gradient.

**colorInner**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The inner color of the gradient.

**startDeg** `[?]`

`number`

The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)`

**percentage** `[?]`

`number`

The percentage of the circle to draw, in the range [0.0-1.0]. `(default: 1.0)`

Draws a circle with a gradient.

## Triangle

`Render.Triangle(points, color, [thickness]):` `nil`

Name

Type

Description

**points**

[`Vec2[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

A table of three Vec2 points defining the vertices of the triangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the triangle's outline.

**thickness** `[?]`

`number`

The thickness of the triangle's outline. `(default: 1.0)`

Draws a triangle outline.

## FilledTriangle

`Render.FilledTriangle(points, color):` `nil`

Name

Type

Description

**points**

[`Vec2[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

A table of three Vec2 points defining the vertices of the triangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the triangle.

Draws a filled triangle.

## TexturedPoly

`Render.TexturedPoly(points, textureHandle, color, [grayscale]):` `nil`

Name

Type

Description

**points**

[`Vertex[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

A table of Vertex points defining the vertices of the polygon. Each Vertex contains a position (Vec2) and a texture coordinate (Vec2).

**textureHandle**

`integer`

The handle to the texture to be applied to the polygon.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color to apply over the texture. This can be used to tint the texture.

**grayscale** `[?]`

`number`

The grayscale of the image. `(default: 0.0)`

Draws a textured polygon.

## LoadFont

`Render.LoadFont(fontName, [fontFlag], [weight]):` `integer`

Name

Type

Description

**fontName**

`string`

The name of the font to load.

**fontFlag** `[?]`

[`Enum.FontCreate`](/api-v2.0/cheats-types-and-callbacks/enums#enum.fontcreate) | `integer`

Flags for font creation, such as antialiasing. `(default: Enum.FontCreate.FONTFLAG_NONE)`

**weight** `[?]`

`integer`

The weight (thickness) of the font. Typically, 0 means default weight. `(default: 400)`

Loads a font and returns its handle. Returns handle to the loaded font.

## Text

`Render.Text(font, fontSize, text, pos, color):` `nil`

Name

Type

Description

**font**

`integer`

The handle to the font used for drawing the text.

**fontSize**

`number`

The size of the font.

**text**

`string`

The text to be drawn.

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The position where the text will be drawn.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the text.

Draws text at a specified position.

## WorldToScreen

`Render.WorldToScreen(pos):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2), `boolean`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The 3D world position to be converted.

Converts a 3D world position to a 2D screen position. Returns A Vec2 representing the 2D screen position and a boolean indicating visibility on the screen.

#### Example

## ScreenSize

`Render.ScreenSize():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Retrieves the current screen size, returning it as a Vec2 where x is the width and y is the height of the screen.

## TextSize

`Render.TextSize(font, fontSize, text):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Name

Type

Description

**font**

`integer`

The handle to the font used for measuring the text.

**fontSize**

`number`

The size of the font.

**text**

`string`

The text to measure.

Calculates the size of the given text using the specified font, returning the size as a Vec2 where x is the width and y is the height of the text.

## LoadImage

`Render.LoadImage(path):` `integer`

Name

Type

Description

**path**

`string`

Path to the image.

Loads an image and returns its handle.

## Image

`Render.Image(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

The handle to the image.

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The position to draw the image.

**size**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The size of the image.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color to tint the image.

**rounding** `[?]`

`number`

The rounding radius of the image corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

**uvMin** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})`

**uvMax** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})`

**grayscale** `[?]`

`number`

The grayscale of the image. `(default: 0.0)`

Draws an image at a specified position and size.

## ImageCentered

`Render.ImageCentered(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` `nil`

Name

Type

Description

**imageHandle**

`integer`

The handle to the image.

**pos**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center position to draw the image.

**size**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The size of the image.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color to tint the image.

**rounding** `[?]`

`number`

The rounding radius of the image corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

**uvMin** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})`

**uvMax** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})`

**grayscale** `[?]`

`number`

The grayscale of the image. `(default: 0.0)`

Draws an image centered at a specified position and size.

## ImageSize

`Render.ImageSize(imageHandle):` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Name

Type

Description

**imageHandle**

`integer`

The handle to the image.

Retrieves the size of an image. Returns the size of the image as a Vec2.

## OutlineGradient

`Render.OutlineGradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags], [thickness]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the gradient rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the gradient rectangle.

**topLeft**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the top-left corner.

**topRight**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the top-right corner.

**bottomLeft**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the bottom-left corner.

**bottomRight**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the bottom-right corner.

**rounding** `[?]`

`number`

The rounding radius of the rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

**thickness** `[?]`

`number`

The thickness of the outline. `(default: 1.0)`

Draws a outlined gradient rectangle.

## Gradient

`Render.Gradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the gradient rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the gradient rectangle.

**topLeft**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the top-left corner.

**topRight**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the top-right corner.

**bottomLeft**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the bottom-left corner.

**bottomRight**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the bottom-right corner.

**rounding** `[?]`

`number`

The rounding radius of the rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing. `(default: Enum.DrawFlags.None)`

Draws a filled gradient rectangle.

## Shadow

`Render.Shadow(start, end_, color, thickness, [obj_rounding], [flags], [offset]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the shadow rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the shadow rectangle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the shadow.

**thickness**

`number`

The thickness of the shadow.

**obj\_rounding** `[?]`

`number`

The rounding radius of the shadow rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The offset of the shadow from the original rectangle. `(default: {0.0, 0.0})`

Draws a shadow effect within a specified rectangular area.

## ShadowCircle

`Render.ShadowCircle(center, radius, color, thickness, [num_segments], [flags], [offset]):` `nil`

Name

Type

Description

**center**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center point of the circle.

**radius**

`number`

The radius of the circle.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the shadow.

**thickness**

`number`

The thickness of the shadow.

**num\_segments** `[?]`

`integer`

The number of segments for drawing the circle. `(default: 12)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The offset of the shadow from the circle. `(default: {0.0, 0.0})`

Draws a circle shadow effect.

## ShadowConvexPoly

`Render.ShadowConvexPoly(points, color, thickness, [flags], [offset]):` `nil`

Name

Type

Description

**points**

[`Vec2[]`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Table of Vec2 points defining the convex polygon. Should be more than 2 points.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the shadow.

**thickness**

`number`

The thickness of the shadow.

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The offset of the shadow from the polygon. `(default: {0.0, 0.0})`

Draws a shadow convex polygon effect.

## ShadowNGon

`Render.ShadowNGon(center, radius, color, thickness, num_segments, [flags], [offset]):` `nil`

Name

Type

Description

**center**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The center point of the n-gon.

**radius**

`number`

The radius of the n-gon.

**color**

[`Color`](/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the shadow.

**thickness**

`number`

The thickness of the shadow.

**num\_segments**

`integer`

The number of segments (sides) of the n-gon.

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)`

**offset** `[?]`

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The offset of the shadow from the n-gon. `(default: {0.0, 0.0})`

Draws a shadow n-gon (polygon with n sides) effect.

## Blur

`Render.Blur(start, end_, [strength], [alpha], [rounding], [flags]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the blur rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the blur rectangle.

**strength** `[?]`

`number`

The strength of the blur effect. `(default: 1.0)`

**alpha** `[?]`

`number`

The alpha value of the blur effect. `(default: 1.0)`

**rounding** `[?]`

`number`

The rounding radius of the blur rectangle corners. `(default: 0.0)`

**flags** `[?]`

[`Enum.DrawFlags`](/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for the blur effect. `(default: Enum.DrawFlags.None)`

Applies a blur effect within a specified rectangular area.

## PushClip

`Render.PushClip(start, end_, [intersect]):` `nil`

Name

Type

Description

**start**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the clipping rectangle.

**end\_**

[`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The ending point of the clipping rectangle.

**intersect** `[?]`

`boolean`

If true, the new clipping area is intersected with the current clipping area. `(default: false)`

Begins a new clipping region. Only the rendering within the specified rectangular area will be displayed.

## PopClip

`Render.PopClip():` `nil`

Ends the most recently begun clipping region, restoring the previous clipping region.

## StartRotation

`Render.StartRotation(angle):` `nil`

Name

Type

Description

**angle**

`number`

The rotation angle.

Begins a new rotation.

## StopRotation

`Render.StopRotation():` `nil`

End the rotation.

## SetGlobalAlpha

Do not forget to reset the global alpha value after your rendering.

`Render.SetGlobalAlpha(alpha):` \*\*`nil`\*\*

Name

Type

Description

**alpha**

`number`

The alpha value to set [0..1]

Set the global alpha value for rendering.

## ResetGlobalAlpha

`Render.ResetGlobalAlpha():` `nil`

Reset the global alpha value for rendering to 1.0.

[PreviousRenderer](/api-v2.0/game-components/rendering-and-visuals/renderv1)[NextMiniMap](/api-v2.0/game-components/rendering-and-visuals/minimap)

Last updated 2 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/minimap -->

Copy

# 🗺️MiniMap

Table to work with in-game minimap.

## Ping

`MiniMap.Ping(pos, type):` `nil`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to ping

**type**

[`Enum.PingType`](/api-v2.0/cheats-types-and-callbacks/enums#enum.pingtype)

ping type

Pings on the minimap.

## SendLine

`MiniMap.SendLine(pos, initial, clientside):` `nil`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to draw line to

**initial**

`boolean`

start a new line, otherwise continue the last one

**clientside**

`boolean`

draw only for local player

Draws a line on the minimap.

## SendLine

`MiniMap.SendLine(x, y, initial, clientside):` `nil`

Name

Type

Description

**x**

`number`

x world position to draw line

**y**

`number`

y world position to draw line

**initial**

`boolean`

start a new line, otherwise continue the last one

**clientside**

`boolean`

draw only for local player

Draws a line on the minimap.

## DrawCircle

`MiniMap.DrawCircle(pos, [r], [g], [b], [a], [size]):` `nil`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to draw circle

**r** `[?]`

`integer`

red color `(default: 255)`

**g** `[?]`

`integer`

green color `(default: 255)`

**b** `[?]`

`integer`

blue color `(default: 255)`

**a** `[?]`

`integer`

alpha color `(default: 255)`

**size** `[?]`

`number`

circle size `(default: 800)`

Draws a circle on the minimap.

## DrawHeroIcon

`MiniMap.DrawHeroIcon(unitName, pos, [r], [g], [b], [a], [size]):` `nil`

Name

Type

Description

**unitName**

`string`

unit name to draw icon. Can get it from `NPC.GetUnitName`

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to draw icon

**r** `[?]`

`integer`

red color `(default: 255)`

**g** `[?]`

`integer`

green color `(default: 255)`

**b** `[?]`

`integer`

blue color `(default: 255)`

**a** `[?]`

`integer`

alpha color `(default: 255)`

**size** `[?]`

`number`

icon size `(default: 800)`

Draws a hero icon on the minimap.

## DrawIconByName

`MiniMap.DrawIconByName(iconName, pos, [r], [g], [b], [a], [size]):` `nil`

Name

Type

Description

**iconName**

`string`

could get it from game\dota\pak01\_dir.vpk (scripts\mod\_textures.txt).

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

world position to draw icon

**r** `[?]`

`integer`

red color `(default: 255)`

**g** `[?]`

`integer`

green color `(default: 255)`

**b** `[?]`

`integer`

blue color `(default: 255)`

**a** `[?]`

`integer`

alpha color `(default: 255)`

**size** `[?]`

`number`

icon size `(default: 800)`

Draws a icon on the minimap.

## GetMousePosInWorld

`MiniMap.GetMousePosInWorld():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world position the mouse on the minimap, if the mouse is not on the minimap, it will return (0,0,0).

## IsCursorOnMinimap

`MiniMap.IsCursorOnMinimap():` `boolean`

Returns `true` if the mouse is on the minimap.

## GetMinimapToWorld

`MiniMap.GetMinimapToWorld(ScreenX, ScreenY):` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Name

Type

Description

**ScreenX**

`integer`

**ScreenY**

`integer`

Returns world position from minimap position. The same as `GetMousePosInWorld`, but you can pass any position on screen, not only mouse position.

[PreviousRender](/api-v2.0/game-components/rendering-and-visuals/renderv2)[NextPanorama](/api-v2.0/game-components/rendering-and-visuals/panorama)

Last updated 8 months ago


--------------------------------------------------------------------------------

### Rendering - Panorama UI

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama -->

Copy

# 🖼️Panorama

[🖼️Panorama](/api-v2.0/game-components/rendering-and-visuals/panorama/panorama)[🖼️UIPanel](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

[PreviousMiniMap](/api-v2.0/game-components/rendering-and-visuals/minimap)[NextPanorama](/api-v2.0/game-components/rendering-and-visuals/panorama/panorama)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama -->

Copy

# 🖼️Panorama

Table to work with Dota Panorama system.

## GetPanelInfo

`Panorama.GetPanelInfo(path, [bLogError], [useJsFunc]):` `{x:number, y:number, w:number, h:number}`

Name

Type

Description

**path**

`string[]`

Path to the panel.

**bLogError** `[?]`

`boolean` | `nil`

`(default: false)`

**useJsFunc** `[?]`

`boolean` | `nil`

Use js GetPositionWithinWindow function to get position. `(default: false)`

Get panel info. GetPanelByName for first argument then FindChild others and accumulate x and y.

## GetPanelByPath

`Panorama.GetPanelByPath(path, [bLogError]):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**path**

`string[]`

Path to the panel.

**bLogError** `[?]`

`boolean`

Log error if panel not found. `(default: false)`

Get panel by path.

## GetPanelByName

`Panorama.GetPanelByName(id, is_type_name):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**id**

`string`

Id of the panel.

**is\_type\_name**

`boolean`

Check type name instead of names.

Get panel by id.

## CreatePanel

`Panorama.CreatePanel(type, id, parent, classes, styles):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

Name

Type

Description

**type**

`string`

panel type to create

**id**

`string` | `nil`

id of the panel

**parent**

[`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

parent panel

**classes**

`string` | `nil`

space separated classes to add

**styles**

`string` | `nil`

styles to set

Creates a new panorama panel

#### Example

[PreviousPanorama](/api-v2.0/game-components/rendering-and-visuals/panorama)[NextUIPanel](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel -->

Copy

# 🖼️UIPanel

UIPanel metatable

## \_\_tostring

`:__tostring():` `nil`

## \_\_eq

Overload for operator ==.

`:__eq(other):` `boolean`

Name

Type

Description

**other**

[`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

## FindChild

`:FindChild(id):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**id**

`string`

id of the child.

Finds child by name.

## IsVisible

`:IsVisible():` `boolean`

Returns visible state.

## SetVisible

`:SetVisible(newState):` `nil`

Name

Type

Description

**newState**

`boolean`

Sets visible state.

## GetClassList

`:GetClassList():` `string[]`

Returns class name list.

## FindChildInLayoutFile

`:FindChildInLayoutFile(id):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**id**

`string`

???.

## FindPanelInLayoutFile

`:FindPanelInLayoutFile(id):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**id**

`string`

???.

## FindChildTraverse

`:FindChildTraverse(id):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**id**

`string`

Recursive find child by id.

## GetChildCount

`:GetChildCount():` `integer`

Returns child by count.

## GetChild

`:GetChild(index):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**index**

`number`

Returns child by index.

## GetChildByPath

`:GetChildByPath(path, [bLogError]):` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Name

Type

Description

**path**

`string[]`

**bLogError** `[?]`

`boolean`

Log error if panel not found. `(default: false)`

Returns child by path using FindChild.

## GetChildIndex

`:GetChildIndex():` `integer`

Returns index in parent children list. Starts from 0.

## GetFirstChild

`:GetFirstChild():` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Returns first child.

## GetLastChild

`:GetLastChild():` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Returns last child.

## HasID

`:HasID():` `boolean`

Returns `true` if the panel has an id.

## GetID

`:GetID():` `string`

Returns id of panel.

## SetID

`:SetID(id):` `nil`

Name

Type

Description

**id**

`string`

Sets the panel's id.

## GetLayoutHeight

`:GetLayoutHeight():` `integer`

Returns the panel height.

## GetLayoutWidth

`:GetLayoutWidth():` `integer`

Returns the panel width.

## GetParent

`:GetParent():` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Returns the panel's parent.

## GetRootParent

`:GetRootParent():` [`UIPanel`](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | `nil`

Returns the panel's root parent. ???

## GetXOffset

`:GetXOffset():` `integer`

Returns the panel's relative X offset.

## GetYOffset

`:GetYOffset():` `integer`

Returns the panel's relative Y offset.

## GetBounds

`:GetBounds([useJsFunc]):` `{x:number, y:number, w:number, h:number}`

Name

Type

Description

**useJsFunc** `[?]`

`boolean` | `nil`

Use js GetPositionWithinWindow function to get position. `(default: false)`

Returns the panel's bounds. Iterate over the parent hierarchy to get the absolute bounds.

## GetImageSrc

`:GetImageSrc():` `string`

Return the panel source image.

## GetPanelType

`:GetPanelType():` `string`

Returns the panel's type.

## BSetProperty

`:BSetProperty(key, value):` `boolean`

Name

Type

Description

**key**

`string`

**value**

`string`

Sets the panel property.

## SetStyle

`:SetStyle(cssString):` `boolean`

Name

Type

Description

**cssString**

`string`

Sets the panel style.

#### Example

## SetAttribute

`:SetAttribute(key, value):` `nil`

Name

Type

Description

**key**

`string`

**value**

`string`

Sets the panel's attribute.

## GetAttribute

`:GetAttribute(key, default):` `string` | `nil`

Name

Type

Description

**key**

`string`

**default**

`string`

Returns the panel's attribute.

## GetPositionWithinWindow

`:GetPositionWithinWindow():` [`Vec2`](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns the panel's window position. Not sure about optimization.

## GetText

This method is only available for Label panels.

`:GetText():` `string`

Returns the label panel's text.

## SetText

This method is only available for Label panels.

`:SetText(text):` `nil`

Name

Type

Description

**text**

`string`

Sets the label panel's text.

## GetTextType

This method is only available for Label panels.

`:GetTextType():` `integer`

Gets the label panel's text type. (2 = plain, 3 = html)

## SetTextType

This method is only available for Label panels.

`:SetTextType(new):` \*\*`nil`\*\*

Name

Type

Description

**new**

`integer`

value

Sets the label panel's text type. (2 = plain, 3 = html). Should always set text type before setting the text

#### Example

## IsValid

`:IsValid():` `boolean`

Checks if the panel is valid

## HasClass

`:HasClass(className):` `boolean`

Name

Type

Description

**className**

`string`

Class name.

Checks if the panel has a class.

## AddClasses

`:AddClasses(classNames):` `nil`

Name

Type

Description

**classNames**

`string`

Could be a space separated list of classes.

Adds a class to the panel.

## RemoveClasses

`:RemoveClasses(classNames):` `nil`

Name

Type

Description

**classNames**

`string`

Could be a space separated list of classes.

Removes a class to the panel.

[PreviousPanorama](/api-v2.0/game-components/rendering-and-visuals/panorama/panorama)[NextConfiguration & Utilities](/api-v2.0/game-components/configuration-and-utilities)

Last updated 4 months ago


--------------------------------------------------------------------------------

## Configuration and Utilities

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities -->

Copy

# 📁Configuration & Utilities

[⚒️Config](/api-v2.0/game-components/configuration-and-utilities/config)[🤖Humanizer](/api-v2.0/game-components/configuration-and-utilities/humanizer)[📓Log](/api-v2.0/game-components/configuration-and-utilities/log)[🗣️Localizer](/api-v2.0/game-components/configuration-and-utilities/localizer)[📝GameLocalizer](/api-v2.0/game-components/configuration-and-utilities/gamelocalizer)

[PreviousUIPanel](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)[NextConfig](/api-v2.0/game-components/configuration-and-utilities/config)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config -->

Copy

# ⚒️Config

Table to work with configs that are stored in the `configs` folder with the `.ini` extention.

## ReadInt

`Config.ReadInt(config, key, [def]):` `integer`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to read.

**def** `[?]`

`integer`

The default value to return if the key is not found. `(default: 0)`

Read an integer from a config file.

## ReadFloat

`Config.ReadFloat(config, key, [def]):` `number`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to read.

**def** `[?]`

`number`

The default value to return if the key is not found. `(default: 0.0)`

Read a float from a config file.

## ReadString

`Config.ReadString(config, key, [def]):` `string`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to read.

**def** `[?]`

`string`

The default value to return if the key is not found. `(default: "")`

Read a string from a config file.

## WriteInt

`Config.WriteInt(config, key, value):` `nil`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to write.

**value**

`integer`

The value to write.

Write an integer to a config file.

## WriteFloat

`Config.WriteFloat(config, key, value):` `nil`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to write.

**value**

`number`

The value to write.

Write a float to a config file.

## WriteString

`Config.WriteString(config, key, value):` `nil`

Name

Type

Description

**config**

`string`

The config file name.

**key**

`string`

The key to write.

**value**

`string`

The value to write.

Write a string to a config file.

[PreviousConfiguration & Utilities](/api-v2.0/game-components/configuration-and-utilities)[NextHumanizer](/api-v2.0/game-components/configuration-and-utilities/humanizer)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer -->

Copy

# 🤖Humanizer

Table to work with humanizer.

## IsInServerCameraBounds

`Humanizer.IsInServerCameraBounds(pos):` `boolean`

Name

Type

Description

**pos**

[`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

Returns `true` if the world position is in server camera bounds.

## GetServerCameraPos

`Humanizer.GetServerCameraPos():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns server camera position.

## GetClientCameraPos

`Humanizer.GetClientCameraPos():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns client camera position.

## GetServerCursorPos

`Humanizer.GetServerCursorPos():` [`Vector`](/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the server cursor position.

## GetOrderQueue

`Humanizer.GetOrderQueue():` `{player: CPlayer, orderType: Enum.UnitOrder, targetIndex: integer, position: Vector, abilityIndex: integer, orderIssuer: Enum.PlayerOrderIssuer, unit: CNPC, orderQueueBehavior: integer, showEffects: boolean, triggerCallBack: boolean, isByMiniMap: boolean, addTime: number }[]`

Returns information about the current humanizer order queue.

## IsSafeTarget

`Humanizer.IsSafeTarget(entity):` `boolean`

Name

Type

Description

**entity**

[`CEntity`](/api-v2.0/game-components/core/entity)

Returns information about the current humanizer order queue.

## ForceUserOrderByMinimap

`Humanizer.ForceUserOrderByMinimap():` `nil`

Forces current user order by minimap. Must be called in OnPrepareUnitOrder

[PreviousConfig](/api-v2.0/game-components/configuration-and-utilities/config)[NextLog](/api-v2.0/game-components/configuration-and-utilities/log)

Last updated 5 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log -->

Copy

# 📓Log

Table to log.

## Write

`Log.Write(arg):` `nil`

Name

Type

Description

**arg**

`any`

Message to write

Writes a message to the console.

[PreviousHumanizer](/api-v2.0/game-components/configuration-and-utilities/humanizer)[NextLocalizer](/api-v2.0/game-components/configuration-and-utilities/localizer)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer -->

Copy

# 🗣️Localizer

Table to work with cheat localizer.

## Get

`Localizer.Get(str):` `string`

Name

Type

Description

**str**

`string`

Returns localized string using current language.

## RegToken

`Localizer.RegToken(str):` `nil`

Name

Type

Description

**str**

`string`

Registers key (token) string to localizer.

[PreviousLog](/api-v2.0/game-components/configuration-and-utilities/log)[NextGameLocalizer](/api-v2.0/game-components/configuration-and-utilities/gamelocalizer)

Last updated 8 months ago

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/gamelocalizer -->

Copy

# 📝GameLocalizer

Table to work with game localization.
Localization tokens are stored in `resource/localization` folder in `pak01_dir.vpk`

## Find

`GameLocalizer.Find(token):` `string`

Name

Type

Description

**token**

`string`

should be in format `#token`

Returns localized string by token or returns empty string if token not found.

#### Example

Copy

```
GameLocalizer.Find("#DOTA_AutocastAbility5") -- Autocast Ability Ultimate
```

## FindAbility

`GameLocalizer.FindAbility(ability_name):` `string`

Name

Type

Description

**ability\_name**

`string`

Returns localized string by ability name or returns empty string if ability not found.

#### Example

Copy

```
GameLocalizer.FindAbility("antimage_mana_void") -- Mana Void
```

## FindItem

`GameLocalizer.FindItem(item_name):` `string`

Name

Type

Description

**item\_name**

`string`

Returns localized string by item name or returns empty string if item not found.

#### Example

## FindNPC

`GameLocalizer.FindNPC(unit_name):` `string`

Name

Type

Description

**unit\_name**

`string`

Returns localized string by unit name or returns empty string if unit not found.

#### Example

[PreviousLocalizer](/api-v2.0/game-components/configuration-and-utilities/localizer)

Last updated 8 months ago

