# 🧭GridNav

Table to work with in\-game navigation API\.

## [](#createnpcmap)CreateNpcMap

You should always call \`GridNav\.ReleaseNpcMap\` after you done with your build pathing

\`GridNav\.CreateNpcMap\(\[excluded\_npcs\]\, \[includeTempTrees\]\):\` \[\*\*\`GridNavNpcMap\`\*\*\]\(GridNavNpcMap\.md\)

Name

Type

Description

**excluded\_npcs**`[?]`

[`CEntity[]`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity) \| `nil`

table with npc to exclude from the map\. for example you want to exclude local hero if you build path from local hero position `(default: nil)`

**includeTempTrees**`[?]`

`boolean`

`true` if you want include temp trees to the map e\.g\. furion's 1st spell\, iron branch `(default: true)`

Creates a new `GridNavNpcMap`

## [](#releasenpcmap)ReleaseNpcMap

`GridNav.ReleaseNpcMap(npc_map):` `nil`

**npc\_map**

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md)

map to release to release

Releases allocated memory for `GridNavNpcMap`

## [](#istraversable)IsTraversable

`GridNav.IsTraversable(pos, [flag]):` `boolean`\, `integer`

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

position to check

**flag**`[?]`

`number`

flag to check `(default: 1)`

Returns `true` if the world position is traversable\.

## [](#buildpath)BuildPath

`GridNav.BuildPath(start, end_, [ignoreTrees], [npc_map]):` [`Vector[]`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**start**

position to start

**end\_**

position to end

**ignoreTrees**`[?]`

`true` if you want to exclude static trees from the pathing `(default: false)`

**npc\_map**`[?]`

[`GridNavNpcMap`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/GridNavNpcMap.md) \| `nil`

map with the npc's positions which works as additional mask for terrain map `(default: nil)`

Build path from start to end\. Returns an array with builded positions\.

#### [](#example)Example

```
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

## [](#istraversablefromto)IsTraversableFromTo

`GridNav.IsTraversableFromTo(start, end_, [ignoreTrees], [npc_map]):` `boolean`

Lite version of GridNav\.BuildPath function which just cheking if the path is exists\.

## [](#debugrender)DebugRender

`GridNav.DebugRender([grid_range], [npc_map], [render_cell_flags]):` `boolean`

**grid\_range**`[?]`

`integer`

grid radius in "cell units" from Vector\(0\,0\,0\) `(default: 50)`

**render\_cell\_flags**`[?]`

render the flags value for each not approachable cell \(don't think you ever want to see this numbers\, so ignore this arg\) `(default: false)`

Debug render of current GridNav with GridNavNpcMap \(if provided\)

Last updated 19 days ago

