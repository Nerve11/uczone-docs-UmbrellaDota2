# 🌐Vector

Vector metatable

### [](#fields)Fields

Name

Type

Description

**x**

`number`

**y**

**z**

## [](#vector)Vector

`Vector([x], [y], [z]):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**x**`[?]`

`(default: 0.0)`

**y**`[?]`

**z**`[?]`

Create a new Vector\.

## [](#tostring)\_\_tostring

`:__tostring():` `string`

## [](#add)\_\_add

Overload for operator \+

`:__add(other):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**other**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector) \| [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2) \| `number`

## [](#sub)\_\_sub

Overload for operator \-

`:__sub(other):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

## [](#div)\_\_div

Overload for operator /

`:__div(other):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

## [](#mul)\_\_mul

Overload for operator \*

`:__mul(other):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

## [](#eq)\_\_eq

Overload for operator ==

\`:\_\_eq\(other\):\` \*\*\`boolean\`\*\*

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

## [](#distance)Distance

`:Distance(other):` `number`

Computes the distance from this vector to other\.

## [](#distance2d)Distance2D

`:Distance2D(other):` `number`

Computes the distance from this vector to other ignoring Z axis\.

## [](#normalized)Normalized

`:Normalized():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns this vector with a length of 1\.
When normalized\, a vector keeps the same direction but its length is 1\.0\.
Note that the current vector is unchanged and a new normalized vector is returned\. If you want to normalize the current vector\, use `Vector:Normalize` function\.

## [](#normalize)Normalize

`:Normalize():` `nil`

Makes this vector have a length of 1\.
When normalized\, a vector keeps the same direction but its length is 1\.0\.
Note that this function will change the current vector\. If you want to keep the current vector unchanged\, use `Vector:Normalized` function\.

## [](#dot)Dot

`:Dot(vector):` `number`

**vector**

Dot Product of two vectors\.
The dot product is a float value equal to the magnitudes of the two vectors multiplied together and then multiplied by the cosine of the angle between them\.
For normalized vectors Dot returns 1 if they point in exactly the same direction\, \-1 if they point in completely opposite directions and zero if the vectors are perpendicular\.

[More](https://medium.com/@r.w.overdijk/unity-vector3-dot-what-11feb258052e)

## [](#dot2d)Dot2D

`:Dot2D(vector):` `number`

Dot Product of two vectors ignoring Z axis\.

## [](#scaled)Scaled

`:Scaled(scale):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**scale**

Returns this vector multiplied by the given number\. The same as `Vector * number`\.

## [](#scale)Scale

`:Scale(scale):` `nil`

Multiplies this vector by the given number\. The same as `Vector = Vector * number`\.

## [](#length)Length

`:Length():` `number`

Returns the length of this vector\.
The length of the vector is `math.sqrt(x*x+y*y+z*z)`\.
If you only need to compare length of some vectors\, you can compare squared magnitudes of them using LengthSqr \(computing squared length is faster\)\.

## [](#lengthsqr)LengthSqr

`:LengthSqr():` `number`

Returns the squared length of this vector\.
This method is faster than Length because it avoids computing a square root\. Use this method if you need to compare vectors\.

## [](#length2d)Length2D

`:Length2D():` `number`

Returns the length of this vector ignoring Z axis\.

## [](#length2dsqr)Length2DSqr

`:Length2DSqr():` `number`

Returns the squared length of this vector ignoring Z axis\.
This method is faster than Length2D because it avoids computing a square root\. Use this method if you need to compare vectors\.

## [](#rotated)Rotated

`:Rotated(angle):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**angle**

`number` \| [`Angle`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

Returns the new vector rotated counterclockwise by the given angle in the XY\-plane\, leaving the Z\-axis unaffected\.

## [](#rotate)Rotate

`:Rotate(angle):` `nil`

Rotates this vector counterclockwise by the given angle in the XY\-plane\, leaving the Z\-axis unaffected\.

## [](#lerp)Lerp

`:Lerp(b, t):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

**b**

end value\, returned when t = 1

**t**

value used to interpolate between a and b\.

Returns linearly interpolated vector between two vectors\.
The value returned equals **a \+ \(b \- a\) \* t** \(which can also be written **a \* \(1\-t\) \+ b\*t**\)\.
When `t = 0`\, **a:Lerp\(b\, t\)** returns `a`\.
When `t = 1`\, **a:Lerp\(b\, t\)** returns `b`\.
When `t = 0.5`\, **a:Lerp\(b\, t\)** returns the point midway between `a` and `b`\.

## [](#cross)Cross

`:Cross(vector):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Returns cross product of two vectors\.

[More](https://docs.unity3d.com/ScriptReference/Vector3.Cross.html)
[Visualization](https://www.youtube.com/watch?v=kz92vvioeng)

## [](#moveforward)MoveForward

`:MoveForward(angle, distance):` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

[`Angle`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle)

**distance**

distance to move

Moves vector forward by a specified distance in the direction defined by a given Angle\.

#### [](#example)Example

```
-- entity position moved forward by 300
local pos = Entity.GetAbsOrigin(entity):MoveForward(Entity.GetRotation(entity), 300);
```

## [](#toangle)ToAngle

`:ToAngle():` [`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

Converts Vector to Angle\. See
https://github\.com/ValveSoftware/source\-sdk\-2013/blob/0565403b153dfcde602f6f58d8f4d13483696a13/src/mathlib/mathlib\_base\.cpp\#L535

## [](#toscreen)ToScreen

`:ToScreen():` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)\, `boolean`

Converts Vector to screen coordinate

## [](#get)Get

`:Get():` `number`\, `number`\, `number`

Returns x\, y and z of this vector\.

## [](#getx)GetX

`:GetX():` `number`

Returns x of this vector\. The same as Vector\.x\.

## [](#gety)GetY

`:GetY():` `number`

Returns y of this vector\. The same as Vector\.y\.

## [](#getz)GetZ

`:GetZ():` `number`

Returns z of this vector\. The same as Vector\.z\.

## [](#setx)SetX

`:SetX(value):` `nil`

**value**

Sets x\. The same as Vector\.x = value\.

## [](#sety)SetY

`:SetY(value):` `nil`

Sets y\. The same as Vector\.y = value\.

## [](#setz)SetZ

`:SetZ(value):` `nil`

Sets z\. The same as Vector\.z = value\.

Last updated 19 days ago

