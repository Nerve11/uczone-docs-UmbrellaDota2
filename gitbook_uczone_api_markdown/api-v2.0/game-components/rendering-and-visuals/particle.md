# ✨Particle

Table to work with particles\.

## [](#create)Create

`Particle.Create(particle, [attach_type], [entity]):` `integer`

Name

Type

Description

**particle**

`string`

Particle path

**attach\_type**`[?]`

[`Enum.ParticleAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.particleattachment)

attach\_type Attach type `(default: Enum.ParticleAttachment.PATTACH_WORLDORIGIN)`

**entity**`[?]`

[`CEntity`](https://uczone.gitbook.io/api-v2.0/game-components/core/entity)

Entity to own of the particle\. If not specified\, the local hero will be used\. `(default: Players.GetLocal())`

Creates a particle and returns its index\.

## [](#setcontrolpoint)SetControlPoint

`Particle.SetControlPoint(particle_index, control_point, value):` `nil`

**particle\_index**

`integer`

Particle index

**control\_point**

Control point

**value**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Control point value

Sets the control point value of a particle\.

## [](#setshoulddraw)SetShouldDraw

`Particle.SetShouldDraw(particle_index, value):` `nil`

`bool`

set value

Enables or disables the drawing of a particle\.

## [](#setcontrolpointent)SetControlPointEnt

`Particle.SetControlPointEnt(particle_index, control_point, entity, attach_type, attach_name, position, lock_orientation):` `nil`

**entity**

Entity to attach

**attach\_type**

Attach type

**attach\_name**

`string` \| `nil`

Attach name\. See `NPC.GetAttachment` function

**position**

Control point position

**lock\_orientation**

`boolean`

Lock orientation\. No idea what it does

Sets the control point entity value of a particle\.

## [](#setparticlecontroltransform)SetParticleControlTransform

`Particle.SetParticleControlTransform(particle_index, control_point, position, angle):` `nil`

**angle**

[`Angle`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Control point angle

Sets the control point's position and angle\.

## [](#destroy)Destroy

`Particle.Destroy(particle_index):` `nil`

Destroys the particle by index\.

Last updated 19 days ago

