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

# Callbacks

Callbacks for lua Scripts should return a table with the following functions. If the table contains one of the functions below, it will be registered as a callback and will be called at the appropriate time.

## <sub>OnScriptsLoaded</sub>

`Callbacks.OnScriptsLoaded():` <mark style="color:purple;">**`nil`**</mark>

Called after all scripts are loaded.

## <sub>OnDraw</sub>

`Callbacks.OnDraw():` <mark style="color:purple;">**`nil`**</mark>

Called when the game is drawing. Works only in the game.\
Recommended to use for drawing only.

## <sub>OnFrame</sub>

`Callbacks.OnFrame():` <mark style="color:purple;">**`nil`**</mark>

The same as OnDraw, but called in the menu too.

## <sub>OnUpdate</sub>

`Callbacks.OnUpdate():` <mark style="color:purple;">**`nil`**</mark>

Called every game update. Works only in the game.\
Recommended to use for logic.

## <sub>OnPreHumanizer</sub>

`Callbacks.OnPreHumanizer():` <mark style="color:purple;">**`nil`**</mark>

TODO

## <sub>OnUpdateEx</sub>

`Callbacks.OnUpdateEx():` <mark style="color:purple;">**`nil`**</mark>

Called every game update. Same as OnUpdate but as well called in the menu.\
Recommended to use for logic.

## <sub>OnEntityCreate</sub>

`Callbacks.OnEntityCreate(entity):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | The entity that was created. |

Called when a new entity is created.

## <sub>OnNpcSpawned</sub>

`Callbacks.OnNpcSpawned(npc):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                          | Description               |
| ------- | --------------------------------------------- | ------------------------- |
| **npc** | <mark style="color:purple;">**`CNpc`**</mark> | The npc that was created. |

Called when a npc is spawned. Unlike OnAddEntity, the entity is fully initialized here.

## <sub>OnEntityDestroy</sub>

`Callbacks.OnEntityDestroy(entity):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | The entity that was destroyed. |

Called when an entity is destroyed.

## <sub>OnModifierCreate</sub>

`Callbacks.OnModifierCreate(entity, modifier):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **entity**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)           | The entity that has the modifier. |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | The modifier that was created.    |

Called when a modifier is created.

## <sub>OnModifierDestroy</sub>

`Callbacks.OnModifierDestroy(entity, modifier):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **entity**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)           | The entity that has the modifier. |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | The modifier that was destroyed.  |

Called when a modifier is destroyed.

## <sub>OnModifierUpdate</sub>

`Callbacks.OnModifierUpdate(entity, modifier):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **entity**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)           | The entity that has the modifier. |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | The modifier that was updated.    |

Called when a modifier is updated/refreshed.

## <sub>OnEntityHurt</sub>

{% hint style="info" %}
This callback is called only in unsafe mode.
{% endhint %}

`Callbacks.OnEntityHurt(data):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                                                                                                                                                                       | Description               |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **data** | <mark style="color:purple;">**`{source:CEntity`**</mark> \| <mark style="color:purple;">**`nil, target:CEntity`**</mark> \| <mark style="color:purple;">**`nil, ability:CAbility`**</mark> \| <mark style="color:purple;">**`nil, damage:number}`**</mark> | The data about the event. |

Called when an entity is hurt.

## <sub>OnEntityKilled</sub>

{% hint style="info" %}
This callback is called only in unsafe mode.
{% endhint %}

`Callbacks.OnEntityKilled(data):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                                                                                                                                                        | Description               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **data** | <mark style="color:purple;">**`{source:CEntity`**</mark> \| <mark style="color:purple;">**`nil, target:CEntity`**</mark> \| <mark style="color:purple;">**`nil, ability:CAbility`**</mark> \| <mark style="color:purple;">**`nil}`**</mark> | The data about the event. |

Called when an entity is killed.

## <sub>OnFireEventClient</sub>

{% hint style="info" %}
This callback is called only in unsafe mode.
{% endhint %}

\`Callbacks.OnFireEventClient(data):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name     | Type                                                                | Description               |
| -------- | ------------------------------------------------------------------- | ------------------------- |
| **data** | <mark style="color:purple;">**`{name:string, event:Event}`**</mark> | The data about the event. |

Called when a game event is fired.

## <sub>OnUnitAnimation</sub>

`Callbacks.OnUnitAnimation(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                          | Type                                                                                                         | Description                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **data**                      | <mark style="color:purple;">**`table`**</mark>                                                               | The data about the event.           |
|  .**unit**                    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The unit that played the animation. |
|  .**sequenceVariant**         | <mark style="color:purple;">**`number`**</mark>                                                              | The sequence variant.               |
|  .**playbackRate**            | <mark style="color:purple;">**`number`**</mark>                                                              | The playback rate.                  |
|  .**castpoint**               | <mark style="color:purple;">**`number`**</mark>                                                              | The castpoint.                      |
|  .**type**                    | <mark style="color:purple;">**`integer`**</mark>                                                             | The type.                           |
|  .**activity**                | <mark style="color:purple;">**`integer`**</mark>                                                             | The activity.                       |
|  .**sequence**                | <mark style="color:purple;">**`integer`**</mark>                                                             | The sequence.                       |
|  .**sequenceName**            | <mark style="color:purple;">**`string`**</mark>                                                              | The sequence name.                  |
|  .**lag\_compensation\_time** | <mark style="color:purple;">**`number`**</mark>                                                              | The lag compensation time.          |

Called when a unit animation is played.

## <sub>OnUnitAnimationEnd</sub>

`Callbacks.OnUnitAnimationEnd(data):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                         | Description                         |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **data**   | <mark style="color:purple;">**`table`**</mark>                                                               | The data about the event.           |
|  .**unit** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The unit that played the animation. |
|  .**snap** | <mark style="color:purple;">**`boolean`**</mark>                                                             | The snap.                           |

Called when a unit animation ends.

## <sub>OnProjectile</sub>

`Callbacks.OnProjectile(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                        | Type                                                                                                                                 | Description                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **data**                    | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.             |
|  .**source**                | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The source entity.                    |
|  .**target**                | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The target entity.                    |
|  .**ability**               | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)                 | The ability linked to the projectile. |
|  .**moveSpeed**             | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The move speed.                       |
|  .**sourceAttachment**      | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The source attachment.                |
|  .**particleSystemHandle**  | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The particle system handle.           |
|  .**dodgeable**             | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | The dodgeable.                        |
|  .**isAttack**              | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | The is attack.                        |
|  .**expireTime**            | <mark style="color:purple;">**`number`**</mark>                                                                                      | The expire time.                      |
|  .**maxImpactTime**         | <mark style="color:purple;">**`number`**</mark>                                                                                      | The max impact time.                  |
|  .**launch\_tick**          | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The tick the pojectile was launched.  |
|  .**colorGemColor**         | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The color gem color.                  |
|  .**fullName**              | <mark style="color:purple;">**`string`**</mark>                                                                                      | The full name of projectile.          |
|  .**name**                  | <mark style="color:purple;">**`string`**</mark>                                                                                      | The short name of projectile.         |
|  .**handle**                | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The handle of projectile.             |
|  .**target\_loc**           | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The location of the target.           |
|  .**original\_move\_speed** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The original move speed.              |

Called when new projectile is created.

## <sub>OnProjectileLoc</sub>

`Callbacks.OnProjectileLoc(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                 | Description                         |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **data**                                                       | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.           |
|  .**target&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The source entity. `(default: nil)` |
|  .**sourceLoc**                                                | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The source location.                |
|  .**targetLoc**                                                | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The target location.                |
|  .**moveSpeed**                                                | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The move speed.                     |
|  .**original\_move\_speed**                                    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The original move speed.            |
|  .**particleSystemHandle**                                     | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The particle system handle.         |
|  .**dodgeable**                                                | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | The dodgeable.                      |
|  .**isAttack**                                                 | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | The is attack.                      |
|  .**expireTime**                                               | <mark style="color:purple;">**`number`**</mark>                                                                                      | The expire time.                    |
|  .**colorGemColor**                                            | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The color gem color.                |
|  .**launchTick**                                               | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The launch tick.                    |
|  .**handle**                                                   | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The handle of projectile.           |
|  .**fullName**                                                 | <mark style="color:purple;">**`string`**</mark>                                                                                      | The full name of projectile.        |
|  .**name**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                      | The short name of projectile.       |

Called when new projectile loc is created.

## <sub>OnLinearProjectileCreate</sub>

`Callbacks.OnLinearProjectileCreate(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                                                                                                                 | Description                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **data**            | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.     |
|  .**source**        | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The source entity.            |
|  .**origin**        | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The origin.                   |
|  .**velocity**      | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The velocity.                 |
|  .**particleIndex** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The particle index.           |
|  .**handle**        | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The handle of projectile.     |
|  .**acceleration**  | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The acceleration.             |
|  .**maxSpeed**      | <mark style="color:purple;">**`number`**</mark>                                                                                      | The max speed.                |
|  .**fowRadius**     | <mark style="color:purple;">**`number`**</mark>                                                                                      | The fow radius.               |
|  .**distance**      | <mark style="color:purple;">**`number`**</mark>                                                                                      | The distance.                 |
|  .**colorGemColor** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The color gem color.          |
|  .**fullName**      | <mark style="color:purple;">**`string`**</mark>                                                                                      | The full name of projectile.  |
|  .**name**          | <mark style="color:purple;">**`string`**</mark>                                                                                      | The short name of projectile. |

Called when new linear projectile is created.

## <sub>OnLinearProjectileDestroy</sub>

`Callbacks.OnLinearProjectileDestroy(data):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                             | Description               |
| ------------ | ------------------------------------------------ | ------------------------- |
| **data**     | <mark style="color:purple;">**`table`**</mark>   | The data about the event. |
|  .**handle** | <mark style="color:purple;">**`integer`**</mark> | The handle of projectile. |

Called when linear projectile is destroyed.

## <sub>OnParticleCreate</sub>

`Callbacks.OnParticleCreate(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                       | Type                                                                                                                                 | Description                                |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| **data**                                                                   | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.                  |
|  .**index**                                                                | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The index of particle.                     |
|  .**entity&#x20;**<mark style="color:orange;">**`[?]`**</mark>             | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The entity. `(default: nil)`               |
|  .**entity\_id**                                                           | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The entity id.                             |
|  .**entityForModifiers&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The entity for modifiers. `(default: nil)` |
|  .**entity\_for\_modifiers\_id**                                           | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The entity for modifiers id.               |
|  .**attachType**                                                           | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.particleattachment) | The attach type.                           |
|  .**fullName**                                                             | <mark style="color:purple;">**`string`**</mark>                                                                                      | The full name of particle.                 |
|  .**name**                                                                 | <mark style="color:purple;">**`string`**</mark>                                                                                      | The short name of particle.                |
|  .**hash**                                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The hash of particle.                      |
|  .**particleNameIndex**                                                    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The particle name index.                   |

Called when new particle is created.

## <sub>OnParticleUpdate</sub>

`Callbacks.OnParticleUpdate(data):` <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                                                 | Description               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| **data**           | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event. |
|  .**index**        | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The index of particle.    |
|  .**controlPoint** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The control point.        |
|  .**position**     | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The position.             |

Called when particle is updated.

## <sub>OnParticleUpdateFallback</sub>

`Callbacks.OnParticleUpdateFallback(data):` <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                                                 | Description               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| **data**           | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event. |
|  .**index**        | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The index of particle.    |
|  .**controlPoint** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The control point.        |
|  .**position**     | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The position.             |

Called when particle is updated. Alternative version for some particles.

## <sub>OnParticleUpdateEntity</sub>

`Callbacks.OnParticleUpdateEntity(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                   | Type                                                                                                                                 | Description               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| **data**               | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event. |
|  .**index**            | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The index of particle.    |
|  .**controlPoint**     | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The control point.        |
|  .**entity**           | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                   | The entity.               |
|  .**entIdx**           | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The entity id.            |
|  .**attachType**       | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.particleattachment) | The attach type.          |
|  .**attachmentName**   | <mark style="color:purple;">**`string`**</mark>                                                                                      | The attachment name.      |
|  .**position**         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The position.             |
|  .**includeWearables** | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Include wearables.        |

Called when particle is updated on entity.

## <sub>OnParticleDestroy</sub>

`Callbacks.OnParticleDestroy(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                     | Type                                             | Description                      |
| ------------------------ | ------------------------------------------------ | -------------------------------- |
| **data**                 | <mark style="color:purple;">**`table`**</mark>   | The data about the event.        |
|  .**index**              | <mark style="color:purple;">**`integer`**</mark> | The index of destroyed particle. |
|  .**destroyImmediately** | <mark style="color:purple;">**`boolean`**</mark> | Destroy immediately.             |

Called when particle is destroyed.

## <sub>OnStartSound</sub>

`Callbacks.OnStartSound(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                 | Description                           |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **data**                                                       | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.             |
|  .**source&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                   | The source of sound. `(default: nil)` |
|  .**hash**                                                     | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The hash of sound.                    |
|  .**guid**                                                     | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The guid of sound.                    |
|  .**seed**                                                     | <mark style="color:purple;">**`integer`**</mark>                                                                                     | The seed of sound.                    |
|  .**name**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                      | The name of sound.                    |
|  .**position**                                                 | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The position of sound.                |

Called when sound is started.

## <sub>OnSpeak</sub>

`Callbacks.OnSpeak(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                                                         | Description               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| **data**     | <mark style="color:purple;">**`table`**</mark>                                                                                                               | The data about the event. |
|  .**source** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| <mark style="color:purple;">**`nil`**</mark> | The unit who speak.       |
|  .**name**   | <mark style="color:purple;">**`string`**</mark>                                                                                                              | The name of the sound.    |

Called every time unit/announcer talk. You could return false to prevent the sound from being played.

## <sub>OnChatEvent</sub>

`Callbacks.OnChatEvent(data):` <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                             | Description                    |
| ----------------- | ------------------------------------------------ | ------------------------------ |
| **data**          | <mark style="color:purple;">**`table`**</mark>   | The data about the event.      |
|  .**type**        | <mark style="color:purple;">**`integer`**</mark> | The type of chat event.        |
|  .**value**       | <mark style="color:purple;">**`integer`**</mark> | The value of chat event.       |
|  .**value2**      | <mark style="color:purple;">**`integer`**</mark> | The value2 of chat event.      |
|  .**value3**      | <mark style="color:purple;">**`integer`**</mark> | The value3 of chat event.      |
|  .**playerid\_1** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_1 of chat event. |
|  .**playerid\_2** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_2 of chat event. |
|  .**playerid\_3** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_3 of chat event. |
|  .**playerid\_4** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_4 of chat event. |
|  .**playerid\_5** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_5 of chat event. |
|  .**playerid\_6** | <mark style="color:purple;">**`integer`**</mark> | The playerid\_6 of chat event. |

Called on chat event.

## <sub>OnOverHeadEvent</sub>

`Callbacks.OnOverHeadEvent(data):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                                                                                                                                    | Description                    |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **data** | <mark style="color:purple;">**`{player_source:CPlayer`**</mark> \| <mark style="color:purple;">**`nil, player_target:CPlayer`**</mark> \| <mark style="color:purple;">**`nil, target_npc:CNPC, value:integer}`**</mark> | The table with the event info. |

Called on event above the hero's head.

## <sub>OnUnitAddGesture</sub>

`Callbacks.OnUnitAddGesture(data):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                        | Type                                                                                                         | Description                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| **data**                                                    | <mark style="color:purple;">**`table`**</mark>                                                               | The data about the event.                             |
|  .**npc&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The unit that is added to a gesture. `(default: nil)` |
|  .**sequenceVariant**                                       | <mark style="color:purple;">**`integer`**</mark>                                                             | The sequence variant.                                 |
|  .**playbackRate**                                          | <mark style="color:purple;">**`number`**</mark>                                                              | The playback rate.                                    |
|  .**fadeIn**                                                | <mark style="color:purple;">**`number`**</mark>                                                              | The fade in.                                          |
|  .**fadeOut**                                               | <mark style="color:purple;">**`number`**</mark>                                                              | The fade out.                                         |
|  .**slot**                                                  | <mark style="color:purple;">**`integer`**</mark>                                                             | The slot.                                             |
|  .**activity**                                              | <mark style="color:purple;">**`integer`**</mark>                                                             | The activity.                                         |
|  .**sequenceName**                                          | <mark style="color:purple;">**`string`**</mark>                                                              | The sequence name.                                    |

Called when a unit is added to a gesture.

## <sub>OnPrepareUnitOrders</sub>

`Callbacks.OnPrepareUnitOrders(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                            | Type                                                                                                                                 | Description                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| **data**                                                        | <mark style="color:purple;">**`table`**</mark>                                                                                       | The data about the event.                  |
|  .**player**                                                    | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player)                   | The player that issued the order.          |
|  .**order**                                                     | [<mark style="color:purple;">**`Enum.UnitOrder`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.unitorder)                   | The order type.                            |
|  .**target&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                   | The target of the order. `(default: nil)`  |
|  .**position**                                                  | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The position of the order.                 |
|  .**ability&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)                 | The ability of the order. `(default: nil)` |
|  .**orderIssuer**                                               | [<mark style="color:purple;">**`Enum.PlayerOrderIssuer`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.playerorderissuer)   | The order issuer.                          |
|  .**npc**                                                       | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The unit of the order.                     |
|  .**queue**                                                     | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | If the order is queued.                    |
|  .**showEffects**                                               | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | The show effects of the order.             |

Called on every player order. Return false to prevent the order from being executed.

## <sub>OnGCMessage</sub>

`Callbacks.OnGCMessage(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                                         | Type                                              | Description                                                 |
| ---------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------- |
| **data**                                                                     | <mark style="color:purple;">**`table`**</mark>    |                                                             |
|  .**msg\_type**                                                              | <mark style="color:purple;">**`number`**</mark>   | The message type.                                           |
|  .**size**                                                                   | <mark style="color:purple;">**`number`**</mark>   | The size of the message.                                    |
|  .**binary\_buffer\_send&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`userdata`**</mark> | The binary buffer of the send message. `(default: nil)`     |
|  .**binary\_buffer\_recv&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`userdata`**</mark> | The binary buffer of the recieved message. `(default: nil)` |

Called when a game coordinator protobuff message is received. Return false to prevent the message\
from being sent (doesnt work with recieved messages). For more look at GC table description.

#### Example

```lua
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

## <sub>OnSendNetMessage</sub>

`Callbacks.OnSendNetMessage(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name                | Type                                                   | Description                        |
| ------------------- | ------------------------------------------------------ | ---------------------------------- |
| **data**            | <mark style="color:purple;">**`table`**</mark>         | The data about the event.          |
|  .**message\_id**   | <mark style="color:purple;">**`number`**</mark>        | The message id.                    |
|  .**message\_name** | <mark style="color:purple;">**`string`**</mark>        | The message name.                  |
|  .**buffer**        | <mark style="color:purple;">**`lightuserdata`**</mark> | The encoded buffer of the message. |
|  .**size**          | <mark style="color:purple;">**`number`**</mark>        | The size of the message.           |

Called when a net message is sent. Return false to prevent the message from being sent. See\
example

#### Example

```lua
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

## <sub>OnPostReceivedNetMessage</sub>

`Callbacks.OnPostReceivedNetMessage(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name              | Type                                                   | Description                        |
| ----------------- | ------------------------------------------------------ | ---------------------------------- |
| **data**          | <mark style="color:purple;">**`table`**</mark>         | The data about the event.          |
|  .**message\_id** | <mark style="color:purple;">**`number`**</mark>        | The message id.                    |
|  .**msg\_object** | <mark style="color:purple;">**`lightuserdata`**</mark> | The encoded buffer of the message. |

Called when a net message is received. Return false to prevent the message from being recieved

#### Example

```lua
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

## <sub>OnGameEnd</sub>

`Callbacks.OnGameEnd():` <mark style="color:purple;">**`nil`**</mark>

Called on game end.\
Recommended to use for zeroing.

## <sub>OnKeyEvent</sub>

`Callbacks.OnKeyEvent(data):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description               |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **data**    | <mark style="color:purple;">**`table`**</mark>                                                                       | The data about the event. |
|  .**key**   | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode) | The key code.             |
|  .**event** | [<mark style="color:purple;">**`Enum.EKeyEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.ekeyevent)   | Key event.                |

Called on key and mouse input. Return false to prevent the event from being processed.

## <sub>OnUnitInventoryUpdated</sub>

`Callbacks.OnUnitInventoryUpdated(data):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                         | Description               |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------------------------- |
| **data** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The data about the event. |

Called on unit inventory updated.

## <sub>OnSetDormant</sub>

`Callbacks.OnSetDormant(npc, type):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                                     | Description         |
| -------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)             | The target npc.     |
| **type** | [<mark style="color:purple;">**`Enum.DormancyType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.dormancytype) | The type of change. |

Called on NPC dormancy state changed.

## <sub>OnGameRulesStateChange</sub>

`Callbacks.OnGameRulesStateChange(data):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                        | Description                         |
| -------- | ------------------------------------------- | ----------------------------------- |
| **data** | <mark style="color:purple;">**`{}`**</mark> | The table with new game state info. |

Called on gamestate change.

## <sub>OnNpcDying</sub>

`Callbacks.OnNpcDying(npc):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target npc. |

Called on NPC dying.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums -->

# Enums

## <mark style="color:purple;">Enum.ShopType</mark>

| Key                                                    | Value |
| ------------------------------------------------------ | ----- |
| <mark style="color:green;">`DOTA_SHOP_HOME`</mark>     | 0     |
| <mark style="color:green;">`DOTA_SHOP_SIDE`</mark>     | 1     |
| <mark style="color:green;">`DOTA_SHOP_SECRET`</mark>   | 2     |
| <mark style="color:green;">`DOTA_SHOP_GROUND`</mark>   | 3     |
| <mark style="color:green;">`DOTA_SHOP_SIDE2`</mark>    | 4     |
| <mark style="color:green;">`DOTA_SHOP_SECRET2`</mark>  | 5     |
| <mark style="color:green;">`DOTA_SHOP_CUSTOM`</mark>   | 6     |
| <mark style="color:green;">`DOTA_SHOP_NEUTRALS`</mark> | 7     |
| <mark style="color:green;">`DOTA_SHOP_NONE`</mark>     | 8     |

## <mark style="color:purple;">Enum.AbilityTypes</mark>

| Key                                                         | Value |
| ----------------------------------------------------------- | ----- |
| <mark style="color:green;">`ABILITY_TYPE_BASIC`</mark>      | 0     |
| <mark style="color:green;">`ABILITY_TYPE_ULTIMATE`</mark>   | 1     |
| <mark style="color:green;">`ABILITY_TYPE_ATTRIBUTES`</mark> | 2     |
| <mark style="color:green;">`ABILITY_TYPE_HIDDEN`</mark>     | 3     |

## <mark style="color:purple;">Enum.AbilityBehavior</mark>

| Key                                                                                      | Value         |
| ---------------------------------------------------------------------------------------- | ------------- |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_NONE`</mark>                           | 0             |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_HIDDEN`</mark>                         | 1             |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_PASSIVE`</mark>                        | 2             |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_NO_TARGET`</mark>                      | 4             |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_UNIT_TARGET`</mark>                    | 8             |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_POINT`</mark>                          | 16            |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_AOE`</mark>                            | 32            |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_NOT_LEARNABLE`</mark>                  | 64            |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_CHANNELLED`</mark>                     | 128           |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_ITEM`</mark>                           | 256           |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_TOGGLE`</mark>                         | 512           |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DIRECTIONAL`</mark>                    | 1024          |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IMMEDIATE`</mark>                      | 2048          |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_AUTOCAST`</mark>                       | 4096          |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET`</mark>           | 8192          |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_OPTIONAL_POINT`</mark>                 | 16384         |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_OPTIONAL_NO_TARGET`</mark>             | 32768         |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_AURA`</mark>                           | 65536         |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_ATTACK`</mark>                         | 131072        |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT`</mark>           | 262144        |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES`</mark>                  | 524288        |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_UNRESTRICTED`</mark>                   | 1048576       |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IGNORE_PSEUDO_QUEUE`</mark>            | 2097152       |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL`</mark>                 | 4194304       |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT`</mark>           | 8388608       |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DONT_ALERT_TARGET`</mark>              | 16777216      |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK`</mark>             | 33554432      |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_NORMAL_WHEN_STOLEN`</mark>             | 67108864      |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING`</mark>               | 134217728     |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_RUNE_TARGET`</mark>                    | 268435456     |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_CHANNEL`</mark>            | 536870912     |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_VECTOR_TARGETING`</mark>               | 1073741824    |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_LAST_RESORT_POINT`</mark>              | 2147483648    |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_CAN_SELF_CAST`</mark>                  | 4294967296    |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_SHOW_IN_GUIDES`</mark>                 | 8589934592    |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_UNLOCKED_BY_EFFECT_INDEX`</mark>       | 17179869184   |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE`</mark> | 34359738368   |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_FREE_DRAW_TARGETING`</mark>            | 68719476736   |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IGNORE_SILENCE`</mark>                 | 137438953472  |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_IGNORE_MUTED`</mark>                   | 549755813888  |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_ALT_CASTABLE`</mark>                   | 1099511627776 |
| <mark style="color:green;">`DOTA_ABILITY_BEHAVIOR_SKIP_FOR_KEYBINDS`</mark>              | 4398046511104 |

## <mark style="color:purple;">Enum.TargetTeam</mark>

| Key                                                                | Value |
| ------------------------------------------------------------------ | ----- |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TEAM_NONE`</mark>     | 0     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TEAM_FRIENDLY`</mark> | 1     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TEAM_ENEMY`</mark>    | 2     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TEAM_CUSTOM`</mark>   | 4     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TEAM_BOTH`</mark>     | 3     |

## <mark style="color:purple;">Enum.TargetType</mark>

| Key                                                                    | Value |
| ---------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_UNIT_TARGET_NONE`</mark>              | 0     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_HERO`</mark>              | 1     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_CREEP`</mark>             | 2     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_BUILDING`</mark>          | 4     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_COURIER`</mark>           | 16    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_OTHER`</mark>             | 32    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_TREE`</mark>              | 64    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_CUSTOM`</mark>            | 128   |
| <mark style="color:green;">`DOTA_UNIT_TARGET_SELF`</mark>              | 256   |
| <mark style="color:green;">`DOTA_UNIT_TARGET_BASIC`</mark>             | 18    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_ALL`</mark>               | 55    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_HEROES_AND_CREEPS`</mark> | 19    |

## <mark style="color:purple;">Enum.TargetFlags</mark>

| Key                                                                               | Value   |
| --------------------------------------------------------------------------------- | ------- |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NONE`</mark>                    | 0       |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_RANGED_ONLY`</mark>             | 2       |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_MELEE_ONLY`</mark>              | 4       |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_DEAD`</mark>                    | 8       |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_MAGIC_IMMUNE_ENEMIES`</mark>    | 16      |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_MAGIC_IMMUNE_ALLIES`</mark> | 32      |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_INVULNERABLE`</mark>            | 64      |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_FOW_VISIBLE`</mark>             | 128     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NO_INVIS`</mark>                | 256     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_ANCIENTS`</mark>            | 512     |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_PLAYER_CONTROLLED`</mark>       | 1024    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_DOMINATED`</mark>           | 2048    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_SUMMONED`</mark>            | 4096    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_ILLUSIONS`</mark>           | 8192    |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_ATTACK_IMMUNE`</mark>       | 16384   |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_MANA_ONLY`</mark>               | 32768   |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_CHECK_DISABLE_HELP`</mark>      | 65536   |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_CREEP_HERO`</mark>          | 131072  |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_OUT_OF_WORLD`</mark>            | 262144  |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_NOT_NIGHTMARED`</mark>          | 524288  |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_PREFER_ENEMIES`</mark>          | 1048576 |
| <mark style="color:green;">`DOTA_UNIT_TARGET_FLAG_RESPECT_OBSTRUCTIONS`</mark>    | 2097152 |

## <mark style="color:purple;">Enum.DamageTypes</mark>

| Key                                                        | Value |
| ---------------------------------------------------------- | ----- |
| <mark style="color:green;">`DAMAGE_TYPE_NONE`</mark>       | 0     |
| <mark style="color:green;">`DAMAGE_TYPE_PHYSICAL`</mark>   | 1     |
| <mark style="color:green;">`DAMAGE_TYPE_MAGICAL`</mark>    | 2     |
| <mark style="color:green;">`DAMAGE_TYPE_PURE`</mark>       | 4     |
| <mark style="color:green;">`DAMAGE_TYPE_HP_REMOVAL`</mark> | 8     |
| <mark style="color:green;">`DAMAGE_TYPE_ALL`</mark>        | 7     |

## <mark style="color:purple;">Enum.TalentTypes</mark>

| Key                                          | Value |
| -------------------------------------------- | ----- |
| <mark style="color:green;">`TALENT_1`</mark> | 1     |
| <mark style="color:green;">`TALENT_2`</mark> | 2     |
| <mark style="color:green;">`TALENT_3`</mark> | 4     |
| <mark style="color:green;">`TALENT_4`</mark> | 8     |
| <mark style="color:green;">`TALENT_5`</mark> | 16    |
| <mark style="color:green;">`TALENT_6`</mark> | 32    |
| <mark style="color:green;">`TALENT_7`</mark> | 64    |
| <mark style="color:green;">`TALENT_8`</mark> | 128   |

## <mark style="color:purple;">Enum.ImmunityTypes</mark>

| Key                                                                      | Value |
| ------------------------------------------------------------------------ | ----- |
| <mark style="color:green;">`SPELL_IMMUNITY_NONE`</mark>                  | 0     |
| <mark style="color:green;">`SPELL_IMMUNITY_ALLIES_YES`</mark>            | 1     |
| <mark style="color:green;">`SPELL_IMMUNITY_ALLIES_NO`</mark>             | 2     |
| <mark style="color:green;">`SPELL_IMMUNITY_ENEMIES_YES`</mark>           | 3     |
| <mark style="color:green;">`SPELL_IMMUNITY_ENEMIES_NO`</mark>            | 4     |
| <mark style="color:green;">`SPELL_IMMUNITY_ALLIES_YES_ENEMIES_NO`</mark> | 5     |

## <mark style="color:purple;">Enum.DispellableTypes</mark>

| Key                                                              | Value |
| ---------------------------------------------------------------- | ----- |
| <mark style="color:green;">`SPELL_DISPELLABLE_NONE`</mark>       | 0     |
| <mark style="color:green;">`SPELL_DISPELLABLE_YES_STRONG`</mark> | 1     |
| <mark style="color:green;">`SPELL_DISPELLABLE_YES`</mark>        | 2     |
| <mark style="color:green;">`SPELL_DISPELLABLE_NO`</mark>         | 3     |

## <mark style="color:purple;">Enum.TeamType</mark>

| Key                                             | Value |
| ----------------------------------------------- | ----- |
| <mark style="color:green;">`TEAM_ENEMY`</mark>  | 0     |
| <mark style="color:green;">`TEAM_FRIEND`</mark> | 1     |
| <mark style="color:green;">`TEAM_BOTH`</mark>   | 2     |

## <mark style="color:purple;">Enum.ECampType</mark>

| Key                                                   | Value |
| ----------------------------------------------------- | ----- |
| <mark style="color:green;">`ECampType_SMALL`</mark>   | 0     |
| <mark style="color:green;">`ECampType_MEDIUM`</mark>  | 1     |
| <mark style="color:green;">`ECampType_LARGE`</mark>   | 2     |
| <mark style="color:green;">`ECampType_ANCIENT`</mark> | 3     |

## <mark style="color:purple;">Enum.EKeyEvent</mark>

| Key                                                       | Value |
| --------------------------------------------------------- | ----- |
| <mark style="color:green;">`EKeyEvent_SCROLL_DOWN`</mark> | 0     |
| <mark style="color:green;">`EKeyEvent_SCROLL_UP`</mark>   | 1     |
| <mark style="color:green;">`EKeyEvent_KEY_DOWN`</mark>    | 2     |
| <mark style="color:green;">`EKeyEvent_KEY_UP`</mark>      | 3     |

## <mark style="color:purple;">Enum.CourierState</mark>

| Key                                                                    | Value      |
| ---------------------------------------------------------------------- | ---------- |
| <mark style="color:green;">`COURIER_STATE_INIT`</mark>                 | 4294967295 |
| <mark style="color:green;">`COURIER_STATE_IDLE`</mark>                 | 0          |
| <mark style="color:green;">`COURIER_STATE_AT_BASE`</mark>              | 1          |
| <mark style="color:green;">`COURIER_STATE_MOVING`</mark>               | 2          |
| <mark style="color:green;">`COURIER_STATE_DELIVERING_ITEMS`</mark>     | 3          |
| <mark style="color:green;">`COURIER_STATE_RETURNING_TO_BASE`</mark>    | 4          |
| <mark style="color:green;">`COURIER_STATE_DEAD`</mark>                 | 5          |
| <mark style="color:green;">`COURIER_STATE_GOING_TO_SECRET_SHOP`</mark> | 6          |
| <mark style="color:green;">`COURIER_STATE_AT_SECRET_SHOP`</mark>       | 7          |
| <mark style="color:green;">`COURIER_NUM_STATES`</mark>                 | 8          |

## <mark style="color:purple;">Enum.RuneType</mark>

| Key                                                        | Value      |
| ---------------------------------------------------------- | ---------- |
| <mark style="color:green;">`DOTA_RUNE_INVALID`</mark>      | 4294967295 |
| <mark style="color:green;">`DOTA_RUNE_DOUBLEDAMAGE`</mark> | 0          |
| <mark style="color:green;">`DOTA_RUNE_HASTE`</mark>        | 1          |
| <mark style="color:green;">`DOTA_RUNE_ILLUSION`</mark>     | 2          |
| <mark style="color:green;">`DOTA_RUNE_INVISIBILITY`</mark> | 3          |
| <mark style="color:green;">`DOTA_RUNE_REGENERATION`</mark> | 4          |
| <mark style="color:green;">`DOTA_RUNE_BOUNTY`</mark>       | 5          |
| <mark style="color:green;">`DOTA_RUNE_ARCANE`</mark>       | 6          |
| <mark style="color:green;">`DOTA_RUNE_WATER`</mark>        | 7          |
| <mark style="color:green;">`DOTA_RUNE_XP`</mark>           | 8          |
| <mark style="color:green;">`DOTA_RUNE_SHIELD`</mark>       | 9          |
| <mark style="color:green;">`DOTA_RUNE_COUNT`</mark>        | 10         |

## <mark style="color:purple;">Enum.ModifierState</mark>

| Key                                                                                   | Value |
| ------------------------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`MODIFIER_STATE_ROOTED`</mark>                             | 0     |
| <mark style="color:green;">`MODIFIER_STATE_DISARMED`</mark>                           | 1     |
| <mark style="color:green;">`MODIFIER_STATE_ATTACK_IMMUNE`</mark>                      | 2     |
| <mark style="color:green;">`MODIFIER_STATE_SILENCED`</mark>                           | 3     |
| <mark style="color:green;">`MODIFIER_STATE_MUTED`</mark>                              | 4     |
| <mark style="color:green;">`MODIFIER_STATE_STUNNED`</mark>                            | 5     |
| <mark style="color:green;">`MODIFIER_STATE_HEXED`</mark>                              | 6     |
| <mark style="color:green;">`MODIFIER_STATE_INVISIBLE`</mark>                          | 7     |
| <mark style="color:green;">`MODIFIER_STATE_INVULNERABLE`</mark>                       | 8     |
| <mark style="color:green;">`MODIFIER_STATE_MAGIC_IMMUNE`</mark>                       | 9     |
| <mark style="color:green;">`MODIFIER_STATE_PROVIDES_VISION`</mark>                    | 10    |
| <mark style="color:green;">`MODIFIER_STATE_NIGHTMARED`</mark>                         | 11    |
| <mark style="color:green;">`MODIFIER_STATE_BLOCK_DISABLED`</mark>                     | 12    |
| <mark style="color:green;">`MODIFIER_STATE_EVADE_DISABLED`</mark>                     | 13    |
| <mark style="color:green;">`MODIFIER_STATE_UNSELECTABLE`</mark>                       | 14    |
| <mark style="color:green;">`MODIFIER_STATE_CANNOT_TARGET_ENEMIES`</mark>              | 15    |
| <mark style="color:green;">`MODIFIER_STATE_CANNOT_TARGET_BUILDINGS`</mark>            | 16    |
| <mark style="color:green;">`MODIFIER_STATE_CANNOT_MISS`</mark>                        | 17    |
| <mark style="color:green;">`MODIFIER_STATE_SPECIALLY_DENIABLE`</mark>                 | 18    |
| <mark style="color:green;">`MODIFIER_STATE_FROZEN`</mark>                             | 19    |
| <mark style="color:green;">`MODIFIER_STATE_COMMAND_RESTRICTED`</mark>                 | 20    |
| <mark style="color:green;">`MODIFIER_STATE_NOT_ON_MINIMAP`</mark>                     | 21    |
| <mark style="color:green;">`MODIFIER_STATE_LOW_ATTACK_PRIORITY`</mark>                | 22    |
| <mark style="color:green;">`MODIFIER_STATE_NO_HEALTH_BAR`</mark>                      | 23    |
| <mark style="color:green;">`MODIFIER_STATE_NO_HEALTH_BAR_FOR_ENEMIES`</mark>          | 24    |
| <mark style="color:green;">`MODIFIER_STATE_NO_HEALTH_BAR_FOR_OTHER_PLAYERS`</mark>    | 25    |
| <mark style="color:green;">`MODIFIER_STATE_FLYING`</mark>                             | 26    |
| <mark style="color:green;">`MODIFIER_STATE_NO_UNIT_COLLISION`</mark>                  | 27    |
| <mark style="color:green;">`MODIFIER_STATE_NO_TEAM_MOVE_TO`</mark>                    | 28    |
| <mark style="color:green;">`MODIFIER_STATE_NO_TEAM_SELECT`</mark>                     | 29    |
| <mark style="color:green;">`MODIFIER_STATE_PASSIVES_DISABLED`</mark>                  | 30    |
| <mark style="color:green;">`MODIFIER_STATE_DOMINATED`</mark>                          | 31    |
| <mark style="color:green;">`MODIFIER_STATE_BLIND`</mark>                              | 32    |
| <mark style="color:green;">`MODIFIER_STATE_OUT_OF_GAME`</mark>                        | 33    |
| <mark style="color:green;">`MODIFIER_STATE_FAKE_ALLY`</mark>                          | 34    |
| <mark style="color:green;">`MODIFIER_STATE_FLYING_FOR_PATHING_PURPOSES_ONLY`</mark>   | 35    |
| <mark style="color:green;">`MODIFIER_STATE_TRUESIGHT_IMMUNE`</mark>                   | 36    |
| <mark style="color:green;">`MODIFIER_STATE_UNTARGETABLE`</mark>                       | 37    |
| <mark style="color:green;">`MODIFIER_STATE_UNTARGETABLE_ALLIED`</mark>                | 38    |
| <mark style="color:green;">`MODIFIER_STATE_UNTARGETABLE_ENEMY`</mark>                 | 39    |
| <mark style="color:green;">`MODIFIER_STATE_UNTARGETABLE_SELF`</mark>                  | 40    |
| <mark style="color:green;">`MODIFIER_STATE_IGNORING_MOVE_AND_ATTACK_ORDERS`</mark>    | 41    |
| <mark style="color:green;">`MODIFIER_STATE_ALLOW_PATHING_THROUGH_TREES`</mark>        | 42    |
| <mark style="color:green;">`MODIFIER_STATE_NOT_ON_MINIMAP_FOR_ENEMIES`</mark>         | 43    |
| <mark style="color:green;">`MODIFIER_STATE_UNSLOWABLE`</mark>                         | 44    |
| <mark style="color:green;">`MODIFIER_STATE_TETHERED`</mark>                           | 45    |
| <mark style="color:green;">`MODIFIER_STATE_IGNORING_STOP_ORDERS`</mark>               | 46    |
| <mark style="color:green;">`MODIFIER_STATE_FEARED`</mark>                             | 47    |
| <mark style="color:green;">`MODIFIER_STATE_TAUNTED`</mark>                            | 48    |
| <mark style="color:green;">`MODIFIER_STATE_CANNOT_BE_MOTION_CONTROLLED`</mark>        | 49    |
| <mark style="color:green;">`MODIFIER_STATE_FORCED_FLYING_VISION`</mark>               | 50    |
| <mark style="color:green;">`MODIFIER_STATE_ATTACK_ALLIES`</mark>                      | 51    |
| <mark style="color:green;">`MODIFIER_STATE_ALLOW_PATHING_THROUGH_CLIFFS`</mark>       | 52    |
| <mark style="color:green;">`MODIFIER_STATE_ALLOW_PATHING_THROUGH_FISSURE`</mark>      | 53    |
| <mark style="color:green;">`MODIFIER_STATE_SPECIALLY_UNDENIABLE`</mark>               | 54    |
| <mark style="color:green;">`MODIFIER_STATE_ALLOW_PATHING_THROUGH_OBSTRUCTIONS`</mark> | 55    |
| <mark style="color:green;">`MODIFIER_STATE_DEBUFF_IMMUNE`</mark>                      | 56    |
| <mark style="color:green;">`MODIFIER_STATE_NEUTRALS_DONT_ATTACK`</mark>               | 63    |
| <mark style="color:green;">`MODIFIER_STATE_ALLOW_PATHING_THROUGH_BASE_BLOCKER`</mark> | 57    |
| <mark style="color:green;">`MODIFIER_STATE_IGNORING_MOVE_ORDERS`</mark>               | 58    |
| <mark style="color:green;">`MODIFIER_STATE_ATTACKS_ARE_MELEE`</mark>                  | 59    |
| <mark style="color:green;">`MODIFIER_STATE_CAN_USE_BACKPACK_ITEMS`</mark>             | 60    |
| <mark style="color:green;">`MODIFIER_STATE_CASTS_IGNORE_CHANNELING`</mark>            | 61    |
| <mark style="color:green;">`MODIFIER_STATE_ATTACKS_DONT_REVEAL`</mark>                | 62    |
| <mark style="color:green;">`MODIFIER_STATE_LAST`</mark>                               | 64    |

## <mark style="color:purple;">Enum.GameActivity</mark>

| Key                                                                        | Value |
| -------------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`ACT_DOTA_IDLE`</mark>                          | 1500  |
| <mark style="color:green;">`ACT_DOTA_IDLE_RARE`</mark>                     | 1501  |
| <mark style="color:green;">`ACT_DOTA_RUN`</mark>                           | 1502  |
| <mark style="color:green;">`ACT_DOTA_ATTACK`</mark>                        | 1503  |
| <mark style="color:green;">`ACT_DOTA_ATTACK2`</mark>                       | 1504  |
| <mark style="color:green;">`ACT_DOTA_ATTACK_EVENT`</mark>                  | 1505  |
| <mark style="color:green;">`ACT_DOTA_DIE`</mark>                           | 1506  |
| <mark style="color:green;">`ACT_DOTA_FLINCH`</mark>                        | 1507  |
| <mark style="color:green;">`ACT_DOTA_FLAIL`</mark>                         | 1508  |
| <mark style="color:green;">`ACT_DOTA_DISABLED`</mark>                      | 1509  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_1`</mark>                | 1510  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2`</mark>                | 1511  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_3`</mark>                | 1512  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_4`</mark>                | 1513  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_5`</mark>                | 1514  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_6`</mark>                | 1515  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_ABILITY_1`</mark>            | 1516  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_ABILITY_2`</mark>            | 1517  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_ABILITY_3`</mark>            | 1518  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_ABILITY_4`</mark>            | 1519  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_1`</mark>             | 1520  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_2`</mark>             | 1521  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_3`</mark>             | 1522  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_4`</mark>             | 1523  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_5`</mark>             | 1524  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_6`</mark>             | 1525  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_1`</mark>         | 1526  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_2`</mark>         | 1527  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_3`</mark>         | 1528  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_4`</mark>         | 1529  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_5`</mark>         | 1530  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_END_ABILITY_6`</mark>         | 1531  |
| <mark style="color:green;">`ACT_DOTA_CONSTANT_LAYER`</mark>                | 1532  |
| <mark style="color:green;">`ACT_DOTA_CAPTURE`</mark>                       | 1533  |
| <mark style="color:green;">`ACT_DOTA_SPAWN`</mark>                         | 1534  |
| <mark style="color:green;">`ACT_DOTA_KILLTAUNT`</mark>                     | 1535  |
| <mark style="color:green;">`ACT_DOTA_TAUNT`</mark>                         | 1536  |
| <mark style="color:green;">`ACT_DOTA_THIRST`</mark>                        | 1537  |
| <mark style="color:green;">`ACT_DOTA_CAST_DRAGONBREATH`</mark>             | 1538  |
| <mark style="color:green;">`ACT_DOTA_ECHO_SLAM`</mark>                     | 1539  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_1_END`</mark>            | 1540  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2_END`</mark>            | 1541  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_3_END`</mark>            | 1542  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_4_END`</mark>            | 1543  |
| <mark style="color:green;">`ACT_MIRANA_LEAP_END`</mark>                    | 1544  |
| <mark style="color:green;">`ACT_WAVEFORM_START`</mark>                     | 1545  |
| <mark style="color:green;">`ACT_WAVEFORM_END`</mark>                       | 1546  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_ROT`</mark>              | 1547  |
| <mark style="color:green;">`ACT_DOTA_DIE_SPECIAL`</mark>                   | 1548  |
| <mark style="color:green;">`ACT_DOTA_RATTLETRAP_BATTERYASSAULT`</mark>     | 1549  |
| <mark style="color:green;">`ACT_DOTA_RATTLETRAP_POWERCOGS`</mark>          | 1550  |
| <mark style="color:green;">`ACT_DOTA_RATTLETRAP_HOOKSHOT_START`</mark>     | 1551  |
| <mark style="color:green;">`ACT_DOTA_RATTLETRAP_HOOKSHOT_LOOP`</mark>      | 1552  |
| <mark style="color:green;">`ACT_DOTA_RATTLETRAP_HOOKSHOT_END`</mark>       | 1553  |
| <mark style="color:green;">`ACT_STORM_SPIRIT_OVERLOAD_RUN_OVERRIDE`</mark> | 1554  |
| <mark style="color:green;">`ACT_DOTA_TINKER_REARM1`</mark>                 | 1555  |
| <mark style="color:green;">`ACT_DOTA_TINKER_REARM2`</mark>                 | 1556  |
| <mark style="color:green;">`ACT_DOTA_TINKER_REARM3`</mark>                 | 1557  |
| <mark style="color:green;">`ACT_TINY_AVALANCHE`</mark>                     | 1558  |
| <mark style="color:green;">`ACT_TINY_TOSS`</mark>                          | 1559  |
| <mark style="color:green;">`ACT_TINY_GROWL`</mark>                         | 1560  |
| <mark style="color:green;">`ACT_DOTA_WEAVERBUG_ATTACH`</mark>              | 1561  |
| <mark style="color:green;">`ACT_DOTA_CAST_WILD_AXES_END`</mark>            | 1562  |
| <mark style="color:green;">`ACT_DOTA_CAST_LIFE_BREAK_START`</mark>         | 1563  |
| <mark style="color:green;">`ACT_DOTA_CAST_LIFE_BREAK_END`</mark>           | 1564  |
| <mark style="color:green;">`ACT_DOTA_NIGHTSTALKER_TRANSITION`</mark>       | 1565  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_RAGE`</mark>              | 1566  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_OPEN_WOUNDS`</mark>       | 1567  |
| <mark style="color:green;">`ACT_DOTA_SAND_KING_BURROW_IN`</mark>           | 1568  |
| <mark style="color:green;">`ACT_DOTA_SAND_KING_BURROW_OUT`</mark>          | 1569  |
| <mark style="color:green;">`ACT_DOTA_EARTHSHAKER_TOTEM_ATTACK`</mark>      | 1570  |
| <mark style="color:green;">`ACT_DOTA_WHEEL_LAYER`</mark>                   | 1571  |
| <mark style="color:green;">`ACT_DOTA_ALCHEMIST_CHEMICAL_RAGE_START`</mark> | 1572  |
| <mark style="color:green;">`ACT_DOTA_ALCHEMIST_CONCOCTION`</mark>          | 1573  |
| <mark style="color:green;">`ACT_DOTA_JAKIRO_LIQUIDFIRE_START`</mark>       | 1574  |
| <mark style="color:green;">`ACT_DOTA_JAKIRO_LIQUIDFIRE_LOOP`</mark>        | 1575  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_INFEST`</mark>            | 1576  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_INFEST_END`</mark>        | 1577  |
| <mark style="color:green;">`ACT_DOTA_LASSO_LOOP`</mark>                    | 1578  |
| <mark style="color:green;">`ACT_DOTA_ALCHEMIST_CONCOCTION_THROW`</mark>    | 1579  |
| <mark style="color:green;">`ACT_DOTA_ALCHEMIST_CHEMICAL_RAGE_END`</mark>   | 1580  |
| <mark style="color:green;">`ACT_DOTA_CAST_COLD_SNAP`</mark>                | 1581  |
| <mark style="color:green;">`ACT_DOTA_CAST_GHOST_WALK`</mark>               | 1582  |
| <mark style="color:green;">`ACT_DOTA_CAST_TORNADO`</mark>                  | 1583  |
| <mark style="color:green;">`ACT_DOTA_CAST_EMP`</mark>                      | 1584  |
| <mark style="color:green;">`ACT_DOTA_CAST_ALACRITY`</mark>                 | 1585  |
| <mark style="color:green;">`ACT_DOTA_CAST_CHAOS_METEOR`</mark>             | 1586  |
| <mark style="color:green;">`ACT_DOTA_CAST_SUN_STRIKE`</mark>               | 1587  |
| <mark style="color:green;">`ACT_DOTA_CAST_FORGE_SPIRIT`</mark>             | 1588  |
| <mark style="color:green;">`ACT_DOTA_CAST_ICE_WALL`</mark>                 | 1589  |
| <mark style="color:green;">`ACT_DOTA_CAST_DEAFENING_BLAST`</mark>          | 1590  |
| <mark style="color:green;">`ACT_DOTA_VICTORY`</mark>                       | 1591  |
| <mark style="color:green;">`ACT_DOTA_DEFEAT`</mark>                        | 1592  |
| <mark style="color:green;">`ACT_DOTA_SPIRIT_BREAKER_CHARGE_POSE`</mark>    | 1593  |
| <mark style="color:green;">`ACT_DOTA_SPIRIT_BREAKER_CHARGE_END`</mark>     | 1594  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT`</mark>                      | 1595  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_END`</mark>                  | 1596  |
| <mark style="color:green;">`ACT_DOTA_CAST_REFRACTION`</mark>               | 1597  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_7`</mark>                | 1598  |
| <mark style="color:green;">`ACT_DOTA_CANCEL_SIREN_SONG`</mark>             | 1599  |
| <mark style="color:green;">`ACT_DOTA_CHANNEL_ABILITY_7`</mark>             | 1600  |
| <mark style="color:green;">`ACT_DOTA_LOADOUT`</mark>                       | 1601  |
| <mark style="color:green;">`ACT_DOTA_FORCESTAFF_END`</mark>                | 1602  |
| <mark style="color:green;">`ACT_DOTA_POOF_END`</mark>                      | 1603  |
| <mark style="color:green;">`ACT_DOTA_SLARK_POUNCE`</mark>                  | 1604  |
| <mark style="color:green;">`ACT_DOTA_MAGNUS_SKEWER_START`</mark>           | 1605  |
| <mark style="color:green;">`ACT_DOTA_MAGNUS_SKEWER_END`</mark>             | 1606  |
| <mark style="color:green;">`ACT_DOTA_MEDUSA_STONE_GAZE`</mark>             | 1607  |
| <mark style="color:green;">`ACT_DOTA_RELAX_START`</mark>                   | 1608  |
| <mark style="color:green;">`ACT_DOTA_RELAX_LOOP`</mark>                    | 1609  |
| <mark style="color:green;">`ACT_DOTA_RELAX_END`</mark>                     | 1610  |
| <mark style="color:green;">`ACT_DOTA_CENTAUR_STAMPEDE`</mark>              | 1611  |
| <mark style="color:green;">`ACT_DOTA_BELLYACHE_START`</mark>               | 1612  |
| <mark style="color:green;">`ACT_DOTA_BELLYACHE_LOOP`</mark>                | 1613  |
| <mark style="color:green;">`ACT_DOTA_BELLYACHE_END`</mark>                 | 1614  |
| <mark style="color:green;">`ACT_DOTA_ROQUELAIRE_LAND`</mark>               | 1615  |
| <mark style="color:green;">`ACT_DOTA_ROQUELAIRE_LAND_IDLE`</mark>          | 1616  |
| <mark style="color:green;">`ACT_DOTA_GREEVIL_CAST`</mark>                  | 1617  |
| <mark style="color:green;">`ACT_DOTA_GREEVIL_OVERRIDE_ABILITY`</mark>      | 1618  |
| <mark style="color:green;">`ACT_DOTA_GREEVIL_HOOK_START`</mark>            | 1619  |
| <mark style="color:green;">`ACT_DOTA_GREEVIL_HOOK_END`</mark>              | 1620  |
| <mark style="color:green;">`ACT_DOTA_GREEVIL_BLINK_BONE`</mark>            | 1621  |
| <mark style="color:green;">`ACT_DOTA_IDLE_SLEEPING`</mark>                 | 1622  |
| <mark style="color:green;">`ACT_DOTA_INTRO`</mark>                         | 1623  |
| <mark style="color:green;">`ACT_DOTA_GESTURE_POINT`</mark>                 | 1624  |
| <mark style="color:green;">`ACT_DOTA_GESTURE_ACCENT`</mark>                | 1625  |
| <mark style="color:green;">`ACT_DOTA_SLEEPING_END`</mark>                  | 1626  |
| <mark style="color:green;">`ACT_DOTA_AMBUSH`</mark>                        | 1627  |
| <mark style="color:green;">`ACT_DOTA_ITEM_LOOK`</mark>                     | 1628  |
| <mark style="color:green;">`ACT_DOTA_STARTLE`</mark>                       | 1629  |
| <mark style="color:green;">`ACT_DOTA_FRUSTRATION`</mark>                   | 1630  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_REACT`</mark>                | 1631  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_END_REACT`</mark>            | 1632  |
| <mark style="color:green;">`ACT_DOTA_SHRUG`</mark>                         | 1633  |
| <mark style="color:green;">`ACT_DOTA_RELAX_LOOP_END`</mark>                | 1634  |
| <mark style="color:green;">`ACT_DOTA_PRESENT_ITEM`</mark>                  | 1635  |
| <mark style="color:green;">`ACT_DOTA_IDLE_IMPATIENT`</mark>                | 1636  |
| <mark style="color:green;">`ACT_DOTA_SHARPEN_WEAPON`</mark>                | 1637  |
| <mark style="color:green;">`ACT_DOTA_SHARPEN_WEAPON_OUT`</mark>            | 1638  |
| <mark style="color:green;">`ACT_DOTA_IDLE_SLEEPING_END`</mark>             | 1639  |
| <mark style="color:green;">`ACT_DOTA_BRIDGE_DESTROY`</mark>                | 1640  |
| <mark style="color:green;">`ACT_DOTA_TAUNT_SNIPER`</mark>                  | 1641  |
| <mark style="color:green;">`ACT_DOTA_DEATH_BY_SNIPER`</mark>               | 1642  |
| <mark style="color:green;">`ACT_DOTA_LOOK_AROUND`</mark>                   | 1643  |
| <mark style="color:green;">`ACT_DOTA_CAGED_CREEP_RAGE`</mark>              | 1644  |
| <mark style="color:green;">`ACT_DOTA_CAGED_CREEP_RAGE_OUT`</mark>          | 1645  |
| <mark style="color:green;">`ACT_DOTA_CAGED_CREEP_SMASH`</mark>             | 1646  |
| <mark style="color:green;">`ACT_DOTA_CAGED_CREEP_SMASH_OUT`</mark>         | 1647  |
| <mark style="color:green;">`ACT_DOTA_IDLE_IMPATIENT_SWORD_TAP`</mark>      | 1648  |
| <mark style="color:green;">`ACT_DOTA_INTRO_LOOP`</mark>                    | 1649  |
| <mark style="color:green;">`ACT_DOTA_BRIDGE_THREAT`</mark>                 | 1650  |
| <mark style="color:green;">`ACT_DOTA_DAGON`</mark>                         | 1651  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2_ES_ROLL_START`</mark>  | 1652  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2_ES_ROLL`</mark>        | 1653  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2_ES_ROLL_END`</mark>    | 1654  |
| <mark style="color:green;">`ACT_DOTA_NIAN_PIN_START`</mark>                | 1655  |
| <mark style="color:green;">`ACT_DOTA_NIAN_PIN_LOOP`</mark>                 | 1656  |
| <mark style="color:green;">`ACT_DOTA_NIAN_PIN_END`</mark>                  | 1657  |
| <mark style="color:green;">`ACT_DOTA_LEAP_STUN`</mark>                     | 1658  |
| <mark style="color:green;">`ACT_DOTA_LEAP_SWIPE`</mark>                    | 1659  |
| <mark style="color:green;">`ACT_DOTA_NIAN_INTRO_LEAP`</mark>               | 1660  |
| <mark style="color:green;">`ACT_DOTA_AREA_DENY`</mark>                     | 1661  |
| <mark style="color:green;">`ACT_DOTA_NIAN_PIN_TO_STUN`</mark>              | 1662  |
| <mark style="color:green;">`ACT_DOTA_RAZE_1`</mark>                        | 1663  |
| <mark style="color:green;">`ACT_DOTA_RAZE_2`</mark>                        | 1664  |
| <mark style="color:green;">`ACT_DOTA_RAZE_3`</mark>                        | 1665  |
| <mark style="color:green;">`ACT_DOTA_UNDYING_DECAY`</mark>                 | 1666  |
| <mark style="color:green;">`ACT_DOTA_UNDYING_SOUL_RIP`</mark>              | 1667  |
| <mark style="color:green;">`ACT_DOTA_UNDYING_TOMBSTONE`</mark>             | 1668  |
| <mark style="color:green;">`ACT_DOTA_WHIRLING_AXES_RANGED`</mark>          | 1669  |
| <mark style="color:green;">`ACT_DOTA_SHALLOW_GRAVE`</mark>                 | 1670  |
| <mark style="color:green;">`ACT_DOTA_COLD_FEET`</mark>                     | 1671  |
| <mark style="color:green;">`ACT_DOTA_ICE_VORTEX`</mark>                    | 1672  |
| <mark style="color:green;">`ACT_DOTA_CHILLING_TOUCH`</mark>                | 1673  |
| <mark style="color:green;">`ACT_DOTA_ENFEEBLE`</mark>                      | 1674  |
| <mark style="color:green;">`ACT_DOTA_FATAL_BONDS`</mark>                   | 1675  |
| <mark style="color:green;">`ACT_DOTA_MIDNIGHT_PULSE`</mark>                | 1676  |
| <mark style="color:green;">`ACT_DOTA_ANCESTRAL_SPIRIT`</mark>              | 1677  |
| <mark style="color:green;">`ACT_DOTA_THUNDER_STRIKE`</mark>                | 1678  |
| <mark style="color:green;">`ACT_DOTA_KINETIC_FIELD`</mark>                 | 1679  |
| <mark style="color:green;">`ACT_DOTA_STATIC_STORM`</mark>                  | 1680  |
| <mark style="color:green;">`ACT_DOTA_MINI_TAUNT`</mark>                    | 1681  |
| <mark style="color:green;">`ACT_DOTA_ARCTIC_BURN_END`</mark>               | 1682  |
| <mark style="color:green;">`ACT_DOTA_LOADOUT_RARE`</mark>                  | 1683  |
| <mark style="color:green;">`ACT_DOTA_SWIM`</mark>                          | 1684  |
| <mark style="color:green;">`ACT_DOTA_FLEE`</mark>                          | 1685  |
| <mark style="color:green;">`ACT_DOTA_TROT`</mark>                          | 1686  |
| <mark style="color:green;">`ACT_DOTA_SHAKE`</mark>                         | 1687  |
| <mark style="color:green;">`ACT_DOTA_SWIM_IDLE`</mark>                     | 1688  |
| <mark style="color:green;">`ACT_DOTA_WAIT_IDLE`</mark>                     | 1689  |
| <mark style="color:green;">`ACT_DOTA_GREET`</mark>                         | 1690  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_COOP_START`</mark>           | 1691  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_COOP_WAIT`</mark>            | 1692  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_COOP_END`</mark>             | 1693  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_COOP_EXIT`</mark>            | 1694  |
| <mark style="color:green;">`ACT_DOTA_SHOPKEEPER_PET_INTERACT`</mark>       | 1695  |
| <mark style="color:green;">`ACT_DOTA_ITEM_PICKUP`</mark>                   | 1696  |
| <mark style="color:green;">`ACT_DOTA_ITEM_DROP`</mark>                     | 1697  |
| <mark style="color:green;">`ACT_DOTA_CAPTURE_PET`</mark>                   | 1698  |
| <mark style="color:green;">`ACT_DOTA_PET_WARD_OBSERVER`</mark>             | 1699  |
| <mark style="color:green;">`ACT_DOTA_PET_WARD_SENTRY`</mark>               | 1700  |
| <mark style="color:green;">`ACT_DOTA_PET_LEVEL`</mark>                     | 1701  |
| <mark style="color:green;">`ACT_DOTA_CAST_BURROW_END`</mark>               | 1702  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_ASSIMILATE`</mark>        | 1703  |
| <mark style="color:green;">`ACT_DOTA_LIFESTEALER_EJECT`</mark>             | 1704  |
| <mark style="color:green;">`ACT_DOTA_ATTACK_EVENT_BASH`</mark>             | 1705  |
| <mark style="color:green;">`ACT_DOTA_CAPTURE_RARE`</mark>                  | 1706  |
| <mark style="color:green;">`ACT_DOTA_AW_MAGNETIC_FIELD`</mark>             | 1707  |
| <mark style="color:green;">`ACT_DOTA_CAST_GHOST_SHIP`</mark>               | 1708  |
| <mark style="color:green;">`ACT_DOTA_FXANIM`</mark>                        | 1709  |
| <mark style="color:green;">`ACT_DOTA_VICTORY_START`</mark>                 | 1710  |
| <mark style="color:green;">`ACT_DOTA_DEFEAT_START`</mark>                  | 1711  |
| <mark style="color:green;">`ACT_DOTA_DP_SPIRIT_SIPHON`</mark>              | 1712  |
| <mark style="color:green;">`ACT_DOTA_TRICKS_END`</mark>                    | 1713  |
| <mark style="color:green;">`ACT_DOTA_ES_STONE_CALLER`</mark>               | 1714  |
| <mark style="color:green;">`ACT_DOTA_MK_STRIKE`</mark>                     | 1715  |
| <mark style="color:green;">`ACT_DOTA_VERSUS`</mark>                        | 1716  |
| <mark style="color:green;">`ACT_DOTA_CAPTURE_CARD`</mark>                  | 1717  |
| <mark style="color:green;">`ACT_DOTA_MK_SPRING_SOAR`</mark>                | 1718  |
| <mark style="color:green;">`ACT_DOTA_MK_SPRING_END`</mark>                 | 1719  |
| <mark style="color:green;">`ACT_DOTA_MK_TREE_SOAR`</mark>                  | 1720  |
| <mark style="color:green;">`ACT_DOTA_MK_TREE_END`</mark>                   | 1721  |
| <mark style="color:green;">`ACT_DOTA_MK_FUR_ARMY`</mark>                   | 1722  |
| <mark style="color:green;">`ACT_DOTA_MK_SPRING_CAST`</mark>                | 1723  |
| <mark style="color:green;">`ACT_DOTA_NECRO_GHOST_SHROUD`</mark>            | 1724  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_ARCANA`</mark>               | 1725  |
| <mark style="color:green;">`ACT_DOTA_SLIDE`</mark>                         | 1726  |
| <mark style="color:green;">`ACT_DOTA_SLIDE_LOOP`</mark>                    | 1727  |
| <mark style="color:green;">`ACT_DOTA_GENERIC_CHANNEL_1`</mark>             | 1728  |
| <mark style="color:green;">`ACT_DOTA_GS_SOUL_CHAIN`</mark>                 | 1729  |
| <mark style="color:green;">`ACT_DOTA_GS_INK_CREATURE`</mark>               | 1730  |
| <mark style="color:green;">`ACT_DOTA_TRANSITION`</mark>                    | 1731  |
| <mark style="color:green;">`ACT_DOTA_BLINK_DAGGER`</mark>                  | 1732  |
| <mark style="color:green;">`ACT_DOTA_BLINK_DAGGER_END`</mark>              | 1733  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_ATTACK`</mark>           | 1734  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_IDLE`</mark>             | 1735  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_DIE`</mark>              | 1736  |
| <mark style="color:green;">`ACT_DOTA_CAST_COLD_SNAP_ORB`</mark>            | 1737  |
| <mark style="color:green;">`ACT_DOTA_CAST_GHOST_WALK_ORB`</mark>           | 1738  |
| <mark style="color:green;">`ACT_DOTA_CAST_TORNADO_ORB`</mark>              | 1739  |
| <mark style="color:green;">`ACT_DOTA_CAST_EMP_ORB`</mark>                  | 1740  |
| <mark style="color:green;">`ACT_DOTA_CAST_ALACRITY_ORB`</mark>             | 1741  |
| <mark style="color:green;">`ACT_DOTA_CAST_CHAOS_METEOR_ORB`</mark>         | 1742  |
| <mark style="color:green;">`ACT_DOTA_CAST_SUN_STRIKE_ORB`</mark>           | 1743  |
| <mark style="color:green;">`ACT_DOTA_CAST_FORGE_SPIRIT_ORB`</mark>         | 1744  |
| <mark style="color:green;">`ACT_DOTA_CAST_ICE_WALL_ORB`</mark>             | 1745  |
| <mark style="color:green;">`ACT_DOTA_CAST_DEAFENING_BLAST_ORB`</mark>      | 1746  |
| <mark style="color:green;">`ACT_DOTA_NOTICE`</mark>                        | 1747  |
| <mark style="color:green;">`ACT_DOTA_CAST_ABILITY_2_ALLY`</mark>           | 1748  |
| <mark style="color:green;">`ACT_DOTA_SHUFFLE_L`</mark>                     | 1749  |
| <mark style="color:green;">`ACT_DOTA_SHUFFLE_R`</mark>                     | 1750  |
| <mark style="color:green;">`ACT_DOTA_OVERRIDE_LOADOUT`</mark>              | 1751  |
| <mark style="color:green;">`ACT_DOTA_TAUNT_SPECIAL`</mark>                 | 1752  |
| <mark style="color:green;">`ACT_DOTA_TELEPORT_START`</mark>                | 1753  |
| <mark style="color:green;">`ACT_DOTA_GENERIC_CHANNEL_1_START`</mark>       | 1754  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_IDLE_RARE`</mark>        | 1755  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_TAUNT`</mark>            | 1756  |
| <mark style="color:green;">`ACT_DOTA_CUSTOM_TOWER_HIGH_FIVE`</mark>        | 1757  |
| <mark style="color:green;">`ACT_DOTA_ATTACK_SPECIAL`</mark>                | 1758  |
| <mark style="color:green;">`ACT_DOTA_TRANSITION_IDLE`</mark>               | 1759  |
| <mark style="color:green;">`ACT_DOTA_PIERCE_THE_VEIL`</mark>               | 1760  |
| <mark style="color:green;">`ACT_DOTA_RUN_RARE`</mark>                      | 1761  |
| <mark style="color:green;">`ACT_DOTA_VIPER_DIVE`</mark>                    | 1762  |
| <mark style="color:green;">`ACT_DOTA_VIPER_DIVE_END`</mark>                | 1763  |
| <mark style="color:green;">`ACT_DOTA_MK_STRIKE_END`</mark>                 | 1764  |

## <mark style="color:purple;">Enum.Attributes</mark>

| Key                                                          | Value      |
| ------------------------------------------------------------ | ---------- |
| <mark style="color:green;">`DOTA_ATTRIBUTE_STRENGTH`</mark>  | 0          |
| <mark style="color:green;">`DOTA_ATTRIBUTE_AGILITY`</mark>   | 1          |
| <mark style="color:green;">`DOTA_ATTRIBUTE_INTELLECT`</mark> | 2          |
| <mark style="color:green;">`DOTA_ATTRIBUTE_ALL`</mark>       | 3          |
| <mark style="color:green;">`DOTA_ATTRIBUTE_MAX`</mark>       | 4          |
| <mark style="color:green;">`DOTA_ATTRIBUTE_INVALID`</mark>   | 4294967295 |

## <mark style="color:purple;">Enum.UnitTypeFlags</mark>

| Key                                                      | Value |
| -------------------------------------------------------- | ----- |
| <mark style="color:green;">`TYPE_HERO`</mark>            |       |
| <mark style="color:green;">`TYPE_CONSIDERED_HERO`</mark> |       |
| <mark style="color:green;">`TYPE_TOWER`</mark>           |       |
| <mark style="color:green;">`TYPE_STRUCTURE`</mark>       |       |
| <mark style="color:green;">`TYPE_ANCIENT`</mark>         |       |
| <mark style="color:green;">`TYPE_BARRACKS`</mark>        |       |
| <mark style="color:green;">`TYPE_CREEP`</mark>           |       |
| <mark style="color:green;">`TYPE_COURIER`</mark>         |       |
| <mark style="color:green;">`TYPE_SHOP`</mark>            |       |
| <mark style="color:green;">`TYPE_LANE_CREEP`</mark>      |       |
| <mark style="color:green;">`TYPE_WARD`</mark>            |       |
| <mark style="color:green;">`TYPE_ROSHAN`</mark>          |       |

## <mark style="color:purple;">Enum.UnitOrder</mark>

| Key                                                                                   | Value |
| ------------------------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_UNIT_ORDER_NONE`</mark>                              | 0     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_MOVE_TO_POSITION`</mark>                  | 1     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_MOVE_TO_TARGET`</mark>                    | 2     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_ATTACK_MOVE`</mark>                       | 3     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_ATTACK_TARGET`</mark>                     | 4     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_POSITION`</mark>                     | 5     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_TARGET`</mark>                       | 6     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_TARGET_TREE`</mark>                  | 7     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_NO_TARGET`</mark>                    | 8     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_TOGGLE`</mark>                       | 9     |
| <mark style="color:green;">`DOTA_UNIT_ORDER_HOLD_POSITION`</mark>                     | 10    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_TRAIN_ABILITY`</mark>                     | 11    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_DROP_ITEM`</mark>                         | 12    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_GIVE_ITEM`</mark>                         | 13    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PICKUP_ITEM`</mark>                       | 14    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PICKUP_RUNE`</mark>                       | 15    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PURCHASE_ITEM`</mark>                     | 16    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_SELL_ITEM`</mark>                         | 17    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_DISASSEMBLE_ITEM`</mark>                  | 18    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_MOVE_ITEM`</mark>                         | 19    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_TOGGLE_AUTO`</mark>                  | 20    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_STOP`</mark>                              | 21    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_TAUNT`</mark>                             | 22    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_BUYBACK`</mark>                           | 23    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_GLYPH`</mark>                             | 24    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_EJECT_ITEM_FROM_STASH`</mark>             | 25    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_RUNE`</mark>                         | 26    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PING_ABILITY`</mark>                      | 27    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_MOVE_TO_DIRECTION`</mark>                 | 28    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PATROL`</mark>                            | 29    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_VECTOR_TARGET_POSITION`</mark>            | 30    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_RADAR`</mark>                             | 31    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_SET_ITEM_COMBINE_LOCK`</mark>             | 32    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CONTINUE`</mark>                          | 33    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_VECTOR_TARGET_CANCELED`</mark>            | 34    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_RIVER_PAINT`</mark>                  | 35    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_PREGAME_ADJUST_ITEM_ASSIGNMENT`</mark>    | 36    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_DROP_ITEM_AT_FOUNTAIN`</mark>             | 37    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_TAKE_ITEM_FROM_NEUTRAL_ITEM_STASH`</mark> | 38    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_MOVE_RELATIVE`</mark>                     | 39    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CAST_TOGGLE_ALT`</mark>                   | 40    |
| <mark style="color:green;">`DOTA_UNIT_ORDER_CONSUME_ITEM`</mark>                      | 41    |

## <mark style="color:purple;">Enum.PlayerOrderIssuer</mark>

| Key                                                                     | Value |
| ----------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_ORDER_ISSUER_SELECTED_UNITS`</mark>    | 0     |
| <mark style="color:green;">`DOTA_ORDER_ISSUER_CURRENT_UNIT_ONLY`</mark> | 1     |
| <mark style="color:green;">`DOTA_ORDER_ISSUER_HERO_ONLY`</mark>         | 2     |
| <mark style="color:green;">`DOTA_ORDER_ISSUER_PASSED_UNIT_ONLY`</mark>  | 3     |

## <mark style="color:purple;">Enum.GameState</mark>

| Key                                                                               | Value |
| --------------------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_INIT`</mark>                     | 0     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD`</mark> | 1     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_HERO_SELECTION`</mark>           | 2     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_STRATEGY_TIME`</mark>            | 3     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_PRE_GAME`</mark>                 | 4     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_GAME_IN_PROGRESS`</mark>         | 5     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_POST_GAME`</mark>                | 6     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_DISCONNECT`</mark>               | 7     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_TEAM_SHOWCASE`</mark>            | 8     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP`</mark>        | 9     |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_WAIT_FOR_MAP_TO_LOAD`</mark>     | 10    |
| <mark style="color:green;">`DOTA_GAMERULES_STATE_LAST`</mark>                     | 13    |

## <mark style="color:purple;">Enum.GameMode</mark>

| Key                                                                 | Value |
| ------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_GAMEMODE_NONE`</mark>              | 0     |
| <mark style="color:green;">`DOTA_GAMEMODE_AP`</mark>                | 1     |
| <mark style="color:green;">`DOTA_GAMEMODE_CM`</mark>                | 2     |
| <mark style="color:green;">`DOTA_GAMEMODE_RD`</mark>                | 3     |
| <mark style="color:green;">`DOTA_GAMEMODE_SD`</mark>                | 4     |
| <mark style="color:green;">`DOTA_GAMEMODE_AR`</mark>                | 5     |
| <mark style="color:green;">`DOTA_GAMEMODE_INTRO`</mark>             | 6     |
| <mark style="color:green;">`DOTA_GAMEMODE_HW`</mark>                | 7     |
| <mark style="color:green;">`DOTA_GAMEMODE_REVERSE_CM`</mark>        | 8     |
| <mark style="color:green;">`DOTA_GAMEMODE_XMAS`</mark>              | 9     |
| <mark style="color:green;">`DOTA_GAMEMODE_TUTORIAL`</mark>          | 10    |
| <mark style="color:green;">`DOTA_GAMEMODE_MO`</mark>                | 11    |
| <mark style="color:green;">`DOTA_GAMEMODE_LP`</mark>                | 12    |
| <mark style="color:green;">`DOTA_GAMEMODE_POOL1`</mark>             | 13    |
| <mark style="color:green;">`DOTA_GAMEMODE_FH`</mark>                | 14    |
| <mark style="color:green;">`DOTA_GAMEMODE_CUSTOM`</mark>            | 15    |
| <mark style="color:green;">`DOTA_GAMEMODE_CD`</mark>                | 16    |
| <mark style="color:green;">`DOTA_GAMEMODE_BD`</mark>                | 17    |
| <mark style="color:green;">`DOTA_GAMEMODE_ABILITY_DRAFT`</mark>     | 18    |
| <mark style="color:green;">`DOTA_GAMEMODE_1V1MID`</mark>            | 21    |
| <mark style="color:green;">`DOTA_GAMEMODE_ALL_DRAFT`</mark>         | 22    |
| <mark style="color:green;">`DOTA_GAMEMODE_TURBO`</mark>             | 23    |
| <mark style="color:green;">`DOTA_GAMEMODE_MUTATION`</mark>          | 24    |
| <mark style="color:green;">`DOTA_GAMEMODE_COACHES_CHALLENGE`</mark> | 25    |

## <mark style="color:purple;">Enum.Flow</mark>

| Key                                               | Value |
| ------------------------------------------------- | ----- |
| <mark style="color:green;">`FLOW_OUTGOING`</mark> | 0     |
| <mark style="color:green;">`FLOW_INCOMING`</mark> | 1     |
| <mark style="color:green;">`MAX_FLOWS`</mark>     | 2     |

## <mark style="color:purple;">Enum.ParticleAttachment</mark>

| Key                                                             | Value      |
| --------------------------------------------------------------- | ---------- |
| <mark style="color:green;">`PATTACH_INVALID`</mark>             | 4294967295 |
| <mark style="color:green;">`PATTACH_ABSORIGIN`</mark>           | 0          |
| <mark style="color:green;">`PATTACH_ABSORIGIN_FOLLOW`</mark>    | 1          |
| <mark style="color:green;">`PATTACH_CUSTOMORIGIN`</mark>        | 2          |
| <mark style="color:green;">`PATTACH_CUSTOMORIGIN_FOLLOW`</mark> | 3          |
| <mark style="color:green;">`PATTACH_POINT`</mark>               | 4          |
| <mark style="color:green;">`PATTACH_POINT_FOLLOW`</mark>        | 5          |
| <mark style="color:green;">`PATTACH_EYES_FOLLOW`</mark>         | 6          |
| <mark style="color:green;">`PATTACH_OVERHEAD_FOLLOW`</mark>     | 7          |
| <mark style="color:green;">`PATTACH_WORLDORIGIN`</mark>         | 8          |
| <mark style="color:green;">`PATTACH_ROOTBONE_FOLLOW`</mark>     | 9          |
| <mark style="color:green;">`PATTACH_RENDERORIGIN_FOLLOW`</mark> | 10         |
| <mark style="color:green;">`PATTACH_MAIN_VIEW`</mark>           | 11         |
| <mark style="color:green;">`PATTACH_WATERWAKE`</mark>           | 12         |
| <mark style="color:green;">`PATTACH_CENTER_FOLLOW`</mark>       | 13         |
| <mark style="color:green;">`PATTACH_CUSTOM_GAME_STATE_1`</mark> | 14         |
| <mark style="color:green;">`PATTACH_HEALTHBAR`</mark>           | 15         |
| <mark style="color:green;">`MAX_PATTACH_TYPES`</mark>           | 16         |

## <mark style="color:purple;">Enum.ButtonCode</mark>

| Key                                                      | Value |
| -------------------------------------------------------- | ----- |
| <mark style="color:green;">`BUTTON_CODE_INVALID`</mark>  |       |
| <mark style="color:green;">`BUTTON_CODE_NONE`</mark>     |       |
| <mark style="color:green;">`KEY_FIRST`</mark>            |       |
| <mark style="color:green;">`KEY_NONE`</mark>             |       |
| <mark style="color:green;">`KEY_0`</mark>                |       |
| <mark style="color:green;">`KEY_1`</mark>                |       |
| <mark style="color:green;">`KEY_2`</mark>                |       |
| <mark style="color:green;">`KEY_3`</mark>                |       |
| <mark style="color:green;">`KEY_4`</mark>                |       |
| <mark style="color:green;">`KEY_5`</mark>                |       |
| <mark style="color:green;">`KEY_6`</mark>                |       |
| <mark style="color:green;">`KEY_7`</mark>                |       |
| <mark style="color:green;">`KEY_8`</mark>                |       |
| <mark style="color:green;">`KEY_9`</mark>                |       |
| <mark style="color:green;">`KEY_A`</mark>                |       |
| <mark style="color:green;">`KEY_B`</mark>                |       |
| <mark style="color:green;">`KEY_C`</mark>                |       |
| <mark style="color:green;">`KEY_D`</mark>                |       |
| <mark style="color:green;">`KEY_E`</mark>                |       |
| <mark style="color:green;">`KEY_F`</mark>                |       |
| <mark style="color:green;">`KEY_G`</mark>                |       |
| <mark style="color:green;">`KEY_H`</mark>                |       |
| <mark style="color:green;">`KEY_I`</mark>                |       |
| <mark style="color:green;">`KEY_J`</mark>                |       |
| <mark style="color:green;">`KEY_K`</mark>                |       |
| <mark style="color:green;">`KEY_L`</mark>                |       |
| <mark style="color:green;">`KEY_M`</mark>                |       |
| <mark style="color:green;">`KEY_N`</mark>                |       |
| <mark style="color:green;">`KEY_O`</mark>                |       |
| <mark style="color:green;">`KEY_P`</mark>                |       |
| <mark style="color:green;">`KEY_Q`</mark>                |       |
| <mark style="color:green;">`KEY_R`</mark>                |       |
| <mark style="color:green;">`KEY_S`</mark>                |       |
| <mark style="color:green;">`KEY_T`</mark>                |       |
| <mark style="color:green;">`KEY_U`</mark>                |       |
| <mark style="color:green;">`KEY_V`</mark>                |       |
| <mark style="color:green;">`KEY_W`</mark>                |       |
| <mark style="color:green;">`KEY_X`</mark>                |       |
| <mark style="color:green;">`KEY_Y`</mark>                |       |
| <mark style="color:green;">`KEY_Z`</mark>                |       |
| <mark style="color:green;">`KEY_PAD_0`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_1`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_2`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_3`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_4`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_5`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_6`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_7`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_8`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_9`</mark>            |       |
| <mark style="color:green;">`KEY_PAD_DIVIDE`</mark>       |       |
| <mark style="color:green;">`KEY_PAD_MULTIPLY`</mark>     |       |
| <mark style="color:green;">`KEY_PAD_MINUS`</mark>        |       |
| <mark style="color:green;">`KEY_PAD_PLUS`</mark>         |       |
| <mark style="color:green;">`KEY_PAD_ENTER`</mark>        |       |
| <mark style="color:green;">`KEY_PAD_DECIMAL`</mark>      |       |
| <mark style="color:green;">`KEY_LBRACKET`</mark>         |       |
| <mark style="color:green;">`KEY_RBRACKET`</mark>         |       |
| <mark style="color:green;">`KEY_SEMICOLON`</mark>        |       |
| <mark style="color:green;">`KEY_APOSTROPHE`</mark>       |       |
| <mark style="color:green;">`KEY_BACKQUOTE`</mark>        |       |
| <mark style="color:green;">`KEY_COMMA`</mark>            |       |
| <mark style="color:green;">`KEY_PERIOD`</mark>           |       |
| <mark style="color:green;">`KEY_SLASH`</mark>            |       |
| <mark style="color:green;">`KEY_BACKSLASH`</mark>        |       |
| <mark style="color:green;">`KEY_MINUS`</mark>            |       |
| <mark style="color:green;">`KEY_EQUAL`</mark>            |       |
| <mark style="color:green;">`KEY_ENTER`</mark>            |       |
| <mark style="color:green;">`KEY_SPACE`</mark>            |       |
| <mark style="color:green;">`KEY_BACKSPACE`</mark>        |       |
| <mark style="color:green;">`KEY_TAB`</mark>              |       |
| <mark style="color:green;">`KEY_CAPSLOCK`</mark>         |       |
| <mark style="color:green;">`KEY_NUMLOCK`</mark>          |       |
| <mark style="color:green;">`KEY_ESCAPE`</mark>           |       |
| <mark style="color:green;">`KEY_SCROLLLOCK`</mark>       |       |
| <mark style="color:green;">`KEY_INSERT`</mark>           |       |
| <mark style="color:green;">`KEY_DELETE`</mark>           |       |
| <mark style="color:green;">`KEY_HOME`</mark>             |       |
| <mark style="color:green;">`KEY_END`</mark>              |       |
| <mark style="color:green;">`KEY_PAGEUP`</mark>           |       |
| <mark style="color:green;">`KEY_PAGEDOWN`</mark>         |       |
| <mark style="color:green;">`KEY_BREAK`</mark>            |       |
| <mark style="color:green;">`KEY_LSHIFT`</mark>           |       |
| <mark style="color:green;">`KEY_RSHIFT`</mark>           |       |
| <mark style="color:green;">`KEY_LALT`</mark>             |       |
| <mark style="color:green;">`KEY_RALT`</mark>             |       |
| <mark style="color:green;">`KEY_LCONTROL`</mark>         |       |
| <mark style="color:green;">`KEY_RCONTROL`</mark>         |       |
| <mark style="color:green;">`KEY_LWIN`</mark>             |       |
| <mark style="color:green;">`KEY_RWIN`</mark>             |       |
| <mark style="color:green;">`KEY_APP`</mark>              |       |
| <mark style="color:green;">`KEY_UP`</mark>               |       |
| <mark style="color:green;">`KEY_LEFT`</mark>             |       |
| <mark style="color:green;">`KEY_DOWN`</mark>             |       |
| <mark style="color:green;">`KEY_RIGHT`</mark>            |       |
| <mark style="color:green;">`KEY_F1`</mark>               |       |
| <mark style="color:green;">`KEY_F2`</mark>               |       |
| <mark style="color:green;">`KEY_F3`</mark>               |       |
| <mark style="color:green;">`KEY_F4`</mark>               |       |
| <mark style="color:green;">`KEY_F5`</mark>               |       |
| <mark style="color:green;">`KEY_F6`</mark>               |       |
| <mark style="color:green;">`KEY_F7`</mark>               |       |
| <mark style="color:green;">`KEY_F8`</mark>               |       |
| <mark style="color:green;">`KEY_F9`</mark>               |       |
| <mark style="color:green;">`KEY_F10`</mark>              |       |
| <mark style="color:green;">`KEY_F11`</mark>              |       |
| <mark style="color:green;">`KEY_F12`</mark>              |       |
| <mark style="color:green;">`KEY_F13`</mark>              |       |
| <mark style="color:green;">`KEY_F14`</mark>              |       |
| <mark style="color:green;">`KEY_F15`</mark>              |       |
| <mark style="color:green;">`KEY_F16`</mark>              |       |
| <mark style="color:green;">`KEY_F17`</mark>              |       |
| <mark style="color:green;">`KEY_F18`</mark>              |       |
| <mark style="color:green;">`KEY_F19`</mark>              |       |
| <mark style="color:green;">`KEY_F20`</mark>              |       |
| <mark style="color:green;">`KEY_F21`</mark>              |       |
| <mark style="color:green;">`KEY_F22`</mark>              |       |
| <mark style="color:green;">`KEY_F23`</mark>              |       |
| <mark style="color:green;">`KEY_F24`</mark>              |       |
| <mark style="color:green;">`KEY_CAPSLOCKTOGGLE`</mark>   |       |
| <mark style="color:green;">`KEY_NUMLOCKTOGGLE`</mark>    |       |
| <mark style="color:green;">`KEY_SCROLLLOCKTOGGLE`</mark> |       |
| <mark style="color:green;">`KEY_MOUSE1`</mark>           |       |
| <mark style="color:green;">`KEY_MOUSE2`</mark>           |       |
| <mark style="color:green;">`KEY_MOUSE3`</mark>           |       |
| <mark style="color:green;">`KEY_MOUSE4`</mark>           |       |
| <mark style="color:green;">`KEY_MOUSE5`</mark>           |       |
| <mark style="color:green;">`KEY_MWHEELUP`</mark>         |       |
| <mark style="color:green;">`KEY_MWHEELDOWN`</mark>       |       |

## <mark style="color:purple;">Enum.FontCreate</mark>

| Key                                                       | Value |
| --------------------------------------------------------- | ----- |
| <mark style="color:green;">`FONTFLAG_NONE`</mark>         | 0     |
| <mark style="color:green;">`FONTFLAG_ITALIC`</mark>       | 1     |
| <mark style="color:green;">`FONTFLAG_UNDERLINE`</mark>    | 2     |
| <mark style="color:green;">`FONTFLAG_STRIKEOUT`</mark>    | 4     |
| <mark style="color:green;">`FONTFLAG_SYMBOL`</mark>       | 8     |
| <mark style="color:green;">`FONTFLAG_ANTIALIAS`</mark>    | 16    |
| <mark style="color:green;">`FONTFLAG_GAUSSIANBLUR`</mark> | 32    |
| <mark style="color:green;">`FONTFLAG_ROTARY`</mark>       | 64    |
| <mark style="color:green;">`FONTFLAG_DROPSHADOW`</mark>   | 128   |
| <mark style="color:green;">`FONTFLAG_ADDITIVE`</mark>     | 256   |
| <mark style="color:green;">`FONTFLAG_OUTLINE`</mark>      | 512   |
| <mark style="color:green;">`FONTFLAG_CUSTOM`</mark>       | 1024  |
| <mark style="color:green;">`FONTFLAG_BITMAP`</mark>       | 2048  |

## <mark style="color:purple;">Enum.FontWeight</mark>

| Key                                            | Value |
| ---------------------------------------------- | ----- |
| <mark style="color:green;">`THIN`</mark>       |       |
| <mark style="color:green;">`ULTRALIGHT`</mark> |       |
| <mark style="color:green;">`LIGHT`</mark>      |       |
| <mark style="color:green;">`NORMAL`</mark>     |       |
| <mark style="color:green;">`MEDIUM`</mark>     |       |
| <mark style="color:green;">`SEMIBOLD`</mark>   |       |
| <mark style="color:green;">`BOLD`</mark>       |       |
| <mark style="color:green;">`EXTRABOLD`</mark>  |       |
| <mark style="color:green;">`HEAVY`</mark>      |       |

## <mark style="color:purple;">Enum.WidgetType</mark>

| Key                                                    | Value |
| ------------------------------------------------------ | ----- |
| <mark style="color:green;">`MenuFirstTab`</mark>       |       |
| <mark style="color:green;">`MenuSection`</mark>        |       |
| <mark style="color:green;">`MenuSecondTab`</mark>      |       |
| <mark style="color:green;">`MenuThirdTab`</mark>       |       |
| <mark style="color:green;">`MenuGroup`</mark>          |       |
| <mark style="color:green;">`MenuSwitch`</mark>         |       |
| <mark style="color:green;">`MenuBind`</mark>           |       |
| <mark style="color:green;">`MenuSliderFloat`</mark>    |       |
| <mark style="color:green;">`MenuSliderInt`</mark>      |       |
| <mark style="color:green;">`MenuColorPicker`</mark>    |       |
| <mark style="color:green;">`MenuButton`</mark>         |       |
| <mark style="color:green;">`MenuComboBox`</mark>       |       |
| <mark style="color:green;">`MenuMultiComboBox`</mark>  |       |
| <mark style="color:green;">`MenuGearAttachment`</mark> |       |
| <mark style="color:green;">`MenuInputBox`</mark>       |       |
| <mark style="color:green;">`MenuMultiSelect`</mark>    |       |
| <mark style="color:green;">`MenuSearch`</mark>         |       |
| <mark style="color:green;">`MenuThemePicker`</mark>    |       |
| <mark style="color:green;">`MenuLabel`</mark>          |       |
| <mark style="color:green;">`MenuCustomBind`</mark>     |       |
| <mark style="color:green;">`MenuTypesCount`</mark>     |       |
| <mark style="color:green;">`MenuTypeInvalid`</mark>    |       |

## <mark style="color:purple;">Enum.GroupSide</mark>

## <mark style="color:purple;">Enum.PingType</mark>

| Key                                                       | Value |
| --------------------------------------------------------- | ----- |
| <mark style="color:green;">`PINGTYPE_INFO`</mark>         | 0     |
| <mark style="color:green;">`PINGTYPE_WARNING`</mark>      | 1     |
| <mark style="color:green;">`PINGTYPE_LOCATION`</mark>     | 2     |
| <mark style="color:green;">`PINGTYPE_DANGER`</mark>       | 3     |
| <mark style="color:green;">`PINGTYPE_ATTACK`</mark>       | 4     |
| <mark style="color:green;">`PINGTYPE_ENEMY_VISION`</mark> | 5     |
| <mark style="color:green;">`PINGTYPE_OWN_VISION`</mark>   | 6     |
| <mark style="color:green;">`PINGTYPE_LIKE`</mark>         | 7     |

## <mark style="color:purple;">Enum.DotaChatMessage</mark>

| Key                                                                                        | Value |
| ------------------------------------------------------------------------------------------ | ----- |
| <mark style="color:green;">`CHAT_MESSAGE_INVALID`</mark>                                   | -1    |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_KILL`</mark>                                 | 0     |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_DENY`</mark>                                 | 1     |
| <mark style="color:green;">`CHAT_MESSAGE_BARRACKS_KILL`</mark>                             | 2     |
| <mark style="color:green;">`CHAT_MESSAGE_TOWER_KILL`</mark>                                | 3     |
| <mark style="color:green;">`CHAT_MESSAGE_TOWER_DENY`</mark>                                | 4     |
| <mark style="color:green;">`CHAT_MESSAGE_FIRSTBLOOD`</mark>                                | 5     |
| <mark style="color:green;">`CHAT_MESSAGE_STREAK_KILL`</mark>                               | 6     |
| <mark style="color:green;">`CHAT_MESSAGE_BUYBACK`</mark>                                   | 7     |
| <mark style="color:green;">`CHAT_MESSAGE_AEGIS`</mark>                                     | 8     |
| <mark style="color:green;">`CHAT_MESSAGE_ROSHAN_KILL`</mark>                               | 9     |
| <mark style="color:green;">`CHAT_MESSAGE_COURIER_LOST`</mark>                              | 10    |
| <mark style="color:green;">`CHAT_MESSAGE_COURIER_RESPAWNED`</mark>                         | 11    |
| <mark style="color:green;">`CHAT_MESSAGE_GLYPH_USED`</mark>                                | 12    |
| <mark style="color:green;">`CHAT_MESSAGE_ITEM_PURCHASE`</mark>                             | 13    |
| <mark style="color:green;">`CHAT_MESSAGE_CONNECT`</mark>                                   | 14    |
| <mark style="color:green;">`CHAT_MESSAGE_DISCONNECT`</mark>                                | 15    |
| <mark style="color:green;">`CHAT_MESSAGE_DISCONNECT_WAIT_FOR_RECONNECT`</mark>             | 16    |
| <mark style="color:green;">`CHAT_MESSAGE_DISCONNECT_TIME_REMAINING`</mark>                 | 17    |
| <mark style="color:green;">`CHAT_MESSAGE_DISCONNECT_TIME_REMAINING_PLURAL`</mark>          | 18    |
| <mark style="color:green;">`CHAT_MESSAGE_RECONNECT`</mark>                                 | 19    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_LEFT`</mark>                               | 20    |
| <mark style="color:green;">`CHAT_MESSAGE_SAFE_TO_LEAVE`</mark>                             | 21    |
| <mark style="color:green;">`CHAT_MESSAGE_RUNE_PICKUP`</mark>                               | 22    |
| <mark style="color:green;">`CHAT_MESSAGE_RUNE_BOTTLE`</mark>                               | 23    |
| <mark style="color:green;">`CHAT_MESSAGE_INTHEBAG`</mark>                                  | 24    |
| <mark style="color:green;">`CHAT_MESSAGE_SECRETSHOP`</mark>                                | 25    |
| <mark style="color:green;">`CHAT_MESSAGE_ITEM_AUTOPURCHASED`</mark>                        | 26    |
| <mark style="color:green;">`CHAT_MESSAGE_ITEMS_COMBINED`</mark>                            | 27    |
| <mark style="color:green;">`CHAT_MESSAGE_SUPER_CREEPS`</mark>                              | 28    |
| <mark style="color:green;">`CHAT_MESSAGE_CANT_USE_ACTION_ITEM`</mark>                      | 29    |
| <mark style="color:green;">`CHAT_MESSAGE_CANTPAUSE`</mark>                                 | 31    |
| <mark style="color:green;">`CHAT_MESSAGE_NOPAUSESLEFT`</mark>                              | 32    |
| <mark style="color:green;">`CHAT_MESSAGE_CANTPAUSEYET`</mark>                              | 33    |
| <mark style="color:green;">`CHAT_MESSAGE_PAUSED`</mark>                                    | 34    |
| <mark style="color:green;">`CHAT_MESSAGE_UNPAUSE_COUNTDOWN`</mark>                         | 35    |
| <mark style="color:green;">`CHAT_MESSAGE_UNPAUSED`</mark>                                  | 36    |
| <mark style="color:green;">`CHAT_MESSAGE_AUTO_UNPAUSED`</mark>                             | 37    |
| <mark style="color:green;">`CHAT_MESSAGE_YOUPAUSED`</mark>                                 | 38    |
| <mark style="color:green;">`CHAT_MESSAGE_CANTUNPAUSETEAM`</mark>                           | 39    |
| <mark style="color:green;">`CHAT_MESSAGE_VOICE_TEXT_BANNED`</mark>                         | 41    |
| <mark style="color:green;">`CHAT_MESSAGE_SPECTATORS_WATCHING_THIS_GAME`</mark>             | 42    |
| <mark style="color:green;">`CHAT_MESSAGE_REPORT_REMINDER`</mark>                           | 43    |
| <mark style="color:green;">`CHAT_MESSAGE_ECON_ITEM`</mark>                                 | 44    |
| <mark style="color:green;">`CHAT_MESSAGE_TAUNT`</mark>                                     | 45    |
| <mark style="color:green;">`CHAT_MESSAGE_RANDOM`</mark>                                    | 46    |
| <mark style="color:green;">`CHAT_MESSAGE_RD_TURN`</mark>                                   | 47    |
| <mark style="color:green;">`CHAT_MESSAGE_DROP_RATE_BONUS`</mark>                           | 49    |
| <mark style="color:green;">`CHAT_MESSAGE_NO_BATTLE_POINTS`</mark>                          | 50    |
| <mark style="color:green;">`CHAT_MESSAGE_DENIED_AEGIS`</mark>                              | 51    |
| <mark style="color:green;">`CHAT_MESSAGE_INFORMATIONAL`</mark>                             | 52    |
| <mark style="color:green;">`CHAT_MESSAGE_AEGIS_STOLEN`</mark>                              | 53    |
| <mark style="color:green;">`CHAT_MESSAGE_ROSHAN_CANDY`</mark>                              | 54    |
| <mark style="color:green;">`CHAT_MESSAGE_ITEM_GIFTED`</mark>                               | 55    |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_KILL_WITH_GREEVIL`</mark>                    | 56    |
| <mark style="color:green;">`CHAT_MESSAGE_HOLDOUT_TOWER_DESTROYED`</mark>                   | 57    |
| <mark style="color:green;">`CHAT_MESSAGE_HOLDOUT_WALL_DESTROYED`</mark>                    | 58    |
| <mark style="color:green;">`CHAT_MESSAGE_HOLDOUT_WALL_FINISHED`</mark>                     | 59    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_LEFT_LIMITED_HERO`</mark>                  | 62    |
| <mark style="color:green;">`CHAT_MESSAGE_ABANDON_LIMITED_HERO_EXPLANATION`</mark>          | 63    |
| <mark style="color:green;">`CHAT_MESSAGE_DISCONNECT_LIMITED_HERO`</mark>                   | 64    |
| <mark style="color:green;">`CHAT_MESSAGE_LOW_PRIORITY_COMPLETED_EXPLANATION`</mark>        | 65    |
| <mark style="color:green;">`CHAT_MESSAGE_RECRUITMENT_DROP_RATE_BONUS`</mark>               | 66    |
| <mark style="color:green;">`CHAT_MESSAGE_FROSTIVUS_SHINING_BOOSTER_ACTIVE`</mark>          | 67    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_LEFT_AFK`</mark>                           | 73    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_LEFT_DISCONNECTED_TOO_LONG`</mark>         | 74    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_ABANDONED`</mark>                          | 75    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_ABANDONED_AFK`</mark>                      | 76    |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_ABANDONED_DISCONNECTED_TOO_LONG`</mark>    | 77    |
| <mark style="color:green;">`CHAT_MESSAGE_WILL_NOT_BE_SCORED`</mark>                        | 78    |
| <mark style="color:green;">`CHAT_MESSAGE_WILL_NOT_BE_SCORED_RANKED`</mark>                 | 79    |
| <mark style="color:green;">`CHAT_MESSAGE_WILL_NOT_BE_SCORED_NETWORK`</mark>                | 80    |
| <mark style="color:green;">`CHAT_MESSAGE_WILL_NOT_BE_SCORED_NETWORK_RANKED`</mark>         | 81    |
| <mark style="color:green;">`CHAT_MESSAGE_CAN_QUIT_WITHOUT_ABANDON`</mark>                  | 82    |
| <mark style="color:green;">`CHAT_MESSAGE_RANKED_GAME_STILL_SCORED_LEAVERS_GET_LOSS`</mark> | 83    |
| <mark style="color:green;">`CHAT_MESSAGE_ABANDON_RANKED_BEFORE_FIRST_BLOOD_PARTY`</mark>   | 84    |
| <mark style="color:green;">`CHAT_MESSAGE_COMPENDIUM_LEVEL`</mark>                          | 85    |
| <mark style="color:green;">`CHAT_MESSAGE_VICTORY_PREDICTION_STREAK`</mark>                 | 86    |
| <mark style="color:green;">`CHAT_MESSAGE_ASSASSIN_ANNOUNCE`</mark>                         | 87    |
| <mark style="color:green;">`CHAT_MESSAGE_ASSASSIN_SUCCESS`</mark>                          | 88    |
| <mark style="color:green;">`CHAT_MESSAGE_ASSASSIN_DENIED`</mark>                           | 89    |
| <mark style="color:green;">`CHAT_MESSAGE_VICTORY_PREDICTION_SINGLE_USER_CONFIRM`</mark>    | 90    |
| <mark style="color:green;">`CHAT_MESSAGE_EFFIGY_KILL`</mark>                               | 91    |
| <mark style="color:green;">`CHAT_MESSAGE_VOICE_TEXT_BANNED_OVERFLOW`</mark>                | 92    |
| <mark style="color:green;">`CHAT_MESSAGE_YEAR_BEAST_KILLED`</mark>                         | 93    |
| <mark style="color:green;">`CHAT_MESSAGE_PAUSE_COUNTDOWN`</mark>                           | 94    |
| <mark style="color:green;">`CHAT_MESSAGE_COINS_WAGERED`</mark>                             | 95    |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_NOMINATED_BAN`</mark>                        | 96    |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_BANNED`</mark>                               | 97    |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_BAN_COUNT`</mark>                            | 98    |
| <mark style="color:green;">`CHAT_MESSAGE_RIVER_PAINTED`</mark>                             | 99    |
| <mark style="color:green;">`CHAT_MESSAGE_SCAN_USED`</mark>                                 | 100   |
| <mark style="color:green;">`CHAT_MESSAGE_SHRINE_KILLED`</mark>                             | 101   |
| <mark style="color:green;">`CHAT_MESSAGE_WAGER_TOKEN_SPENT`</mark>                         | 102   |
| <mark style="color:green;">`CHAT_MESSAGE_RANK_WAGER`</mark>                                | 103   |
| <mark style="color:green;">`CHAT_MESSAGE_NEW_PLAYER_REMINDER`</mark>                       | 104   |
| <mark style="color:green;">`CHAT_MESSAGE_OBSERVER_WARD_KILLED`</mark>                      | 105   |
| <mark style="color:green;">`CHAT_MESSAGE_SENTRY_WARD_KILLED`</mark>                        | 106   |
| <mark style="color:green;">`CHAT_MESSAGE_ITEM_PLACED_IN_NEUTRAL_STASH`</mark>              | 107   |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_CHOICE_INVALID`</mark>                       | 108   |
| <mark style="color:green;">`CHAT_MESSAGE_BOUNTY`</mark>                                    | 109   |
| <mark style="color:green;">`CHAT_MESSAGE_ABILITY_DRAFT_START`</mark>                       | 110   |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_FOUND_CANDY`</mark>                          | 111   |
| <mark style="color:green;">`CHAT_MESSAGE_ABILITY_DRAFT_RANDOMED`</mark>                    | 112   |
| <mark style="color:green;">`CHAT_MESSAGE_PRIVATE_COACH_CONNECTED`</mark>                   | 113   |
| <mark style="color:green;">`CHAT_MESSAGE_CANT_PAUSE_TOO_EARLY`</mark>                      | 115   |
| <mark style="color:green;">`CHAT_MESSAGE_HERO_KILL_WITH_PENGUIN`</mark>                    | 116   |
| <mark style="color:green;">`CHAT_MESSAGE_MINIBOSS_KILL`</mark>                             | 117   |
| <mark style="color:green;">`CHAT_MESSAGE_PLAYER_IN_GAME_BAN_TEXT`</mark>                   | 118   |
| <mark style="color:green;">`CHAT_MESSAGE_BANNER_PLANTED`</mark>                            | 119   |

## <mark style="color:purple;">Enum.AbilityLearnResult</mark>

| Key                                                                           | Value |
| ----------------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`ABILITY_CAN_BE_UPGRADED`</mark>                   | 0     |
| <mark style="color:green;">`ABILITY_CANNOT_BE_UPGRADED_NOT_UPGRADABLE`</mark> | 1     |
| <mark style="color:green;">`ABILITY_CANNOT_BE_UPGRADED_AT_MAX`</mark>         | 2     |
| <mark style="color:green;">`ABILITY_CANNOT_BE_UPGRADED_REQUIRES_LEVEL`</mark> | 3     |
| <mark style="color:green;">`ABILITY_NOT_LEARNABLE`</mark>                     | 4     |

## <mark style="color:purple;">Enum.AbilityCastResult</mark>

| Key                                             | Value |
| ----------------------------------------------- | ----- |
| <mark style="color:green;">`READY`</mark>       |       |
| <mark style="color:green;">`NOT_LEARNED`</mark> |       |
| <mark style="color:green;">`NO_MANA`</mark>     |       |
| <mark style="color:green;">`ABILITY_CD`</mark>  |       |
| <mark style="color:green;">`PASSIVE`</mark>     |       |
| <mark style="color:green;">`HIDDEN`</mark>      |       |
| <mark style="color:green;">`ITEM_CD`</mark>     |       |

## <mark style="color:purple;">Enum.ModifierFunction</mark>

| Key                                                                                              | Value |
| ------------------------------------------------------------------------------------------------ | ----- |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE`</mark>                     | 0     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_TARGET`</mark>              | 1     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_PROC`</mark>                | 2     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE_POST_CRIT`</mark>           | 3     |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASEATTACK_BONUSDAMAGE`</mark>                     | 4     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_PHYSICAL`</mark>           | 5     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_CONVERT_PHYSICAL_TO_MAGICAL`</mark>     | 6     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_MAGICAL`</mark>            | 7     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_PURE`</mark>               | 8     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_BONUS_DAMAGE_MAGICAL_TARGET`</mark>     | 9     |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROCATTACK_FEEDBACK`</mark>                        | 10    |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ATTACK_DAMAGE`</mark>                     | 11    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PRE_ATTACK`</mark>                                 | 12    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INVISIBILITY_LEVEL`</mark>                         | 13    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INVISIBILITY_ATTACK_BEHAVIOR_EXCEPTION`</mark>     | 14    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PERSISTENT_INVISIBILITY`</mark>                    | 15    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT`</mark>                   | 16    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BASE_OVERRIDE`</mark>                    | 17    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE`</mark>                 | 20    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE_UNIQUE`</mark>          | 21    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_UNIQUE`</mark>                     | 22    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_UNIQUE_2`</mark>                   | 23    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT_UNIQUE`</mark>            | 24    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_BONUS_CONSTANT_UNIQUE_2`</mark>          | 25    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE`</mark>                         | 26    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE_MIN`</mark>                     | 27    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_ABSOLUTE_MAX`</mark>                     | 28    |
| <mark style="color:green;">`MODIFIER_PROPERTY_IGNORE_MOVESPEED_LIMIT`</mark>                     | 29    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_LIMIT`</mark>                            | 30    |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACKSPEED_BASE_OVERRIDE`</mark>                  | 31    |
| <mark style="color:green;">`MODIFIER_PROPERTY_FIXED_ATTACK_RATE`</mark>                          | 32    |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACKSPEED_BONUS_CONSTANT`</mark>                 | 33    |
| <mark style="color:green;">`MODIFIER_PROPERTY_IGNORE_ATTACKSPEED_LIMIT`</mark>                   | 34    |
| <mark style="color:green;">`MODIFIER_PROPERTY_COOLDOWN_REDUCTION_CONSTANT`</mark>                | 35    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANACOST_REDUCTION_CONSTANT`</mark>                | 36    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTHCOST_REDUCTION_CONSTANT`</mark>              | 37    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_ATTACK_TIME_CONSTANT`</mark>                  | 38    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_ATTACK_TIME_CONSTANT_ADJUST`</mark>           | 39    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_ATTACK_TIME_PERCENTAGE`</mark>                | 40    |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_POINT_CONSTANT`</mark>                      | 41    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUSDAMAGEOUTGOING_PERCENTAGE`</mark>             | 42    |
| <mark style="color:green;">`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE`</mark>                  | 43    |
| <mark style="color:green;">`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_ILLUSION`</mark>         | 44    |
| <mark style="color:green;">`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_ILLUSION_AMPLIFY`</mark> | 45    |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOTALDAMAGEOUTGOING_PERCENTAGE`</mark>             | 46    |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_CREEP`</mark>             | 47    |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE`</mark>                   | 48    |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELL_AMPLIFY_PERCENTAGE_UNIQUE`</mark>            | 49    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEAL_AMPLIFY_PERCENTAGE_SOURCE`</mark>             | 51    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEAL_AMPLIFY_PERCENTAGE_TARGET`</mark>             | 52    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HP_REGEN_AMPLIFY_PERCENTAGE`</mark>                | 53    |
| <mark style="color:green;">`MODIFIER_PROPERTY_LIFESTEAL_AMPLIFY_PERCENTAGE`</mark>               | 54    |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELL_LIFESTEAL_AMPLIFY_PERCENTAGE`</mark>         | 55    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MP_REGEN_AMPLIFY_PERCENTAGE`</mark>                | 57    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANA_DRAIN_AMPLIFY_PERCENTAGE`</mark>              | 59    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MP_RESTORE_AMPLIFY_PERCENTAGE`</mark>              | 60    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASEDAMAGEOUTGOING_PERCENTAGE`</mark>              | 61    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASEDAMAGEOUTGOING_PERCENTAGE_UNIQUE`</mark>       | 62    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_DAMAGE_PERCENTAGE`</mark>                 | 63    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_PERCENTAGE`</mark>        | 64    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_PHYSICAL_DAMAGE_CONSTANT`</mark>          | 65    |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_SPELL_DAMAGE_CONSTANT`</mark>             | 66    |
| <mark style="color:green;">`MODIFIER_PROPERTY_EVASION_CONSTANT`</mark>                           | 67    |
| <mark style="color:green;">`MODIFIER_PROPERTY_NEGATIVE_EVASION_CONSTANT`</mark>                  | 68    |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATUS_RESISTANCE`</mark>                          | 69    |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATUS_RESISTANCE_STACKING`</mark>                 | 70    |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATUS_RESISTANCE_CASTER`</mark>                   | 71    |
| <mark style="color:green;">`MODIFIER_PROPERTY_AVOID_DAMAGE`</mark>                               | 72    |
| <mark style="color:green;">`MODIFIER_PROPERTY_AVOID_SPELL`</mark>                                | 73    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MISS_PERCENTAGE`</mark>                            | 74    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BASE_PERCENTAGE`</mark>             | 75    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_TOTAL_PERCENTAGE`</mark>            | 76    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS`</mark>                       | 77    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_UNIQUE`</mark>                | 78    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_UNIQUE_ACTIVE`</mark>         | 79    |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_ARMOR_BONUS_POST`</mark>                  | 80    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MIN_PHYSICAL_ARMOR`</mark>                         | 81    |
| <mark style="color:green;">`MODIFIER_PROPERTY_IGNORE_PHYSICAL_ARMOR`</mark>                      | 82    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BASE_REDUCTION`</mark>          | 83    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_DIRECT_MODIFICATION`</mark>     | 84    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS`</mark>                   | 85    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS_ILLUSIONS`</mark>         | 86    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_BONUS_UNIQUE`</mark>            | 87    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_RESISTANCE_DECREPIFY_UNIQUE`</mark>        | 88    |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_MANA_REGEN`</mark>                            | 89    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANA_REGEN_CONSTANT`</mark>                        | 90    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANA_REGEN_CONSTANT_UNIQUE`</mark>                 | 91    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANA_REGEN_TOTAL_PERCENTAGE`</mark>                | 92    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTH_REGEN_CONSTANT`</mark>                      | 93    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTH_REGEN_PERCENTAGE`</mark>                    | 94    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTH_REGEN_PERCENTAGE_UNIQUE`</mark>             | 95    |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTH_BONUS`</mark>                               | 96    |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANA_BONUS`</mark>                                 | 97    |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_STRENGTH_BONUS`</mark>                       | 98    |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_HEALTH_BONUS`</mark>                         | 99    |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_MANA_BONUS`</mark>                           | 100   |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_MANA_BONUS_PERCENTAGE`</mark>                | 101   |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_HEALTH_PERCENTAGE`</mark>                    | 102   |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXTRA_MANA_PERCENTAGE`</mark>                      | 103   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_STRENGTH_BONUS`</mark>                       | 104   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_AGILITY_BONUS`</mark>                        | 105   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_INTELLECT_BONUS`</mark>                      | 106   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_STRENGTH_BONUS_PERCENTAGE`</mark>            | 107   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_AGILITY_BONUS_PERCENTAGE`</mark>             | 108   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STATS_INTELLECT_BONUS_PERCENTAGE`</mark>           | 109   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CAST_RANGE_BONUS`</mark>                           | 110   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CAST_RANGE_BONUS_PERCENTAGE`</mark>                | 111   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CAST_RANGE_BONUS_TARGET`</mark>                    | 112   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CAST_RANGE_BONUS_STACKING`</mark>                  | 113   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_RANGE_BASE_OVERRIDE`</mark>                 | 114   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS`</mark>                         | 115   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS_UNIQUE`</mark>                  | 116   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_RANGE_BONUS_PERCENTAGE`</mark>              | 117   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAX_ATTACK_RANGE`</mark>                           | 118   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROJECTILE_SPEED_BONUS`</mark>                     | 119   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROJECTILE_SPEED_BONUS_PERCENTAGE`</mark>          | 120   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROJECTILE_NAME`</mark>                            | 121   |
| <mark style="color:green;">`MODIFIER_PROPERTY_REINCARNATION`</mark>                              | 122   |
| <mark style="color:green;">`MODIFIER_PROPERTY_REINCARNATION_SUPPRESS_FX`</mark>                  | 123   |
| <mark style="color:green;">`MODIFIER_PROPERTY_RESPAWNTIME`</mark>                                | 124   |
| <mark style="color:green;">`MODIFIER_PROPERTY_RESPAWNTIME_PERCENTAGE`</mark>                     | 125   |
| <mark style="color:green;">`MODIFIER_PROPERTY_RESPAWNTIME_STACKING`</mark>                       | 126   |
| <mark style="color:green;">`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE`</mark>                        | 127   |
| <mark style="color:green;">`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE_ONGOING`</mark>                | 128   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CASTTIME_PERCENTAGE`</mark>                        | 129   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_ANIM_TIME_PERCENTAGE`</mark>                | 130   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANACOST_PERCENTAGE`</mark>                        | 131   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MANACOST_PERCENTAGE_STACKING`</mark>               | 132   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTHCOST_PERCENTAGE`</mark>                      | 133   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTHCOST_PERCENTAGE_STACKING`</mark>             | 134   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DEATHGOLDCOST`</mark>                              | 135   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PERCENTAGE_DEATHGOLDCOST`</mark>                   | 136   |
| <mark style="color:green;">`MODIFIER_PROPERTY_EXP_RATE_BOOST`</mark>                             | 137   |
| <mark style="color:green;">`MODIFIER_PROPERTY_GOLD_RATE_BOOST`</mark>                            | 138   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_CRITICALSTRIKE`</mark>                   | 139   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_TARGET_CRITICALSTRIKE`</mark>            | 140   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAGICAL_CONSTANT_BLOCK`</mark>                     | 141   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_CONSTANT_BLOCK`</mark>                    | 142   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICAL_CONSTANT_BLOCK_SPECIAL`</mark>            | 143   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK_UNAVOIDABLE_PRE_ARMOR`</mark> | 145   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK`</mark>                       | 146   |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ANIMATION`</mark>                         | 147   |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ANIMATION_RATE`</mark>                    | 148   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABSORB_SPELL`</mark>                               | 149   |
| <mark style="color:green;">`MODIFIER_PROPERTY_REFLECT_SPELL`</mark>                              | 150   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DISABLE_AUTOATTACK`</mark>                         | 151   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_DAY_VISION`</mark>                           | 152   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_DAY_VISION_PERCENTAGE`</mark>                | 153   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_NIGHT_VISION`</mark>                         | 154   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_NIGHT_VISION_UNIQUE`</mark>                  | 155   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_VISION_PERCENTAGE`</mark>                    | 156   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FIXED_DAY_VISION`</mark>                           | 157   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FIXED_NIGHT_VISION`</mark>                         | 158   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MIN_HEALTH`</mark>                                 | 159   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PHYSICAL`</mark>                | 161   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_MAGICAL`</mark>                 | 162   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_PURE`</mark>                    | 163   |
| <mark style="color:green;">`MODIFIER_PROPERTY_IS_ILLUSION`</mark>                                | 164   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ILLUSION_LABEL`</mark>                             | 165   |
| <mark style="color:green;">`MODIFIER_PROPERTY_STRONG_ILLUSION`</mark>                            | 166   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPER_ILLUSION`</mark>                             | 167   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPER_ILLUSION_WITH_ULTIMATE`</mark>               | 168   |
| <mark style="color:green;">`MODIFIER_PROPERTY_XP_DURING_DEATH`</mark>                            | 169   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TURN_RATE_PERCENTAGE`</mark>                       | 170   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TURN_RATE_OVERRIDE`</mark>                         | 171   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DISABLE_HEALING`</mark>                            | 172   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ALWAYS_ALLOW_ATTACK`</mark>                        | 174   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ALWAYS_ETHEREAL_ATTACK`</mark>                     | 175   |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ATTACK_MAGICAL`</mark>                    | 176   |
| <mark style="color:green;">`MODIFIER_PROPERTY_UNIT_STATS_NEEDS_REFRESH`</mark>                   | 177   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BOUNTY_CREEP_MULTIPLIER`</mark>                    | 178   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BOUNTY_OTHER_MULTIPLIER`</mark>                    | 179   |
| <mark style="color:green;">`MODIFIER_PROPERTY_UNIT_DISALLOW_UPGRADING`</mark>                    | 180   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DODGE_PROJECTILE`</mark>                           | 181   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TRIGGER_COSMETIC_AND_END_ATTACK`</mark>            | 182   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MAX_DEBUFF_DURATION`</mark>                        | 183   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PRIMARY_STAT_DAMAGE_MULTIPLIER`</mark>             | 184   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREATTACK_DEADLY_BLOW`</mark>                      | 185   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ALWAYS_AUTOATTACK_WHILE_HOLD_POSITION`</mark>      | 186   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_SPELL_TARGET_READY`</mark>                         | 191   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_RECORD`</mark>                              | 192   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_START`</mark>                               | 193   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK`</mark>                                     | 194   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_LANDED`</mark>                              | 195   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_FAIL`</mark>                                | 196   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_ALLIED`</mark>                              | 197   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_PROJECTILE_DODGE`</mark>                           | 198   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ORDER`</mark>                                      | 199   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_UNIT_MOVED`</mark>                                 | 200   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ABILITY_START`</mark>                              | 201   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ABILITY_EXECUTED`</mark>                           | 202   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ABILITY_FULLY_CAST`</mark>                         | 203   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_BREAK_INVISIBILITY`</mark>                         | 204   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ABILITY_END_CHANNEL`</mark>                        | 205   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_PROCESS_UPGRADE`</mark>                            | 206   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_REFRESH`</mark>                                    | 207   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TAKEDAMAGE`</mark>                                 | 208   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DEATH_PREVENTED`</mark>                            | 209   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_STATE_CHANGED`</mark>                              | 210   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ORB_EFFECT`</mark>                                 | 211   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_PROCESS_CLEAVE`</mark>                             | 212   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DAMAGE_CALCULATED`</mark>                          | 213   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MAGIC_DAMAGE_CALCULATED`</mark>                    | 214   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACKED`</mark>                                   | 215   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DEATH`</mark>                                      | 216   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DEATH_COMPLETED`</mark>                            | 217   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_RESPAWN`</mark>                                    | 218   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_SPENT_MANA`</mark>                                 | 219   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_SPENT_HEALTH`</mark>                               | 220   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TELEPORTING`</mark>                                | 221   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TELEPORTED`</mark>                                 | 222   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_SET_LOCATION`</mark>                               | 223   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_HEALTH_GAINED`</mark>                              | 224   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MANA_GAINED`</mark>                                | 225   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TAKEDAMAGE_KILLCREDIT`</mark>                      | 226   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_HERO_KILLED`</mark>                                | 227   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_HEAL_RECEIVED`</mark>                              | 228   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_BUILDING_KILLED`</mark>                            | 229   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MODEL_CHANGED`</mark>                              | 230   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MODIFIER_ADDED`</mark>                             | 231   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MODIFIER_REMOVED`</mark>                           | 232   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOOLTIP`</mark>                                    | 233   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MODEL_CHANGE`</mark>                               | 234   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MODEL_SCALE`</mark>                                | 235   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MODEL_SCALE_ANIMATE_TIME`</mark>                   | 236   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MODEL_SCALE_USE_IN_OUT_EASE`</mark>                | 237   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MODEL_SCALE_CONSTANT`</mark>                       | 238   |
| <mark style="color:green;">`MODIFIER_PROPERTY_IS_SCEPTER`</mark>                                 | 239   |
| <mark style="color:green;">`MODIFIER_PROPERTY_IS_SHARD`</mark>                                   | 240   |
| <mark style="color:green;">`MODIFIER_PROPERTY_RADAR_COOLDOWN_REDUCTION`</mark>                   | 241   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TRANSLATE_ACTIVITY_MODIFIERS`</mark>               | 242   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TRANSLATE_ATTACK_SOUND`</mark>                     | 243   |
| <mark style="color:green;">`MODIFIER_PROPERTY_LIFETIME_FRACTION`</mark>                          | 244   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROVIDES_FOW_POSITION`</mark>                      | 245   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELLS_REQUIRE_HP`</mark>                          | 246   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CONVERT_MANA_COST_TO_HEALTH_COST`</mark>           | 247   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FORCE_DRAW_MINIMAP`</mark>                         | 248   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DISABLE_TURNING`</mark>                            | 249   |
| <mark style="color:green;">`MODIFIER_PROPERTY_IGNORE_CAST_ANGLE`</mark>                          | 250   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CHANGE_ABILITY_VALUE`</mark>                       | 251   |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL`</mark>                   | 252   |
| <mark style="color:green;">`MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL_VALUE`</mark>             | 253   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABILITY_LAYOUT`</mark>                             | 254   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DOMINATED`</mark>                                  | 255   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_KILL`</mark>                                       | 256   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ASSIST`</mark>                                     | 257   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TEMPEST_DOUBLE`</mark>                             | 258   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PRESERVE_PARTICLES_ON_MODEL_CHANGE`</mark>         | 259   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_FINISHED`</mark>                            | 260   |
| <mark style="color:green;">`MODIFIER_PROPERTY_IGNORE_COOLDOWN`</mark>                            | 261   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CAN_ATTACK_TREES`</mark>                           | 262   |
| <mark style="color:green;">`MODIFIER_PROPERTY_VISUAL_Z_DELTA`</mark>                             | 263   |
| <mark style="color:green;">`MODIFIER_PROPERTY_VISUAL_Z_SPEED_BASE_OVERRIDE`</mark>               | 264   |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_DAMAGE_ILLUSION`</mark>                   | 265   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DONT_GIVE_VISION_OF_ATTACKER`</mark>               | 266   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOOLTIP2`</mark>                                   | 267   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_RECORD_DESTROY`</mark>                      | 268   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_PROJECTILE_OBSTRUCTION_HIT`</mark>                 | 269   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPPRESS_TELEPORT`</mark>                          | 270   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTACK_CANCELLED`</mark>                           | 271   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPPRESS_CLEAVE`</mark>                            | 272   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BOT_ATTACK_SCORE_BONUS`</mark>                     | 273   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACKSPEED_REDUCTION_PERCENTAGE`</mark>           | 274   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MOVESPEED_REDUCTION_PERCENTAGE`</mark>             | 275   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_WHILE_MOVING_TARGET`</mark>                 | 276   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACKSPEED_PERCENTAGE`</mark>                     | 277   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ATTEMPT_PROJECTILE_DODGE`</mark>                   | 278   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_PREDEBUFF_APPLIED`</mark>                          | 279   |
| <mark style="color:green;">`MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE_STACKING`</mark>               | 280   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SPELL_REDIRECT_TARGET`</mark>                      | 281   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TURN_RATE_CONSTANT`</mark>                         | 282   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PACK_RAT`</mark>                                   | 283   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PHYSICALDAMAGEOUTGOING_PERCENTAGE`</mark>          | 284   |
| <mark style="color:green;">`MODIFIER_PROPERTY_KNOCKBACK_AMPLIFICATION_PERCENTAGE`</mark>         | 285   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEALTHBAR_PIPS`</mark>                             | 286   |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT`</mark>                   | 287   |
| <mark style="color:green;">`MODIFIER_EVENT_SPELL_APPLIED_SUCCESSFULLY`</mark>                    | 288   |
| <mark style="color:green;">`MODIFIER_PROPERTY_AVOID_DAMAGE_AFTER_REDUCTIONS`</mark>              | 289   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FAIL_ATTACK`</mark>                                | 290   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PREREDUCE_INCOMING_DAMAGE_MULT`</mark>             | 291   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPPRESS_FULLSCREEN_DEATH_FX`</mark>               | 292   |
| <mark style="color:green;">`MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT_POST`</mark>              | 293   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_MULTIPLICATIVE`</mark>   | 294   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TICK_GOLD_MULTIPLIER`</mark>                       | 295   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SLOW_RESISTANCE_UNIQUE`</mark>                     | 296   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SLOW_RESISTANCE_STACKING`</mark>                   | 297   |
| <mark style="color:green;">`MODIFIER_PROPERTY_AOE_BONUS_PERCENTAGE`</mark>                       | 299   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROJECTILE_SPEED`</mark>                           | 300   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PROJECTILE_SPEED_TARGET`</mark>                    | 301   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BECOME_STRENGTH`</mark>                            | 302   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BECOME_AGILITY`</mark>                             | 303   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BECOME_INTELLIGENCE`</mark>                        | 304   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BECOME_UNIVERSAL`</mark>                           | 305   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_FORCE_PROC_MAGIC_STICK`</mark>                     | 306   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DAMAGE_HPLOSS`</mark>                              | 307   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SHARE_XPRUNE`</mark>                               | 308   |
| <mark style="color:green;">`MODIFIER_PROPERTY_NO_FREE_TP_SCROLL_ON_DEATH`</mark>                 | 310   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HAS_BONUS_NEUTRAL_ITEM_CHOICE`</mark>              | 311   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FORCE_MAX_HEALTH`</mark>                           | 313   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FORCE_MAX_MANA`</mark>                             | 314   |
| <mark style="color:green;">`MODIFIER_PROPERTY_AOE_BONUS_CONSTANT`</mark>                         | 315   |
| <mark style="color:green;">`MODIFIER_PROPERTY_AOE_BONUS_CONSTANT_STACKING`</mark>                | 316   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TAKEDAMAGE_POST_UNAVOIDABLE_BLOCK`</mark>          | 317   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_MUTE_DAMAGE_ABILITIES`</mark>                      | 318   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPPRESS_CRIT`</mark>                              | 319   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ABILITY_POINTS`</mark>                             | 320   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BUYBACK_PENALTY_PERCENT`</mark>                    | 321   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ITEM_SELLBACK_COST`</mark>                         | 322   |
| <mark style="color:green;">`MODIFIER_PROPERTY_DISASSEMBLE_ANYTHING`</mark>                       | 323   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FIXED_MANA_REGEN`</mark>                           | 324   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_UPHILL_MISS_CHANCE`</mark>                   | 325   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CREEP_DENY_PERCENT`</mark>                         | 326   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACKSPEED_ABSOLUTE_MAX`</mark>                   | 327   |
| <mark style="color:green;">`MODIFIER_PROPERTY_FOW_TEAM`</mark>                                   | 328   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_HERO_BEGIN_DYING`</mark>                           | 329   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BONUS_LOTUS_HEAL`</mark>                           | 330   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_HP_REGEN_PER_STR_BONUS_PERCENTAGE`</mark>     | 331   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_ARMOR_PER_AGI_BONUS_PERCENTAGE`</mark>        | 332   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_MP_REGEN_PER_INT_BONUS_PERCENTAGE`</mark>     | 333   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASE_MRES_PER_INT_BONUS_PERCENTAGE`</mark>         | 334   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_DAY_STARTED`</mark>                                | 335   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CREATE_BONUS_ILLUSION_CHANCE`</mark>               | 337   |
| <mark style="color:green;">`MODIFIER_PROPERTY_CREATE_BONUS_ILLUSION_COUNT`</mark>                | 338   |
| <mark style="color:green;">`MODIFIER_PROPERTY_PSEUDORANDOM_BONUS`</mark>                         | 339   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ATTACK_HEIGHT_BONUS`</mark>                        | 340   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SKIP_ATTACK_REGULATOR`</mark>                      | 341   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MISS_PERCENTAGE_TARGET`</mark>                     | 342   |
| <mark style="color:green;">`MODIFIER_PROPERTY_ADDITIONAL_NEUTRAL_ITEM_DROPS`</mark>              | 343   |
| <mark style="color:green;">`MODIFIER_PROPERTY_KILL_STREAK_BONUS_GOLD_PERCENTAGE`</mark>          | 344   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HP_REGEN_MULTIPLIER_PRE_AMPLIFICATION`</mark>      | 345   |
| <mark style="color:green;">`MODIFIER_PROPERTY_HEROFACET_OVERRIDE`</mark>                         | 346   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TREE_CUT_DOWN`</mark>                              | 347   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_CLEAVE_ATTACK_LANDED`</mark>                       | 348   |
| <mark style="color:green;">`MODIFIER_PROPERTY_MIN_ATTRIBUTE_LEVEL`</mark>                        | 349   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TIER_TOKEN_REROLL`</mark>                          | 350   |
| <mark style="color:green;">`MODIFIER_PROPERTY_TOTAL_CONSTANT_BLOCK_STACKING`</mark>              | 352   |
| <mark style="color:green;">`MODIFIER_PROPERTY_INVENTORY_SLOT_RESTRICTED`</mark>                  | 353   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_TIER_TOKEN_REROLLED`</mark>                        | 354   |
| <mark style="color:green;">`MODIFIER_PROPERTY_REDIRECT_SPELL`</mark>                             | 355   |
| <mark style="color:green;">`MODIFIER_PROPERTY_BASEATTACK_POSTBONUS`</mark>                       | 356   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_FOW_TEAM_CHANGED`</mark>                           | 357   |
| <mark style="color:green;">`MODIFIER_PROPERTY_SUPPRESS_ATTACK_PROCS`</mark>                      | 358   |
| <mark style="color:green;">`MODIFIER_EVENT_ON_ABILITY_TOGGLED`</mark>                            | 359   |
| <mark style="color:green;">`MODIFIER_FUNCTION_LAST`</mark>                                       | 378   |
| <mark style="color:green;">`MODIFIER_FUNCTION_INVALID`</mark>                                    | 65535 |

## <mark style="color:purple;">Enum.DrunkenBrawlerState</mark>

| Key                                                             | Value |
| --------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DRUNKEN_BRAWLER_STATE_EARTH`</mark> | 0     |
| <mark style="color:green;">`DRUNKEN_BRAWLER_STATE_STORM`</mark> | 1     |
| <mark style="color:green;">`DRUNKEN_BRAWLER_STATE_FIRE`</mark>  | 2     |

## <mark style="color:purple;">Enum.OverHeadAlert</mark>

| Key                                                                    | Value |
| ---------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`OVERHEAD_ALERT_GOLD`</mark>                | 0     |
| <mark style="color:green;">`OVERHEAD_ALERT_DENY`</mark>                | 1     |
| <mark style="color:green;">`OVERHEAD_ALERT_CRITICAL`</mark>            | 2     |
| <mark style="color:green;">`OVERHEAD_ALERT_XP`</mark>                  | 3     |
| <mark style="color:green;">`OVERHEAD_ALERT_BONUS_SPELL_DAMAGE`</mark>  | 4     |
| <mark style="color:green;">`OVERHEAD_ALERT_MISS`</mark>                | 5     |
| <mark style="color:green;">`OVERHEAD_ALERT_DAMAGE`</mark>              | 6     |
| <mark style="color:green;">`OVERHEAD_ALERT_EVADE`</mark>               | 7     |
| <mark style="color:green;">`OVERHEAD_ALERT_BLOCK`</mark>               | 8     |
| <mark style="color:green;">`OVERHEAD_ALERT_BONUS_POISON_DAMAGE`</mark> | 9     |
| <mark style="color:green;">`OVERHEAD_ALERT_HEAL`</mark>                | 10    |
| <mark style="color:green;">`OVERHEAD_ALERT_MANA_ADD`</mark>            | 11    |
| <mark style="color:green;">`OVERHEAD_ALERT_MANA_LOSS`</mark>           | 12    |
| <mark style="color:green;">`OVERHEAD_ALERT_MAGICAL_BLOCK`</mark>       | 16    |
| <mark style="color:green;">`OVERHEAD_ALERT_INCOMING_DAMAGE`</mark>     | 17    |
| <mark style="color:green;">`OVERHEAD_ALERT_OUTGOING_DAMAGE`</mark>     | 18    |
| <mark style="color:green;">`OVERHEAD_ALERT_DISABLE_RESIST`</mark>      | 19    |
| <mark style="color:green;">`OVERHEAD_ALERT_DEATH`</mark>               | 20    |
| <mark style="color:green;">`OVERHEAD_ALERT_BLOCKED`</mark>             | 21    |
| <mark style="color:green;">`OVERHEAD_ALERT_ITEM_RECEIVED`</mark>       | 22    |
| <mark style="color:green;">`OVERHEAD_ALERT_SHARD`</mark>               | 23    |
| <mark style="color:green;">`OVERHEAD_ALERT_DEADLY_BLOW`</mark>         | 24    |

## <mark style="color:purple;">Enum.ShareAbility</mark>

| Key                                                          | Value |
| ------------------------------------------------------------ | ----- |
| <mark style="color:green;">`ITEM_FULLY_SHAREABLE`</mark>     | 0     |
| <mark style="color:green;">`ITEM_PARTIALLY_SHAREABLE`</mark> | 1     |
| <mark style="color:green;">`ITEM_NOT_SHAREABLE`</mark>       | 2     |

## <mark style="color:purple;">Enum.TeamNum</mark>

| Key                                              | Value |
| ------------------------------------------------ | ----- |
| <mark style="color:green;">`TEAM_NONE`</mark>    |       |
| <mark style="color:green;">`TEAM_DIRE`</mark>    |       |
| <mark style="color:green;">`TEAM_RADIANT`</mark> |       |
| <mark style="color:green;">`TEAM_NEUTRAL`</mark> |       |

## <mark style="color:purple;">Enum.UIState</mark>

| Key                                                                   | Value |
| --------------------------------------------------------------------- | ----- |
| <mark style="color:green;">`DOTA_GAME_UI_STATE_INVALID`</mark>        |       |
| <mark style="color:green;">`DOTA_GAME_UI_STATE_LOADING_SCREEN`</mark> |       |
| <mark style="color:green;">`DOTA_GAME_UI_DOTA_INGAME`</mark>          |       |
| <mark style="color:green;">`DOTA_GAME_UI_STATE_DASHBOARD`</mark>      |       |

## <mark style="color:purple;">Enum.DormancyType</mark>

| Key                                                    | Value |
| ------------------------------------------------------ | ----- |
| <mark style="color:green;">`ENTITY_NOT_DORMANT`</mark> | 0     |
| <mark style="color:green;">`ENTITY_DORMANT`</mark>     | 1     |
| <mark style="color:green;">`ENTITY_SUSPENDED`</mark>   | 2     |

## <mark style="color:purple;">Enum.ECourierState</mark>

| Key                                             | Value |
| ----------------------------------------------- | ----- |
| <mark style="color:green;">`k_eIdle`</mark>     | 0     |
| <mark style="color:green;">`k_eGoToShop`</mark> | 2     |
| <mark style="color:green;">`k_eGoToUnit`</mark> | 3     |
| <mark style="color:green;">`k_eManual`</mark>   | 4     |

## <mark style="color:purple;">Enum.DrawFlags</mark>

| Key                                                             | Value |
| --------------------------------------------------------------- | ----- |
| <mark style="color:green;">`None`</mark>                        |       |
| <mark style="color:green;">`Closed`</mark>                      |       |
| <mark style="color:green;">`RoundCornersTopLeft`</mark>         |       |
| <mark style="color:green;">`RoundCornersTopRight`</mark>        |       |
| <mark style="color:green;">`RoundCornersBottomLeft`</mark>      |       |
| <mark style="color:green;">`RoundCornersBottomRight`</mark>     |       |
| <mark style="color:green;">`RoundCornersNone`</mark>            |       |
| <mark style="color:green;">`RoundCornersTop`</mark>             |       |
| <mark style="color:green;">`RoundCornersBottom`</mark>          |       |
| <mark style="color:green;">`RoundCornersLeft`</mark>            |       |
| <mark style="color:green;">`RoundCornersRight`</mark>           |       |
| <mark style="color:green;">`RoundCornersAll`</mark>             |       |
| <mark style="color:green;">`RoundCornersDefault_`</mark>        |       |
| <mark style="color:green;">`RoundCornersMask_`</mark>           |       |
| <mark style="color:green;">`ShadowCutOutShapeBackground`</mark> |       |


--------------------------------------------------------------------------------

### Classes - Color

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color -->

# Color

Color metatable

### Fields

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **r** | <mark style="color:purple;">**`number`**</mark> | red         |
| **g** | <mark style="color:purple;">**`number`**</mark> | green       |
| **b** | <mark style="color:purple;">**`number`**</mark> | blue        |
| **a** | <mark style="color:purple;">**`number`**</mark> | alpha       |

## <sub>Color</sub>

`Color([r], [g], [b], [a]):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name                                                    | Type                                            | Description      |
| ------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |

Create a new Color.

## <sub>Color</sub>

`Color(hex):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name    | Type                                            | Description                        |
| ------- | ----------------------------------------------- | ---------------------------------- |
| **hex** | <mark style="color:purple;">**`string`**</mark> | Hex string. Do not use "#" symbol. |

Create a new Color from hex string.

## <sub>AsFraction</sub>

`:AsFraction(r, g, b, a):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name  | Type                                            | Description                                                |
| ----- | ----------------------------------------------- | ---------------------------------------------------------- |
| **r** | <mark style="color:purple;">**`number`**</mark> | New R color range as a percentage in the range \[0.0, 1.0] |
| **g** | <mark style="color:purple;">**`number`**</mark> | New G color range as a percentage in the range \[0.0, 1.0] |
| **b** | <mark style="color:purple;">**`number`**</mark> | New B color range as a percentage in the range \[0.0, 1.0] |
| **a** | <mark style="color:purple;">**`number`**</mark> | New A color range as a percentage in the range \[0.0, 1.0] |

Overwrites the color's ranges using the fraction values. Returns itself.

## <sub>AsInt</sub>

`:AsInt(value):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name      | Type                                            | Description     |
| --------- | ----------------------------------------------- | --------------- |
| **value** | <mark style="color:purple;">**`number`**</mark> | int color value |

Overwrites the color's ranges converting the int value to RGBA values. Returns\
itself.

## <sub>AsHsv</sub>

`:AsHsv(h, s, v, a):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name  | Type                                            | Description                        |
| ----- | ----------------------------------------------- | ---------------------------------- |
| **h** | <mark style="color:purple;">**`number`**</mark> | Hue color range \[0.0, 1.0]        |
| **s** | <mark style="color:purple;">**`number`**</mark> | Saturation color range \[0.0, 1.0] |
| **v** | <mark style="color:purple;">**`number`**</mark> | Value color range \[0.0, 1.0]      |
| **a** | <mark style="color:purple;">**`number`**</mark> | Alpha color range \[0.0, 1.0]      |

Overwrites the color's ranges converting the HSV to RGBA values. Returns itself.

## <sub>AsHsl</sub>

`:AsHsl(h, s, l, a):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name  | Type                                            | Description                        |
| ----- | ----------------------------------------------- | ---------------------------------- |
| **h** | <mark style="color:purple;">**`number`**</mark> | Hue color range \[0.0, 1.0]        |
| **s** | <mark style="color:purple;">**`number`**</mark> | Saturation color range \[0.0, 1.0] |
| **l** | <mark style="color:purple;">**`number`**</mark> | Lightness color range \[0.0, 1.0]  |
| **a** | <mark style="color:purple;">**`number`**</mark> | Alpha color range \[0.0, 1.0]      |

Overwrites the color's ranges converting the HSL to RGBA values. Returns itself.

## <sub>ToFraction</sub>

`:ToFraction():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns the r, g, b, and a ranges of the color as a percentage in the range of\
\[0.0, 1.0].

## <sub>ToInt</sub>

`:ToInt():` <mark style="color:purple;">**`number`**</mark>

Returns the int value representing the color.

## <sub>ToHsv</sub>

`:ToHsv():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns the HSV representation of the color.

## <sub>ToHsl</sub>

`:ToHsl():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns the ToHsl representation of the color.

## <sub>ToHex</sub>

`:ToHex():` <mark style="color:purple;">**`string`**</mark>

Returns the hex string representing the color.

## <sub>Lerp</sub>

`:Lerp(other, weight):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name       | Type                                                                                                                          | Description                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **other**  | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | The color to interpolate to                                    |
| **weight** | <mark style="color:purple;">**`number`**</mark>                                                                               | A value between 0 and 1 that indicates the weight of **other** |

Returns the linearly interpolated color between two colors by the specified weight.

## <sub>Grayscale</sub>

`:Grayscale(weight):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name       | Type                                            | Description                                                        |
| ---------- | ----------------------------------------------- | ------------------------------------------------------------------ |
| **weight** | <mark style="color:purple;">**`number`**</mark> | A value between 0 and 1 that indicates the weight of **grayscale** |

Returns the grayscaled color.

## <sub>AlphaModulate</sub>

`:AlphaModulate(alpha):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name      | Type                                            | Description                   |
| --------- | ----------------------------------------------- | ----------------------------- |
| **alpha** | <mark style="color:purple;">**`number`**</mark> | Alpha color range \[0.0, 1.0] |

Returns the alpha modulated color.

## <sub>Clone</sub>

`:Clone():` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Creates and returns a copy of the color object.

## <sub>Unpack</sub>

`:Unpack():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns the r, g, b, and a values of the color. Note that these fields can be\
accessed by indexing r, g, b, and a.

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

Returns hex string representing the color.


--------------------------------------------------------------------------------

### Classes - Menu System

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu -->

# Menu

Table to work with Menu.

## <sub>Find</sub>

`Menu.Find(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName, widgetName, attachmentName, widgetInGearName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [<mark style="color:purple;">**`CMenuButton`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | <mark style="color:purple;">**`nil`**</mark>

| Name                 | Type                                            | Description |
| -------------------- | ----------------------------------------------- | ----------- |
| **firstTabName**     | <mark style="color:purple;">**`string`**</mark> |             |
| **sectionName**      | <mark style="color:purple;">**`string`**</mark> |             |
| **secondTabName**    | <mark style="color:purple;">**`string`**</mark> |             |
| **thirdTabName**     | <mark style="color:purple;">**`string`**</mark> |             |
| **groupTabName**     | <mark style="color:purple;">**`string`**</mark> |             |
| **widgetName**       | <mark style="color:purple;">**`string`**</mark> |             |
| **attachmentName**   | <mark style="color:purple;">**`string`**</mark> |             |
| **widgetInGearName** | <mark style="color:purple;">**`string`**</mark> |             |

Returns menu item.

## <sub>Create</sub>

`Menu.Create(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

| Name              | Type                                            | Description |
| ----------------- | ----------------------------------------------- | ----------- |
| **firstTabName**  | <mark style="color:purple;">**`string`**</mark> |             |
| **sectionName**   | <mark style="color:purple;">**`string`**</mark> |             |
| **secondTabName** | <mark style="color:purple;">**`string`**</mark> |             |
| **thirdTabName**  | <mark style="color:purple;">**`string`**</mark> |             |
| **groupTabName**  | <mark style="color:purple;">**`string`**</mark> |             |

Creates tab/section/group. Returns menu item.

## <sub>Style</sub>

`Menu.Style(styleColor):` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **styleColor** | <mark style="color:purple;">**`string`**</mark> |             |

Creates tab/section/group. Returns color of specified style var or table of all style colors\
depends on param.

## <sub>Opened</sub>

`Menu.Opened():` <mark style="color:purple;">**`boolean`**</mark>

Returns current menu open state.

## <sub>VisualsIsEnabled</sub>

`Menu.VisualsIsEnabled():` <mark style="color:purple;">**`boolean`**</mark>

Returns current visuals enabled state.

## <sub>Alpha</sub>

`Menu.Alpha():` <mark style="color:purple;">**`number`**</mark>

Returns current menu alpha.

## <sub>Pos</sub>

`Menu.Pos():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu pos.

## <sub>Size</sub>

`Menu.Size():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu size.

## <sub>Scale</sub>

`Menu.Scale():` <mark style="color:purple;">**`integer`**</mark>

Returns current menu scale percentage.

## <sub>AnimDuration</sub>

`Menu.AnimDuration():` <mark style="color:purple;">**`number`**</mark>

Returns current menu animation duration.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection -->

# CTabSection

CTabSection metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CFirstTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(sectionName):` [<mark style="color:purple;">**`CSecondTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CSecondTab`.

## <sub>Find</sub>

`:Find(sectionName):` [<mark style="color:purple;">**`CSecondTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CSecondTab` by name.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab -->

# CFirstTab

CFirstTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` <mark style="color:purple;">**`nil`**</mark>

Returns parent. It's `nil` for CFirstTab.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(sectionName):` [<mark style="color:purple;">**`CTabSection`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CTabSection`.

## <sub>Find</sub>

`:Find(sectionName):` [<mark style="color:purple;">**`CTabSection`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CTabSection` by name.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab -->

# CSecondTab

CSecondTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CTabSection`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(tabName):` [<mark style="color:purple;">**`CThirdTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **tabName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CThirdTab`.

## <sub>Find</sub>

`:Find(tabName):` [<mark style="color:purple;">**`CThirdTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **tabName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CThirdTab` by name.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets tab's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
-- https://fontawesome.com/icons/user?f=classic&s=solid
tab:Icon( "\u{f007}" )
```

## <sub>LinkHero</sub>

`:LinkHero(heroId, attribute):` <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                                                                                                 | Description                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **heroId**    | <mark style="color:purple;">**`integer`**</mark>                                                                     | See `Engine.GetHeroIDByName` |
| **attribute** | [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.attributes) |                              |

Links tab to hero and attribute.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab -->

# CThirdTab

CThirdTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CSecondTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(groupName, [side]):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

| Name                                                       | Type                                                                                                               | Description                         |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **groupName**                                              | <mark style="color:purple;">**`string`**</mark>                                                                    |                                     |
| **side&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.GroupSide`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.groupside) | `(default: Enum.GroupSide.Default)` |

Creates new `CMenuGroup`.

## <sub>Find</sub>

`:Find(groupName):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                            | Description |
| ------------- | ----------------------------------------------- | ----------- |
| **groupName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CMenuGroup` by name.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets third tab's visible state. Depends on argument.

#### Example

```lua
-- setter
third_tab:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = third_tab:Visible()
```

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets tab's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
-- https://fontawesome.com/icons/user?f=classic&s=solid
tab:Icon( "\u{f007}")
```

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup -->

# CMenuGroup

CMenuGroup metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns group's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CThirdTab`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Returns group's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Find</sub>

`:Find(widgetName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [<mark style="color:purple;">**`CMenuButton`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **widgetName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the widget by name.

## <sub>Switch</sub>

`:Switch(switchName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

| Name                                                               | Type                                             | Description                                                |
| ------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------- |
| **switchName**                                                     | <mark style="color:purple;">**`string`**</mark>  |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | `(default: false)`                                         |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>  | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuSwitch`.

## <sub>Bind</sub>

`:Bind(bindName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

| Name                                                               | Type                                                                                                                 | Description                                                |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **bindName**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                      |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode) | `(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`           |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuBind`.

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

| Name                                                         | Type                                                                                                                   | Description                                                               |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **sliderName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                        |                                                                           |
| **minValue**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **maxValue**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **defaultValue**                                             | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **format&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`fun(value: integer):string`**</mark> | Format string or function to format value. See example. `(default: "%d")` |

Creates new `CMenuSliderInt` or `CMenuSliderFloat` depents on arg types.\
`minValue`, `maxValue` and `defaultValue` should be integer to create `CMenuSliderInt`.

#### Example

```lua
-- Create slider with integer values
group:Slider( "slider", 0, 100, 50, "%d" )
-- Create slider with integer values and custom format function
group:Slider( "slider", 0, 100, 50, function( value ) return "%d%%" end ) -- turns into
"50%"
```

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

| Name                                                         | Type                                                                                                                  | Description                                                               |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **sliderName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                       |                                                                           |
| **minValue**                                                 | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **maxValue**                                                 | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **defaultValue**                                             | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **format&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`fun(value: number):string`**</mark> | Format string or function to format value. See example. `(default: "%f")` |

Creates new `CMenuSliderFloat`.

#### Example

```lua
-- Create slider with float values
group:Slider( "slider", 0.0, 1.0, 0.5, "%.2f" ) -- turns into "0.50"
-- Create slider with float values and custom format function
group:Slider( "slider", 0.0, 100.0, 50.0, function( value )
	if value < 50 then
		return "Low(%f)"
	else
		return "High(%f)"
  end
end )
```

## <sub>ColorPicker</sub>

`:ColorPicker(colorPickerName, color, [imageIcon]):` [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

| Name                                                            | Type                                                                                                                          | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **colorPickerName**                                             | <mark style="color:purple;">**`string`**</mark>                                                                               |                                                            |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark>                                                                               | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuColorPicker`.

## <sub>Button</sub>

`:Button(buttonName, callback, [altStyle], [widthPercent]):` [<mark style="color:purple;">**`CMenuButton`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)

| Name                                                               | Type                                              | Description                                                     |
| ------------------------------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------- |
| **buttonName**                                                     | <mark style="color:purple;">**`string`**</mark>   |                                                                 |
| **callback**                                                       | <mark style="color:purple;">**`function`**</mark> | `func(this: CMenuButton):nil` function to call on button click. |
| **altStyle&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`boolean`**</mark>  | Use alternative button style. `(default: false)`                |
| **widthPercent&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>   | Button width in percents. \[0.0, 1.0] `(default: 1.0)`          |

Creates new `CMenuButton`.

#### Example

```lua
group:Button( "button", function( this )
	Log.Write( "Button '" .. this:Name() .. "' has been clicked."  )
end )
```

## <sub>Combo</sub>

`:Combo(comboName, items, [defaultValue]):` [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

| Name                                                               | Type                                              | Description                                           |
| ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **comboName**                                                      | <mark style="color:purple;">**`string`**</mark>   |                                                       |
| **items**                                                          | <mark style="color:purple;">**`string[]`**</mark> |                                                       |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>  | Index of default item. (starts from 0) `(default: 0)` |

Creates new `CMenuComboBox`.

## <sub>MultiCombo</sub>

`:MultiCombo(multiComboName, items, enabledItems):` [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

| Name               | Type                                              | Description            |
| ------------------ | ------------------------------------------------- | ---------------------- |
| **multiComboName** | <mark style="color:purple;">**`string`**</mark>   |                        |
| **items**          | <mark style="color:purple;">**`string[]`**</mark> |                        |
| **enabledItems**   | <mark style="color:purple;">**`string[]`**</mark> | table of enabled items |

Creates new `CMenuMultiComboBox`.

#### Example

```lua
group:MultiCombo( "multiCombo", { "item1", "item2", "item3" }, { "item1", "item3" } )
```

## <sub>MultiSelect</sub>

`:MultiSelect(multiSelectName, items, [expanded]):` [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

| Name                                                           | Type                                                                                               | Description                                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **multiSelectName**                                            | <mark style="color:purple;">**`string`**</mark>                                                    |                                                                                |
| **items**                                                      | <mark style="color:purple;">**`{nameId: string, imagePath: string, isEnabled: boolean}[]`**</mark> | See example.                                                                   |
| **expanded&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                   | false if you want to create MultiSelect in collapsed state. `(default: false)` |

Creates new `CMenuMultiSelect`.

#### Example

```lua
group:MultiSelect( "multiSelect", {
 	{ "1", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
 	{ "2", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
}, true )
```

## <sub>Input</sub>

`:Input(inputName, defaultValue, [imageIcon]):` [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

| Name                                                            | Type                                            | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **inputName**                                                   | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **defaultValue**                                                | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuInputBox`.

## <sub>Label</sub>

`:Label(labelText, [imageIcon]):` [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

| Name                                                            | Type                                            | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **labelText**                                                   | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuLabel`.

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets group's disabled state. Depends on argument.

#### Example

```lua
-- setter
group:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = group:Disabled()
```

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets group's visible state. Depends on argument.

#### Example

```lua
-- setter
group:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = group:Visible()
```

## <sub>SearchHidden</sub>

`:SearchHidden(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets group's search state. Depends on argument.

#### Example

```lua
-- setter
group:SearchHidden(false)
```

## <sub>SearchHidden</sub>

`:SearchHidden():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isSearchHidden = group:SearchHidden()
```


--------------------------------------------------------------------------------

### Classes - UI Widgets

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets -->

# Widgets

- [CMenuSwitch](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md)
- [CMenuSliderFloat](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md)
- [CMenuSliderInt](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md)
- [CMenuButton](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md)
- [CMenuColorPicker](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md)
- [CMenuColorPickerAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)
- [CMenuComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md)
- [CMenuGearAttachment](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)
- [CMenuInputBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md)
- [CMenuMultiComboBox](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md)
- [CMenuMultiSelect](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md)
- [CMenuBind](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md)
- [CMenuLabel](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch -->

# CMenuSwitch

CMenuSwitch metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
switch:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = switch:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
switch:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = switch:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`boolean`**</mark>

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                | Description                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuSwitch):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                    | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                | Description                                     |
| ------------ | ------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuSwitch):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat -->

# CMenuSliderFloat

CMenuSliderFloat metatable.

## <sub>Update</sub>

`:Update(minValue, maxValue, defaultValue):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                            | Description |
| ---------------- | ----------------------------------------------- | ----------- |
| **minValue**     | <mark style="color:purple;">**`number`**</mark> |             |
| **maxValue**     | <mark style="color:purple;">**`number`**</mark> |             |
| **defaultValue** | <mark style="color:purple;">**`number`**</mark> |             |

Updates the slider values.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
switch:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = switch:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
switch:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = switch:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`number`**</mark>

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                     | Description                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuSliderFloat):nil`**</mark> | function to be called on widget change.\\                                |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                         | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                     | Description                                     |
| ------------ | ------------------------------------------------------------------------ | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuSliderFloat):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint -->

# CMenuSliderInt

CMenuSliderInt metatable.

## <sub>Update</sub>

`:Update(minValue, maxValue, defaultValue):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| **minValue**     | <mark style="color:purple;">**`integer`**</mark> |             |
| **maxValue**     | <mark style="color:purple;">**`integer`**</mark> |             |
| **defaultValue** | <mark style="color:purple;">**`integer`**</mark> |             |

Updates the slider values.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
switch:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = switch:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
switch:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = switch:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`integer`**</mark>

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`integer`**</mark> |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                   | Description                                                              |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuSliderInt):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                       | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                   | Description                                     |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuSliderInt):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton -->

# CMenuButton

CMenuButton metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                | Description                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuButton):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                    | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                | Description                                     |
| ------------ | ------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuButton):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker -->

# CMenuColorPicker

CMenuColorPicker metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                                          | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **value** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                     | Description                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuColorPicker):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                         | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                     | Description                                     |
| ------------ | ------------------------------------------------------------------------ | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuColorPicker):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>HideAlphaBar</sub>

`:HideAlphaBar(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets alpha bar state. Depends on argument.

#### Example

```lua
-- setter
widget:HideAlphaBar( true )
```

## <sub>HideAlphaBar</sub>

`:HideAlphaBar():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isAlphaBarHidden = widget:HideAlphaBar()
```

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment -->

# CMenuColorPickerAttachment

CMenuColorPickerAttachment metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Get</sub>

`:Get():` [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                                          | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **value** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) |             |

Sets widget's value.

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                               | Description                                                              |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuColorPickerAttachment):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                   | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                               | Description                                     |
| ------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuColorPickerAttachment):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox -->

# CMenuComboBox

CMenuComboBox metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Update</sub>

`:Update(items, [defaultValue]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                               | Type                                              | Description                                           |
| ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **items**                                                          | <mark style="color:purple;">**`string[]`**</mark> |                                                       |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>  | Index of default item. (starts from 0) `(default: 0)` |

Update the combo box values.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`integer`**</mark>

Returns index of the selected item. It starts from 0.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`integer`**</mark> |             |

Sets widget's value.

## <sub>List</sub>

`:List():` <mark style="color:purple;">**`string[]`**</mark>

Returns array of the items.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                  | Description                                                              |
| --------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuComboBox):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                      | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                  | Description                                     |
| ------------ | --------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuComboBox):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment -->

# CMenuGearAttachment

CMenuGearAttachment metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

\`:ForceLocalization(newText):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>Find</sub>

`:Find(widgetName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) | [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **widgetName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the widget by name.

## <sub>Switch</sub>

`:Switch(switchName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

| Name                                                               | Type                                             | Description                                                |
| ------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------- |
| **switchName**                                                     | <mark style="color:purple;">**`string`**</mark>  |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | `(default: false)`                                         |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>  | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuSwitch`.

## <sub>Bind</sub>

`:Bind(bindName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuBind`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

| Name                                                               | Type                                                                                                                 | Description                                                |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **bindName**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                      |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode) | `(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`           |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuBind`.

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

| Name                                                         | Type                                                                                                                   | Description                                                               |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **sliderName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                        |                                                                           |
| **minValue**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **maxValue**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **defaultValue**                                             | <mark style="color:purple;">**`integer`**</mark>                                                                       |                                                                           |
| **format&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`fun(value: integer):string`**</mark> | Format string or function to format value. See example. `(default: "%d")` |

Creates new `CMenuSliderInt` or `CMenuSliderFloat` depents on arg types.\
`minValue`, `maxValue` and `defaultValue` should be integer to create `CMenuSliderInt`.

#### Example

```lua
-- Create slider with integer values
gear:Slider( "slider", 0, 100, 50, "%d" )
-- Create slider with integer values and custom format function
gear:Slider( "slider", 0, 100, 50, function( value ) return "%d%%" end ) -- turns into
"50%"
```

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

| Name                                                         | Type                                                                                                                  | Description                                                               |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **sliderName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                       |                                                                           |
| **minValue**                                                 | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **maxValue**                                                 | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **defaultValue**                                             | <mark style="color:purple;">**`number`**</mark>                                                                       |                                                                           |
| **format&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`fun(value: number):string`**</mark> | Format string or function to format value. See example. `(default: "%f")` |

Creates new `CMenuSliderFloat`.

#### Example

```lua
-- Create slider with float values
gear:Slider( "slider", 0.0, 1.0, 0.5, "%.2f" ) -- turns into "0.50"
-- Create slider with float values and custom format function
gear:Slider( "slider", 0.0, 100.0, 50.0, function( value )
	if value < 50 then
		return "Low(%f)"
	else
		return "High(%f)"
  end
end )
```

## <sub>ColorPicker</sub>

`:ColorPicker(colorPickerName, color, [imageIcon]):` [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

| Name                                                            | Type                                                                                                                          | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **colorPickerName**                                             | <mark style="color:purple;">**`string`**</mark>                                                                               |                                                            |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark>                                                                               | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuColorPicker`.

## <sub>Combo</sub>

`:Combo(comboName, items, [defaultValue]):` [<mark style="color:purple;">**`CMenuComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

| Name                                                               | Type                                              | Description                                           |
| ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **comboName**                                                      | <mark style="color:purple;">**`string`**</mark>   |                                                       |
| **items**                                                          | <mark style="color:purple;">**`string[]`**</mark> |                                                       |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>  | Index of default item. (starts from 0) `(default: 0)` |

Creates new `CMenuComboBox`.

## <sub>MultiCombo</sub>

`:MultiCombo(multiComboName, items, enabledItems):` [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

| Name               | Type                                              | Description            |
| ------------------ | ------------------------------------------------- | ---------------------- |
| **multiComboName** | <mark style="color:purple;">**`string`**</mark>   |                        |
| **items**          | <mark style="color:purple;">**`string[]`**</mark> |                        |
| **enabledItems**   | <mark style="color:purple;">**`string[]`**</mark> | table of enabled items |

Creates new `CMenuMultiComboBox`.

#### Example

```lua
gear:MultiCombo( "multiCombo", { "item1", "item2", "item3" }, { "item1", "item3" } )
```

## <sub>MultiSelect</sub>

`:MultiSelect(multiSelectName, items, [expanded]):` [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

| Name                                                           | Type                                                                                               | Description                                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **multiSelectName**                                            | <mark style="color:purple;">**`string`**</mark>                                                    |                                                                                |
| **items**                                                      | <mark style="color:purple;">**`{nameId: string, imagePath: string, isEnabled: boolean}[]`**</mark> | See example.                                                                   |
| **expanded&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                   | false if you want to create MultiSelect in collapsed state. `(default: false)` |

Creates new `CMenuMultiSelect`.

#### Example

```lua
gear:MultiSelect( "multiSelect", {
 	{ "1", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
 	{ "2", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
}, true )
```

## <sub>Input</sub>

`:Input(inputName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuInputBox`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

| Name                                                               | Type                                            | Description                                                |
| ------------------------------------------------------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| **inputName**                                                      | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | `(default: "")`                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuInputBox`.

## <sub>Label</sub>

`:Label(labelText, [imageIcon]):` [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel)

| Name                                                            | Type                                            | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **labelText**                                                   | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuLabel`.

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox -->

# CMenuInputBox

CMenuInputBox metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
switch:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = switch:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
switch:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = switch:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`string`**</mark>

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`string`**</mark> |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                  | Description                                                              |
| --------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuInputBox):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                      | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                  | Description                                     |
| ------------ | --------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuInputBox):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox -->

# CMenuMultiComboBox

CMenuMultiComboBox metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Update</sub>

`:Update(items, enabledItems):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                              | Description            |
| ---------------- | ------------------------------------------------- | ---------------------- |
| **items**        | <mark style="color:purple;">**`string[]`**</mark> |                        |
| **enabledItems** | <mark style="color:purple;">**`string[]`**</mark> | table of enabled items |

Updates the multicombo values.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get(itemId):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                            | Description |
| ---------- | ----------------------------------------------- | ----------- |
| **itemId** | <mark style="color:purple;">**`string`**</mark> |             |

Returns enable state of the item in combo box.

## <sub>Set</sub>

`:Set(enabledItems):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                              | Description                                             |
| ---------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **enabledItems** | <mark style="color:purple;">**`string[]`**</mark> | A table of enabled items; other items will be disabled. |

Sets a new value for the item by itemId or sets a new list of enabled items

## <sub>Set</sub>

`:Set(itemId, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description |
| ---------- | ------------------------------------------------ | ----------- |
| **itemId** | <mark style="color:purple;">**`string`**</mark>  |             |
| **value**  | <mark style="color:purple;">**`boolean`**</mark> |             |

## <sub>List</sub>

`:List():` <mark style="color:purple;">**`string[]`**</mark>

Returns array of itemIds.

## <sub>ListEnabled</sub>

`:ListEnabled():` <mark style="color:purple;">**`string[]`**</mark>

Returns array of enabled itemIds.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                       | Description                                                              |
| --------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuMultiComboBox):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                           | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                       | Description                                     |
| ------------ | -------------------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuMultiComboBox):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect -->

# CMenuMultiSelect

CMenuMultiSelect metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Update</sub>

`:Update(items, [expanded], [saveToConfig]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                               | Type                                                                                               | Description                                                                    |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **items**                                                          | <mark style="color:purple;">**`{nameId: string, imagePath: string, isEnabled: boolean}[]`**</mark> | See `CMenuGroup:MultiSelect`.                                                  |
| **expanded&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`boolean`**</mark>                                                   | false if you want to create MultiSelect in collapsed state. `(default: false)` |
| **saveToConfig&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                   | true if you want to save to config `(default: false)`                          |

Updates the multiselect values.

## <sub>OneItemSelection</sub>

`:OneItemSelection(newState):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                             | Description |
| ------------ | ------------------------------------------------ | ----------- |
| **newState** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets one item selection state. One item selection allows only one item to be\
selected. Depends on the argument.

## <sub>OneItemSelection</sub>

`:OneItemSelection():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>DragAllowed</sub>

`:DragAllowed(newState):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                             | Description |
| ------------ | ------------------------------------------------ | ----------- |
| **newState** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets drag allowed state. Drag allows items to be ordered by cursor.\
Depends on the argument.

## <sub>DragAllowed</sub>

`:DragAllowed():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get(itemId):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                            | Description |
| ---------- | ----------------------------------------------- | ----------- |
| **itemId** | <mark style="color:purple;">**`string`**</mark> |             |

Returns enable state of the item in multiselect.

## <sub>Set</sub>

`:Set(enabledItems):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                              | Description                                             |
| ---------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **enabledItems** | <mark style="color:purple;">**`string[]`**</mark> | A table of enabled items; other items will be disabled. |

Sets a new value for the item by itemId or sets a new list of enabled items

## <sub>Set</sub>

`:Set(itemId, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description |
| ---------- | ------------------------------------------------ | ----------- |
| **itemId** | <mark style="color:purple;">**`string`**</mark>  |             |
| **value**  | <mark style="color:purple;">**`boolean`**</mark> |             |

## <sub>List</sub>

`:List():` <mark style="color:purple;">**`string[]`**</mark>

Returns array of itemIds.

## <sub>ListEnabled</sub>

`:ListEnabled():` <mark style="color:purple;">**`string[]`**</mark>

Returns array of enabled itemIds.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                                     | Description                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuMultiSelect):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                         | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                     | Description                                     |
| ------------ | ------------------------------------------------------------------------ | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuMultiSelect):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>UpdateBackgroundColors</sub>

`:UpdateBackgroundColors(colors):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                   | Description                   |
| ---------- | ------------------------------------------------------ | ----------------------------- |
| **colors** | <mark style="color:purple;">**`table<string>`**</mark> | Table with background colors. |

Updates widget's background colors.

## <sub>UpdateImageColors</sub>

`:UpdateImageColors(colors):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                   | Description              |
| ---------- | ------------------------------------------------------ | ------------------------ |
| **colors** | <mark style="color:purple;">**`table<string>`**</mark> | Table with image colors. |

Updates widget's image colors.

## <sub>UpdateToolTips</sub>

`:UpdateToolTips(colors):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                   | Description             |
| ---------- | ------------------------------------------------------ | ----------------------- |
| **colors** | <mark style="color:purple;">**`table<string>`**</mark> | Table with new tooltips |

Updates widget's tooltips

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind -->

# CMenuBind

CMenuBind metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.widgettype)

Returns widget's type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

{% hint style="info" %}
Not recommended for use due to its complexity
{% endhint %}

`:ForceLocalization(newText):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>ToolTip</sub>

`:ToolTip(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Gets or sets tooltip. Tooltip is displayed when mouse cursor is over the widget.\
Depends on the argument.

## <sub>ToolTip</sub>

`:ToolTip():` <mark style="color:purple;">**`string`**</mark>

## <sub>Visible</sub>

`:Visible(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets visible state. Depends on argument.

#### Example

```lua
-- setter
widget:Visible(false)
```

## <sub>Visible</sub>

`:Visible():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isVisible = widget:Visible()
```

## <sub>Disabled</sub>

`:Disabled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets disabled state. Depends on argument.

#### Example

```lua
-- setter
widget:Disabled( false )
```

## <sub>Disabled</sub>

`:Disabled():` <mark style="color:purple;">**`boolean`**</mark>

#### Example

```lua
-- getter
local isDisabled = widget:Disabled()
```

## <sub>Unsafe</sub>

`:Unsafe(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets unsafe state. Unsafe widgets have warning sign.\
Depends on argument.

## <sub>Unsafe</sub>

`:Unsafe():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>Get</sub>

`:Get([idx]):` [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode)

| Name                                                      | Type                                                                                     | Description                                          |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **idx&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`0`**</mark> \| <mark style="color:purple;">**`1`**</mark> | index of the button to get value from `(default: 0)` |

Returns widget's value. To get both of the buttons use `Buttons` method.

## <sub>Set</sub>

`:Set(key1, [key2]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                       | Type                                                                                                                 | Description                                                 |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **key1**                                                   | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode) | primary button code                                         |
| **key2&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode) | secondary button code `(default: Enum.ButtonCode.KEY_NONE)` |

Sets widget's value.

## <sub>Buttons</sub>

`:Buttons():` [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode), [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/enums#enum.buttoncode)

Returns widget's buttons value.

## <sub>IsDown</sub>

`:IsDown():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` when the key or both keys is down.

## <sub>IsPressed</sub>

`:IsPressed():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` when the key or both keys is pressed for the first time.

## <sub>IsToggled</sub>

`:IsToggled():` <mark style="color:purple;">**`boolean`**</mark>

Bind stores it's toggle state and switches it when the key is pressed. This method\
returns this state.

## <sub>SetToggled</sub>

`:SetToggled(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **value** | <mark style="color:purple;">**`boolean`**</mark> |             |

Sets the toggle state manually.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                                                  | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                                                 |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                             | Description                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                  | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

{% hint style="info" %}
Multiple callbacks could be set.
{% endhint %}

\`:SetCallback(callback, \[forceCall]):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name                                                            | Type                                                              | Description                                                              |
| --------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **callback**                                                    | <mark style="color:purple;">**`fun(this: CMenuBind):nil`**</mark> | function to be called on widget change.                                  |
| **forceCall&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                  | true if you want to call callback on widget creation. `(default: false)` |

Sets widget's on change callback.

## <sub>UnsetCallback</sub>

`:UnsetCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                              | Description                                     |
| ------------ | ----------------------------------------------------------------- | ----------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuBind):nil`**</mark> | function to be removed from widget's callbacks. |

Removes widget's on change callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

| Name      | Type                                                                                                                          | Description             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                                               | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

## <sub>Properties</sub>

`:Properties([name], [value], [markAsToggle]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                               | Type                                             | Description                                                                                                                                                                                                                |
| ------------------------------------------------------------------ | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`string`**</mark>  | Overridden name to display in bind list. `(default: nil)`                                                                                                                                                                  |
| **value&#x20;**<mark style="color:orange;">**`[?]`**</mark>        | <mark style="color:purple;">**`string`**</mark>  | Overridden value to display alongside the name in the bind list. This can be used to provide additional context about the bind. `(default: nil)`                                                                           |
| **markAsToggle&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Indicates whether the bind should be marked as a toggle, which is particularly useful if the bind's functionality includes toggling states. Recommended to be used in conjunction with the IsToggled(). `(default: false)` |

Updates the properties of a widget for display in the bind list.

## <sub>ShowInBindIsland</sub>

`:ShowInBindIsland(newStatus):` <mark style="color:purple;">**`boolean`**</mark>

| Name          | Type                                             | Description |
| ------------- | ------------------------------------------------ | ----------- |
| **newStatus** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets the visibility of the bind in the bind island.

## <sub>ShowInBindIsland</sub>

`:ShowInBindIsland():` <mark style="color:purple;">**`boolean`**</mark>

## <sub>MouseBinding</sub>

`:MouseBinding(newStatus):` <mark style="color:purple;">**`boolean`**</mark>

| Name          | Type                                             | Description |
| ------------- | ------------------------------------------------ | ----------- |
| **newStatus** | <mark style="color:purple;">**`boolean`**</mark> |             |

Gets or sets the ability to bind the mouse button.

## <sub>MouseBinding</sub>

`:MouseBinding():` <mark style="color:purple;">**`boolean`**</mark>


--------------------------------------------------------------------------------

### Classes - Math

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math -->

# Math

- [Vector](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)
- [Angle](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)
- [Vec2](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)
- [Vertex](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector -->

# Vector

Vector metatable

### Fields

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |
| **z** | <mark style="color:purple;">**`number`**</mark> |             |

## <sub>Vector</sub>

`Vector([x], [y], [z]):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name                                                    | Type                                            | Description      |
| ------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **x&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **y&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **z&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |

Create a new Vector.

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>\_\_add</sub>

{% hint style="info" %}
Overload for operator +
{% endhint %}

`:__add(other):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                                                                                                                                                                                                                                        | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_sub</sub>

{% hint style="info" %}
Overload for operator -
{% endhint %}

`:__sub(other):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                                                                                                                                                                                                                                        | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_div</sub>

{% hint style="info" %}
Overload for operator /
{% endhint %}

`:__div(other):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                                                                                                                                                                                                                                        | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_mul</sub>

{% hint style="info" %}
Overload for operator \*
{% endhint %}

`:__mul(other):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                                                                                                                                                                                                                                        | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_eq</sub>

{% hint style="info" %}
Overload for operator ==
{% endhint %}

\`:\_\_eq(other):\` <mark style="color:purple;">\*\*\`boolean\`\*\*</mark>

| Name      | Type                                                                                                                                 | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

## <sub>Distance</sub>

`:Distance(other):` <mark style="color:purple;">**`number`**</mark>

| Name      | Type                                                                                                                                 | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

Computes the distance from this vector to other.

## <sub>Distance2D</sub>

`:Distance2D(other):` <mark style="color:purple;">**`number`**</mark>

| Name      | Type                                                                                                                                 | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

Computes the distance from this vector to other ignoring Z axis.

## <sub>Normalized</sub>

`:Normalized():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns this vector with a length of 1.\
When normalized, a vector keeps the same direction but its length is 1.0.\
Note that the current vector is unchanged and a new normalized vector is returned. If you want to normalize the current vector, use `Vector:Normalize` function.

## <sub>Normalize</sub>

`:Normalize():` <mark style="color:purple;">**`nil`**</mark>

Makes this vector have a length of 1.\
When normalized, a vector keeps the same direction but its length is 1.0.\
Note that this function will change the current vector. If you want to keep the current vector unchanged, use `Vector:Normalized` function.

## <sub>Dot</sub>

`:Dot(vector):` <mark style="color:purple;">**`number`**</mark>

| Name       | Type                                                                                                                                 | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **vector** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

Dot Product of two vectors.\
The dot product is a float value equal to the magnitudes of the two vectors multiplied together and then multiplied by the cosine of the angle between them.\
For normalized vectors Dot returns 1 if they point in exactly the same direction, -1 if they point in completely opposite directions and zero if the vectors are perpendicular.\
\
[More](https://medium.com/@r.w.overdijk/unity-vector3-dot-what-11feb258052e)

## <sub>Dot2D</sub>

`:Dot2D(vector):` <mark style="color:purple;">**`number`**</mark>

| Name       | Type                                                                                                                                 | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **vector** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

Dot Product of two vectors ignoring Z axis.

## <sub>Scaled</sub>

`:Scaled(scale):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **scale** | <mark style="color:purple;">**`number`**</mark> |             |

Returns this vector multiplied by the given number. The same as `Vector * number`.

## <sub>Scale</sub>

`:Scale(scale):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **scale** | <mark style="color:purple;">**`number`**</mark> |             |

Multiplies this vector by the given number. The same as `Vector = Vector * number`.

## <sub>Length</sub>

`:Length():` <mark style="color:purple;">**`number`**</mark>

Returns the length of this vector.\
The length of the vector is `math.sqrt(x*x+y*y+z*z)`.\
If you only need to compare length of some vectors, you can compare squared magnitudes of them using LengthSqr (computing squared length is faster).

## <sub>LengthSqr</sub>

`:LengthSqr():` <mark style="color:purple;">**`number`**</mark>

Returns the squared length of this vector.\
This method is faster than Length because it avoids computing a square root. Use this method if you need to compare vectors.

## <sub>Length2D</sub>

`:Length2D():` <mark style="color:purple;">**`number`**</mark>

Returns the length of this vector ignoring Z axis.

## <sub>Length2DSqr</sub>

`:Length2DSqr():` <mark style="color:purple;">**`number`**</mark>

Returns the squared length of this vector ignoring Z axis.\
This method is faster than Length2D because it avoids computing a square root. Use this method if you need to compare vectors.

## <sub>Rotated</sub>

`:Rotated(angle):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                                                                                                  | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **angle** | <mark style="color:purple;">**`number`**</mark> \| [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle) |             |

Returns the new vector rotated counterclockwise by the given angle in the XY-plane, leaving the Z-axis unaffected.

## <sub>Rotate</sub>

`:Rotate(angle):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                                                                                                  | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **angle** | <mark style="color:purple;">**`number`**</mark> \| [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle) |             |

Rotates this vector counterclockwise by the given angle in the XY-plane, leaving the Z-axis unaffected.

## <sub>Lerp</sub>

`:Lerp(b, t):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name  | Type                                                                                                                                 | Description                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| **b** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | end value, returned when t = 1             |
| **t** | <mark style="color:purple;">**`number`**</mark>                                                                                      | value used to interpolate between a and b. |

Returns linearly interpolated vector between two vectors.\
The value returned equals **a + (b - a) \* t** (which can also be written **a \* (1-t) + b\*t**).\
When `t = 0`, **a:Lerp(b, t)** returns `a`.\
When `t = 1`, **a:Lerp(b, t)** returns `b`.\
When `t = 0.5`, **a:Lerp(b, t)** returns the point midway between `a` and `b`.

## <sub>Cross</sub>

`:Cross(vector):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name       | Type                                                                                                                                 | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **vector** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) |             |

Returns cross product of two vectors.\
\
[More](https://docs.unity3d.com/ScriptReference/Vector3.Cross.html)\
[Visualization](https://www.youtube.com/watch?v=kz92vvioeng)

## <sub>MoveForward</sub>

`:MoveForward(angle, distance):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name         | Type                                                                                                                               | Description      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **angle**    | [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle) |                  |
| **distance** | <mark style="color:purple;">**`number`**</mark>                                                                                    | distance to move |

Moves vector forward by a specified distance in the direction defined by a given Angle.

#### Example

```lua
-- entity position moved forward by 300
local pos = Entity.GetAbsOrigin(entity):MoveForward(Entity.GetRotation(entity), 300);
```

## <sub>ToAngle</sub>

`:ToAngle():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Converts Vector to Angle. See\
<https://github.com/ValveSoftware/source-sdk-2013/blob/0565403b153dfcde602f6f58d8f4d13483696a13/src/mathlib/mathlib\\_base.cpp#L535>

## <sub>ToScreen</sub>

`:ToScreen():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2), <mark style="color:purple;">**`boolean`**</mark>

Converts Vector to screen coordinate

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns x, y and z of this vector.

## <sub>GetX</sub>

`:GetX():` <mark style="color:purple;">**`number`**</mark>

Returns x of this vector. The same as Vector.x.

## <sub>GetY</sub>

`:GetY():` <mark style="color:purple;">**`number`**</mark>

Returns y of this vector. The same as Vector.y.

## <sub>GetZ</sub>

`:GetZ():` <mark style="color:purple;">**`number`**</mark>

Returns z of this vector. The same as Vector.z.

## <sub>SetX</sub>

`:SetX(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets x. The same as Vector.x = value.

## <sub>SetY</sub>

`:SetY(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets y. The same as Vector.y = value.

## <sub>SetZ</sub>

`:SetZ(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets z. The same as Vector.z = value.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle -->

# Angle

Angle metatable

### Fields

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **pitch** | <mark style="color:purple;">**`number`**</mark> |             |
| **yaw**   | <mark style="color:purple;">**`number`**</mark> |             |
| **roll**  | <mark style="color:purple;">**`number`**</mark> |             |

## <sub>Angle</sub>

`Angle([pitch], [yaw], [roll]):` [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

| Name                                                        | Type                                            | Description      |
| ----------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **pitch&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **yaw&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **roll&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |

Create a new Angle.

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>GetForward</sub>

`:GetForward():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward vector from a given Angle.

## <sub>GetVectors</sub>

`:GetVectors():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector), [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector), [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the forward, right and up.

## <sub>GetYaw</sub>

`:GetYaw():` <mark style="color:purple;">**`number`**</mark>

Returns the yaw. The same as Angle.yaw.

## <sub>GetRoll</sub>

`:GetRoll():` <mark style="color:purple;">**`number`**</mark>

Returns the roll. The same as Angle.roll.

## <sub>GetPitch</sub>

`:GetPitch():` <mark style="color:purple;">**`number`**</mark>

Returns the pitch. The same as Angle.pitch.

## <sub>SetYaw</sub>

`:SetYaw(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets the yaw. The same as Angle.yaw = value.

## <sub>SetRoll</sub>

`:SetRoll(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets the roll. The same as Angle.roll = value.

## <sub>SetPitch</sub>

`:SetPitch(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets the pitch. The same as Angle.pitch = value.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2 -->

# Vec2

Vec2 metatable

### Fields

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

## <sub>Vec2</sub>

`Vec2(x, y):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

Create a new Vec2.

## <sub>Vec2</sub>

`Vec2():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Create a new Vec2(0,0).

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>\_\_add</sub>

{% hint style="info" %}
Overload for operator +
{% endhint %}

`:__add(other):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

| Name      | Type                                                                                                                                                                                | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_sub</sub>

{% hint style="info" %}
Overload for operator -
{% endhint %}

`:__sub(other):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

| Name      | Type                                                                                                                                                                                | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_div</sub>

{% hint style="info" %}
Overload for operator /
{% endhint %}

\`:\_\_div(other):\` \[<mark style="color:purple;">\*\*\`Vec2\`\*\*</mark>]\(Vec2.md)

| Name      | Type                                                                                                                                                                                | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>Length</sub>

`:Length():` <mark style="color:purple;">**`number`**</mark>

Returns the length of the vector.

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns x, y of this vector.

## <sub>GetX</sub>

`:GetX():` <mark style="color:purple;">**`number`**</mark>

Returns x of this vector. The same as Vec2.x.

## <sub>GetY</sub>

`:GetY():` <mark style="color:purple;">**`number`**</mark>

Returns y of this vector. The same as Vec2.y.

## <sub>SetX</sub>

`:SetX(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets x. The same as Vec2.x = value.

## <sub>SetY</sub>

`:SetY(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **value** | <mark style="color:purple;">**`number`**</mark> |             |

Sets y. The same as Vec2.y = value.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex -->

# Vertex

Vertex metatable

### Fields

| Name    | Type                                                                                                                             | Description |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **pos** | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | screen pos  |
| **uv**  | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | texture uv  |

## <sub>Vertex</sub>

`Vertex(pos, uv):` [<mark style="color:purple;">**`Vertex`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

| Name    | Type                                                                                                                             | Description |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **pos** | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) |             |
| **uv**  | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) |             |

Create a new Vertex.

## <sub>Vertex</sub>

`Vertex(posx, posy, uvx, uvy):` [<mark style="color:purple;">**`Vertex`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

| Name     | Type                                            | Description |
| -------- | ----------------------------------------------- | ----------- |
| **posx** | <mark style="color:purple;">**`number`**</mark> |             |
| **posy** | <mark style="color:purple;">**`number`**</mark> |             |
| **uvx**  | <mark style="color:purple;">**`number`**</mark> |             |
| **uvy**  | <mark style="color:purple;">**`number`**</mark> |             |

Create a new Vertex(0,0).

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>\_\_add</sub>

{% hint style="info" %}
Overload for operator +
{% endhint %}

`:__add(other):` [<mark style="color:purple;">**`Vertex`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

| Name      | Type                                                                                                                                                                                    | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vertex`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_sub</sub>

{% hint style="info" %}
Overload for operator -
{% endhint %}

\`:\_\_sub(other):\` \[<mark style="color:purple;">\*\*\`Vertex\`\*\*</mark>]\(Vertex.md)

| Name      | Type                                                                                                                                                                                    | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vertex`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex) \| <mark style="color:purple;">**`number`**</mark> |             |


--------------------------------------------------------------------------------

## Game Components - Entity Lists

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists -->

# Lists

- [Abilities](/api-v2.0/game-components/lists/abilities.md)
- [Couriers](/api-v2.0/game-components/lists/couriers.md)
- [CustomEntities](/api-v2.0/game-components/lists/customentities.md)
- [Entities](/api-v2.0/game-components/lists/entities.md)
- [Heroes](/api-v2.0/game-components/lists/heroes.md)
- [NPCs](/api-v2.0/game-components/lists/npcs.md)
- [Camps](/api-v2.0/game-components/lists/camps.md)
- [Players](/api-v2.0/game-components/lists/players.md)
- [Runes](/api-v2.0/game-components/lists/runes.md)
- [TempTrees](/api-v2.0/game-components/lists/temptrees.md)
- [Towers](/api-v2.0/game-components/lists/towers.md)
- [Trees](/api-v2.0/game-components/lists/trees.md)
- [Physical Items](/api-v2.0/game-components/lists/physicalitems.md)
- [Modifiers](/api-v2.0/game-components/lists/modifiers.md)
- [LinearProjectiles](/api-v2.0/game-components/lists/linearprojectiles.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/abilities -->

# Abilities

Table to work with ability list.

## <sub>Count</sub>

`Abilities.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of ability list.

## <sub>Get</sub>

`Abilities.Get(index):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                     |
| --------- | ------------------------------------------------ | ------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of ability in cheat list. |

Return ability by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Abilities.GetAll():` [<mark style="color:purple;">**`CAbility[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

Return all abilities in cheat list.

## <sub>Contains</sub>

`Abilities.Contains(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description       |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | Ability to check. |

Check ability in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/couriers -->

# Couriers

Table to work with courier list.

## <sub>Count</sub>

`Couriers.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of courier list.

## <sub>Get</sub>

`Couriers.Get(index):` [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                     |
| --------- | ------------------------------------------------ | ------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of courier in cheat list. |

Return courier by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Couriers.GetAll():` [<mark style="color:purple;">**`CCourier[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier)

Return all couriers in cheat list.

## <sub>Contains</sub>

`Couriers.Contains(courier):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description       |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | Courier to check. |

Check courier in cheat list.

## <sub>GetLocal</sub>

`Couriers.GetLocal():` [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | <mark style="color:purple;">**`nil`**</mark>

Return local courier.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/customentities -->

# CustomEntities

Table to work with specific abilities.

## <sub>GetSpiritBear</sub>

`CustomEntities.GetSpiritBear(spiritBear):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                                                                                                 | Description              |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **spiritBear** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | The Spirit Bear ability. |

Accept the Spirit Bear ability and return linked Bear.

## <sub>GetVengeIllusion</sub>

`CustomEntities.GetVengeIllusion(commandAura):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                                                                                                 | Description               |
| --------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **commandAura** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | The Command Aura ability. |

Accept the Vengeful Spirit's Command Aura ability and return scepter linked illusion.

## <sub>GetTetheredUnit</sub>

`CustomEntities.GetTetheredUnit(tether):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                 | Description         |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **tether** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | The Tether ability. |

Accept the Wisp's Tether ability and return linked unit.

## <sub>GetTempestDouble</sub>

`CustomEntities.GetTempestDouble(tempestDouble):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                                                                                                 | Description                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **tempestDouble** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | The Tempest Double ability. |

Accept the Arc Warden's Tempest Double ability and return linked clone.

## <sub>GetMeepoIndex</sub>

`CustomEntities.GetMeepoIndex(dividedWeStand):` <mark style="color:purple;">**`integer`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                                 | Description                   |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **dividedWeStand** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | The Divided We Stand ability. |

Accept the Meepo's Divided We Stand ability and return index of Meepo.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/entities -->

# Entities

Table to work with entity list.

## <sub>GetAll</sub>

`Entities.GetAll():` [<mark style="color:purple;">**`CEntity[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)

Get all entities on the map.

## <sub>Contains</sub>

`Entities.Contains(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description      |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | Entity to check. |

Check entity in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/heroes -->

# Heroes

Table to work with hero list.

## <sub>Count</sub>

`Heroes.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of hero list.

## <sub>Get</sub>

`Heroes.Get(index):` [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of hero in cheat list. |

Return hero by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Heroes.GetAll():` [<mark style="color:purple;">**`CHero[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

Return all heroes in cheat list.

## <sub>Contains</sub>

`Heroes.Contains(hero):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description    |
| -------- | -------------------------------------------------------------------------------------------------------------- | -------------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | Hero to check. |

Check hero in cheat list.

## <sub>InRadius</sub>

`Heroes.InRadius(pos, radius, teamNum, teamType, [omitIllusions], [omitDormant]):` [<mark style="color:purple;">**`CHero[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

| Name                                                                | Type                                                                                                                                        | Description                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **pos**                                                             | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)        | Position to check.                                                      |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                             | Radius to check.                                                        |
| **teamNum**                                                         | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)   | Team number to check.                                                   |
| **teamType**                                                        | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | Team type to filter by. Relative to teamNum param.                      |
| **omitIllusions&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without illusions `(default: false)`    |
| **omitDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without dormant units `(default: true)` |

Return all heroes in radius.

## <sub>GetLocal</sub>

`Heroes.GetLocal():` [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | <mark style="color:purple;">**`nil`**</mark>

Return local hero.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/npcs -->

# NPCs

Table to work with NPC list.

## <sub>Count</sub>

`NPCs.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of NPC list.

## <sub>Get</sub>

`NPCs.Get(index):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                 |
| --------- | ------------------------------------------------ | --------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of NPC in cheat list. |

Return NPC by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`NPCs.GetAll([filter]):` [<mark style="color:purple;">**`CNPC[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

| Name                                                         | Type                                                                                                                                                                                                                     | Description      |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **filter&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.UnitTypeFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags) \| <mark style="color:purple;">**`fun(npc: CNPC):boolean`**</mark> | `(default: nil)` |

Return all NPCs in cheat list. Can be filtered by unit type or custom function.\
Unit type filter is a much faster than custom function and can be or'ed to filter multiple types.

#### Example

```lua
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

## <sub>GetInScreen</sub>

`NPCs.GetInScreen([filter], [skipDormant]):` <mark style="color:purple;">**`{entity:CNPC, position:Vec2}[]`**</mark>

| Name                                                              | Type                                                                                                                                                                                                  | Description                                                             |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **filter&#x20;**<mark style="color:orange;">**`[?]`**</mark>      | [<mark style="color:purple;">**`Enum.UnitTypeFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags) \| <mark style="color:purple;">**`nil`**</mark> | `(default: nil)`                                                        |
| **skipDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                      | `true` if you want to get table without dormant units `(default: true)` |

Return all NPCs in cheat list that visible on your screen. Can be filtered by unit type argument.

## <sub>InRadius</sub>

`NPCs.InRadius(pos, radius, teamNum, teamType, [omitIllusions], [omitDormant]):` [<mark style="color:purple;">**`CNPC[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

| Name                                                                | Type                                                                                                                                        | Description                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **pos**                                                             | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)        | Position to check.                                                      |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                             | Radius to check.                                                        |
| **teamNum**                                                         | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)   | Team number to check.                                                   |
| **teamType**                                                        | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | Team type to filter by. Relative to teamNum param.                      |
| **omitIllusions&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without illusions `(default: false)`    |
| **omitDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without dormant units `(default: true)` |

Return all NPCs in radius.

## <sub>Contains</sub>

`NPCs.Contains(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description   |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | NPC to check. |

Check NPC in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/camps -->

# Camps

Table to work with list of neutral spawners.

## <sub>Count</sub>

`Camps.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of neutral spawner list.

## <sub>Get</sub>

`Camps.Get(index):` [<mark style="color:purple;">**`CCamp`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                             |
| --------- | ------------------------------------------------ | --------------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of neutral spawner in cheat list. |

Return neutral spawner by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Camps.GetAll():` [<mark style="color:purple;">**`CCamp[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp)

Return all neutral spawners in cheat list.

## <sub>InRadius</sub>

`Camps.InRadius(pos, radius):` [<mark style="color:purple;">**`CCamp[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp)

| Name       | Type                                                                                                                                 | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **pos**    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Position to check. |
| **radius** | <mark style="color:purple;">**`number`**</mark>                                                                                      | Radius to check.   |

Return all neutral spawners in radius.

## <sub>Contains</sub>

`Camps.Contains(camp):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description               |
| -------- | -------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp) | Neutral spawner to check. |

Check neutral spawner in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/players -->

# Players

Table to work with player list.

## <sub>Count</sub>

`Players.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of player list.

## <sub>Get</sub>

`Players.Get(index):` [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                    |
| --------- | ------------------------------------------------ | ------------------------------ |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of player in cheat list. |

Return player by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Players.GetAll():` [<mark style="color:purple;">**`CPlayer[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player)

Return all players in cheat list.

## <sub>Contains</sub>

`Players.Contains(player):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description      |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | Player to check. |

Check player in cheat list.

## <sub>GetLocal</sub>

`Players.GetLocal():` [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player)

Return local player.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/runes -->

# Runes

Table to work with rune list.

## <sub>Count</sub>

`Runes.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of rune list.

## <sub>Get</sub>

`Runes.Get(index):` [<mark style="color:purple;">**`CRune`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/rune) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of rune in cheat list. |

Return rune by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Runes.GetAll():` [<mark style="color:purple;">**`CRune[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/rune)

Return all runes in cheat list.

## <sub>Contains</sub>

`Runes.Contains(rune):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description    |
| -------- | -------------------------------------------------------------------------------------------------------------- | -------------- |
| **rune** | [<mark style="color:purple;">**`CRune`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/rune) | Rune to check. |

Check rune in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/temptrees -->

# TempTrees

Table to work with list of temp trees.

## <sub>Count</sub>

`TempTrees.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of temp trees list.

## <sub>Get</sub>

`TempTrees.Get(index):` [<mark style="color:purple;">**`CTree`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                       |
| --------- | ------------------------------------------------ | --------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of temp tree in cheat list. |

Return temp tree by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`TempTrees.GetAll():` [<mark style="color:purple;">**`CTree[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Return all temp trees in cheat list.

## <sub>InRadius</sub>

`TempTrees.InRadius(pos, radius):` [<mark style="color:purple;">**`CTree[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

| Name       | Type                                                                                                                                 | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **pos**    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Position to check. |
| **radius** | <mark style="color:purple;">**`number`**</mark>                                                                                      | Radius to check.   |

Return all temp trees in radius.

## <sub>Contains</sub>

`TempTrees.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description         |
| -------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) | Temp tree to check. |

Check temp tree in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/towers -->

# Towers

Table to work with tower list.

## <sub>Count</sub>

`Towers.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of tower list.

## <sub>Get</sub>

`Towers.Get(index):` [<mark style="color:purple;">**`CTower`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tower) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                   |
| --------- | ------------------------------------------------ | ----------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of tower in cheat list. |

Return tower by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Towers.GetAll():` [<mark style="color:purple;">**`CTower[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tower)

Return all towers in cheat list.

## <sub>InRadius</sub>

`Towers.InRadius(pos, radius, teamNum, [teamType]):` [<mark style="color:purple;">**`CTower[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tower)

| Name                                                           | Type                                                                                                                                        | Description                                                 |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **pos**                                                        | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)        | Position to check.                                          |
| **radius**                                                     | <mark style="color:purple;">**`number`**</mark>                                                                                             | Radius to check.                                            |
| **teamNum**                                                    | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)   | Team number to check.                                       |
| **teamType&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | Team number to check. `(default: Enum.TeamType.TEAM_ENEMY)` |

Return all towers in radius.

## <sub>Contains</sub>

`Towers.Contains(tower):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                             | Description     |
| --------- | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| **tower** | [<mark style="color:purple;">**`CTower`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tower) | Tower to check. |

Check tower in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/trees -->

# Trees

Table to work with list of trees.

## <sub>Count</sub>

`Trees.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of tree list.

## <sub>Get</sub>

`Trees.Get(index):` [<mark style="color:purple;">**`CTree`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of tree in cheat list. |

Return tree by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Trees.GetAll():` [<mark style="color:purple;">**`CTree[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

Return all trees in cheat list.

## <sub>InRadius</sub>

`Trees.InRadius(pos, radius, [active]):` [<mark style="color:purple;">**`CTree[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

| Name                                                         | Type                                                                                                                                 | Description                              |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **pos**                                                      | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Position to check.                       |
| **radius**                                                   | <mark style="color:purple;">**`number`**</mark>                                                                                      | Radius to check.                         |
| **active&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Active state to check. `(default: true)` |

Return all trees in radius.

## <sub>Contains</sub>

`Trees.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description    |
| -------- | -------------------------------------------------------------------------------------------------------------- | -------------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) | Tree to check. |

Check tree in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/physicalitems -->

# Physical Items

Table to work with list of phisical items.

## <sub>Count</sub>

`PhysicalItems.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of physical item list.

## <sub>Get</sub>

`PhysicalItems.Get(index):` [<mark style="color:purple;">**`CPhysicalItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                           |
| --------- | ------------------------------------------------ | ------------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of physical item in cheat list. |

Return physical item by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`PhysicalItems.GetAll():` [<mark style="color:purple;">**`CPhysicalItem[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem)

Return all physical items in cheat list.

## <sub>Contains</sub>

`PhysicalItems.Contains(physical):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                           | Description                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **physical** | [<mark style="color:purple;">**`CPhysicalItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem) | item Physical item to check. |

Check physical item in cheat list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/modifiers -->

# Modifiers

Table to work with list of modifiers.

## <sub>Count</sub>

`Modifiers.Count():` <mark style="color:purple;">**`integer`**</mark>

Returns size of modifiers list.

## <sub>Get</sub>

`Modifiers.Get(index):` [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                       |
| --------- | ------------------------------------------------ | --------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of temp tree in cheat list. |

Returns modifiers by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Modifiers.GetAll():` [<mark style="color:purple;">**`CModifier[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier)

Returns all modifiers in cheat list.

## <sub>Contains</sub>

`Modifiers.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                                   | Description         |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **tree** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | Temp tree to check. |

Checks if modifiers is in list.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/linearprojectiles -->

# LinearProjectiles

Table to work linear projectiles.

## <sub>GetAll</sub>

`LinearProjectiles.GetAll():` <mark style="color:purple;">**`{handle: integer, max_speed: number, max_dist: number, start_position: Vector, position: Vector, velocity: Vector, original_velocity: Vector, acceleration: Vector, fow_radius: number, source: CEntity}[]`**</mark>

Returns the 1-based indexed table with all existing projectiles. See example.

#### Example

```lua
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


--------------------------------------------------------------------------------

## Game Components - Core Objects

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core -->

# Core

- [Player](/api-v2.0/game-components/core/player.md)
- [Modifier](/api-v2.0/game-components/core/modifier.md)
- [Entity](/api-v2.0/game-components/core/entity.md)
- [NPC](/api-v2.0/game-components/core/npc.md)
- [Hero](/api-v2.0/game-components/core/hero.md)
- [Ability](/api-v2.0/game-components/core/ability.md)
- [Item](/api-v2.0/game-components/core/item.md)
- [Rune](/api-v2.0/game-components/core/rune.md)
- [Tower](/api-v2.0/game-components/core/tower.md)
- [Tree](/api-v2.0/game-components/core/tree.md)
- [Vambrace](/api-v2.0/game-components/core/vambrace.md)
- [Camp](/api-v2.0/game-components/core/camp.md)
- [Bottle](/api-v2.0/game-components/core/bottle.md)
- [Courier](/api-v2.0/game-components/core/courier.md)
- [DrunkenBrawler](/api-v2.0/game-components/core/drunkenbrawler.md)
- [PhysicalItem](/api-v2.0/game-components/core/physicalitem.md)
- [PowerTreads](/api-v2.0/game-components/core/powertreads.md)
- [TierToken](/api-v2.0/game-components/core/tiertoken.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/player -->

# Player

Table to work with `CPlayer`. <mark style="color:purple;">**`CPlayer`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>PrepareUnitOrders</sub>

`Player.PrepareUnitOrders(player, type, target, pos, ability, issuer, issuer_npc, [queue], [show_effects], [callback], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                                                                                                                                           | Description                                                                                       |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **player**                                                           | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player)                                                                                                             | The player issuing the order.                                                                     |
| **type**                                                             | [<mark style="color:purple;">**`Enum.UnitOrder`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unitorder)                                                                                  | The type of order to be issued.                                                                   |
| **target**                                                           | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| <mark style="color:purple;">**`nil`**</mark>                                                             | The target entity, if applicable.                                                                 |
| **pos**                                                              | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                                                                                           | The positional coordinates for the order.                                                         |
| **ability**                                                          | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) \| <mark style="color:purple;">**`nil`**</mark>                                                           | The ability for order.                                                                            |
| **issuer**                                                           | [<mark style="color:purple;">**`Enum.PlayerOrderIssuer`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.playerorderissuer)                                                                  | The issuer capture mode.                                                                          |
| **issuer\_npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) \| [<mark style="color:purple;">**`CNPC[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The specific NPC or group of NPC that will issue the order.                                       |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                                               | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **show\_effects&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                                               | If true, visual effects will indicate the position of the order. `(default: false)`               |
| **callback&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                                               | If true, the order will be pushed to the `OnPrepareUnitOrders` callback. `(default: false)`       |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                                               | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                                               | If true, the order will be forced by the minimap if possible. `(default: true)`                   |

Provides ability to execute such game actions as moving, attacking, or casting spells etc.

## <sub>HoldPosition</sub>

`Player.HoldPosition(player, issuer_npc, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                               | Description                                                                                       |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **player**                                                          | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The player issuing the order.                                                                     |
| **issuer\_npc**                                                     | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)       | The specific NPC that will issue the order.                                                       |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`         |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                    | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |

Sends the hold position action.

## <sub>AttackTarget</sub>

`Player.AttackTarget(player, issuer_npc, target, [queue], [push], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                               | Description                                                                                       |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **player**                                                           | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The player issuing the order.                                                                     |
| **issuer\_npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)       | The specific NPC that will issue the order.                                                       |
| **target**                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)       | The target NPC.                                                                                   |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`         |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                    | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                   | If true, the order will be forced by the minimap if possible. `(default: true)`                   |

Sends the attack target position.

## <sub>GetPlayerID</sub>

`Player.GetPlayerID(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player ID within the current game session.\
If the player ID is not valid, it will return -1.

## <sub>GetPlayerSlot</sub>

`Player.GetPlayerSlot(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player slot number within the current game session.

## <sub>GetPlayerTeamSlot</sub>

`Player.GetPlayerTeamSlot(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the team slot number assigned to the player within their respective team.

## <sub>GetName</sub>

`Player.GetName(player):` <mark style="color:purple;">**`string`**</mark>, <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player nickname and his proname

## <sub>GetProName</sub>

`Player.GetProName(steamId):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                             | Description |
| ----------- | ------------------------------------------------ | ----------- |
| **steamId** | <mark style="color:purple;">**`integer`**</mark> |             |

Returns cached player's proname. Works only in game callbacks

## <sub>GetPlayerData</sub>

`Player.GetPlayerData(player):` <mark style="color:purple;">**`{valid:boolean, fullyJoined:boolean, fakeClient:boolean, connectionState:integer, steamid:integer, PlusSubscriber:boolean, MVPLastGame:boolean, PlayerName:string, ProName:string}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player data table.

## <sub>GetTeamData</sub>

`Player.GetTeamData(player):` <mark style="color:purple;">**`{selected_hero_id:integer, kills:integer, assists:integer, deaths:integer, streak:integer, respawnTime:integer, selected_hero_variant:integer, lane_selection_flags:integer, last_buyback_time:number}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player team data table.\
Team data is only available for players on the local team.

## <sub>GetNeutralStashItems</sub>

`Player.GetNeutralStashItems(player):` <mark style="color:purple;">**`{item: CItem }[]`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns table with `CItem`s available in the neutral stash.

## <sub>GetTeamPlayer</sub>

`Player.GetTeamPlayer(player):` <mark style="color:purple;">**`{reliable_gold:integer, unreliable_gold:integer, starting_position:integer, totalearned_gold:integer, totalearned_xp:integer, shared_gold:integer, hero_kill_gold:integer, creep_kill_gold:integer, neutral_kill_gold:integer, courier_gold:integer, bounty_gold:integer, roshan_gold:integer, building_gold:integer, other_gold:integer, comeback_gold:integer, experimental_gold:integer, experimental2_gold:integer, creepdeny_gold:integer, tp_scrolls_purchased:integer, custom_stats:number, income_gold:integer, ward_kill_gold:integer, ability_gold:integer, networth:integer, deny_count:integer, lasthit_count:integer, lasthit_streak:integer, lasthit_multikill:integer, nearby_creep_death_count:integer, claimed_deny_count:integer, claimed_miss_count:integer, miss_count:integer, possible_hero_selection:integer, meta_level:integer, meta_experience:integer, meta_experience_awarded:integer, buyback_cooldown_time:number, buyback_gold_limit_time:number, buyback_cost_time:number, custom_buyback_cooldown:number, stuns:number, healing:number, tower_Kills:integer, roshan_kills:integer, camera_target:CEntity, override_selection_entity:CEntity, observer_wards_placed:integer, sentry_wards_placed:integer, creeps_stacked:integer, camps_stacked:integer, rune_pickups:integer, gold_spent_on_support:integer, hero_damage:integer, wards_purchased:integer, wards_destroyed:integer, commands_issued:integer, gold_spent_on_consumables:integer, gold_spent_on_items:integer, gold_spent_on_buybacks:integer, gold_lost_to_death:integer, is_new_player:boolean, is_guide_player:boolean, acquired_madstone:integer, current_madstone:integer}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns **Team Player Data** table

## <sub>GetPlayerNeutralInfo</sub>

`Player.GetPlayerNeutralInfo(player):` <mark style="color:purple;">**`nil`**</mark> | <mark style="color:purple;">**`{acquired_madstone:integer, current_madstone:integer, trinket_choices:integer[], enhancement_choices:integer[], selected_trinkets:integer[], selected_enhancements:integer[], times_crafted:integer[]}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns info about player's neutral items

## <sub>IsMuted</sub>

`Player.IsMuted(player):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns the player mute status.

## <sub>GetSelectedUnits</sub>

`Player.GetSelectedUnits(player):` [<mark style="color:purple;">**`CNPC[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns table of selected units by player.

## <sub>AddSelectedUnit</sub>

`Player.AddSelectedUnit(player, NPC):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |
| **NPC**    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)       | To select.         |

Adds unit to player selection.

## <sub>ClearSelectedUnits</sub>

`Player.ClearSelectedUnits(player):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Clears player selection.

## <sub>GetQuickBuyInfo</sub>

`Player.GetQuickBuyInfo(player):` <mark style="color:purple;">**`{m_quickBuyItems:integer[], m_quickBuyIsPurchasable:boolean[]}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns table with m\_quickBuyItems(item ids) and m\_quickBuyIsPurchasable(table of booleans).

## <sub>GetCourierControllerInfo</sub>

`Player.GetCourierControllerInfo(player):` <mark style="color:purple;">**`{state:integer, shop:integer}`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns table with m\_CourierController structure

## <sub>GetTotalGold</sub>

`Player.GetTotalGold(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns total gold of player.

## <sub>GetAssignedHero</sub>

`Player.GetAssignedHero(player):` [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns player's assigned hero.

## <sub>GetActiveAbility</sub>

`Player.GetActiveAbility(player):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/player) | The target player. |

Returns player's active ability.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/modifier -->

# Modifier

Table to work with `CModifier`. You can get modifiers from `NPC.GetModifier`function.

## <sub>GetName</sub>

`Modifier.GetName(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                                                   | Description             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get name of |

Returns the name of the modifier.

## <sub>GetClass</sub>

`Modifier.GetClass(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                                                   | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) |             |

Returns the name of the modifier's class.

## <sub>GetModifierAura</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetModifierAura(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                                                   | Description             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get aura of |

Should return the name of the modifier's aura, but instead, it returns an empty string in all\
the cases I have tested.

## <sub>GetSerialNumber</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetSerialNumber(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get serial number of |

Should return the serial number of the modifier, but instead, it returns 0 in all the cases I\
have tested.

## <sub>GetStringIndex</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetStringIndex(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get string index of |

Should return the string index of the modifier, but instead, it returns 0 in all the cases I\
have tested.

## <sub>GetIndex</sub>

`Modifier.GetIndex(modifier):` <mark style="color:purple;">**`GetIndex`**</mark>

| Name         | Type                                                                                                                   | Description              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get index of |

Returns the hero's modifier index. The index is an incrementable value with each new modifier\
the NPC gets

## <sub>GetCreationTime</sub>

`Modifier.GetCreationTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get creation time of |

Returns the game time when the modifier was created.

## <sub>GetCreationFrame</sub>

`Modifier.GetCreationFrame(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get creation frame of |

Returns the frame when the modifier was created. You could get current frame count from\
`GlobalVars.GetFrameCount` function.

## <sub>GetLastAppliedTime</sub>

`Modifier.GetLastAppliedTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get last applied time of |

Returns the game time when the modifier was last applied. Don't know cases when it can be\
different from `GetCreationTime`.

## <sub>GetDuration</sub>

`Modifier.GetDuration(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                 |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get duration of |

Returns the duration of the modifier.

## <sub>GetDieTime</sub>

`Modifier.GetDieTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get expiration time of |

Returns the game time when the modifier will expire.

## <sub>GetStackCount</sub>

`Modifier.GetStackCount(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get stack count of |

If there are stacks of the modifier, it returns the amount of stacks; otherwise, it returns\
0\.

## <sub>GetAuraSearchTeam</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAuraSearchTeam(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get aura search team of |

Returns aura search team of the modifier.

## <sub>GetAuraSearchType</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAuraSearchType(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get aura search type of |

Returns aura search type of the modifier.

## <sub>GetAuraSearchFlags</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAuraSearchFlags(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get aura search flags of |

Returns aura search flags of the modifier.

## <sub>GetAuraRadius</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAuraRadius(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get aura radius of |

Returns aura radius of the modifier.

## <sub>GetTeam</sub>

`Modifier.GetTeam(modifier):` [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

| Name         | Type                                                                                                                   | Description             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get team of |

Returns team of the modifier.

## <sub>GetAttributes</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAttributes(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                                                   | Description                   |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get attributes of |

Returns the attributes of the modifier.

## <sub>IsAura</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.IsAura(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if the modifier is an aura.

## <sub>IsAuraActiveOnDeath</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.IsAuraActiveOnDeath(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if the modifier aura active on death.

## <sub>GetMarkedForDeletion</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetMarkedForDeletion(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if the modifier is marked for deletion.

## <sub>GetAuraIsHeal</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetAuraIsHeal(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if aura is heal.

## <sub>GetProvidedByAura</sub>

`Modifier.GetProvidedByAura(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if modifier is provided by an aura.

## <sub>GetPreviousTick</sub>

`Modifier.GetPreviousTick(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get last tick time of |

Returns the game time of the last modifier tick (\~0.033 seconds).

## <sub>GetThinkInterval</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

`Modifier.GetThinkInterval(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get think interval of |

Returns the modifier's think interval.

## <sub>GetThinkTimeAccumulator</sub>

{% hint style="info" %}
Deprecated.
{% endhint %}

\`Modifier.GetThinkTimeAccumulator(modifier):\` <mark style="color:purple;">\*\*\`number\`\*\*</mark>

| Name         | Type                                                                                                                   | Description                               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get think time accumulator of |

Return the modifier's think interval time accumulator.

## <sub>IsCurrentlyInAuraRange</sub>

`Modifier.IsCurrentlyInAuraRange(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if is in aura range.

## <sub>GetAbility</sub>

`Modifier.GetAbility(modifier):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

| Name         | Type                                                                                                                   | Description                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get ability of |

Returns the modifier's ability.

## <sub>GetAuraOwner</sub>

`Modifier.GetAuraOwner(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier    |

Returns the owner of aura

## <sub>GetParent</sub>

`Modifier.GetParent(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier    |

Returns the parent of modifier

## <sub>GetCaster</sub>

`Modifier.GetCaster(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                   | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier    |

Returns caster of modifier

## <sub>GetState</sub>

`Modifier.GetState(modifier):` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                   | Description              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get state of |

Returns the modifier state masks. See the example.

#### Example

```lua
local m_nEnabledStateMask, m_nDisabledStateMask = Modifier.GetState(mod)
local mod_is_hex = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_HEXED & 1) > 0
local mod_is_stun = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_STUNNED & 1) > 0
```

## <sub>IsDebuff</sub>

`Modifier.IsDebuff(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                                   | Description       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to check |

Returns `true` if the modifier is a debuff.

## <sub>GetField</sub>

`Modifier.GetField(modifier, fieldName, [dbgPrint]):` <mark style="color:purple;">**`any`**</mark>

| Name                                                           | Type                                                                                                                   | Description                              |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **modifier**                                                   | [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | modifier to get field from               |
| **fieldName**                                                  | <mark style="color:purple;">**`string`**</mark>                                                                        | field name                               |
| **dbgPrint&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                       | print possible errors `(default: false)` |

Returns value of the field.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/entity -->

# Entity

Table to work with `CEntity`.

<mark style="color:purple;">**`CEntity`**</mark> is base class for all entities in the game e.g. <mark style="color:purple;">**`CNPC`**</mark>, <mark style="color:purple;">**`Hero`**</mark>, <mark style="color:purple;">**`CPlayer`**</mark>, <mark style="color:purple;">**`CAbility`**</mark>

## <sub>IsEntity</sub>

`Entity.IsEntity(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is in entity list. Search in unordered set.

## <sub>IsNPC</sub>

`Entity.IsNPC(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is in NPC list. Search in unordered set.

## <sub>IsHero</sub>

`Entity.IsHero(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is in hero list. Search in unordered set.

## <sub>IsPlayer</sub>

`Entity.IsPlayer(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is in player list. Search in unordered set.

## <sub>IsAbility</sub>

`Entity.IsAbility(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is in ability list. Search in unordered set. Item is ability.

## <sub>Get</sub>

{% hint style="info" %}
Not the same as Entities.Get(index). See example.
{% endhint %}

`Entity.Get(index):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description |
| --------- | ------------------------------------------------ | ----------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> |             |

Returns entity by game index.

#### Example

```lua
-- get_by_index.lua
local hero = Heroes.GetLocal();
local index = Entity.GetIndex(hero);
local entity_by_index = Entity.Get(index);
assert(hero == entity_by_index, "Entity.Get() is broken!"); -- true
```

## <sub>GetIndex</sub>

`Entity.GetIndex(entity):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns game index of entity.

## <sub>GetClassName</sub>

`Entity.GetClassName(entity):` <mark style="color:purple;">**`string`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's class name.

## <sub>GetUnitName</sub>

`Entity.GetUnitName(entity):` <mark style="color:purple;">**`string`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's name.

## <sub>GetUnitDesignerName</sub>

`Entity.GetUnitDesignerName(entity):` <mark style="color:purple;">**`string`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's designerName field.

## <sub>GetTeamNum</sub>

`Entity.GetTeamNum(entity):` [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's team number.

## <sub>IsSameTeam</sub>

`Entity.IsSameTeam(entity1, entity2):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                               | Description |
| ----------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity1** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |
| **entity2** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entities are in the same team.

## <sub>GetAbsOrigin</sub>

`Entity.GetAbsOrigin(entity):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's position.

## <sub>GetNetOrigin</sub>

`Entity.GetNetOrigin(entity):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's net position.

## <sub>GetRotation</sub>

`Entity.GetRotation(entity):` [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's rotation.

#### Example

```lua
-- forward_pos.lua
return {
    -- get local hero's forward position and draw a circle around it
    OnUpdate = function ()
        local hero = Heroes.GetLocal();
        local rotation = Entity.GetRotation(hero);
        -- forward_direction is a vector that points 100 units in direction of my hero's rotation
        local forward_direction = rotation:GetForward():Normalized():Scaled(100);
        -- add forward_direction to my hero's position to get the forward position
        local forward_pos = Entity.GetAbsOrigin(hero) + forward_direction;
        -- screen_x and screen_y are the coordinates of forward_pos on the screen
        local screen_x, screen_y, is_on_screen = Renderer.WorldToScreen(forward_pos);
        if is_on_screen then
            -- draw a circle around the position
            Renderer.SetDrawColor(255, 255, 255, 255);
            Renderer.DrawFilledCircle(screen_x, screen_y, 10, 10);
            -- result: https://i.imgur.com/ERf1Pxk.png
        end
    end
}
```

## <sub>IsAlive</sub>

`Entity.IsAlive(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is alive.

## <sub>IsDormant</sub>

`Entity.IsDormant(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns `true` if the entity is not visible to the local player.

## <sub>GetHealth</sub>

`Entity.GetHealth(entity):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's health.

## <sub>GetMaxHealth</sub>

`Entity.GetMaxHealth(entity):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's max health.

## <sub>GetOwner</sub>

`Entity.GetOwner(entity):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's owner or `nil` if the entity has no owner.\ e.g. for <mark style="color:purple;">**`CPlayer`**</mark> -> `npc_dota_hero_ember_spirit` -> `npc_dota_hero_ember_spirit_fire_remnant`\
ownership chain `Entity.GetOwner(remnant)` will return Ember Spirit's entity.

## <sub>OwnedBy</sub>

`Entity.OwnedBy(entity, owner):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | - entity to check      |
| **owner**  | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | - owner for comparison |

Returns `true` if the entity is owned by another entity-owner. It will check the first owner only.

## <sub>RecursiveGetOwner</sub>

`Entity.RecursiveGetOwner(entity):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns the entity's last owner.\ e.g. for <mark style="color:purple;">**`CPlayer`**</mark> -> `npc_dota_hero_ember_spirit` -> `npc_dota_hero_ember_spirit_fire_remnant`\
ownership chain `Entity.GetOwner(remnant)` will return <mark style="color:purple;">**`CPlayer`**</mark>.

## <sub>RecursiveOwnedBy</sub>

`Entity.RecursiveOwnedBy(entity, owner):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description          |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to check      |
| **owner**  | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | owner for comparison |

Returns `true` if the entity is owned by another entity-owner. It will check the whole ownership chain.

## <sub>GetHeroesInRadius</sub>

`Entity.GetHeroesInRadius(entity, radius, [teamType], [omitIllusions], [omitDormant]):` [<mark style="color:purple;">**`CHero[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)

| Name                                                                | Type                                                                                                                                        | Description                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **entity**                                                          | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                          | entity to get position                                                  |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                             | radius to search around                                                 |
| **teamType&#x20;**<mark style="color:orange;">**`[?]`**</mark>      | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | relative to the entity `(default: TEAM_ENEMY)`                          |
| **omitIllusions&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without illusions `(default: false)`    |
| **omitDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without dormant units `(default: true)` |

Returns an array of all alive and visible heroes in radius of the entity. Exclude illusion.

#### Example

```lua
local hero = Heroes.GetLocal()
-- get all enemy heroes in 1200 radius
local heroes_around = Entity.GetHeroesInRadius(hero, 1200)
for i = 1, #heroes_around do
	local hero = heroes_around[i];
	Log.Write(NPC.GetUnitName(hero) .. " is near!");
end
```

## <sub>GetUnitsInRadius</sub>

`Entity.GetUnitsInRadius(entity, radius, [teamType], [omitIllusions], [omitDormant]):` [<mark style="color:purple;">**`CNPC[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)

| Name                                                                | Type                                                                                                                                        | Description                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **entity**                                                          | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                          | entity to get position                                                  |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                             | radius to search around                                                 |
| **teamType&#x20;**<mark style="color:orange;">**`[?]`**</mark>      | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | relative to the entity `(default: TEAM_ENEMY)`                          |
| **omitIllusions&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without illusions `(default: false)`    |
| **omitDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | `true` if you want to get table without dormant units `(default: true)` |

Returns an array of all alive and visible NPCs in radius of the entity.

#### Example

```lua
local hero = Heroes.GetLocal()
-- get all ally NPCs in 1200 radius
local units_around = Entity.GetUnitsInRadius(hero, 1200, Enum.TeamType.TEAM_FRIEND)
for i = 1, #units_around do
	local unit = units_around[i];
	Log.Write(NPC.GetUnitName(unit) .. " is near!");
end
```

## <sub>GetTreesInRadius</sub>

{% hint style="info" %}
Active means that tree is not destroyed.
{% endhint %}

`Entity.GetTreesInRadius(entity, radius, [active]):` [<mark style="color:purple;">**`CTree[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree)

| Name                                                         | Type                                                                                                               | Description                                                                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **entity**                                                   | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to get position                                                                                 |
| **radius**                                                   | <mark style="color:purple;">**`number`**</mark>                                                                    | radius to search around                                                                                |
| **active&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                   | `true` if you want to get table with active trees only, otherwise for inactive trees `(default: true)` |

Returns an array of all not temporary trees in radius of the entity.

#### Example

```lua
local hero = Heroes.GetLocal()
-- get all trees in 400 radius
local trees_around = Entity.GetTreesInRadius(hero, 400, true)
for i = 1, #trees_around do
	local tree = trees_around[i];
	Log.Write(Entity.GetClassName(tree) .. " is near!");
end
```

## <sub>GetTempTreesInRadius</sub>

{% hint style="info" %}
Temporary trees are trees planted by abilities or items.
{% endhint %}

\`Entity.GetTempTreesInRadius(entity, radius):\` \[<mark style="color:purple;">\*\*\`CTree\[]\`\*\*</mark>]\(Tree.md)

| Name       | Type                                                                                                               | Description             |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to get position  |
| **radius** | <mark style="color:purple;">**`number`**</mark>                                                                    | radius to search around |

Returns an array of all temporary trees in radius of the entity.

#### Example

```lua
local hero = Heroes.GetLocal()
-- get all trees in 400 radius
local trees_around = Entity.GetTempTreesInRadius(hero, 400)
for i = 1, #trees_around do
	local tree = trees_around[i];
	Log.Write(Entity.GetClassName(tree) .. " is near!");
end
```

## <sub>IsControllableByPlayer</sub>

`Entity.IsControllableByPlayer(entity, playerId):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                               | Description     |
| ------------ | ------------------------------------------------------------------------------------------------------------------ | --------------- |
| **entity**   | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to check |
| **playerId** | <mark style="color:purple;">**`integer`**</mark>                                                                   | player id       |

Returns `true` if entity is controllable by player.

## <sub>GetRoshanHealth</sub>

`Entity.GetRoshanHealth():` <mark style="color:purple;">**`integer`**</mark>

Returns Roshan's health. Onyly works in unsafe mode.

## <sub>GetForwardPosition</sub>

`Entity.GetForwardPosition(entity, distance):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name         | Type                                                                                                               | Description              |
| ------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| **entity**   | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to get position   |
| **distance** | <mark style="color:purple;">**`number`**</mark>                                                                    | distance to move forward |

Returns position in front of entity or (0,0,0) if entity is invalid.

## <sub>GetClassID</sub>

`Entity.GetClassID(entity):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                               | Description            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to get class id |

Returns entity class id. Could be as a optimized way to check entity type.

## <sub>GetField</sub>

`Entity.GetField(entity, fieldName, [dbgPrint]):` <mark style="color:purple;">**`any`**</mark>

| Name                                                           | Type                                                                                                               | Description                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **entity**                                                     | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | entity to get field from                 |
| **fieldName**                                                  | <mark style="color:purple;">**`string`**</mark>                                                                    | field name                               |
| **dbgPrint&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                   | print possible errors `(default: false)` |

Returns value of the field.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/npc -->

# NPC

Table to work with `CNPC`. <mark style="color:purple;">**`CNPC`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetOwnerNPC</sub>

`NPC.GetOwnerNPC(npc):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                                         | Description           |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to get owner from |

Returns owner of the `CNPC`. Works for spirit bear.

## <sub>GetItem</sub>

`NPC.GetItem(npc, name, [isReal]):` [<mark style="color:purple;">**`CItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/item) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                         | Description                                                                                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to get item from                                                                                                           |
| **name**                                                     | <mark style="color:purple;">**`string`**</mark>                                                              | name of the item                                                                                                               |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `CItem` by name.

## <sub>HasItem</sub>

`NPC.HasItem(npc, name, [isReal]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                         | Type                                                                                                         | Description                                                                                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check                                                                                                                   |
| **name**                                                     | <mark style="color:purple;">**`string`**</mark>                                                              | name of the item                                                                                                               |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `true` if the `CNPC` has item with specified name.

## <sub>HasModifier</sub>

`NPC.HasModifier(npc, name):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                         | Description          |
| -------- | ------------------------------------------------------------------------------------------------------------ | -------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check         |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | name of the modifier |

Returns `true` if the `CNPC` has modifier with specified name.

## <sub>GetModifier</sub>

`NPC.GetModifier(npc, name):` [<mark style="color:purple;">**`CModifier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/modifier) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                         | Description              |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------------------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to get modifier from |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | name of the modifier     |

Returns `CModifier` by name.

## <sub>GetModifiers</sub>

\`poperty\_filter\` doesn\`t filter all modifiers every call, it uses already prefiltered list. {% endhint %} \`

NPC.GetModifiers(npc, \[poperty\_filter]): `[<mark style="color:purple">**`CModifier\[]\`\*\*]\(Modifier.md)

| Name                                                                  | Type                                                                                                                                                        | Description                                                                                         |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **npc**                                                               | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                                | npc to get modifiers from                                                                           |
| **poperty\_filter&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction) | Filter modifiers by specified property `(default: Enum.ModifierFunction.MODIFIER_FUNCTION_INVALID)` |

Returns an array of all NPC's `CModifier`s.

## <sub>HasInventorySlotFree</sub>

`NPC.HasInventorySlotFree(npc, [isReal]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                         | Type                                                                                                         | Description                                                                                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check                                                                                                                   |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `true` if the `CNPC` has free inventory slot.

## <sub>HasState</sub>

`NPC.HasState(npc, state):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                                                  | Description    |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                          | npc to check   |
| **state** | [<mark style="color:purple;">**`Enum.ModifierState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierstate) | state to check |

Returns `true` if the `CNPC` has state. The best way to check if the `CNPC` is stunned, silenced, hexed, has BKB immune etc.

## <sub>GetStatesDuration</sub>

`NPC.GetStatesDuration(npc, states, [only_active_states]):` <mark style="color:purple;">**`table`**</mark>

| Name                                                                       | Type                                                                                                         | Description                                                                                                                         |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **npc**                                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check                                                                                                                        |
| **states**                                                                 | <mark style="color:purple;">**`integer[]`**</mark>                                                           | states to check                                                                                                                     |
| **only\_active\_states&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | if `true` then check only states that active on unit, otherwise check all states. e.g. rooted while debuff immune `(default: true)` |

Returns table of remaining modifier states duration. See the example

#### Example

```lua
local states_to_check = {
		[Enum.ModifierState.MODIFIER_STATE_STUNNED] = true,
		[Enum.ModifierState.MODIFIER_STATE_HEXED] = true,
}
local states = NPC.GetStatesDuration(unit, states_to_check)
local hex_duration = states[Enum.ModifierState.MODIFIER_STATE_HEXED]
local stun_duration = states[Enum.ModifierState.MODIFIER_STATE_STUNNED]
```

## <sub>IsWaitingToSpawn</sub>

`NPC.IsWaitingToSpawn(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if waiting to spawn. For example, creeps are waiting to spawn under the ground near the barracks.

## <sub>IsIllusion</sub>

`NPC.IsIllusion(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is illusion.

## <sub>IsVisible</sub>

`NPC.IsVisible(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is visible to local player.

## <sub>IsVisibleToEnemies</sub>

`NPC.IsVisibleToEnemies(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is visible enemies.

## <sub>IsCourier</sub>

`NPC.IsCourier(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a courier.

## <sub>IsRanged</sub>

`NPC.IsRanged(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a ranged unit.

## <sub>IsCreep</sub>

`NPC.IsCreep(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a creep.

## <sub>IsLaneCreep</sub>

`NPC.IsLaneCreep(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a lane creep.

## <sub>IsStructure</sub>

`NPC.IsStructure(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a structure.

## <sub>IsTower</sub>

`NPC.IsTower(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a tower.

## <sub>GetUnitType</sub>

`NPC.GetUnitType(npc):` [<mark style="color:purple;">**`Enum.UnitTypeFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.unittypeflags)

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns unit type flags.

## <sub>IsConsideredHero</sub>

`NPC.IsConsideredHero(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if it is unit a considered a hero for targeting purposes.

## <sub>IsBarracks</sub>

`NPC.IsBarracks(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a barracks.

## <sub>IsAncient</sub>

`NPC.IsAncient(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is an ancient creeps.

## <sub>IsRoshan</sub>

`NPC.IsRoshan(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a Roshan.

## <sub>IsNeutral</sub>

`NPC.IsNeutral(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a neutral. Neutral creeps, ancient creeps.

## <sub>IsHero</sub>

`NPC.IsHero(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a hero.

## <sub>IsWard</sub>

`NPC.IsWard(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a ward.

## <sub>IsMeepoClone</sub>

`NPC.IsMeepoClone(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is a meepo clone.

## <sub>IsEntityInRange</sub>

`NPC.IsEntityInRange(npc, npc2, range):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                         | Description    |
| --------- | ------------------------------------------------------------------------------------------------------------ | -------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check   |
| **npc2**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check   |
| **range** | <mark style="color:purple;">**`number`**</mark>                                                              | range to check |

Returns `true` if the `CNPC` in range of other `CNPC`.

## <sub>IsPositionInRange</sub>

`NPC.IsPositionInRange(npc, pos, range, [hull]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                       | Type                                                                                                                                 | Description                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| **npc**                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | npc to check                              |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | position to check                         |
| **range**                                                  | <mark style="color:purple;">**`number`**</mark>                                                                                      | range to check                            |
| **hull&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                      | hull just added to range `(default: 0.0)` |

Returns `true` if the `CNPC` in range of position.

## <sub>IsLinkensProtected</sub>

`NPC.IsLinkensProtected(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is protected by Linkens Sphere.

## <sub>IsMirrorProtected</sub>

`NPC.IsMirrorProtected(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is protected by Mirror Shield.

## <sub>IsChannellingAbility</sub>

{% hint style="info" %}
Do not work for items.
{% endhint %}

`NPC.IsChannellingAbility(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description  |
| ------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |

Returns `true` if the `CNPC` is channeling ability. Black Hole, Life Drain, etc.

## <sub>GetChannellingAbility</sub>

`NPC.GetChannellingAbility(npc):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the currently channelling `CAbility`.

## <sub>IsRunning</sub>

`NPC.IsRunning(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` is running.

## <sub>IsAttacking</sub>

`NPC.IsAttacking(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` is attacking.

## <sub>IsSilenced</sub>

`NPC.IsSilenced(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` is silenced.

## <sub>IsStunned</sub>

`NPC.IsStunned(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` is stunned.

## <sub>HasAegis</sub>

`NPC.HasAegis(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` has aegis.

## <sub>IsKillable</sub>

`NPC.IsKillable(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns `true` if the `CNPC` has killable. Example: false if affected by Eul.

## <sub>GetActivity</sub>

`NPC.GetActivity(npc):` [<mark style="color:purple;">**`Enum.GameActivity`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity)

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the `CNPC` activity, such as running, attacking, casting, etc.

## <sub>GetAnimationInfo</sub>

`NPC.GetAnimationInfo(npc):` <mark style="color:purple;">**`{sequence:integer, cycle:number, name:string, mdl_name:string}`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns information about the current animation of the `CNPC`.

## <sub>GetAttackRange</sub>

`NPC.GetAttackRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the base attack range of the `CNPC`.

## <sub>GetAttackRangeBonus</sub>

`NPC.GetAttackRangeBonus(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the bonus attack range of the `CNPC`.

## <sub>GetCastRangeBonus</sub>

`NPC.GetCastRangeBonus(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the bonus cast range of the `CNPC`.

## <sub>GetPhysicalArmorValue</sub>

`NPC.GetPhysicalArmorValue(npc, [excludeWhiteArmor]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                    | Type                                                                                                         | Description                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **npc**                                                                 | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                            |
| **excludeWhiteArmor&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | exclude white armor `(default: true)` |

Returns the physical armor value of the `CNPC`.

## <sub>GetPhysicalDamageReduction</sub>

`NPC.GetPhysicalDamageReduction(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the physical damage reduction value of the `CNPC`.

## <sub>GetArmorDamageMultiplier</sub>

`NPC.GetArmorDamageMultiplier(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the physical damage multiplier value of the `CNPC`.

## <sub>GetMagicalArmorValue</sub>

`NPC.GetMagicalArmorValue(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the magical armor value of the `CNPC`.

## <sub>GetMagicalArmorDamageMultiplier</sub>

`NPC.GetMagicalArmorDamageMultiplier(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the magical damage multiplier value of the `CNPC`.

## <sub>GetIncreasedAttackSpeed</sub>

`NPC.GetIncreasedAttackSpeed(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                                         | Description                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | ignore temporary attack speed `(default: false)` |

Returns increased attack speed of the `CNPC`.

## <sub>GetAttacksPerSecond</sub>

`NPC.GetAttacksPerSecond(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                                         | Description                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | ignore temporary attack speed `(default: false)` |

Returns the number of attacks per second that the `CNPC` can deal.

## <sub>GetAttackTime</sub>

`NPC.GetAttackTime(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the amount of time needed for the `CNPC` to perform an attack.

## <sub>GetAttackSpeed</sub>

`NPC.GetAttackSpeed(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                                         | Description                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | ignore temporary attack speed `(default: false)` |

Returns the attack speed of the `CNPC`.

## <sub>GetBaseAttackSpeed</sub>

`NPC.GetBaseAttackSpeed(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the base attack speed of the `CNPC`.

## <sub>GetHullRadius</sub>

`NPC.GetHullRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the model interaction radius of the `CNPC`.

## <sub>GetPaddedCollisionRadius</sub>

`NPC.GetPaddedCollisionRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the collision hull radius (including padding) of this `NPC`.

## <sub>GetCollisionPadding</sub>

`NPC.GetCollisionPadding(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the collision including padding of this `NPC`.

## <sub>GetPaddedCollisionRadius</sub>

`NPC.GetPaddedCollisionRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the ring radius of this `NPC`.

## <sub>GetProjectileCollisionSize</sub>

{% hint style="info" %}
see: <https://dota2.fandom.com/wiki/Unit\\_Size#Collision\\_Size>
{% endhint %}

`NPC.GetProjectileCollisionSize(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the collision size of the `CNPC`. Collision size is the internal size that prevents other units from passing through.

## <sub>GetTurnRate</sub>

{% hint style="info" %}
see: <https://dota2.fandom.com/wiki/Turn\\_rate>
{% endhint %}

`NPC.GetTurnRate(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the turn rate, which is the speed at which the `CNPC` can turn.

## <sub>GetAttackAnimPoint</sub>

{% hint style="info" %}
see: <https://dota2.fandom.com/wiki/Attack\\_animation>
{% endhint %}

`NPC.GetAttackAnimPoint(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the attack animation point, `nil` if not found.

## <sub>GetAttackProjectileSpeed</sub>

{% hint style="info" %}
see: <https://dota2.fandom.com/wiki/Projectile\\_Speed>
{% endhint %}

`NPC.GetAttackProjectileSpeed(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the attack projectile speed, `nil` if not found.

## <sub>IsTurning</sub>

`NPC.IsTurning(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns true if the `CNPC` is turning.

## <sub>GetAngleDiff</sub>

{% hint style="info" %}
doesn't work for creeps
{% endhint %}

`NPC.GetAngleDiff(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the remaining degree angle needed to complete the turn of the `CNPC`.

## <sub>GetPhysicalArmorMainValue</sub>

`NPC.GetPhysicalArmorMainValue(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the (main) white armor of the `CNPC`.

## <sub>GetTimeToFace</sub>

`NPC.GetTimeToFace(npc, target):` <mark style="color:purple;">**`number`**</mark>

| Name       | Type                                                                                                         | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc**    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | source npc  |
| **target** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the amount of time needed for the source `CNPC` to face the target `CNPC`.

## <sub>FindRotationAngle</sub>

`NPC.FindRotationAngle(npc, pos):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                                                 | Description                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | source npc                          |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | position to find the rotation angle |

Returns the rotation angle of the `CNPC`.

## <sub>GetTimeToFacePosition</sub>

`NPC.GetTimeToFacePosition(npc, pos):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                                                 | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | source npc      |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | target position |

Returns the amount of time needed for the source `CNPC` to face a specific position.

## <sub>FindFacingNPC</sub>

`NPC.FindFacingNPC(npc, ignoreNpc, [team_type], [angle], [distance]):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                                                        | Description                            |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **npc**                                                          | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                | source npc                             |
| **ignoreNpc**                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                | ignore npc                             |
| **team\_type&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | team type `(default: TEAM_BOTH)`       |
| **angle&#x20;**<mark style="color:orange;">**`[?]`**</mark>      | <mark style="color:purple;">**`number`**</mark>                                                                                             | max angle to check `(default: 0.0)`    |
| **distance&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                                                             | max distance to check `(default: 0.0)` |

Returns the `CNPC` that the source `CNPC` is currently facing.

## <sub>GetBaseSpeed</sub>

`NPC.GetBaseSpeed(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the base move speed of the `CNPC`.

## <sub>GetMoveSpeed</sub>

`NPC.GetMoveSpeed(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the move speed of the `CNPC`.

## <sub>GetMinDamage</sub>

`NPC.GetMinDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the minumum attack damage of the `CNPC`.

## <sub>GetBonusDamage</sub>

`NPC.GetBonusDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the bonus attack damage of the `CNPC`.

## <sub>GetTrueDamage</sub>

`NPC.GetTrueDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the minumum attack damage + bonus damage of the `CNPC`.

## <sub>GetTrueMaximumDamage</sub>

`NPC.GetTrueMaximumDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the maximum attack damage + bonus damage of the `CNPC`.

## <sub>GetItemByIndex</sub>

`NPC.GetItemByIndex(npc, index):` [<mark style="color:purple;">**`CItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/item) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                                             | item index  |

Returns the `CItem` by index.

## <sub>GetAbilityByIndex</sub>

`NPC.GetAbilityByIndex(npc, index):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                         | Description   |
| --------- | ------------------------------------------------------------------------------------------------------------ | ------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc    |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                                             | ability index |

Returns the `CAbility` by index.

## <sub>GetAbilityByActivity</sub>

`NPC.GetAbilityByActivity(npc, activity):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                                                | Description             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                        | npc to get ability from |
| **activity** | [<mark style="color:purple;">**`Enum.GameActivity`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gameactivity) | game activity           |

Returns the `CAbility` by game activity.

## <sub>GetAbility</sub>

`NPC.GetAbility(npc, name):` [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                         | Description  |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc   |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | ability name |

Returns the `CAbility` by name.

## <sub>HasAbility</sub>

`NPC.HasAbility(npc, name):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                         | Description  |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc   |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | ability name |

Returns `true` if the `CNPC` has this ability.

## <sub>GetMana</sub>

`NPC.GetMana(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the current mana of the `CNPC`.

## <sub>GetMaxMana</sub>

`NPC.GetMaxMana(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the maximum mana of the `CNPC`.

## <sub>GetManaRegen</sub>

`NPC.GetManaRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the mana regeneration rate of the `CNPC`.

## <sub>GetHealthRegen</sub>

`NPC.GetHealthRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the health regeneration rate of the `CNPC`.

## <sub>CalculateHealthRegen</sub>

{% hint style="info" %}
Works for creeps but really slow.
{% endhint %}

`NPC.CalculateHealthRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Iterate over all modifiers and returns the health regeneration rate of the `CNPC`.

## <sub>GetCurrentLevel</sub>

`NPC.GetCurrentLevel(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the current level of the `CNPC`.

## <sub>GetDayTimeVisionRange</sub>

`NPC.GetDayTimeVisionRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the day-time vision range of the `CNPC`.

## <sub>GetNightTimeVisionRange</sub>

`NPC.GetNightTimeVisionRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the night-time vision range of the `CNPC`.

## <sub>GetUnitName</sub>

`NPC.GetUnitName(npc):` <mark style="color:purple;">**`string`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the unit-name of the `CNPC`.

## <sub>GetHealthBarOffset</sub>

`NPC.GetHealthBarOffset(npc, [checkOverride]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                                | Type                                                                                                         | Description                                            |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| **npc**                                                             | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                                             |
| **checkOverride&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                             | returns override offset if it exists `(default: true)` |

Returns the health bar offset of the `CNPC`.

## <sub>GetUnitNameIndex</sub>

{% hint style="info" %}
index can change when new unit are added
{% endhint %}

`NPC.GetUnitNameIndex(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns unit-name index of the `CNPC`.

## <sub>GetAttachment</sub>

`NPC.GetAttachment(npc, name):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name     | Type                                                                                                         | Description                            |
| -------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                             |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | attachment name. e.g. "attach\_hitloc" |

Returns the attachment position of the `CNPC` by the name.

#### Example

```lua
-- attachments.txt
attach_hitloc
attach_eye_r
attach_eye_l
attach_mouth
attach_totem
attach_head
attach_tidebringer
attach_tidebringer_2
attach_sword
attach_attack1
attach_weapon
attach_eyes
attach_prop_l
attach_prop_r
attach_light
attach_staff
attach_mouthbase
attach_mouthend
attach_mom_l
attach_mom_r
attach_attack2
attach_fuse
attach_mane
attach_tail
attach_upper_jaw
attach_weapon_core_fx
attach_bow_top
attach_bow_bottom
attach_bow_mid
attach_armor
attach_chimmney
attach_eyeR
attach_eyeL
attach_spine4
attach_spine5
attach_spine6
attach_spine7
attach_spine8
attach_spine9
attach_armlet_1
attach_armlet_2
attach_armlet_3
attach_armlet_4
attach_armlet_5
attach_vanguard_guard_1
attach_vanguard_guard_2
attach_weapon_offhand
attach_vanguard_1
attach_vanguard_2
attach_attack3
attach_attack4
attach_banner
attach_fx
attach_portcullis
attach_gem
```

## <sub>GetAttachmentByIndex</sub>

`NPC.GetAttachmentByIndex(npc, index):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name      | Type                                                                                                         | Description      |
| --------- | ------------------------------------------------------------------------------------------------------------ | ---------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc       |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                                             | attachment index |

Returns the attachment position of the `CNPC` by the specified index.

## <sub>GetAttachmentIndexByName</sub>

`NPC.GetAttachmentIndexByName(npc, name):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                         | Description                            |
| -------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc                             |
| **name** | <mark style="color:purple;">**`string`**</mark>                                                              | attachment name. e.g. "attach\_hitloc" |

Returns the attachment index of the `CNPC` by the name.

## <sub>GetBountyXP</sub>

`NPC.GetBountyXP(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the amount of experience points (XP) you can earn for killing the `CNPC`.

## <sub>GetGoldBountyMin</sub>

`NPC.GetGoldBountyMin(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the minimum amount gold you can earn for killing the `CNPC`.

## <sub>GetGoldBountyMax</sub>

`NPC.GetGoldBountyMax(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                                         | Description |
| ------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | target npc  |

Returns the maximum amount gold you can earn for killing the `CNPC`.

## <sub>MoveTo</sub>

`NPC.MoveTo(npc, position, [queue], [show], [callback], [executeFast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                                                 | Description                                                                             |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **npc**                                                              | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                         | The target NPC.                                                                         |
| **position**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The destination position.                                                               |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Add the order to the Dota queue. `(default: false)`                                     |
| **show&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Show the order position. `(default: false)`                                             |
| **callback&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Push the order to the OnPrepareUnitOrders callback. `(default: false)`                  |
| **executeFast&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Place the order at the top of the queue. `(default: false)`                             |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | If true, the order will be forced by the minimap if possible. `(default: true)`         |

Initiates an order for the `CNPC` to move to a specified position.

## <sub>SetZDelta</sub>

`NPC.SetZDelta(npc, z):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |
| **z**   | <mark style="color:purple;">**`number`**</mark>                                                              | Z pos           |

Sets the Z position of the `CNPC` model.

## <sub>HasScepter</sub>

`NPC.HasScepter(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |

Returns `true` if the `CNPC` has or consumed Aghanim Scepter.

## <sub>HasShard</sub>

`NPC.HasShard(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |

Returns `true` if the `CNPC` has or consumed Aghanim Shard.

## <sub>SequenceDuration</sub>

`NPC.SequenceDuration(npc, sequence):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                         | Description         |
| ------------ | ------------------------------------------------------------------------------------------------------------ | ------------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC.     |
| **sequence** | <mark style="color:purple;">**`integer`**</mark>                                                             | The sequence index. |

Returns sequence duration of the npc with the specified sequence index.

## <sub>GetSecondsPerAttack</sub>

`NPC.GetSecondsPerAttack(npc, bIgnoreTempAttackSpeed):` <mark style="color:purple;">**`number`**</mark>

| Name                       | Type                                                                                                         | Description                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **npc**                    | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC.                |
| **bIgnoreTempAttackSpeed** | <mark style="color:purple;">**`boolean`**</mark>                                                             | Ignore temporary attack speed. |

Returns the seconds per attack of the npc.

## <sub>GetBarriers</sub>

`NPC.GetBarriers(npc):` <mark style="color:purple;">**`{physical:{total:number, current:number}, magic:{total:number, current:number}, all:{total:number, current:number}}`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |

Returns a table with information about the barriers of the `CNPC`.

## <sub>GetGlow</sub>

`NPC.GetGlow(npc):` <mark style="color:purple;">**`{m_bSuppressGlow:boolean, m_bFlashing:boolean, m_bGlowing:boolean, m_iGlowType:integer, r:integer, g:integer, b:integer}`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |

Returns a table with information about the current glow effect of the `CNPC`.

## <sub>SetGlow</sub>

`NPC.SetGlow(npc, suppress_glow, flashing, glowing, glow_type, r, g, b):` <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                         | Description     |
| ------------------ | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc**            | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |
| **suppress\_glow** | <mark style="color:purple;">**`boolean`**</mark>                                                             | suppress\_glow  |
| **flashing**       | <mark style="color:purple;">**`boolean`**</mark>                                                             | flashing        |
| **glowing**        | <mark style="color:purple;">**`boolean`**</mark>                                                             | glowing         |
| **glow\_type**     | <mark style="color:purple;">**`integer`**</mark>                                                             | glow type       |
| **r**              | <mark style="color:purple;">**`integer`**</mark>                                                             | r factor        |
| **g**              | <mark style="color:purple;">**`integer`**</mark>                                                             | g factor        |
| **b**              | <mark style="color:purple;">**`integer`**</mark>                                                             | b factor        |

Sets the `CNPC` glow effect.

## <sub>SetColor</sub>

`NPC.SetColor(npc, r, g, b):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |
| **r**   | <mark style="color:purple;">**`integer`**</mark>                                                             | r factor        |
| **g**   | <mark style="color:purple;">**`integer`**</mark>                                                             | g factor        |
| **b**   | <mark style="color:purple;">**`integer`**</mark>                                                             | b factor        |

Sets the `CNPC` model color.

## <sub>IsInRangeOfShop</sub>

`NPC.IsInRangeOfShop(npc, shop_type, [specific]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                           | Type                                                                                                                                        | Description                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **npc**                                                        | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                | The target NPC.                          |
| **shop\_type**                                                 | [<mark style="color:purple;">**`Enum.ShopType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.shoptype) | Shop type to check.                      |
| **specific&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                            | No idea what is that. `(default: false)` |

Checks if the `CNPC` is in range of a shop.

## <sub>GetBaseSpellAmp</sub>

`NPC.GetBaseSpellAmp(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                         | Description     |
| ------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | The target NPC. |

Returns the base spell amplification of the `CNPC`.

## <sub>GetModifierProperty</sub>

`NPC.GetModifierProperty(npc, property):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                                                        | Description     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                                | The target NPC. |
| **property** | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction) | Property enum.  |

Returns the property value for the `CNPC`.

## <sub>IsControllableByPlayer</sub>

`NPC.IsControllableByPlayer(npc, playerId):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                                         | Description  |
| ------------ | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | npc to check |
| **playerId** | <mark style="color:purple;">**`integer`**</mark>                                                             | player id    |

Returns `true` if npc is controllable by player.

## <sub>GetModifierPropertyHighest</sub>

{% hint style="info" %}
Fixes the issue when you have multiple Kaya items that actually don't stack.
{% endhint %}

\`NPC.GetModifierPropertyHighest(npc, property):\` <mark style="color:purple;">\*\*\`number\`\*\*</mark>

| Name         | Type                                                                                                                                                        | Description     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)                                                | The target NPC. |
| **property** | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.modifierfunction) | Property enum.  |

Returns the hieghest property value for the `CNPC`.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/hero -->

# Hero

Table to work with `CHero`.

<mark style="color:purple;">**`CHero`**</mark> extends <mark style="color:purple;">**`CNPC`**</mark>

## <sub>GetCurrentXP</sub>

`Hero.GetCurrentXP(hero):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the hero's current XP.

## <sub>GetAbilityPoints</sub>

`Hero.GetAbilityPoints(hero):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the hero's available ability points.

## <sub>GetRespawnTime</sub>

{% hint style="info" %}
Could be less than current game time if hero is already alive.
{% endhint %}

\`Hero.GetRespawnTime(hero):\` <mark style="color:purple;">\*\*\`number\`\*\*</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the game time when the hero will respawn.

## <sub>GetRespawnTimePenalty</sub>

`Hero.GetRespawnTimePenalty(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the next respawn time penalty, e.g. buyback.

## <sub>GetPrimaryAttribute</sub>

`Hero.GetPrimaryAttribute(hero):` [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the hero's primary attribute type.

## <sub>GetStrength</sub>

`Hero.GetStrength(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns `white` value of strength.

## <sub>GetAgility</sub>

`Hero.GetAgility(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns `white` value of agility.

## <sub>GetIntellect</sub>

`Hero.GetIntellect(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns `white` value of intellect.

## <sub>GetStrengthTotal</sub>

`Hero.GetStrengthTotal(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns total value of strength.

## <sub>GetAgilityTotal</sub>

`Hero.GetAgilityTotal(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns total value of agility.

## <sub>GetIntellectTotal</sub>

`Hero.GetIntellectTotal(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns total value of intellect.

## <sub>GetLastHurtTime</sub>

`Hero.GetLastHurtTime(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the time when the hero was last hurt.

## <sub>GetHurtAmount</sub>

`Hero.GetHurtAmount(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the amount of damage the hero last received.

## <sub>GetRecentDamage</sub>

`Hero.GetRecentDamage(hero):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the damage taken by the hero in the last in \~1 second.

## <sub>GetPainFactor</sub>

`Hero.GetPainFactor(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the pain factor of the hero. Not sure what it is.

## <sub>GetTargetPainFactor</sub>

`Hero.GetTargetPainFactor(hero):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the pain factor of the hero's target. Not sure what it is.

## <sub>GetLifeState</sub>

`Hero.GetLifeState(hero):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns `true` if the hero is alive. Recommended to use `Entity.IsAlive` instead.

## <sub>GetPlayerID</sub>

`Hero.GetPlayerID(hero):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the ID of the hero player.

## <sub>GetReplicatingOtherHeroModel</sub>

`Hero.GetReplicatingOtherHeroModel(hero):` [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

If the hero is an illusion, Arc's copy, Meepo clone, etc. returns the original hero, otherwise returns nil.

## <sub>TalentIsLearned</sub>

`Hero.TalentIsLearned(hero, talent):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                                                              | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero**   | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero)                                    |             |
| **talent** | [<mark style="color:purple;">**`Enum.TalentTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.talenttypes) |             |

Returns `true` if talent is learned.

#### Example

```lua
TALENT_8 <=> TALENT_7
TALENT_6 <=> TALENT_5
TALENT_4 <=> TALENT_3
TALENT_2 <=> TALENT_1
```

## <sub>GetFacetAbilities</sub>

`Hero.GetFacetAbilities(hero):` [<mark style="color:purple;">**`CAbility[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns facet ability array.

## <sub>GetFacetID</sub>

`Hero.GetFacetID(hero):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns facet id. Start from 1.

## <sub>GetLastMaphackPos</sub>

`Hero.GetLastMaphackPos(hero):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the last hero pos from maphack.

## <sub>GetLastVisibleTime</sub>

`Hero.GetLastVisibleTime(hero):` <mark style="color:purple;">**`float`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) |             |

Returns the last visible time from VBE.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/ability -->

# Ability

Table to work with `CAbility`.

<mark style="color:purple;">**`CAbility`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetOwner</sub>

`Ability.GetOwner(ability):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability owner.

## <sub>IsBasic</sub>

`Ability.IsBasic(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is basic.

## <sub>IsUltimate</sub>

`Ability.IsUltimate(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is an ultimate.

## <sub>IsAttributes</sub>

`Ability.IsAttributes(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is an attribute or a talent.

## <sub>GetType</sub>

`Ability.GetType(ability):` [<mark style="color:purple;">**`Enum.AbilityTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitytypes)

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability type.

## <sub>GetBehavior</sub>

`Ability.GetBehavior(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.AbilityBehavior`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitybehavior)

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns the ability type.

## <sub>IsPassive</sub>

`Ability.IsPassive(ability, [from_static_data]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns `true` if the ability is passive.

## <sub>GetTargetTeam</sub>

`Ability.GetTargetTeam(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.TargetTeam`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targetteam)

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns the target team of this Ability.

## <sub>GetTargetType</sub>

`Ability.GetTargetType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.TargetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targettype)

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns the target type of this Ability.

## <sub>GetTargetFlags</sub>

`Ability.GetTargetFlags(ability):` [<mark style="color:purple;">**`Enum.TargetFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.targetflags)

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the target flags of this Ability.

## <sub>GetDamageType</sub>

`Ability.GetDamageType(ability):` [<mark style="color:purple;">**`Enum.DamageTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.damagetypes)

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the damage type of this Ability.

## <sub>GetImmunityType</sub>

`Ability.GetImmunityType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.ImmunityTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.immunitytypes)

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns the immunity type of this Ability.

## <sub>GetDispellableType</sub>

`Ability.GetDispellableType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.DispellableTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.dispellabletypes)

| Name                                                                     | Type                                                                                                                 | Description                                                      |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | if `true` will check from ability static data `(default: false)` |

Returns the dispel type of this Ability.

## <sub>GetLevelSpecialValueFor</sub>

`Ability.GetLevelSpecialValueFor(ability, name, [lvl]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                      | Type                                                                                                                 | Description                                                                                 |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **ability**                                               | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                                             |
| **name**                                                  | <mark style="color:purple;">**`string`**</mark>                                                                      | Special value name. Can be found in the ability KV file. (`assets/data/npc_abilities.json`) |
| **lvl&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>                                                                     | Ability level, if -1 will automatically get lvl. `(default: -1)`                            |

WRONG API FIX ME IT MUST BE GetSpecialValueFor.

## <sub>IsReady</sub>

`Ability.IsReady(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is ready to use.

## <sub>SecondsSinceLastUse</sub>

`Ability.SecondsSinceLastUse(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the number of seconds passed from the last usage of the ability. Will return -1 if\
the ability is not on the cooldown.

## <sub>GetDamage</sub>

`Ability.GetDamage(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability damage from assets/data/npc\_abilities.json field. Will return 0.0 if the\
ability doesn't contain this field.

## <sub>GetLevel</sub>

`Ability.GetLevel(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the current ability level.

## <sub>GetCastPoint</sub>

`Ability.GetCastPoint(ability, [include_modifiers]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                     | Type                                                                                                                 | Description       |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                   |
| **include\_modifiers&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | `(default: true)` |

Gets the cast delay of this Ability.

## <sub>GetCastPointModifier</sub>

`Ability.GetCastPointModifier(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Gets the cast delay modifier of this Ability.

## <sub>IsCastable</sub>

`Ability.IsCastable(ability, [mana]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                       | Type                                                                                                                 | Description      |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **ability**                                                | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                  |
| **mana&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                      | `(default: 0.0)` |

Returns `true` if the ability is currently castable. Checks for mana cost, cooldown, level,\
and slot for items.

## <sub>IsChannelling</sub>

`Ability.IsChannelling(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is in channeling state. Example: teleport, rearm, powershot\
etc.

## <sub>GetName</sub>

`Ability.GetName(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability name or empty string.

## <sub>GetBaseName</sub>

`Ability.GetBaseName(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability base name or empty string.

## <sub>IsInnate</sub>

`Ability.IsInnate(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is innate.

## <sub>IsInnatePassive</sub>

`Ability.IsInnatePassive(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is passive innate.

## <sub>GetMaxLevel</sub>

`Ability.GetMaxLevel(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns ability's max level.

## <sub>IsGrantedByFacet</sub>

`Ability.IsGrantedByFacet(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` when abiliti is granted by facet.

## <sub>CanBeExecuted</sub>

`Ability.CanBeExecuted(ability):` [<mark style="color:purple;">**`Enum.AbilityCastResult`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitycastresult)

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `-1` if ability can be executed.

## <sub>IsOwnersManaEnough</sub>

`Ability.IsOwnersManaEnough(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if enough mana for cast.

## <sub>CastNoTarget</sub>

`Ability.CastNoTarget(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                 | Description                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Casts the ability that doesn't require a target or position.

## <sub>CastPosition</sub>

`Ability.CastPosition(ability, pos, [queue], [push], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                                                 | Description                                                                             |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **ability**                                                          | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability)                 |                                                                                         |
| **pos**                                                              | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Order position.                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | If true, the order will be forced by the minimap if possible. `(default: true)`         |

Casts the ability at a specified position.

## <sub>CastTarget</sub>

`Ability.CastTarget(ability, target, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                 | Description                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                                         |
| **target**                                                          | [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc)         | Order target.                                                                           |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Casts the ability on a specified target.

## <sub>Toggle</sub>

`Ability.Toggle(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                 | Description                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Toggles the ability. Example: Armlet.

## <sub>ToggleMod</sub>

`Ability.ToggleMod(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                 | Description                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                     | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                      | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Toggles the ability modifier. Example: Frost Arrows, Medusa's Shield.

## <sub>GetDefaultName</sub>

`Ability.GetDefaultName(ability_name):` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                            | Description |
| ----------------- | ----------------------------------------------- | ----------- |
| **ability\_name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns the default ability icon name from items\_game.txt

## <sub>CanBeUpgraded</sub>

`Ability.CanBeUpgraded(ability):` [<mark style="color:purple;">**`Enum.AbilityLearnResult`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.abilitylearnresult) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns if the ability is upgradable with a specific reason.

## <sub>GetAbilityID</sub>

`Ability.GetAbilityID(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns ability id

## <sub>GetIndex</sub>

`Ability.GetIndex(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the index of the ability in the ability owner's list. The index can be used in\
NPC.GetAbilityByIndex later.

## <sub>GetCastRange</sub>

`Ability.GetCastRange(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the cast range of the ability.

## <sub>IsHidden</sub>

`Ability.IsHidden(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if ability is hidden. Example: Zeus's Nimbus before purchasing agh.

## <sub>IsActivated</sub>

`Ability.IsActivated(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is in an activated state.

## <sub>GetDirtyButtons</sub>

`Ability.GetDirtyButtons(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns we don't know what :).

## <sub>GetToggleState</sub>

`Ability.GetToggleState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns if the ability is toggled. Example: Medusa's Shield.

## <sub>IsInAbilityPhase</sub>

`Ability.IsInAbilityPhase(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is in the cast state. Examples: Nature's Prophet's Teleport,\
Meepo's Poof.

## <sub>GetCooldown</sub>

`Ability.GetCooldown(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the amount of time before the ability can be cast.

## <sub>GetCooldownLength</sub>

`Ability.GetCooldownLength(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the amount of time the ability couldn't be cast after being used.

## <sub>GetManaCost</sub>

`Ability.GetManaCost(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the ability mana cost.

## <sub>GetAutoCastState</sub>

`Ability.GetAutoCastState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the autocast state of the ability.

## <sub>GetAltCastState</sub>

`Ability.GetAltCastState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the alt cast state of the ability. Example: Doom's Devour.

## <sub>GetChannelStartTime</sub>

`Ability.GetChannelStartTime(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the gametime the channeling of the ability will start. Requires the ability to be in\
the cast state when called.

## <sub>GetCastStartTime</sub>

`Ability.GetCastStartTime(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the gametime the ability will be casted. Requires the ability to be in the cast state\
when called.

## <sub>IsInIndefinateCooldown</sub>

`Ability.IsInIndefinateCooldown(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the cooldown of the ability is indefinite.

## <sub>IsInIndefinateCooldown</sub>

`Ability.IsInIndefinateCooldown(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the cooldown of the ability is frozen.

## <sub>GetOverrideCastPoint</sub>

`Ability.GetOverrideCastPoint(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the overridden cast point. Example: Arcane Blink.

## <sub>IsStolen</sub>

`Ability.IsStolen(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns `true` if the ability is stolen.

## <sub>GetCurrentCharges</sub>

`Ability.GetCurrentCharges(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the number of charges available.

## <sub>ChargeRestoreTimeRemaining</sub>

`Ability.ChargeRestoreTimeRemaining(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the remaining time for the next charge to restore.

## <sub>GetKeybind</sub>

`Ability.GetKeybind(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/ability) |             |

Returns the keybind of the ability.

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

# Rune

Table to work with `CRune`.<mark style="color:purple;">**`CRune`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetRuneType</sub>

`Rune.GetRuneType(rune):` [<mark style="color:purple;">**`Enum.RuneType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.runetype)

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **rune** | [<mark style="color:purple;">**`CRune`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/rune) |             |

Returns `Enum.RuneType` the rune type.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tower -->

# Tower

Table to work with `CTower`.<mark style="color:purple;">**`CTower`**</mark> extends <mark style="color:purple;">**`CNPC`**</mark>

## <sub>GetAttackTarget</sub>

`Tower.GetAttackTarget(tower):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                             | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| **tower** | [<mark style="color:purple;">**`CTower`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tower) |             |

Returns `CNPC` that is attacked by the tower now.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tree -->

# Tree

Table to work with `CTree`.<mark style="color:purple;">**`CTree`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>IsActive</sub>

`Tree.IsActive(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                                           | Description |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tree) |             |

Returns if the tree is not cut.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace -->

# Vambrace

Table to work with `CVambrace`.<mark style="color:purple;">**`CVambrace`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetStats</sub>

`Vambrace.GetStats(vambrace):` [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

| Name         | Type                                                                                                                   | Description |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| **vambrace** | [<mark style="color:purple;">**`CVambrace`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace) |             |

Returns selected `Enum.Attributes` attribute.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/camp -->

# Camp

Table to work with `CCamp`.<mark style="color:purple;">**`CCamp`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetType</sub>

`Camp.GetType(camp):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                           | Description        |
| -------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp) | The camp to check. |

Returns the camp type.

## <sub>GetCampBox</sub>

`Camp.GetCampBox(camp):` <mark style="color:purple;">**`{min:Vector, max:Vector}`**</mark>

| Name     | Type                                                                                                           | Description        |
| -------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/camp) | The camp to check. |

Returns camp box as a table with **min** and **max** fields(**Vector**).

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/bottle -->

# Bottle

Table to work with `CBottle`.

<mark style="color:purple;">**`CBottle`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetRuneType</sub>

`Bottle.GetRuneType(bottle):` [<mark style="color:purple;">**`Enum.RuneType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.runetype)

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **bottle** | [<mark style="color:purple;">**`CBottle`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/bottle) |             |

Returns the rune inside the bottle.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/courier -->

# Courier

Table to work with `CCourier`.<mark style="color:purple;">**`CCourier`**</mark> extends <mark style="color:purple;">**`CNPC`**</mark>

## <sub>IsFlyingCourier</sub>

`Courier.IsFlyingCourier(courier):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                 | Description           |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | The courier to check. |

Returns `true` if the courier is flying.

## <sub>GetRespawnTime</sub>

`Courier.GetRespawnTime(courier):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                                                 | Description           |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | The courier to check. |

Returns the game time when the courier will respawn.

## <sub>GetCourierState</sub>

`Courier.GetCourierState(courier):` [<mark style="color:purple;">**`Enum.CourierState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.courierstate)

| Name        | Type                                                                                                                 | Description           |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | The courier to check. |

Returns the courier state.

## <sub>GetPlayerID</sub>

`Courier.GetPlayerID(courier):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                                 | Description           |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | The courier to check. |

Returns owner's player id.

## <sub>GetCourierStateEntity</sub>

`Courier.GetCourierStateEntity(courier):` [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                                                                                                 | Description           |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/courier) | The courier to check. |

Returns the entity that the courier is currently interacting with.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler -->

# DrunkenBrawler

Table to work with `CDrunkenBrawler`.<mark style="color:purple;">**`CDrunkenBrawler`**</mark> extends <mark style="color:purple;">**`CAbility`**</mark>

## <sub>GetState</sub>

`DrunkenBrawler.GetState(ability):` [<mark style="color:purple;">**`Enum.DrunkenBrawlerState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drunkenbrawlerstate)

| Name        | Type                                                                                                                               | Description |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CDrunkenBrawler`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler) |             |

Returns the state of the CDrunkenBrawler ability.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem -->

# PhysicalItem

Table to work with `CPhysicalItem`.<mark style="color:purple;">**`CPhysicalItem`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetItem</sub>

`PhysicalItem.GetItem(physical_item):` [<mark style="color:purple;">**`CItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/item) | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                                           | Description |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **physical\_item** | [<mark style="color:purple;">**`CPhysicalItem`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem) |             |

Returns `CItem` object from `CPhysicalItem`.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads -->

# PowerTreads

Table to work with `CPowerTreads`.<mark style="color:purple;">**`CTower`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetStats</sub>

`PowerTreads.GetStats(power_tread):` [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

| Name             | Type                                                                                                                         | Description |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **power\_tread** | [<mark style="color:purple;">**`CPowerTreads`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads) |             |

Returns selected `Enum.Attributes` attribute.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken -->

# TierToken

Table to work with `CTierToken`.<mark style="color:purple;">**`CTierToken`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetChoices</sub>

`TierToken.GetChoices(tier_token):` <mark style="color:purple;">**`integer[]`**</mark>

| Name            | Type                                                                                                                     | Description                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **tier\_token** | [<mark style="color:purple;">**`CTierToken`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken) | The `TierToken` to get the choices from. |

Returns the choices (ability ids) of the `CTierToken`.


--------------------------------------------------------------------------------

## Game Engine

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine -->

# Game Engine

- [Engine](/api-v2.0/game-components/game-engine/engine.md)
- [Event](/api-v2.0/game-components/game-engine/event.md)
- [GameRules](/api-v2.0/game-components/game-engine/gamerules.md)
- [GlobalVars](/api-v2.0/game-components/game-engine/globalvars.md)
- [GridNav](/api-v2.0/game-components/game-engine/gridnav.md)
- [Input](/api-v2.0/game-components/game-engine/input.md)
- [World](/api-v2.0/game-components/game-engine/world.md)
- [FogOfWar](/api-v2.0/game-components/game-engine/fogofwar.md)
- [ConVar](/api-v2.0/game-components/game-engine/convar.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/engine -->

# Engine

Table to work with game engine.

## <sub>IsInGame</sub>

`Engine.IsInGame():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the game is in progress.

## <sub>IsShopOpen</sub>

`Engine.IsShopOpen():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the shop is open.

## <sub>SetQuickBuy</sub>

`Engine.SetQuickBuy(item_name, [reset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                        | Type                                             | Description                                                |
| ----------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| **item\_name**                                              | <mark style="color:purple;">**`string`**</mark>  | The name of the item to quick buy. (e.g. `blink`, `relic`) |
| **reset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Reset the quick buy list. `(default: true)`                |

Add item to quick buy list.

## <sub>RunScript</sub>

`Engine.RunScript(script, [contextPanel]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                               | Type                                                                                                                                                                                             | Description                                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| **script**                                                         | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                  | The script to run.                                                                     |
| **contextPanel&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> \| [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | The id of the panel or the panel itself to run the script in. `(default: "Dashboard")` |

Run a JS script in the panorama context. Return `true` if the script was executed\
successfully. [JS\
documentation](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Panorama/Javascript)

#### Example

```lua
-- in dota console, you should see "Hello from Lua!"
Engine.RunScript("$.Msg('Hello from Lua!')");
```

## <sub>ExecuteCommand</sub>

`Engine.ExecuteCommand(command):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description             |
| ----------- | ----------------------------------------------- | ----------------------- |
| **command** | <mark style="color:purple;">**`string`**</mark> | The command to execute. |

Execute a console command.

#### Example

```lua
-- in dota chat, you should see "Hello from Lua!"
Engine.ExecuteCommand("say \"Hello from Lua!\"");
```

## <sub>PlayVol</sub>

`Engine.PlayVol(sound, [volume]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                            | Description                                                               |
| ------------------------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------- |
| **sound**                                                    | <mark style="color:purple;">**`string`**</mark> | The sound to play. Could find in `sounds` folder in `pak01_dir.vpk` file. |
| **volume&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The volume of the sound. `(default: 0.1)`                                 |

Play a sound with a specific volume.

#### Example

```lua
-- play a sound with a volume of 0.5 (very loud)
Engine.PlayVol("sounds/npc/courier/courier_acknowledge.vsnd_c", 0.5);
```

## <sub>CreateConfig</sub>

`Engine.CreateConfig(config_name, categories):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                                                                                                                | Description             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **config\_name** | <mark style="color:purple;">**`string`**</mark>                                                                                     | The name of the config. |
| **categories**   | <mark style="color:purple;">**`{name: string, hero_ids: integer[], x: number, y: number, width: number, height: number}[]`**</mark> |                         |

Creates a new hero grid config.

#### Example

```lua
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

## <sub>GetCurrentConfigName</sub>

`Engine.GetCurrentConfigName():` <mark style="color:purple;">**`string`**</mark>

Returns the current hero grid config name

## <sub>SetNewGridConfig</sub>

`Engine.SetNewGridConfig(config_name):` <mark style="color:purple;">**`nil`**</mark>

| Name             | Type                                            | Description                   |
| ---------------- | ----------------------------------------------- | ----------------------------- |
| **config\_name** | <mark style="color:purple;">**`string`**</mark> | The name of the config to set |

Set the new hero grid config by name

## <sub>LookAt</sub>

`Engine.LookAt(x, y):` <mark style="color:purple;">**`nil`**</mark>

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

Move camera to a specific position.

## <sub>CanAcceptMatch</sub>

`Engine.CanAcceptMatch():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the player can accept the match.

## <sub>GetGameDirectory</sub>

`Engine.GetGameDirectory():` <mark style="color:purple;">**`string`**</mark>

Returns the current game directory. (e.g. `dota 2 beta`)

## <sub>GetCheatDirectory</sub>

`Engine.GetCheatDirectory():` <mark style="color:purple;">**`string`**</mark>

Returns the current cheat directory.

## <sub>GetLevelName</sub>

`Engine.GetLevelName():` <mark style="color:purple;">**`string`**</mark>

Returns the current level name. (e.g. `maps/hero_demo_main.vpk`)

## <sub>GetLevelNameShort</sub>

`Engine.GetLevelNameShort():` <mark style="color:purple;">**`string`**</mark>

Returns the current level name without the extension and folder. (e.g. `hero_demo_main`)

## <sub>AcceptMatch</sub>

`Engine.AcceptMatch(state):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description         |
| --------- | ------------------------------------------------ | ------------------- |
| **state** | <mark style="color:purple;">**`integer`**</mark> | DOTALobbyReadyState |

Accept match.

## <sub>ConsoleColorPrintf</sub>

`Engine.ConsoleColorPrintf(r, g, b, [a], text):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                    | Type                                             | Description                   |
| ------------------------------------------------------- | ------------------------------------------------ | ----------------------------- |
| **r**                                                   | <mark style="color:purple;">**`integer`**</mark> | Red value.                    |
| **g**                                                   | <mark style="color:purple;">**`integer`**</mark> | Green value.                  |
| **b**                                                   | <mark style="color:purple;">**`integer`**</mark> | Blue value.                   |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | Alpha value. `(default: 255)` |
| **text**                                                | <mark style="color:purple;">**`string`**</mark>  | Text to print.                |

Print a message to the dota console.

## <sub>GetMMR</sub>

`Engine.GetMMR():` <mark style="color:purple;">**`integer`**</mark>

Returns the current MMR.

## <sub>GetMMRV2</sub>

`Engine.GetMMRV2():` <mark style="color:purple;">**`integer`**</mark>

Returns the current MMR. Works better than `Engine.GetMMR`.\
Must be called from the game thread. Ex: OnNetUpdateEx, OnGCMessage, not OnFrame or on\
initialization.

## <sub>ReloadScriptSystem</sub>

`Engine.ReloadScriptSystem():` <mark style="color:purple;">**`nil`**</mark>

Executes script system reload.

## <sub>ShowDotaWindow</sub>

`Engine.ShowDotaWindow():` <mark style="color:purple;">**`nil`**</mark>

Brings the game window to the forefront if it is minimized.\
Use this function to make the game window the topmost window.

## <sub>IsInLobby</sub>

`Engine.IsInLobby():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the player is in a lobby.

## <sub>GetBuildVersion</sub>

`Engine.GetBuildVersion():` <mark style="color:purple;">**`string`**</mark>

Returns the cheat version.

## <sub>GetHeroIDByName</sub>

`Engine.GetHeroIDByName(unitName):` <mark style="color:purple;">**`integer`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                            | Description                             |
| ------------ | ----------------------------------------------- | --------------------------------------- |
| **unitName** | <mark style="color:purple;">**`string`**</mark> | Can be retrieved from `NPC.GetUnitName` |

Returns hero ID by unit name.

#### Example

```lua
local abaddonId = Engine.GetHeroIDByName( "npc_dota_hero_abaddon" )
```

## <sub>GetDisplayNameByUnitName</sub>

`Engine.GetDisplayNameByUnitName(unitName):` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                            | Description                             |
| ------------ | ----------------------------------------------- | --------------------------------------- |
| **unitName** | <mark style="color:purple;">**`string`**</mark> | Can be retrieved from `NPC.GetUnitName` |

Returns hero display name by unit name.

#### Example

```lua
local nevermore_name = Engine.GetDisplayNameByUnitName( "npc_dota_hero_nevermore" )
-- nevermore_name == "Shadow Fiend"
```

## <sub>GetHeroNameByID</sub>

`Engine.GetHeroNameByID(heroID):` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description |
| ---------- | ------------------------------------------------ | ----------- |
| **heroID** | <mark style="color:purple;">**`integer`**</mark> |             |

Returns hero name by ID.

## <sub>GetUIState</sub>

`Engine.GetUIState():` [<mark style="color:purple;">**`Enum.UIState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.uistate)

Returns current UI state.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event -->

# Event

Table to work with game events.

When you install events, you send the subscribe message to the server, which is potentially unsafe.\
Therefore, you won't be able to install new listeners when you have unsafe features disabled in the Settings -> Security tab.

The list of events can be found in the "pak01\_dir.vpk" under "resource/game.gameevents."

## <sub>AddListener</sub>

`Event.AddListener(name):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                            | Description |
| -------- | ----------------------------------------------- | ----------- |
| **name** | <mark style="color:purple;">**`string`**</mark> | Event name  |

Installs an event listener for the desired event.

## <sub>IsReliable</sub>

`Event.IsReliable(event):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |

Checks if the event is reliable.

## <sub>IsLocal</sub>

`Event.IsLocal(event):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |

Checks if the event is local or networked.

## <sub>IsEmpty</sub>

`Event.IsEmpty(event):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |

Checks if the event is empty.

## <sub>GetBool</sub>

`Event.GetBool(event, field):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |
| **field** | <mark style="color:purple;">**`string`**</mark>                                                                         | Field name  |

Returns the boolean value of the specified event field.

## <sub>GetInt</sub>

`Event.GetInt(event, field):` <mark style="color:purple;">**`integer`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |
| **field** | <mark style="color:purple;">**`string`**</mark>                                                                         | Field name  |

Returns the integer value of the specified event field.

## <sub>GetUint64</sub>

`Event.GetUint64(event, field):` <mark style="color:purple;">**`integer`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |
| **field** | <mark style="color:purple;">**`string`**</mark>                                                                         | Field name  |

Returns the uint64 value of the specified event field.

## <sub>GetFloat</sub>

`Event.GetFloat(event, field):` <mark style="color:purple;">**`number`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |
| **field** | <mark style="color:purple;">**`string`**</mark>                                                                         | Field name  |

Returns the floating value of the specified event field.

## <sub>GetString</sub>

`Event.GetString(event, field):` <mark style="color:purple;">**`string`**</mark>

| Name      | Type                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| **event** | [<mark style="color:purple;">**`CEvent`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event) |             |
| **field** | <mark style="color:purple;">**`string`**</mark>                                                                         | Field name  |

Returns the string value of the specified event field.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gamerules -->

# GameRules

Table to work with GameRules.

## <sub>GetServerGameState</sub>

`GameRules.GetServerGameState():` [<mark style="color:purple;">**`Enum.GameState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current server game state.

## <sub>GetGameState</sub>

`GameRules.GetGameState():` [<mark style="color:purple;">**`Enum.GameState`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamestate)

Returns the current game state.

## <sub>GetGameMode</sub>

`GameRules.GetGameMode():` [<mark style="color:purple;">**`Enum.GameMode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.gamemode)

Returns the current game mode.

## <sub>GetPreGameStartTime</sub>

{% hint style="info" %}
Pregame time is the time before the game starts, e.g. ban phase, pick time.
{% endhint %}

`GameRules.GetPreGameStartTime():` <mark style="color:purple;">**`number`**</mark>

Returns pregame duration or 0 if now is pregame time.

## <sub>GetGameStartTime</sub>

{% hint style="info" %}
Game start time is 0:00 on ingame timer.
{% endhint %}

`GameRules.GetGameStartTime():` <mark style="color:purple;">**`number`**</mark>

Returns game start time duration or 0 if game is not start yet.

## <sub>GetGameEndTime</sub>

`GameRules.GetGameEndTime():` <mark style="color:purple;">**`number`**</mark>

Returns game end time or 0 if game is not end yet.

## <sub>GetGameLoadTime</sub>

`GameRules.GetGameLoadTime():` <mark style="color:purple;">**`number`**</mark>

No idea what this function does. Returns 0 in all cases what I've tested.

## <sub>GetGameTime</sub>

{% hint style="info" %}
Can be used to calculate time in an in-game timer. See the example.
{% endhint %}

`GameRules.GetGameTime():` <mark style="color:purple;">**`number`**</mark>

Returns the current game time. Starts counting from pregame state.

#### Example

```lua
local game_time = GameRules.GetGameTime();
local ingame_timer = game_time - GameRules.GetGameStartTime();
Log.Write(string.format("Current time: %d:%02d", math.floor(ingame_timer / 60),
math.floor(ingame_timer % 60)))
```

## <sub>IsPaused</sub>

`GameRules.IsPaused():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if game is paused.

## <sub>IsTemporaryDay</sub>

{% hint style="info" %}
Example: Phoenix's Supernova.
{% endhint %}

`GameRules.IsTemporaryDay():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if it's temporary day.

## <sub>IsTemporaryNight</sub>

{% hint style="info" %}
Example: Luna's Eclipse.
{% endhint %}

`GameRules.IsTemporaryNight():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if it's temporary night.

## <sub>IsNightstalkerNight</sub>

`GameRules.IsNightstalkerNight():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if it's nightstalker's night.

## <sub>GetMatchID</sub>

`GameRules.GetMatchID():` <mark style="color:purple;">**`integer`**</mark>

Returns current match id.

## <sub>GetLobbyID</sub>

`GameRules.GetLobbyID():` <mark style="color:purple;">**`integer`**</mark>

Returns current lobby id.

## <sub>GetGoodGlyphCD</sub>

{% hint style="info" %}
Could be less than current game time if glyph is already available.
{% endhint %}

`GameRules.GetGoodGlyphCD():` <mark style="color:purple;">**`number`**</mark>

Returns game time when next radiant glyph will be available.

## <sub>GetBadGlyphCD</sub>

{% hint style="info" %}
Could be less than current game time if glyph is already available.
{% endhint %}

`GameRules.GetBadGlyphCD():` <mark style="color:purple;">**`number`**</mark>

Returns game time when next dire glyph will be available.

## <sub>GetGoodScanCD</sub>

{% hint style="info" %}
Could be less than current game time if scan is already available.
{% endhint %}

`GameRules.GetGoodScanCD():` <mark style="color:purple;">**`number`**</mark>

Returns game time when next radiant scan will be available.

## <sub>GetBadScanCD</sub>

{% hint style="info" %}
Could be less than current game time if scan is already available.
{% endhint %}

`GameRules.GetBadScanCD():` <mark style="color:purple;">**`number`**</mark>

Returns game time when next dire scan will be available.

## <sub>GetGoodScanCharges</sub>

`GameRules.GetGoodScanCharges():` <mark style="color:purple;">**`integer`**</mark>

Returns current radiant scan charges.

## <sub>GetGoodScanCharges</sub>

`GameRules.GetGoodScanCharges():` <mark style="color:purple;">**`integer`**</mark>

Returns current dire scan charges.

## <sub>GetStockCount</sub>

{% hint style="info" %}
Item id can be found in \`assets/data/items.json\` file in cheat folder.
{% endhint %}

\`GameRules.GetStockCount(item\_id, \[team]):\` <mark style="color:purple;">\*\*\`integer\`\*\*</mark>

| Name                                                       | Type                                                                                                                                      | Description                                                                        |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **item\_id**                                               | <mark style="color:purple;">**`integer`**</mark>                                                                                          |                                                                                    |
| **team&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum) | - Optional. Default is local player's team. `(default: Enum.TeamNum.TEAM_RADIANT)` |

Returns amount of remaining items in shop by item id.

#### Example

```lua
-- "item_ward_observer": {
--     "ID": "42",
Log.Write("Observers available: " .. GameRules.GetStockCount(42))
```

## <sub>GetNextCycleTime</sub>

`GameRules.GetNextCycleTime():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`boolean`**</mark>

Return time remaining to the next cycle.

## <sub>GetDaytimeStart</sub>

`GameRules.GetDaytimeStart():` <mark style="color:purple;">**`number`**</mark>

Returns day start time. To work with it use `GameRules.GetTimeOfDay`

## <sub>GetNighttimeStart</sub>

`GameRules.GetNighttimeStart():` <mark style="color:purple;">**`number`**</mark>

Returns night start time. To work with it use `GameRules.GetTimeOfDay`

## <sub>GetTimeOfDay</sub>

`GameRules.GetTimeOfDay():` <mark style="color:purple;">**`number`**</mark>

Returns current time of day time.

## <sub>IsInBanPhase</sub>

`GameRules.IsInBanPhase():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if game is in ban phase.

## <sub>GetAllDraftPhase</sub>

`GameRules.GetAllDraftPhase():` <mark style="color:purple;">**`integer`**</mark>

Returns index of the current draft phase.

## <sub>IsAllDraftPhaseRadiantFirst</sub>

`GameRules.IsAllDraftPhaseRadiantFirst():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if Radiant picks first.

## <sub>GetDOTATime</sub>

`GameRules.GetDOTATime([pregame], [negative]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                           | Type                                             | Description                                          |
| -------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------- |
| **pregame&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark> | If `true` includes pregame time. `(default: false)`  |
| **negative&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | If `true` includes negative time. `(default: false)` |

Returns the actual DOTA in-game clock time.

## <sub>GetLobbyObjectJson</sub>

`GameRules.GetLobbyObjectJson():` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

Returns CSODOTALobby protobuf object as JSON string.

## <sub>GetBannedHeroes</sub>

`GameRules.GetBannedHeroes():` <mark style="color:purple;">**`integer[]`**</mark> | <mark style="color:purple;">**`nil`**</mark>

Returns zero-based array of banned heroes where index corresponds to the player id.

## <sub>GetStateTransitionTime</sub>

`GameRules.GetStateTransitionTime():` <mark style="color:purple;">**`number`**</mark>

Returns time remaining between state changes.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/globalvars -->

# GlobalVars

Talbe to work with game's global variables.

## <sub>GetFrameCount</sub>

`GlobalVars.GetFrameCount():` <mark style="color:purple;">**`integer`**</mark>

Returns absolute frame counter. Continues to increase even if game is paused.

## <sub>GetAbsFrameTime</sub>

`GlobalVars.GetAbsFrameTime():` <mark style="color:purple;">**`number`**</mark>

Returns absolute frame time.

## <sub>GetAbsFrameTimeDev</sub>

`GlobalVars.GetAbsFrameTimeDev():` <mark style="color:purple;">**`number`**</mark>

Returns absolute frame time. No idea what's the difference between this and `GetAbsFrameTime`.

## <sub>GetMapName</sub>

`GlobalVars.GetMapName():` <mark style="color:purple;">**`string`**</mark>

Returns full name of the current map. For example, "maps/dota.vpk" or "maps/hero\_demo\_main.vpk".

## <sub>GetMapGroupName</sub>

`GlobalVars.GetMapGroupName():` <mark style="color:purple;">**`string`**</mark>

Returns short name of the current map. For example, "dota" or "hero\_demo\_main".

## <sub>GetCurTime</sub>

`GlobalVars.GetCurTime():` <mark style="color:purple;">**`number`**</mark>

TODO

## <sub>GetServerTick</sub>

`GlobalVars.GetServerTick():` <mark style="color:purple;">**`integer`**</mark>

TODO

## <sub>GetIntervalPerTick</sub>

`GlobalVars.GetIntervalPerTick():` <mark style="color:purple;">**`number`**</mark>

TODO

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gridnav -->

# GridNav

Table to work with in-game navigation API.

## <sub>CreateNpcMap</sub>

{% hint style="info" %}
You should always call \`GridNav.ReleaseNpcMap\` after you done with your build pathing
{% endhint %}

\`GridNav.CreateNpcMap(\[excluded\_npcs], \[includeTempTrees], \[customCollisionSizes]):\` \[<mark style="color:purple;">\*\*\`GridNavNpcMap\`\*\*</mark>]\(GridNavNpcMap.md)

| Name                                                                       | Type                                                                                                                                                                 | Description                                                                                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **excluded\_npcs&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | [<mark style="color:purple;">**`CEntity[]`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| <mark style="color:purple;">**`nil`**</mark> | table with npc to exclude from the map. for example you want to exclude local hero if you build path from local hero position `(default: nil)` |
| **includeTempTrees&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                     | `true` if you want include temp trees to the map e.g. furion's 1st spell, iron branch `(default: true)`                                        |
| **customCollisionSizes&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`table`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                                                       | table where key is entity userdata and value is {left, top, right, bottom} offsets from entity position `(default: nil)`                       |

Creates a new `GridNavNpcMap`

## <sub>ReleaseNpcMap</sub>

`GridNav.ReleaseNpcMap(npc_map):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                                           | Description               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **npc\_map** | [<mark style="color:purple;">**`GridNavNpcMap`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) | map to release to release |

Releases allocated memory for `GridNavNpcMap`

## <sub>IsTraversable</sub>

`GridNav.IsTraversable(pos, [flag]):` <mark style="color:purple;">**`boolean`**</mark>, <mark style="color:purple;">**`integer`**</mark>

| Name                                                       | Type                                                                                                                                 | Description                  |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | position to check            |
| **flag&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                      | flag to check `(default: 1)` |

Returns `true` if the world position is traversable.

## <sub>BuildPath</sub>

`GridNav.BuildPath(start, end_, [ignoreTrees], [npc_map]):` [<mark style="color:purple;">**`Vector[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name                                                              | Type                                                                                                                                                                                           | Description                                                                                  |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **start**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                                                           | position to start                                                                            |
| **end\_**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                                                           | position to end                                                                              |
| **ignoreTrees&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                               | `true` if you want to exclude static trees from the pathing `(default: false)`               |
| **npc\_map&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`GridNavNpcMap`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) \| <mark style="color:purple;">**`nil`**</mark> | map with the npc's positions which works as additional mask for terrain map `(default: nil)` |

Build path from start to end. Returns an array with builded positions.

#### Example

```lua
-- build_path.lua
return {
    OnUpdate = function()
        local ignore_trees = false;
        local my_hero = Heroes.GetLocal();
        local start_pos = Entity.GetAbsOrigin(my_hero);
        local end_pos = Input.GetWorldCursorPos();

        -- create npc map with the temp trees but with no local hero in it
        local npc_map = GridNav.CreateNpcMap({Heroes.GetLocal()}, not ignore_trees);

        local path = GridNav.BuildPath(start_pos, end_pos, ignore_trees, npc_map);
        local prev_x, prev_y = nil, nil;
        for i, pos in pairs(path) do
            local x, y, visible = Renderer.WorldToScreen(pos);
            if (prev_x and visible) then
                Renderer.SetDrawColor(255, 255, 255, 255);
                Renderer.DrawLine(prev_x, prev_y, x, y);
            end
            prev_x, prev_y = x, y;
        end

        -- releasing allocated npc map after we done with build pathing
        GridNav.ReleaseNpcMap(npc_map)
    end
}

```

## <sub>IsTraversableFromTo</sub>

`GridNav.IsTraversableFromTo(start, end_, [ignoreTrees], [npc_map]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                              | Type                                                                                                                                                                                           | Description                                                                                  |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **start**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                                                           | position to start                                                                            |
| **end\_**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                                                           | position to end                                                                              |
| **ignoreTrees&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                               | `true` if you want to exclude static trees from the pathing `(default: false)`               |
| **npc\_map&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`GridNavNpcMap`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) \| <mark style="color:purple;">**`nil`**</mark> | map with the npc's positions which works as additional mask for terrain map `(default: nil)` |

Lite version of GridNav.BuildPath function which just cheking if the path is exists.

## <sub>DebugRender</sub>

`GridNav.DebugRender([grid_range], [npc_map], [render_cell_flags]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                                      | Type                                                                                                                                                                                           | Description                                                                                                                                  |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **grid\_range&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                               | grid radius in "cell units" from Vector(0,0,0) `(default: 50)`                                                                               |
| **npc\_map&#x20;**<mark style="color:orange;">**`[?]`**</mark>            | [<mark style="color:purple;">**`GridNavNpcMap`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) \| <mark style="color:purple;">**`nil`**</mark> | map with the npc's positions which works as additional mask for terrain map `(default: nil)`                                                 |
| **render\_cell\_flags&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                               | render the flags value for each not approachable cell (don't think you ever want to see this numbers, so ignore this arg) `(default: false)` |

Debug render of current GridNav with GridNavNpcMap (if provided)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/input -->

# Input

Table to work with input system.

## <sub>GetWorldCursorPos</sub>

`Input.GetWorldCursorPos():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world cursor position.

## <sub>GetCursorPos</sub>

`Input.GetCursorPos():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns screen cursor position (x, y). See example.

#### Example

```lua
local x, y =	Input.GetCursorPos()
```

## <sub>IsCursorInRect</sub>

`Input.IsCursorInRect(x, y, w, h):` <mark style="color:purple;">**`boolean`**</mark>

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> | x position  |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |
| **w** | <mark style="color:purple;">**`number`**</mark> | width       |
| **h** | <mark style="color:purple;">**`number`**</mark> | height      |

Returns `true` if cursor is in rect.

## <sub>IsCursorInBounds</sub>

`Input.IsCursorInBounds(x0, y0, x1, y1):` <mark style="color:purple;">**`boolean`**</mark>

| Name   | Type                                            | Description |
| ------ | ----------------------------------------------- | ----------- |
| **x0** | <mark style="color:purple;">**`number`**</mark> |             |
| **y0** | <mark style="color:purple;">**`number`**</mark> |             |
| **x1** | <mark style="color:purple;">**`number`**</mark> |             |
| **y1** | <mark style="color:purple;">**`number`**</mark> |             |

Returns `true` if cursor is in bounds.

## <sub>GetNearestUnitToCursor</sub>

{% hint style="info" %}
Excludes not visible, illusions and dead units.
{% endhint %}

`Input.GetNearestUnitToCursor(teamNum, teamType):` [<mark style="color:purple;">**`CNPC`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/npc) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                                        | Description                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **teamNum**  | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)   | team number. Could be get from `Entity.GetTeamNum` |
| **teamType** | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | team type to search relative to teamNum param      |

Returns nearest unit to cursor.

## <sub>GetNearestHeroToCursor</sub>

{% hint style="info" %}
Excludes not visible, illusions and dead heroes.
{% endhint %}

`Input.GetNearestHeroToCursor(teamNum, teamType):` [<mark style="color:purple;">**`CHero`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/hero) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                                        | Description                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **teamNum**  | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamnum)   | team number. Could be get from `Entity.GetTeamNum` |
| **teamType** | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.teamtype) | team type to search relative to teamNum param      |

Returns nearest hero to cursor.

## <sub>IsInputCaptured</sub>

`Input.IsInputCaptured():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if input is captured. e.g. opened console, chat, shop.

## <sub>IsKeyDown</sub>

`Input.IsKeyDown(KeyCode):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                                                                            | Description |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **KeyCode** | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode) |             |

Returns `true` if key is down.

## <sub>IsKeyDownOnce</sub>

{% hint style="info" %}
This function will return \`true\` only once per key press.
{% endhint %}

\`Input.IsKeyDownOnce(KeyCode):\` <mark style="color:purple;">\*\*\`boolean\`\*\*</mark>

| Name        | Type                                                                                                                                            | Description |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **KeyCode** | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode) |             |

Return `true` if key is down once.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/world -->

# World

Table containing functions for interacting with the world.

## <sub>GetGroundZ</sub>

`World.GetGroundZ(x, y):` <mark style="color:purple;">**`number`**</mark>

| Name  | Type                                            | Description                              |
| ----- | ----------------------------------------------- | ---------------------------------------- |
| **x** | <mark style="color:purple;">**`number`**</mark> | The X position to get the ground Z from. |
| **y** | <mark style="color:purple;">**`number`**</mark> | The Y position to get the ground Z from. |

Returns the ground Z at the given position.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/fogofwar -->

# FogOfWar

Table to work with FogOfWar API.

## <sub>IsPointVisible</sub>

`FogOfWar.IsPointVisible(pos):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                                                 | Description       |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | position to check |

Returns `true` if the world position is visible.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar -->

# ConVar

Table to work with `CConVars`.\
ConVars are game variable that can be used to retrieve or change some game engine settings.

## <sub>Find</sub>

`ConVar.Find(name):` [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                            | Description |
| -------- | ----------------------------------------------- | ----------- |
| **name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns the found ConVar.

#### Example

```lua
local convar = ConVar.Find("dota_camera_distance")
local camera_distance = ConVar.GetFloat(convar)
```

## <sub>GetString</sub>

`ConVar.GetString(convar):` <mark style="color:purple;">**`string`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |

Returns string value of the Convar

## <sub>GetInt</sub>

`ConVar.GetInt(convar):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |

Returns int value of the Convar

## <sub>GetFloat</sub>

`ConVar.GetFloat(convar):` <mark style="color:purple;">**`number`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |

Returns float value of the Convar

## <sub>GetBool</sub>

`ConVar.GetBool(convar):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |

Returns boolean value of the Convar

## <sub>SetString</sub>

`ConVar.SetString(convar, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |
| **value**  | <mark style="color:purple;">**`string`**</mark>                                                                           |             |

Assigns new string value to the ConVar

## <sub>SetInt</sub>

`ConVar.SetInt(convar, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |
| **value**  | <mark style="color:purple;">**`integer`**</mark>                                                                          |             |

Assigns new int value to the ConVar

## <sub>SetFloat</sub>

`ConVar.SetFloat(convar, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |
| **value**  | <mark style="color:purple;">**`number`**</mark>                                                                           |             |

Assigns new float value to the ConVar

## <sub>SetBool</sub>

`ConVar.SetBool(convar, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **convar** | [<mark style="color:purple;">**`CConVar`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar) |             |
| **value**  | <mark style="color:purple;">**`boolean`**</mark>                                                                          |             |

Assigns new boolean value to the ConVar


--------------------------------------------------------------------------------

## Networking and APIs

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis -->

# Networking & APIs

- [Chat](/api-v2.0/game-components/networking-and-apis/chatapi.md)
- [HTTP](/api-v2.0/game-components/networking-and-apis/http.md)
- [Steam](/api-v2.0/game-components/networking-and-apis/steamapi.md)
- [NetChannel](/api-v2.0/game-components/networking-and-apis/netchannel.md)
- [Game Coordinator](/api-v2.0/game-components/networking-and-apis/gc.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi -->

# Chat

Table to work with chat.

## <sub>GetChannels</sub>

`Chat.GetChannels():` <mark style="color:purple;">**`string[]`**</mark>

Returns an array of channel names.

## <sub>Print</sub>

`Chat.Print(channel, text):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description                             |
| ----------- | ----------------------------------------------- | --------------------------------------- |
| **channel** | <mark style="color:purple;">**`string`**</mark> | The channel name to say the message in. |
| **text**    | <mark style="color:purple;">**`string`**</mark> | The message to say.                     |

Print a message in a channel. This message will not be sent to the server.

## <sub>Say</sub>

`Chat.Say(channel, text):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description                             |
| ----------- | ----------------------------------------------- | --------------------------------------- |
| **channel** | <mark style="color:purple;">**`string`**</mark> | The channel name to say the message in. |
| **text**    | <mark style="color:purple;">**`string`**</mark> | The message to say.                     |

Say a message in a channel.

## <sub>Flip</sub>

`Chat.Flip(channel):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description                           |
| ----------- | ----------------------------------------------- | ------------------------------------- |
| **channel** | <mark style="color:purple;">**`string`**</mark> | The channel name to flip the coin in. |

Flip the coin in a channel.

## <sub>Roll</sub>

`Chat.Roll(channel, [min], [max]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                      | Type                                            | Description                                  |
| --------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| **channel**                                               | <mark style="color:purple;">**`string`**</mark> | The channel name to roll the dice in.        |
| **min&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The minimum number to roll. `(default: 0)`   |
| **max&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The maximum number to roll. `(default: 100)` |

Roll a dice in a channel.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http -->

# HTTP

Table to work with HTTP requests.

## <sub>Request</sub>

`HTTP.Request(method, url, [data], callback, [param]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                        | Type                                                                                                                                                                                                                              | Description                                                                                         |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **method**                                                  | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                                                   | HTTP method                                                                                         |
| **url**                                                     | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                                                   | URL                                                                                                 |
| **data&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`{headers:table<string>, cookies:string`**</mark> \| <mark style="color:purple;">**`table<string>, data:string`**</mark> \| <mark style="color:purple;">**`table<string>, timeout:number}`**</mark> | data to send `(default: {})`                                                                        |
| **callback**                                                | <mark style="color:purple;">**`fun(tbl: {response: string, code: string, header: string, param: string}):nil`**</mark>                                                                                                            | callback function to call when request is done. Take 1 argument - response data table, see example. |
| **param&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                                                   | string parameter to pass to callback function to identify request `(default: "")`                   |

Do HTTP request. Returns `true` if request was sent successfully.

#### Example

```lua
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

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi -->

# Steam

Table to with Steam API functions

## <sub>SetPersonaName</sub>

`Steam.SetPersonaName(name):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                            | Description     |
| -------- | ----------------------------------------------- | --------------- |
| **name** | <mark style="color:purple;">**`string`**</mark> | The name to set |

Sets the player name, stores it on the server and publishes the changes to all friends who\
are online.

## <sub>GetPersonaName</sub>

`Steam.GetPersonaName():` <mark style="color:purple;">**`string`**</mark>

Returns the local players name. This is the same name as on the users community profile page.

## <sub>GetGameLanguage</sub>

`Steam.GetGameLanguage():` <mark style="color:purple;">**`string`**</mark>

Returns the current game language.

## <sub>GetProfilePictureBySteamId</sub>

{% hint style="info" %}
This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.
{% endhint %}

`Steam.GetProfilePictureBySteamId(steamID64, [large]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                        | Type                                             | Description                                                 |
| ----------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| **steamID64**                                               | <mark style="color:purple;">**`integer`**</mark> | The Steam ID of the player                                  |
| **large&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Whether to get the large profile picture `(default: false)` |

Returns the handle of the profile picture of the given Steam ID.

## <sub>GetProfilePictureByAccountId</sub>

{% hint style="info" %}
This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.
{% endhint %}

\`Steam.GetProfilePictureByAccountId(steamID64, \[large]):\` <mark style="color:purple;">\*\*\`integer\`\*\*</mark>

| Name                                                        | Type                                             | Description                                                 |
| ----------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| **steamID64**                                               | <mark style="color:purple;">**`integer`**</mark> | The account id of the player                                |
| **large&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Whether to get the large profile picture `(default: false)` |

Returns the handle of the profile picture of the given account id.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel -->

# NetChannel

Table to work with game's net channel.

## <sub>GetLatency</sub>

`NetChannel.GetLatency([flow]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                       | Type                                                                                                                                | Description                                                 |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **flow&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.Flow`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.flow) | flow to get latency of `(default: Enum.Flow.FLOW_OUTGOING)` |

Returns the latency/ping of the net channel in seconds.

## <sub>GetAvgLatency</sub>

`NetChannel.GetAvgLatency([flow]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                       | Type                                                                                                                                | Description                                                         |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **flow&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.Flow`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.flow) | flow to get average latency of `(default: Enum.Flow.FLOW_OUTGOING)` |

Returns the average latency/ping of the net channel in seconds.

## <sub>SendNetMessage</sub>

{% hint style="info" %}
You can repeat the same message from OnSendNetMessage if you want to know the format of the message.
{% endhint %}

\`NetChannel.SendNetMessage(name, json):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name     | Type                                            | Description             |
| -------- | ----------------------------------------------- | ----------------------- |
| **name** | <mark style="color:purple;">**`string`**</mark> | name of the net message |
| **json** | <mark style="color:purple;">**`string`**</mark> | json of the net message |

Sends a protobuff message to the game server. [List of messages](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs),

#### Example

```lua
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

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/gc -->

# Game Coordinator

Table to work with Game Coordinator (GC).

Possible message types and message bodies could be found at [here](https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/Protobufs)\
Message type id starts with `k_E` prefix, for example `k_EMsgGCMatchmakingStatsRequest = 7197;`.\
Message body starts with with `C` prefix instead of "k\_E", for example `message CMsgDOTAMatchmakingStatsRequest {}`.

## <sub>SendMessage</sub>

`GC.SendMessage(msg, msg_type, msg_size):` <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                              | Description                         |
| ------------- | ------------------------------------------------- | ----------------------------------- |
| **msg**       | <mark style="color:purple;">**`userdata`**</mark> | Pointer to protobuf message buffer. |
| **msg\_type** | <mark style="color:purple;">**`integer`**</mark>  | Protobuf message type ID.           |
| **msg\_size** | <mark style="color:purple;">**`integer`**</mark>  | Size of the protobuf message.       |

Sends protobuff message to game coordinator. Response will be received in `OnGCMessage` callback.

#### Example

```lua
local protobuf = require('protobuf')
local JSON = require('assets.JSON')
local request = protobuf.encodeFromJSON('CMsgDOTAMatchmakingStatsRequest',
	                JSON:encode({}));
GC.SendMessage( request.binary, 7197, request.size )
```

## <sub>GetSteamID</sub>

`GC.GetSteamID():` <mark style="color:purple;">**`string`**</mark>

Returns local player Steam ID as string.


--------------------------------------------------------------------------------

## Rendering and Visuals

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals -->

# Rendering & Visuals

- [Particle](/api-v2.0/game-components/rendering-and-visuals/particle.md)
- [Renderer](/api-v2.0/game-components/rendering-and-visuals/renderv1.md)
- [Render](/api-v2.0/game-components/rendering-and-visuals/renderv2.md)
- [MiniMap](/api-v2.0/game-components/rendering-and-visuals/minimap.md)
- [Panorama](/api-v2.0/game-components/rendering-and-visuals/panorama.md)
- [Panorama](/api-v2.0/game-components/rendering-and-visuals/panorama/panorama.md)
- [UIPanel](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle -->

# Particle

Table to work with particles.

## <sub>Create</sub>

`Particle.Create(particle, [attach_type], [entity]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                               | Type                                                                                                                                                            | Description                                                                                                   |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **particle**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                                                                 | Particle path                                                                                                 |
| **attach\_type&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment) | attach\_type Attach type `(default: Enum.ParticleAttachment.PATTACH_WORLDORIGIN)`                             |
| **entity&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                                              | Entity to own of the particle. If not specified, the local hero will be used. `(default: Players.GetLocal())` |

Creates a particle and returns its index.

## <sub>SetControlPoint</sub>

`Particle.SetControlPoint(particle_index, control_point, value):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                                                                                                                 | Description         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | Particle index      |
| **control\_point**  | <mark style="color:purple;">**`integer`**</mark>                                                                                     | Control point       |
| **value**           | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Control point value |

Sets the control point value of a particle.

## <sub>SetShouldDraw</sub>

`Particle.SetShouldDraw(particle_index, value):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                             | Description    |
| ------------------- | ------------------------------------------------ | -------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark> | Particle index |
| **value**           | <mark style="color:purple;">**`bool`**</mark>    | set value      |

Enables or disables the drawing of a particle.

## <sub>SetControlPointEnt</sub>

`Particle.SetControlPointEnt(particle_index, control_point, entity, attach_type, attach_name, position, lock_orientation):` <mark style="color:purple;">**`nil`**</mark>

| Name                  | Type                                                                                                                                                            | Description                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **particle\_index**   | <mark style="color:purple;">**`integer`**</mark>                                                                                                                | Particle index                                |
| **control\_point**    | <mark style="color:purple;">**`integer`**</mark>                                                                                                                | Control point                                 |
| **entity**            | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)                                              | Entity to attach                              |
| **attach\_type**      | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment) | Attach type                                   |
| **attach\_name**      | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                                                 | Attach name. See `NPC.GetAttachment` function |
| **position**          | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)                            | Control point position                        |
| **lock\_orientation** | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                | Lock orientation. No idea what it does        |

Sets the control point entity value of a particle.

## <sub>SetParticleControlTransform</sub>

`Particle.SetParticleControlTransform(particle_index, control_point, position, angle):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                                                                                                                 | Description            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark>                                                                                     | Particle index         |
| **control\_point**  | <mark style="color:purple;">**`integer`**</mark>                                                                                     | Control point          |
| **position**        | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | Control point position |
| **angle**           | [<mark style="color:purple;">**`Angle`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)   | Control point angle    |

Sets the control point's position and angle.

## <sub>Destroy</sub>

`Particle.Destroy(particle_index):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                             | Description    |
| ------------------- | ------------------------------------------------ | -------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark> | Particle index |

Destroys the particle by index.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1 -->

# Renderer

Table to work with renderer.

## <sub>SetDrawColor</sub>

`Renderer.SetDrawColor([r], [g], [b], [a]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                    | Type                                             | Description                   |
| ------------------------------------------------------- | ------------------------------------------------ | ----------------------------- |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | Red color. `(default: 255)`   |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | Green color. `(default: 255)` |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | Blue color. `(default: 255)`  |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | Alpha color. `(default: 255)` |

Sets the color of the renderer.

## <sub>DrawLine</sub>

`Renderer.DrawLine(x0, y0, x1, y1):` <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                             | Description                       |
| ------ | ------------------------------------------------ | --------------------------------- |
| **x0** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the first point.  |
| **y0** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the first point.  |
| **x1** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the second point. |
| **y1** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the second point. |

Draws a line.

## <sub>DrawPolyLine</sub>

`Renderer.DrawPolyLine(points):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                           | Description      |
| ---------- | ---------------------------------------------- | ---------------- |
| **points** | <mark style="color:purple;">**`table`**</mark> | Table of points. |

Draws a polyline.

## <sub>DrawPolyLineFilled</sub>

`Renderer.DrawPolyLineFilled(points):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                           | Description      |
| ---------- | ---------------------------------------------- | ---------------- |
| **points** | <mark style="color:purple;">**`table`**</mark> | Table of points. |

Draws a filled polyline.

## <sub>DrawFilledRect</sub>

`Renderer.DrawFilledRect(x, y, w, h):` <mark style="color:purple;">**`nil`**</mark>

| Name  | Type                                             | Description                    |
| ----- | ------------------------------------------------ | ------------------------------ |
| **x** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **w** | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.        |
| **h** | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.       |

Draws a filled rectangle.

## <sub>DrawOutlineRect</sub>

`Renderer.DrawOutlineRect(x, y, w, h):` <mark style="color:purple;">**`nil`**</mark>

| Name  | Type                                             | Description                    |
| ----- | ------------------------------------------------ | ------------------------------ |
| **x** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **w** | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.        |
| **h** | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.       |

Draws an outlined rectangle.

## <sub>DrawOutlineCircle</sub>

`Renderer.DrawOutlineCircle(x, y, r, s):` <mark style="color:purple;">**`nil`**</mark>

| Name  | Type                                             | Description                 |
| ----- | ------------------------------------------------ | --------------------------- |
| **x** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the circle. |
| **y** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the circle. |
| **r** | <mark style="color:purple;">**`integer`**</mark> | Radius of the circle.       |
| **s** | <mark style="color:purple;">**`integer`**</mark> | Segments of the circle.     |

Draws an outlined circle.

## <sub>DrawFilledCircle</sub>

`Renderer.DrawFilledCircle(x, y, r):` <mark style="color:purple;">**`nil`**</mark>

| Name  | Type                                             | Description                 |
| ----- | ------------------------------------------------ | --------------------------- |
| **x** | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the circle. |
| **y** | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the circle. |
| **r** | <mark style="color:purple;">**`integer`**</mark> | Radius of the circle.       |

Draws a filled circle.

## <sub>DrawOutlineRoundedRect</sub>

`Renderer.DrawOutlineRoundedRect(x, y, w, h, radius):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description                    |
| ---------- | ------------------------------------------------ | ------------------------------ |
| **x**      | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y**      | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **w**      | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.        |
| **h**      | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.       |
| **radius** | <mark style="color:purple;">**`integer`**</mark> | Radius of the rectangle.       |

Draws an outlined rounded rectangle.

## <sub>DrawFilledRoundedRect</sub>

`Renderer.DrawFilledRoundedRect(x, y, w, h, radius):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description                    |
| ---------- | ------------------------------------------------ | ------------------------------ |
| **x**      | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y**      | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **w**      | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.        |
| **h**      | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.       |
| **radius** | <mark style="color:purple;">**`integer`**</mark> | Radius of the rectangle.       |

Draws a filled rounded rectangle.

## <sub>DrawOutlineTriangle</sub>

`Renderer.DrawOutlineTriangle(points):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                           | Description      |
| ---------- | ---------------------------------------------- | ---------------- |
| **points** | <mark style="color:purple;">**`table`**</mark> | Table of points. |

Draws an outlined triangle.

## <sub>DrawFilledTriangle</sub>

`Renderer.DrawFilledTriangle(points):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                           | Description      |
| ---------- | ---------------------------------------------- | ---------------- |
| **points** | <mark style="color:purple;">**`table`**</mark> | Table of points. |

Draws a filled triangle.

## <sub>DrawTexturedPolygon</sub>

`Renderer.DrawTexturedPolygon(points, texture):` <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                             | Description      |
| ----------- | ------------------------------------------------ | ---------------- |
| **points**  | <mark style="color:purple;">**`table`**</mark>   | Table of points. |
| **texture** | <mark style="color:purple;">**`integer`**</mark> | Texture handle.  |

Draws a textured polygon.

## <sub>LoadFont</sub>

`Renderer.LoadFont(name, size, flags, weight):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                             | Description       |
| ---------- | ------------------------------------------------ | ----------------- |
| **name**   | <mark style="color:purple;">**`string`**</mark>  | Name of the font. |
| **size**   | <mark style="color:purple;">**`integer`**</mark> | Size of the font. |
| **flags**  | <mark style="color:purple;">**`integer`**</mark> | Font flags.       |
| **weight** | <mark style="color:purple;">**`integer`**</mark> | Font weight.      |

Loads a font.

## <sub>DrawText</sub>

`Renderer.DrawText(font, x, y, text):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                             | Description               |
| -------- | ------------------------------------------------ | ------------------------- |
| **font** | <mark style="color:purple;">**`integer`**</mark> | Font handle.              |
| **x**    | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the text. |
| **y**    | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the text. |
| **text** | <mark style="color:purple;">**`string`**</mark>  | Text to draw.             |

Draws a text.

## <sub>WorldToScreen</sub>

`Renderer.WorldToScreen(pos):` <mark style="color:purple;">**`integer`**</mark>, <mark style="color:purple;">**`integer`**</mark>, <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                                                 | Description        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | World coordinates. |

Converts world coordinates to screen coordinates. Returns x, y and visible.

## <sub>GetScreenSize</sub>

`Renderer.GetScreenSize():` <mark style="color:purple;">**`integer`**</mark>, <mark style="color:purple;">**`integer`**</mark>

Returns screen size.

## <sub>GetTextSize</sub>

`Renderer.GetTextSize(font, text):` <mark style="color:purple;">**`integer`**</mark>, <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                             | Description      |
| -------- | ------------------------------------------------ | ---------------- |
| **font** | <mark style="color:purple;">**`integer`**</mark> | Font handle.     |
| **text** | <mark style="color:purple;">**`string`**</mark>  | Text to measure. |

Returns text size.

## <sub>LoadImage</sub>

`Renderer.LoadImage(path):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                            | Description        |
| -------- | ----------------------------------------------- | ------------------ |
| **path** | <mark style="color:purple;">**`string`**</mark> | Path to the image. |

Loads an image. Returns image handle.

## <sub>DrawImage</sub>

`Renderer.DrawImage(handle, x, y, w, h):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description                |
| ---------- | ------------------------------------------------ | -------------------------- |
| **handle** | <mark style="color:purple;">**`integer`**</mark> | Image handle.              |
| **x**      | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the image. |
| **y**      | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the image. |
| **w**      | <mark style="color:purple;">**`integer`**</mark> | Width of the image.        |
| **h**      | <mark style="color:purple;">**`integer`**</mark> | Height of the image.       |

Draws an image.

## <sub>DrawImageCentered</sub>

`Renderer.DrawImageCentered(handle, x, y, w, h):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description                |
| ---------- | ------------------------------------------------ | -------------------------- |
| **handle** | <mark style="color:purple;">**`integer`**</mark> | Image handle.              |
| **x**      | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the image. |
| **y**      | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the image. |
| **w**      | <mark style="color:purple;">**`integer`**</mark> | Width of the image.        |
| **h**      | <mark style="color:purple;">**`integer`**</mark> | Height of the image.       |

Draws an image centered.

## <sub>GetImageSize</sub>

`Renderer.GetImageSize(handle):` <mark style="color:purple;">**`integer`**</mark>, <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                             | Description   |
| ---------- | ------------------------------------------------ | ------------- |
| **handle** | <mark style="color:purple;">**`integer`**</mark> | Image handle. |

Returns image size.

## <sub>DrawFilledRectFade</sub>

`Renderer.DrawFilledRectFade(x0, y0, x1, y1, alpha0, alpha1, bHorizontal):` <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                             | Description                    |
| --------------- | ------------------------------------------------ | ------------------------------ |
| **x0**          | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y0**          | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **x1**          | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y1**          | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **alpha0**      | <mark style="color:purple;">**`integer`**</mark> | Alpha of the first point.      |
| **alpha1**      | <mark style="color:purple;">**`integer`**</mark> | Alpha of the second point.     |
| **bHorizontal** | <mark style="color:purple;">**`boolean`**</mark> | Horizontal fade.               |

Draws a filled rectangle with fade.

## <sub>DrawFilledGradRect</sub>

`Renderer.DrawFilledGradRect(x0, y0, x1, y1, r, g, b, a, r2, g2, b2, a2, bHorizontal):` <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                             | Description                      |
| --------------- | ------------------------------------------------ | -------------------------------- |
| **x0**          | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle.   |
| **y0**          | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle.   |
| **x1**          | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle.   |
| **y1**          | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle.   |
| **r**           | <mark style="color:purple;">**`integer`**</mark> | Red color of the first point.    |
| **g**           | <mark style="color:purple;">**`integer`**</mark> | Green color of the first point.  |
| **b**           | <mark style="color:purple;">**`integer`**</mark> | Blue color of the first point.   |
| **a**           | <mark style="color:purple;">**`integer`**</mark> | Alpha color of the first point.  |
| **r2**          | <mark style="color:purple;">**`integer`**</mark> | Red color of the second point.   |
| **g2**          | <mark style="color:purple;">**`integer`**</mark> | Green color of the second point. |
| **b2**          | <mark style="color:purple;">**`integer`**</mark> | Blue color of the second point.  |
| **a2**          | <mark style="color:purple;">**`integer`**</mark> | Alpha color of the second point. |
| **bHorizontal** | <mark style="color:purple;">**`boolean`**</mark> | Horizontal gradient.             |

Draws a filled gradient rectangle.

## <sub>DrawGlow</sub>

`Renderer.DrawGlow(x0, y0, w, h, thickness, obj_rounding):` <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                             | Description                    |
| ----------------- | ------------------------------------------------ | ------------------------------ |
| **x0**            | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle. |
| **y0**            | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle. |
| **w**             | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.        |
| **h**             | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.       |
| **thickness**     | <mark style="color:purple;">**`integer`**</mark> | Thickness of the glow.         |
| **obj\_rounding** | <mark style="color:purple;">**`integer`**</mark> | Rounding of the glow.          |

Draws a glow.

## <sub>DrawBlur</sub>

`Renderer.DrawBlur(x0, y0, w, h, strength, rounding, alpha):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                            | Description                    |
| ------------ | ----------------------------------------------- | ------------------------------ |
| **x0**       | <mark style="color:purple;">**`number`**</mark> | X coordinate of the rectangle. |
| **y0**       | <mark style="color:purple;">**`number`**</mark> | Y coordinate of the rectangle. |
| **w**        | <mark style="color:purple;">**`number`**</mark> | Width of the rectangle.        |
| **h**        | <mark style="color:purple;">**`number`**</mark> | Height of the rectangle.       |
| **strength** | <mark style="color:purple;">**`number`**</mark> | Strength of the blur.          |
| **rounding** | <mark style="color:purple;">**`number`**</mark> | Rounding of the blur.          |
| **alpha**    | <mark style="color:purple;">**`number`**</mark> | Alpha of the blur.             |

Draws a blur.

## <sub>PushClip</sub>

`Renderer.PushClip(x, y, w, h, intersect):` <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                             | Description                       |
| ------------- | ------------------------------------------------ | --------------------------------- |
| **x**         | <mark style="color:purple;">**`integer`**</mark> | X coordinate of the rectangle.    |
| **y**         | <mark style="color:purple;">**`integer`**</mark> | Y coordinate of the rectangle.    |
| **w**         | <mark style="color:purple;">**`integer`**</mark> | Width of the rectangle.           |
| **h**         | <mark style="color:purple;">**`integer`**</mark> | Height of the rectangle.          |
| **intersect** | <mark style="color:purple;">**`boolean`**</mark> | Intersect with the previous clip. |

Pushes a clip rect.

## <sub>PopClip</sub>

`Renderer.PopClip():` <mark style="color:purple;">**`nil`**</mark>

Pops a clip rect.

## <sub>DrawCenteredNotification</sub>

`Renderer.DrawCenteredNotification(text, duration):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                            | Description                   |
| ------------ | ----------------------------------------------- | ----------------------------- |
| **text**     | <mark style="color:purple;">**`string`**</mark> | Text to draw.                 |
| **duration** | <mark style="color:purple;">**`number`**</mark> | Duration of the notification. |

Draws a centered notification.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2 -->

# Render

Table to work with render v2.

## <sub>FilledRect</sub>

`Render.FilledRect(start, end_, color, [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                          | Description                                                    |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the rectangle.                           |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the rectangle.                             |
| **color**                                                      | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the rectangle.                                    |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |

Draws a filled rectangle.

## <sub>Rect</sub>

`Render.Rect(start, end_, color, [rounding], [flags], [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                          | Description                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the rectangle.                           |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the rectangle.                             |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the rectangle's border.                           |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the rectangle's border. `(default: 1.0)`      |

Draws an unfilled rectangle.

## <sub>RoundedProgressRect</sub>

`Render.RoundedProgressRect(start, end_, color, percent, rounding, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                             | Description                                               |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The starting point of the rectangle.                      |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The ending point of the rectangle.                        |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The color of the rectangle.                               |
| **percent**                                                     | <mark style="color:purple;">**`number`**</mark>                                                                                  | The percentage of the rectangle to fill \[0..1].          |
| **rounding**                                                    | <mark style="color:purple;">**`number`**</mark>                                                                                  | The rounding radius of the rectangle corners.             |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                  | The thickness of the rectangle's border. `(default: 1.0)` |

Draw a progress rectangle.

## <sub>Line</sub>

`Render.Line(start, end_, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                             | Description                                 |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The starting point of the line.             |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The ending point of the line.               |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The color of the line.                      |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                  | The thickness of the line. `(default: 1.0)` |

Draws a line between two points.

## <sub>PolyLine</sub>

`Render.PolyLine(points, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                               | Description                                     |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vec2[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | A table of Vec2 points to connect with lines.   |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)      | The color of the polyline.                      |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                    | The thickness of the polyline. `(default: 1.0)` |

Draws a series of connected lines (polyline).

## <sub>Circle</sub>

`Render.Circle(pos, radius, color, [thickness], [startDeg], [percentage], [rounded], [segments]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                                             | Description                                                                                                          |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                  | The radius of the circle.                                                                                            |
| **color**                                                        | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The color of the circle.                                                                                             |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                  | The thickness of the circle's outline. `(default: 1.0)`                                                              |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                                                  | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                  | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |
| **rounded&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`boolean`**</mark>                                                                                 | Whether the circle is rounded. `(default: false)`                                                                    |
| **segments&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                                                 | The number of segments used for drawing the circle. `(default: 32)`                                                  |

Draws a circle.

## <sub>FilledCircle</sub>

`Render.FilledCircle(pos, radius, color, [startDeg], [percentage], [segments]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                                             | Description                                                                                                          |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                  | The radius of the circle.                                                                                            |
| **color**                                                        | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The color of the circle.                                                                                             |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                                                  | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                  | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |
| **segments&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                                                 | The number of segments used for drawing the circle. `(default: 32)`                                                  |

Draws a filled circle.

## <sub>CircleGradient</sub>

`Render.CircleGradient(pos, radius, colorOuter, colorInner, [startDeg], [percentage]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                                             | Description                                                                                                          |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                  | The radius of the circle.                                                                                            |
| **colorOuter**                                                   | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The outer color of the gradient.                                                                                     |
| **colorInner**                                                   | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The inner color of the gradient.                                                                                     |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                                                  | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                  | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |

Draws a circle with a gradient.

## <sub>Triangle</sub>

`Render.Triangle(points, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                               | Description                                                         |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vec2[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | A table of three Vec2 points defining the vertices of the triangle. |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)      | The color of the triangle's outline.                                |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                    | The thickness of the triangle's outline. `(default: 1.0)`           |

Draws a triangle outline.

## <sub>FilledTriangle</sub>

`Render.FilledTriangle(points, color):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                                               | Description                                                         |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **points** | [<mark style="color:purple;">**`Vec2[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | A table of three Vec2 points defining the vertices of the triangle. |
| **color**  | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)      | The color of the triangle.                                          |

Draws a filled triangle.

## <sub>TexturedPoly</sub>

`Render.TexturedPoly(points, textureHandle, color, [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                   | Description                                                                                                                            |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vertex[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex) | A table of Vertex points defining the vertices of the polygon. Each Vertex contains a position (Vec2) and a texture coordinate (Vec2). |
| **textureHandle**                                               | <mark style="color:purple;">**`integer`**</mark>                                                                                       | The handle to the texture to be applied to the polygon.                                                                                |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)          | The color to apply over the texture. This can be used to tint the texture.                                                             |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                        | The grayscale of the image. `(default: 0.0)`                                                                                           |

Draws a textured polygon.

## <sub>LoadFont</sub>

`Render.LoadFont(fontName, [fontFlag], [weight]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                           | Type                                                                                                                                                                                                | Description                                                                               |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **fontName**                                                   | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                     | The name of the font to load.                                                             |
| **fontFlag&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.FontCreate`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.fontcreate) \| <mark style="color:purple;">**`integer`**</mark> | Flags for font creation, such as antialiasing. `(default: Enum.FontCreate.FONTFLAG_NONE)` |
| **weight&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                                    | The weight (thickness) of the font. Typically, 0 means default weight. `(default: 400)`   |

Loads a font and returns its handle. Returns handle to the loaded font.

## <sub>Text</sub>

`Render.Text(font, fontSize, text, pos, color):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                             | Description                                       |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **font**     | <mark style="color:purple;">**`integer`**</mark>                                                                                 | The handle to the font used for drawing the text. |
| **fontSize** | <mark style="color:purple;">**`number`**</mark>                                                                                  | The size of the font.                             |
| **text**     | <mark style="color:purple;">**`string`**</mark>                                                                                  | The text to be drawn.                             |
| **pos**      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The position where the text will be drawn.        |
| **color**    | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)    | The color of the text.                            |

Draws text at a specified position.

## <sub>WorldToScreen</sub>

`Render.WorldToScreen(pos):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2), <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                                                 | Description                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | The 3D world position to be converted. |

Converts a 3D world position to a 2D screen position. Returns A Vec2 representing the 2D screen position and a boolean indicating visibility on the screen.

#### Example

```lua
-- Example: Convert the center of the map (0,0,0) to screen coordinates.
local worldPos = Vector(0.0, 0.0, 0.0)
local screenPos, isVisible = Render.WorldToScreen(worldPos)
if isVisible then
    Log.Write("Screen Position: " .. screenPos.x .. ", " .. screenPos.y)
else
    Log.Write("Position is not visible on the screen")
end
```

## <sub>ScreenSize</sub>

`Render.ScreenSize():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Retrieves the current screen size, returning it as a Vec2 where x is the width and y is the height of the screen.

## <sub>TextSize</sub>

`Render.TextSize(font, fontSize, text):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

| Name         | Type                                             | Description                                         |
| ------------ | ------------------------------------------------ | --------------------------------------------------- |
| **font**     | <mark style="color:purple;">**`integer`**</mark> | The handle to the font used for measuring the text. |
| **fontSize** | <mark style="color:purple;">**`number`**</mark>  | The size of the font.                               |
| **text**     | <mark style="color:purple;">**`string`**</mark>  | The text to measure.                                |

Calculates the size of the given text using the specified font, returning the size as a Vec2 where x is the width and y is the height of the text.

## <sub>LoadImage</sub>

`Render.LoadImage(path):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                            | Description        |
| -------- | ----------------------------------------------- | ------------------ |
| **path** | <mark style="color:purple;">**`string`**</mark> | Path to the image. |

Loads an image and returns its handle.

## <sub>Image</sub>

`Render.Image(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                          | Description                                                             |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **imageHandle**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                                              | The handle to the image.                                                |
| **pos**                                                         | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The position to draw the image.                                         |
| **size**                                                        | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The size of the image.                                                  |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color to tint the image.                                            |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the image corners. `(default: 0.0)`              |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`              |
| **uvMin&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})` |
| **uvMax&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})` |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The grayscale of the image. `(default: 0.0)`                            |

Draws an image at a specified position and size.

## <sub>ImageCentered</sub>

`Render.ImageCentered(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                          | Description                                                             |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **imageHandle**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                                              | The handle to the image.                                                |
| **pos**                                                         | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The center position to draw the image.                                  |
| **size**                                                        | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The size of the image.                                                  |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color to tint the image.                                            |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the image corners. `(default: 0.0)`              |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`              |
| **uvMin&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})` |
| **uvMax&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})` |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The grayscale of the image. `(default: 0.0)`                            |

Draws an image centered at a specified position and size.

## <sub>ImageSize</sub>

`Render.ImageSize(imageHandle):` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

| Name            | Type                                             | Description              |
| --------------- | ------------------------------------------------ | ------------------------ |
| **imageHandle** | <mark style="color:purple;">**`integer`**</mark> | The handle to the image. |

Retrieves the size of an image. Returns the size of the image as a Vec2.

## <sub>OutlineGradient</sub>

`Render.OutlineGradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags], [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                          | Description                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the gradient rectangle.                  |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the gradient rectangle.                    |
| **topLeft**                                                     | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the top-left corner.                              |
| **topRight**                                                    | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the top-right corner.                             |
| **bottomLeft**                                                  | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the bottom-left corner.                           |
| **bottomRight**                                                 | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the bottom-right corner.                          |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the outline. `(default: 1.0)`                 |

Draws a outlined gradient rectangle.

## <sub>Gradient</sub>

`Render.Gradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                          | Description                                                    |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the gradient rectangle.                  |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the gradient rectangle.                    |
| **topLeft**                                                    | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the top-left corner.                              |
| **topRight**                                                   | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the top-right corner.                             |
| **bottomLeft**                                                 | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the bottom-left corner.                           |
| **bottomRight**                                                | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the bottom-right corner.                          |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |

Draws a filled gradient rectangle.

## <sub>Shadow</sub>

`Render.Shadow(start, end_, color, thickness, [obj_rounding], [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **start**                                                           | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the shadow rectangle.                                                  |
| **end\_**                                                           | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the shadow rectangle.                                                    |
| **color**                                                           | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the shadow.                                                                     |
| **thickness**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the shadow.                                                                 |
| **obj\_rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the shadow rectangle corners. `(default: 0.0)`                        |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark>        | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The offset of the shadow from the original rectangle. `(default: {0.0, 0.0})`                |

Draws a shadow effect within a specified rectangular area.

## <sub>ShadowCircle</sub>

`Render.ShadowCircle(center, radius, color, thickness, [num_segments], [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **center**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The center point of the circle.                                                              |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                               | The radius of the circle.                                                                    |
| **color**                                                           | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the shadow.                                                                     |
| **thickness**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the shadow.                                                                 |
| **num\_segments&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>                                                                                              | The number of segments for drawing the circle. `(default: 12)`                               |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark>        | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The offset of the shadow from the circle. `(default: {0.0, 0.0})`                            |

Draws a circle shadow effect.

## <sub>ShadowConvexPoly</sub>

`Render.ShadowConvexPoly(points, color, thickness, [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **points**                                                   | [<mark style="color:purple;">**`Vec2[]`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)            | Table of Vec2 points defining the convex polygon. Should be more than 2 points.              |
| **color**                                                    | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the shadow.                                                                     |
| **thickness**                                                | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the shadow.                                                                 |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The offset of the shadow from the polygon. `(default: {0.0, 0.0})`                           |

Draws a shadow convex polygon effect.

## <sub>ShadowNGon</sub>

`Render.ShadowNGon(center, radius, color, thickness, num_segments, [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **center**                                                   | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The center point of the n-gon.                                                               |
| **radius**                                                   | <mark style="color:purple;">**`number`**</mark>                                                                                               | The radius of the n-gon.                                                                     |
| **color**                                                    | [<mark style="color:purple;">**`Color`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)                 | The color of the shadow.                                                                     |
| **thickness**                                                | <mark style="color:purple;">**`number`**</mark>                                                                                               | The thickness of the shadow.                                                                 |
| **num\_segments**                                            | <mark style="color:purple;">**`integer`**</mark>                                                                                              | The number of segments (sides) of the n-gon.                                                 |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The offset of the shadow from the n-gon. `(default: {0.0, 0.0})`                             |

Draws a shadow n-gon (polygon with n sides) effect.

## <sub>Blur</sub>

`Render.Blur(start, end_, [strength], [alpha], [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                          | Description                                                         |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The starting point of the blur rectangle.                           |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)              | The ending point of the blur rectangle.                             |
| **strength&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The strength of the blur effect. `(default: 1.0)`                   |
| **alpha&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`number`**</mark>                                                                                               | The alpha value of the blur effect. `(default: 1.0)`                |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                               | The rounding radius of the blur rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags) | Custom flags for the blur effect. `(default: Enum.DrawFlags.None)`  |

Applies a blur effect within a specified rectangular area.

## <sub>PushClip</sub>

`Render.PushClip(start, end_, [intersect]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                             | Description                                                                                      |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The starting point of the clipping rectangle.                                                    |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) | The ending point of the clipping rectangle.                                                      |
| **intersect&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                 | If true, the new clipping area is intersected with the current clipping area. `(default: false)` |

Begins a new clipping region. Only the rendering within the specified rectangular area will be displayed.

## <sub>PopClip</sub>

`Render.PopClip():` <mark style="color:purple;">**`nil`**</mark>

Ends the most recently begun clipping region, restoring the previous clipping region.

## <sub>StartRotation</sub>

`Render.StartRotation(angle):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description         |
| --------- | ----------------------------------------------- | ------------------- |
| **angle** | <mark style="color:purple;">**`number`**</mark> | The rotation angle. |

Begins a new rotation.

## <sub>StopRotation</sub>

`Render.StopRotation():` <mark style="color:purple;">**`nil`**</mark>

End the rotation.

## <sub>SetGlobalAlpha</sub>

{% hint style="info" %}
Do not forget to reset the global alpha value after your rendering.
{% endhint %}

\`Render.SetGlobalAlpha(alpha):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name      | Type                                            | Description                    |
| --------- | ----------------------------------------------- | ------------------------------ |
| **alpha** | <mark style="color:purple;">**`number`**</mark> | The alpha value to set \[0..1] |

Set the global alpha value for rendering.

## <sub>ResetGlobalAlpha</sub>

`Render.ResetGlobalAlpha():` <mark style="color:purple;">**`nil`**</mark>

Reset the global alpha value for rendering to 1.0.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/minimap -->

# MiniMap

Table to work with in-game minimap.

## <sub>Ping</sub>

`MiniMap.Ping(pos, type):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                                                                        | Description            |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **pos**  | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)        | world position to ping |
| **type** | [<mark style="color:purple;">**`Enum.PingType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.pingtype) | ping type              |

Pings on the minimap.

## <sub>SendLine</sub>

`MiniMap.SendLine(pos, initial, clientside):` <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                                                                                                                 | Description                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| **pos**        | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | world position to draw line to                    |
| **initial**    | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | start a new line, otherwise continue the last one |
| **clientside** | <mark style="color:purple;">**`boolean`**</mark>                                                                                     | draw only for local player                        |

Draws a line on the minimap.

## <sub>SendLine</sub>

`MiniMap.SendLine(x, y, initial, clientside):` <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                             | Description                                       |
| -------------- | ------------------------------------------------ | ------------------------------------------------- |
| **x**          | <mark style="color:purple;">**`number`**</mark>  | x world position to draw line                     |
| **y**          | <mark style="color:purple;">**`number`**</mark>  | y world position to draw line                     |
| **initial**    | <mark style="color:purple;">**`boolean`**</mark> | start a new line, otherwise continue the last one |
| **clientside** | <mark style="color:purple;">**`boolean`**</mark> | draw only for local player                        |

Draws a line on the minimap.

## <sub>DrawCircle</sub>

`MiniMap.DrawCircle(pos, [r], [g], [b], [a], [size]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                       | Type                                                                                                                                 | Description                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | world position to draw circle |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | red color `(default: 255)`    |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | green color `(default: 255)`  |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | blue color `(default: 255)`   |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | alpha color `(default: 255)`  |
| **size&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                      | circle size `(default: 800)`  |

Draws a circle on the minimap.

## <sub>DrawHeroIcon</sub>

`MiniMap.DrawHeroIcon(unitName, pos, [r], [g], [b], [a], [size]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                       | Type                                                                                                                                 | Description                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **unitName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                                      | unit name to draw icon. Can get it from `NPC.GetUnitName` |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | world position to draw icon                               |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | red color `(default: 255)`                                |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | green color `(default: 255)`                              |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | blue color `(default: 255)`                               |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | alpha color `(default: 255)`                              |
| **size&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                      | icon size `(default: 800)`                                |

Draws a hero icon on the minimap.

## <sub>DrawIconByName</sub>

`MiniMap.DrawIconByName(iconName, pos, [r], [g], [b], [a], [size]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                       | Type                                                                                                                                 | Description                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **iconName**                                               | <mark style="color:purple;">**`string`**</mark>                                                                                      | could get it from game\dota\pak01\_dir.vpk (scripts\mod\_textures.txt). |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | world position to draw icon                                             |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | red color `(default: 255)`                                              |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | green color `(default: 255)`                                            |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | blue color `(default: 255)`                                             |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`integer`**</mark>                                                                                     | alpha color `(default: 255)`                                            |
| **size&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                      | icon size `(default: 800)`                                              |

Draws a icon on the minimap.

## <sub>GetMousePosInWorld</sub>

`MiniMap.GetMousePosInWorld():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns world position the mouse on the minimap, if the mouse is not on the minimap, it will return (0,0,0).

## <sub>IsCursorOnMinimap</sub>

`MiniMap.IsCursorOnMinimap():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the mouse is on the minimap.

## <sub>GetMinimapToWorld</sub>

`MiniMap.GetMinimapToWorld(ScreenX, ScreenY):` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

| Name        | Type                                             | Description |
| ----------- | ------------------------------------------------ | ----------- |
| **ScreenX** | <mark style="color:purple;">**`integer`**</mark> |             |
| **ScreenY** | <mark style="color:purple;">**`integer`**</mark> |             |

Returns world position from minimap position. The same as `GetMousePosInWorld`, but you can pass any position on screen, not only mouse position.


--------------------------------------------------------------------------------

### Rendering - Panorama UI

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama -->

# Panorama

- [Panorama](/api-v2.0/game-components/rendering-and-visuals/panorama/panorama.md)
- [UIPanel](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama -->

# Panorama

Table to work with Dota Panorama system.

## <sub>GetPanelInfo</sub>

`Panorama.GetPanelInfo(path, [bLogError], [useJsFunc]):` <mark style="color:purple;">**`{x:number, y:number, w:number, h:number}`**</mark>

| Name                                                            | Type                                                                                             | Description                                                                 |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **path**                                                        | <mark style="color:purple;">**`string[]`**</mark>                                                | Path to the panel.                                                          |
| **bLogError&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> \| <mark style="color:purple;">**`nil`**</mark> | `(default: false)`                                                          |
| **useJsFunc&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> \| <mark style="color:purple;">**`nil`**</mark> | Use js GetPositionWithinWindow function to get position. `(default: false)` |

Get panel info. GetPanelByName for first argument then FindChild others and accumulate x and y.

## <sub>GetPanelByPath</sub>

`Panorama.GetPanelByPath(path, [bLogError]):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                              | Description                                      |
| --------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| **path**                                                        | <mark style="color:purple;">**`string[]`**</mark> | Path to the panel.                               |
| **bLogError&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>  | Log error if panel not found. `(default: false)` |

Get panel by path.

## <sub>GetPanelByName</sub>

`Panorama.GetPanelByName(id, is_type_name):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                             | Description                       |
| ------------------ | ------------------------------------------------ | --------------------------------- |
| **id**             | <mark style="color:purple;">**`string`**</mark>  | Id of the panel.                  |
| **is\_type\_name** | <mark style="color:purple;">**`boolean`**</mark> | Check type name instead of names. |

Get panel by id.

## <sub>CreatePanel</sub>

`Panorama.CreatePanel(type, id, parent, classes, styles):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

| Name        | Type                                                                                                                                          | Description                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **type**    | <mark style="color:purple;">**`string`**</mark>                                                                                               | panel type to create           |
| **id**      | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                               | id of the panel                |
| **parent**  | [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | parent panel                   |
| **classes** | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                               | space separated classes to add |
| **styles**  | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                               | styles to set                  |

Creates a new panorama panel

#### Example

```lua
-- create_panel.lua
function create_category()
	local panel = Panorama.GetPanelByPath({"DOTAHeroesPage", "HeroGrid", "Footer", "ViewModeControls", "Filters"}, true);
	if (not panel) then 
		print("not on hero grid page");
		return
	end;

	local filter_category = Panorama.CreatePanel("Panel", nil, panel, "FilterCategory")
	local filter_category_title = Panorama.CreatePanel("Label", nil, filter_category, "FilterCategoryTitle");
	filter_category_title:SetText("Filter");
	local items_panel = Panorama.CreatePanel("Panel", nil, filter_category, "FilterCategoryItems")
	items_panel:AddClasses("FilterCategoryItems")

	local button_styles = {
		["CrossButton"] = 'background-image: url("s2r://panorama/images/control_icons/purgatory_png.vtex");',
		["GearButton"] = 'background-image: url("s2r://panorama/images/control_icons/settings_png.vtex");',
	};
	local buttons = {}
	for id, style in pairs(button_styles) do
		buttons[id] = Panorama.CreatePanel("Button", id, items_panel, "FilterButton", style)
	end
	local button_id, button = next(buttons);

    -- set up the button events
	Engine.RunScript(([[
		(function(){
			let ctx = $.GetContextPanel();
			let button = ctx.FindChildTraverse("%s")
			let items_panel = button.GetParent();

			let children = items_panel.Children();
			let children_count = children.length;
			for (let i = 0; i < children_count; i++) {
				let item = children[i];
				item.SetPanelEvent("onmouseover", () => $.DispatchEvent("UIShowTextTooltipStyled", item, ("Button Id: " + item.id), "GameModeTooltip"));
				item.SetPanelEvent("onmouseout", () => $.DispatchEvent("UIHideTextTooltip", item));
				item.SetPanelEvent("onactivate", () => $.Msg(item.id + " was clicked!"));
			}
		})()
	]]):format(button_id), button)
end
create_category();
```

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel -->

# UIPanel

UIPanel metatable

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`nil`**</mark>

## <sub>\_\_eq</sub>

{% hint style="info" %}
Overload for operator ==.
{% endhint %}

`:__eq(other):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                                          | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) |             |

## <sub>FindChild</sub>

`:FindChild(id):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                            | Description      |
| ------ | ----------------------------------------------- | ---------------- |
| **id** | <mark style="color:purple;">**`string`**</mark> | id of the child. |

Finds child by name.

## <sub>IsVisible</sub>

`:IsVisible():` <mark style="color:purple;">**`boolean`**</mark>

Returns visible state.

## <sub>SetVisible</sub>

`:SetVisible(newState):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                             | Description |
| ------------ | ------------------------------------------------ | ----------- |
| **newState** | <mark style="color:purple;">**`boolean`**</mark> |             |

Sets visible state.

## <sub>GetClassList</sub>

`:GetClassList():` <mark style="color:purple;">**`string[]`**</mark>

Returns class name list.

## <sub>FindChildInLayoutFile</sub>

`:FindChildInLayoutFile(id):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                            | Description |
| ------ | ----------------------------------------------- | ----------- |
| **id** | <mark style="color:purple;">**`string`**</mark> |             |

???.

## <sub>FindPanelInLayoutFile</sub>

`:FindPanelInLayoutFile(id):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                            | Description |
| ------ | ----------------------------------------------- | ----------- |
| **id** | <mark style="color:purple;">**`string`**</mark> |             |

???.

## <sub>FindChildTraverse</sub>

`:FindChildTraverse(id):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                            | Description |
| ------ | ----------------------------------------------- | ----------- |
| **id** | <mark style="color:purple;">**`string`**</mark> |             |

Recursive find child by id.

## <sub>GetChildCount</sub>

`:GetChildCount():` <mark style="color:purple;">**`integer`**</mark>

Returns child by count.

## <sub>GetChild</sub>

`:GetChild(index):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **index** | <mark style="color:purple;">**`number`**</mark> |             |

Returns child by index.

## <sub>GetChildByPath</sub>

`:GetChildByPath(path, [bLogError]):` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                              | Description                                      |
| --------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| **path**                                                        | <mark style="color:purple;">**`string[]`**</mark> |                                                  |
| **bLogError&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>  | Log error if panel not found. `(default: false)` |

Returns child by path using FindChild.

## <sub>GetChildIndex</sub>

`:GetChildIndex():` <mark style="color:purple;">**`integer`**</mark>

Returns index in parent children list. Starts from 0.

## <sub>GetFirstChild</sub>

`:GetFirstChild():` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

Returns first child.

## <sub>GetLastChild</sub>

`:GetLastChild():` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

Returns last child.

## <sub>HasID</sub>

`:HasID():` <mark style="color:purple;">**`boolean`**</mark>

Returns `true` if the panel has an id.

## <sub>GetID</sub>

`:GetID():` <mark style="color:purple;">**`string`**</mark>

Returns id of panel.

## <sub>SetID</sub>

`:SetID(id):` <mark style="color:purple;">**`nil`**</mark>

| Name   | Type                                            | Description |
| ------ | ----------------------------------------------- | ----------- |
| **id** | <mark style="color:purple;">**`string`**</mark> |             |

Sets the panel's id.

## <sub>GetLayoutHeight</sub>

`:GetLayoutHeight():` <mark style="color:purple;">**`integer`**</mark>

Returns the panel height.

## <sub>GetLayoutWidth</sub>

`:GetLayoutWidth():` <mark style="color:purple;">**`integer`**</mark>

Returns the panel width.

## <sub>GetParent</sub>

`:GetParent():` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

Returns the panel's parent.

## <sub>GetRootParent</sub>

`:GetRootParent():` [<mark style="color:purple;">**`UIPanel`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) | <mark style="color:purple;">**`nil`**</mark>

Returns the panel's root parent. ???

## <sub>GetXOffset</sub>

`:GetXOffset():` <mark style="color:purple;">**`integer`**</mark>

Returns the panel's relative X offset.

## <sub>GetYOffset</sub>

`:GetYOffset():` <mark style="color:purple;">**`integer`**</mark>

Returns the panel's relative Y offset.

## <sub>GetBounds</sub>

`:GetBounds([useJsFunc]):` <mark style="color:purple;">**`{x:number, y:number, w:number, h:number}`**</mark>

| Name                                                            | Type                                                                                             | Description                                                                 |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **useJsFunc&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> \| <mark style="color:purple;">**`nil`**</mark> | Use js GetPositionWithinWindow function to get position. `(default: false)` |

Returns the panel's bounds. Iterate over the parent hierarchy to get the absolute bounds.

## <sub>GetImageSrc</sub>

`:GetImageSrc():` <mark style="color:purple;">**`string`**</mark>

Return the panel source image.

## <sub>GetPanelType</sub>

`:GetPanelType():` <mark style="color:purple;">**`string`**</mark>

Returns the panel's type.

## <sub>BSetProperty</sub>

`:BSetProperty(key, value):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **key**   | <mark style="color:purple;">**`string`**</mark> |             |
| **value** | <mark style="color:purple;">**`string`**</mark> |             |

Sets the panel property.

## <sub>SetStyle</sub>

`:SetStyle(cssString):` <mark style="color:purple;">**`boolean`**</mark>

| Name          | Type                                            | Description |
| ------------- | ----------------------------------------------- | ----------- |
| **cssString** | <mark style="color:purple;">**`string`**</mark> |             |

Sets the panel style.

#### Example

```lua
-- set_style.lua
local css_like_table = {
    ["horizontal-align"] = "center",
	["vertical-align"] = "center",
    ["transform"] = "translate3d( 0px, -0px, 0px ) scale3d(1, 1, 1)",
    ["padding-left"] = "0px",
    ["margin"] = "0px",
    ["border-radius"] = "4px",
    ["background-color"] = "none",
    ["box-shadow"] = "none",
    ["color"] = "gradient( linear, 0% 100%, 0% 0%, from( #ff00FF ), to( #5C9C68 ) )",
    ["font-size"] = "20px",
    ["text-align"] = "center",
    ["text-decoration"] = "none",
    ["background-size"] = "0% 0%",
    ["opacity-mask"] = 'url("s2r://panorama/images/masks/hudchat_mask_psd.vtex") 1.0',
    ["hue-rotation"] = "-10deg",
    ["text-shadow"] = "2px 2px #111111b0",
    ["blur"] = "gaussian(0px)",
    ["line-height"] = "120%",
    ["font-family"] = "Radiance",
    ["border-brush"] = "gradient( linear, 0% 0%, 0% 100%, from( #96c5ff96 ), to( #12142d2d ) )",
}


local function css_to_string(tbl)
    local str = ""
    for k, v in pairs(tbl) do
        str = str .. k .. ": " .. v .. "; "
    end
    return str;
end

local health_label = Panorama.GetPanelByName("HealthLabel");
if (health_label) then
    health_label:SetStyle(css_to_string(css_like_table))
end

```

## <sub>SetAttribute</sub>

`:SetAttribute(key, value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **key**   | <mark style="color:purple;">**`string`**</mark> |             |
| **value** | <mark style="color:purple;">**`string`**</mark> |             |

Sets the panel's attribute.

## <sub>GetAttribute</sub>

`:GetAttribute(key, default):` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **key**     | <mark style="color:purple;">**`string`**</mark> |             |
| **default** | <mark style="color:purple;">**`string`**</mark> |             |

Returns the panel's attribute.

## <sub>GetPositionWithinWindow</sub>

`:GetPositionWithinWindow():` [<mark style="color:purple;">**`Vec2`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns the panel's window position. Not sure about optimization.

## <sub>GetText</sub>

{% hint style="info" %}
This method is only available for Label panels.
{% endhint %}

`:GetText():` <mark style="color:purple;">**`string`**</mark>

Returns the label panel's text.

## <sub>SetText</sub>

{% hint style="info" %}
This method is only available for Label panels.
{% endhint %}

`:SetText(text):` <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                            | Description |
| -------- | ----------------------------------------------- | ----------- |
| **text** | <mark style="color:purple;">**`string`**</mark> |             |

Sets the label panel's text.

## <sub>GetTextType</sub>

{% hint style="info" %}
This method is only available for Label panels.
{% endhint %}

`:GetTextType():` <mark style="color:purple;">**`integer`**</mark>

Gets the label panel's text type. (2 = plain, 3 = html)

## <sub>SetTextType</sub>

{% hint style="info" %}
This method is only available for Label panels.
{% endhint %}

\`:SetTextType(new):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name    | Type                                             | Description |
| ------- | ------------------------------------------------ | ----------- |
| **new** | <mark style="color:purple;">**`integer`**</mark> | value       |

Sets the label panel's text type. (2 = plain, 3 = html). Should always set text type before setting the text

#### Example

```lua

label_panel:SetTextType(3)
label_panel:SetText("<font color='#8BFFD8'>Vitória</font>")
```

## <sub>IsValid</sub>

`:IsValid():` <mark style="color:purple;">**`boolean`**</mark>

Checks if the panel is valid

## <sub>HasClass</sub>

`:HasClass(className):` <mark style="color:purple;">**`boolean`**</mark>

| Name          | Type                                            | Description |
| ------------- | ----------------------------------------------- | ----------- |
| **className** | <mark style="color:purple;">**`string`**</mark> | Class name. |

Checks if the panel has a class.

## <sub>AddClasses</sub>

`:AddClasses(classNames):` <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description                                 |
| -------------- | ----------------------------------------------- | ------------------------------------------- |
| **classNames** | <mark style="color:purple;">**`string`**</mark> | Could be a space separated list of classes. |

Adds a class to the panel.

## <sub>RemoveClasses</sub>

`:RemoveClasses(classNames):` <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description                                 |
| -------------- | ----------------------------------------------- | ------------------------------------------- |
| **classNames** | <mark style="color:purple;">**`string`**</mark> | Could be a space separated list of classes. |

Removes a class to the panel.


--------------------------------------------------------------------------------

## Configuration and Utilities

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities -->

# Configuration & Utilities

- [Config](/api-v2.0/game-components/configuration-and-utilities/config.md)
- [Humanizer](/api-v2.0/game-components/configuration-and-utilities/humanizer.md)
- [Log](/api-v2.0/game-components/configuration-and-utilities/log.md)
- [Localizer](/api-v2.0/game-components/configuration-and-utilities/localizer.md)
- [GameLocalizer](/api-v2.0/game-components/configuration-and-utilities/gamelocalizer.md)

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config -->

# Config

Table to work with configs that are stored in the `configs` folder with the `.ini` extention.

## <sub>ReadInt</sub>

`Config.ReadInt(config, key, [def]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                      | Type                                             | Description                                                         |
| --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| **config**                                                | <mark style="color:purple;">**`string`**</mark>  | The config file name.                                               |
| **key**                                                   | <mark style="color:purple;">**`string`**</mark>  | The key to read.                                                    |
| **def&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark> | The default value to return if the key is not found. `(default: 0)` |

Read an integer from a config file.

## <sub>ReadFloat</sub>

`Config.ReadFloat(config, key, [def]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                      | Type                                            | Description                                                           |
| --------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------- |
| **config**                                                | <mark style="color:purple;">**`string`**</mark> | The config file name.                                                 |
| **key**                                                   | <mark style="color:purple;">**`string`**</mark> | The key to read.                                                      |
| **def&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The default value to return if the key is not found. `(default: 0.0)` |

Read a float from a config file.

## <sub>ReadString</sub>

`Config.ReadString(config, key, [def]):` <mark style="color:purple;">**`string`**</mark>

| Name                                                      | Type                                            | Description                                                          |
| --------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------- |
| **config**                                                | <mark style="color:purple;">**`string`**</mark> | The config file name.                                                |
| **key**                                                   | <mark style="color:purple;">**`string`**</mark> | The key to read.                                                     |
| **def&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | The default value to return if the key is not found. `(default: "")` |

Read a string from a config file.

## <sub>WriteInt</sub>

`Config.WriteInt(config, key, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description           |
| ---------- | ------------------------------------------------ | --------------------- |
| **config** | <mark style="color:purple;">**`string`**</mark>  | The config file name. |
| **key**    | <mark style="color:purple;">**`string`**</mark>  | The key to write.     |
| **value**  | <mark style="color:purple;">**`integer`**</mark> | The value to write.   |

Write an integer to a config file.

## <sub>WriteFloat</sub>

`Config.WriteFloat(config, key, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                            | Description           |
| ---------- | ----------------------------------------------- | --------------------- |
| **config** | <mark style="color:purple;">**`string`**</mark> | The config file name. |
| **key**    | <mark style="color:purple;">**`string`**</mark> | The key to write.     |
| **value**  | <mark style="color:purple;">**`number`**</mark> | The value to write.   |

Write a float to a config file.

## <sub>WriteString</sub>

`Config.WriteString(config, key, value):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                            | Description           |
| ---------- | ----------------------------------------------- | --------------------- |
| **config** | <mark style="color:purple;">**`string`**</mark> | The config file name. |
| **key**    | <mark style="color:purple;">**`string`**</mark> | The key to write.     |
| **value**  | <mark style="color:purple;">**`string`**</mark> | The value to write.   |

Write a string to a config file.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer -->

# Humanizer

Table to work with humanizer.

## <sub>IsInServerCameraBounds</sub>

`Humanizer.IsInServerCameraBounds(pos):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                                                 | Description       |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) | position to check |

Returns `true` if the world position is in server camera bounds.

## <sub>GetServerCameraPos</sub>

`Humanizer.GetServerCameraPos():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns server camera position.

## <sub>GetClientCameraPos</sub>

`Humanizer.GetClientCameraPos():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns client camera position.

## <sub>GetServerCursorPos</sub>

`Humanizer.GetServerCursorPos():` [<mark style="color:purple;">**`Vector`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns the server cursor position.

## <sub>GetOrderQueue</sub>

`Humanizer.GetOrderQueue():` <mark style="color:purple;">**`{player: CPlayer, orderType: Enum.UnitOrder, targetIndex: integer, position: Vector, abilityIndex: integer, orderIssuer: Enum.PlayerOrderIssuer, unit: CNPC, orderQueueBehavior: integer, showEffects: boolean, triggerCallBack: boolean, isByMiniMap: boolean, addTime: number }[]`**</mark>

Returns information about the current humanizer order queue.

## <sub>IsSafeTarget</sub>

`Humanizer.IsSafeTarget(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                                               | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) |             |

Returns information about the current humanizer order queue.

## <sub>ForceUserOrderByMinimap</sub>

`Humanizer.ForceUserOrderByMinimap():` <mark style="color:purple;">**`nil`**</mark>

Forces current user order by minimap. Must be called in OnPrepareUnitOrder

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log -->

# Log

Table to log.

## <sub>Write</sub>

`Log.Write(arg):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                         | Description      |
| ------- | -------------------------------------------- | ---------------- |
| **arg** | <mark style="color:purple;">**`any`**</mark> | Message to write |

Writes a message to the console.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer -->

# Localizer

Table to work with cheat localizer.

## <sub>Get</sub>

`Localizer.Get(str):` <mark style="color:purple;">**`string`**</mark>

| Name    | Type                                            | Description |
| ------- | ----------------------------------------------- | ----------- |
| **str** | <mark style="color:purple;">**`string`**</mark> |             |

Returns localized string using current language.

## <sub>RegToken</sub>

`Localizer.RegToken(str):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                            | Description |
| ------- | ----------------------------------------------- | ----------- |
| **str** | <mark style="color:purple;">**`string`**</mark> |             |

Registers key (token) string to localizer.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/gamelocalizer -->

# GameLocalizer

Table to work with game localization.\
Localization tokens are stored in `resource/localization` folder in `pak01_dir.vpk`

## <sub>Find</sub>

`GameLocalizer.Find(token):` <mark style="color:purple;">**`string`**</mark>

| Name      | Type                                            | Description                  |
| --------- | ----------------------------------------------- | ---------------------------- |
| **token** | <mark style="color:purple;">**`string`**</mark> | should be in format `#token` |

Returns localized string by token or returns empty string if token not found.

#### Example

```lua
GameLocalizer.Find("#DOTA_AutocastAbility5") -- Autocast Ability Ultimate
```

## <sub>FindAbility</sub>

`GameLocalizer.FindAbility(ability_name):` <mark style="color:purple;">**`string`**</mark>

| Name              | Type                                            | Description |
| ----------------- | ----------------------------------------------- | ----------- |
| **ability\_name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns localized string by ability name or returns empty string if ability not found.

#### Example

```lua
GameLocalizer.FindAbility("antimage_mana_void") -- Mana Void
```

## <sub>FindItem</sub>

`GameLocalizer.FindItem(item_name):` <mark style="color:purple;">**`string`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **item\_name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns localized string by item name or returns empty string if item not found.

#### Example

```lua
GameLocalizer.FindItem("item_blink") -- Blink Dagger
GameLocalizer.FindItem("item_recipe_arcane_blink") -- Recipe: Arcane Blink
```

## <sub>FindNPC</sub>

`GameLocalizer.FindNPC(unit_name):` <mark style="color:purple;">**`string`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **unit\_name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns localized string by unit name or returns empty string if unit not found.

#### Example

```lua
GameLocalizer.FindNPC("npc_dota_hero_necrolyte") -- Necrophos
```

