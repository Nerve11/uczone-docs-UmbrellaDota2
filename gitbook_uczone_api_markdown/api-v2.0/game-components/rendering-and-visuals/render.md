# 🎨Render

Table to work with render v2\.

## [](#filledrect)FilledRect

`Render.FilledRect(start, end_, color, [rounding], [flags]):` `nil`

Name

Type

Description

**start**

[`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The starting point of the rectangle\.

**end\_**

The ending point of the rectangle\.

**color**

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

The color of the rectangle\.

**rounding**`[?]`

`number`

The rounding radius of the rectangle corners\. `(default: 0.0)`

**flags**`[?]`

[`Enum.DrawFlags`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.drawflags)

Custom flags for drawing\. `(default: Enum.DrawFlags.None)`

Draws a filled rectangle\.

## [](#rect)Rect

`Render.Rect(start, end_, color, [rounding], [flags], [thickness]):` `nil`

The color of the rectangle's border\.

**thickness**`[?]`

The thickness of the rectangle's border\. `(default: 1.0)`

Draws an unfilled rectangle\.

## [](#roundedprogressrect)RoundedProgressRect

`Render.RoundedProgressRect(start, end_, color, percent, rounding, [thickness]):` `nil`

**percent**

The percentage of the rectangle to fill \[0\.\.1\]\.

**rounding**

The rounding radius of the rectangle corners\.

Draw a progress rectangle\.

## [](#line)Line

`Render.Line(start, end_, color, [thickness]):` `nil`

The starting point of the line\.

The ending point of the line\.

The color of the line\.

The thickness of the line\. `(default: 1.0)`

Draws a line between two points\.

## [](#polyline)PolyLine

`Render.PolyLine(points, color, [thickness]):` `nil`

**points**

[`Vec2[]`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

A table of Vec2 points to connect with lines\.

The color of the polyline\.

The thickness of the polyline\. `(default: 1.0)`

Draws a series of connected lines \(polyline\)\.

## [](#circle)Circle

`Render.Circle(pos, radius, color, [thickness], [startDeg], [percentage], [rounded], [segments]):` `nil`

**pos**

The center position of the circle\.

**radius**

The radius of the circle\.

The color of the circle\.

The thickness of the circle's outline\. `(default: 1.0)`

**startDeg**`[?]`

The starting degree for drawing the circle\. 0 is right side\, 90 is bottom\, 180 is left\, 270 is top\. `(default: 0.0)`

**percentage**`[?]`

The percentage of the circle to draw\, in the range \[0\.0\-1\.0\]\. `(default: 1.0)`

**rounded**`[?]`

`boolean`

Whether the circle is rounded\. `(default: false)`

**segments**`[?]`

`integer`

The number of segments used for drawing the circle\. `(default: 32)`

Draws a circle\.

## [](#filledcircle)FilledCircle

`Render.FilledCircle(pos, radius, color, [startDeg], [percentage], [segments]):` `nil`

Draws a filled circle\.

## [](#circlegradient)CircleGradient

`Render.CircleGradient(pos, radius, colorOuter, colorInner, [startDeg], [percentage]):` `nil`

**colorOuter**

The outer color of the gradient\.

**colorInner**

The inner color of the gradient\.

Draws a circle with a gradient\.

## [](#triangle)Triangle

`Render.Triangle(points, color, [thickness]):` `nil`

A table of three Vec2 points defining the vertices of the triangle\.

The color of the triangle's outline\.

The thickness of the triangle's outline\. `(default: 1.0)`

Draws a triangle outline\.

## [](#filledtriangle)FilledTriangle

`Render.FilledTriangle(points, color):` `nil`

The color of the triangle\.

Draws a filled triangle\.

## [](#texturedpoly)TexturedPoly

`Render.TexturedPoly(points, textureHandle, color, [grayscale]):` `nil`

[`Vertex[]`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex)

A table of Vertex points defining the vertices of the polygon\. Each Vertex contains a position \(Vec2\) and a texture coordinate \(Vec2\)\.

**textureHandle**

The handle to the texture to be applied to the polygon\.

The color to apply over the texture\. This can be used to tint the texture\.

**grayscale**`[?]`

The grayscale of the image\. `(default: 0.0)`

Draws a textured polygon\.

## [](#loadfont)LoadFont

`Render.LoadFont(fontName, [fontFlag], [weight]):` `integer`

**fontName**

`string`

The name of the font to load\.

**fontFlag**`[?]`

[`Enum.FontCreate`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.fontcreate) \| `integer`

Flags for font creation\, such as antialiasing\. `(default: Enum.FontCreate.FONTFLAG_NONE)`

**weight**`[?]`

The weight \(thickness\) of the font\. Typically\, 0 means default weight\. `(default: 400)`

Loads a font and returns its handle\. Returns handle to the loaded font\.

## [](#text)Text

`Render.Text(font, fontSize, text, pos, color):` `nil`

**font**

The handle to the font used for drawing the text\.

**fontSize**

The size of the font\.

**text**

The text to be drawn\.

The position where the text will be drawn\.

The color of the text\.

Draws text at a specified position\.

## [](#worldtoscreen)WorldToScreen

`Render.WorldToScreen(pos):` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)\, `boolean`

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

The 3D world position to be converted\.

Converts a 3D world position to a 2D screen position\. Returns A Vec2 representing the 2D screen position and a boolean indicating visibility on the screen\.

#### [](#example)Example

```
-- Example: Convert the center of the map (0,0,0) to screen coordinates.
local worldPos = Vector(0.0, 0.0, 0.0)
local screenPos, isVisible = Render.WorldToScreen(worldPos)
if isVisible then
    Log.Write("Screen Position: " .. screenPos.x .. ", " .. screenPos.y)
else
    Log.Write("Position is not visible on the screen")
end
```

## [](#screensize)ScreenSize

`Render.ScreenSize():` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Retrieves the current screen size\, returning it as a Vec2 where x is the width and y is the height of the screen\.

## [](#textsize)TextSize

`Render.TextSize(font, fontSize, text):` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

The handle to the font used for measuring the text\.

The text to measure\.

Calculates the size of the given text using the specified font\, returning the size as a Vec2 where x is the width and y is the height of the text\.

## [](#loadimage)LoadImage

`Render.LoadImage(path):` `integer`

**path**

Path to the image\.

Loads an image and returns its handle\.

## [](#image)Image

`Render.Image(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` `nil`

**imageHandle**

The handle to the image\.

The position to draw the image\.

**size**

The size of the image\.

The color to tint the image\.

The rounding radius of the image corners\. `(default: 0.0)`

**uvMin**`[?]`

The minimum UV coordinates for texture mapping\. `(default: {0.0, 0.0})`

**uvMax**`[?]`

The maximum UV coordinates for texture mapping\. `(default: {1.0, 1.0})`

Draws an image at a specified position and size\.

## [](#imagecentered)ImageCentered

`Render.ImageCentered(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` `nil`

The center position to draw the image\.

Draws an image centered at a specified position and size\.

## [](#imagesize)ImageSize

`Render.ImageSize(imageHandle):` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Retrieves the size of an image\. Returns the size of the image as a Vec2\.

## [](#outlinegradient)OutlineGradient

`Render.OutlineGradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags], [thickness]):` `nil`

The starting point of the gradient rectangle\.

The ending point of the gradient rectangle\.

**topLeft**

The color of the top\-left corner\.

**topRight**

The color of the top\-right corner\.

**bottomLeft**

The color of the bottom\-left corner\.

**bottomRight**

The color of the bottom\-right corner\.

The thickness of the outline\. `(default: 1.0)`

Draws a outlined gradient rectangle\.

## [](#gradient)Gradient

`Render.Gradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags]):` `nil`

Draws a filled gradient rectangle\.

## [](#shadow)Shadow

`Render.Shadow(start, end_, color, thickness, [obj_rounding], [flags], [offset]):` `nil`

The starting point of the shadow rectangle\.

The ending point of the shadow rectangle\.

The color of the shadow\.

**thickness**

The thickness of the shadow\.

**obj\_rounding**`[?]`

The rounding radius of the shadow rectangle corners\. `(default: 0.0)`

Custom flags for drawing the shadow\. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)`

**offset**`[?]`

The offset of the shadow from the original rectangle\. `(default: {0.0, 0.0})`

Draws a shadow effect within a specified rectangular area\.

## [](#shadowcircle)ShadowCircle

`Render.ShadowCircle(center, radius, color, thickness, [num_segments], [flags], [offset]):` `nil`

**center**

The center point of the circle\.

**num\_segments**`[?]`

The number of segments for drawing the circle\. `(default: 12)`

The offset of the shadow from the circle\. `(default: {0.0, 0.0})`

Draws a circle shadow effect\.

## [](#shadowconvexpoly)ShadowConvexPoly

`Render.ShadowConvexPoly(points, color, thickness, [flags], [offset]):` `nil`

`Vec[]`

Table of Vec2 points defining the convex polygon\. Should be more than 2 points\.

The offset of the shadow from the polygon\. `(default: {0.0, 0.0})`

Draws a shadow convex polygon effect\.

## [](#shadowngon)ShadowNGon

`Render.ShadowNGon(center, radius, color, thickness, num_segments, [flags], [offset]):` `nil`

The center point of the n\-gon\.

The radius of the n\-gon\.

**num\_segments**

The number of segments \(sides\) of the n\-gon\.

The offset of the shadow from the n\-gon\. `(default: {0.0, 0.0})`

Draws a shadow n\-gon \(polygon with n sides\) effect\.

## [](#blur)Blur

`Render.Blur(start, end_, [strength], [alpha], [rounding], [flags]):` `nil`

The starting point of the blur rectangle\.

The ending point of the blur rectangle\.

**strength**`[?]`

The strength of the blur effect\. `(default: 1.0)`

**alpha**`[?]`

The alpha value of the blur effect\. `(default: 1.0)`

The rounding radius of the blur rectangle corners\. `(default: 0.0)`

Custom flags for the blur effect\. `(default: Enum.DrawFlags.None)`

Applies a blur effect within a specified rectangular area\.

## [](#pushclip)PushClip

`Render.PushClip(start, end_, [intersect]):` `nil`

The starting point of the clipping rectangle\.

The ending point of the clipping rectangle\.

**intersect**`[?]`

If true\, the new clipping area is intersected with the current clipping area\. `(default: false)`

Begins a new clipping region\. Only the rendering within the specified rectangular area will be displayed\.

## [](#popclip)PopClip

`Render.PopClip():` `nil`

Ends the most recently begun clipping region\, restoring the previous clipping region\.

## [](#startrotation)StartRotation

`Render.StartRotation(angle):` `nil`

**angle**

The rotation angle\.

Begins a new rotation\.

## [](#stoprotation)StopRotation

`Render.StopRotation():` `nil`

End the rotation\.

## [](#setglobalalpha)SetGlobalAlpha

Do not forget to reset the global alpha value after your rendering\.

\`Render\.SetGlobalAlpha\(alpha\):\` \*\*\`nil\`\*\*

**alpha**

The alpha value to set \[0\.\.1\]

Set the global alpha value for rendering\.

## [](#resetglobalalpha)ResetGlobalAlpha

`Render.ResetGlobalAlpha():` `nil`

Reset the global alpha value for rendering to 1\.0\.

Last updated 19 days ago

