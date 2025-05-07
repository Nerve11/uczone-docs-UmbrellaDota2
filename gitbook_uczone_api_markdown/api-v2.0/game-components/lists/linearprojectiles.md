# 🚀LinearProjectiles

Table to work linear projectiles\.

## [](#getall)GetAll

`LinearProjectiles.GetAll():` `{handle: integer, max_speed: number, max_dist: number, start_position: Vector, position: Vector, velocity: Vector, original_velocity: Vector, acceleration: Vector, fow_radius: number, source: CEntity}[]`

Returns the 1\-based indexed table with all existing projectiles\. See example\.

#### [](#example)Example

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

Last updated 19 days ago

