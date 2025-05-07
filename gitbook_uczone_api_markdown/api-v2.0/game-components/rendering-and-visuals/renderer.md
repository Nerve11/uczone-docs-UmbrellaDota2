# 🖌️Renderer

Table to work with renderer\.

## [](#setdrawcolor)SetDrawColor

`Renderer.SetDrawColor([r], [g], [b], [a]):` `nil`

Name

Type

Description

**r**`[?]`

`integer`

Red color\. `(default: 255)`

**g**`[?]`

Green color\. `(default: 255)`

**b**`[?]`

Blue color\. `(default: 255)`

**a**`[?]`

Alpha color\. `(default: 255)`

Sets the color of the renderer\.

## [](#drawline)DrawLine

`Renderer.DrawLine(x0, y0, x1, y1):` `nil`

**x0**

X coordinate of the first point\.

**y0**

Y coordinate of the first point\.

**x1**

X coordinate of the second point\.

**y1**

Y coordinate of the second point\.

Draws a line\.

## [](#drawpolyline)DrawPolyLine

`Renderer.DrawPolyLine(points):` `nil`

**points**

`table`

Table of points\.

Draws a polyline\.

## [](#drawpolylinefilled)DrawPolyLineFilled

`Renderer.DrawPolyLineFilled(points):` `nil`

Draws a filled polyline\.

## [](#drawfilledrect)DrawFilledRect

`Renderer.DrawFilledRect(x, y, w, h):` `nil`

**x**

X coordinate of the rectangle\.

**y**

Y coordinate of the rectangle\.

**w**

Width of the rectangle\.

**h**

Height of the rectangle\.

Draws a filled rectangle\.

## [](#drawoutlinerect)DrawOutlineRect

`Renderer.DrawOutlineRect(x, y, w, h):` `nil`

Draws an outlined rectangle\.

## [](#drawoutlinecircle)DrawOutlineCircle

`Renderer.DrawOutlineCircle(x, y, r, s):` `nil`

X coordinate of the circle\.

Y coordinate of the circle\.

**r**

Radius of the circle\.

**s**

Segments of the circle\.

Draws an outlined circle\.

## [](#drawfilledcircle)DrawFilledCircle

`Renderer.DrawFilledCircle(x, y, r):` `nil`

Draws a filled circle\.

## [](#drawoutlineroundedrect)DrawOutlineRoundedRect

`Renderer.DrawOutlineRoundedRect(x, y, w, h, radius):` `nil`

**radius**

Radius of the rectangle\.

Draws an outlined rounded rectangle\.

## [](#drawfilledroundedrect)DrawFilledRoundedRect

`Renderer.DrawFilledRoundedRect(x, y, w, h, radius):` `nil`

Draws a filled rounded rectangle\.

## [](#drawoutlinetriangle)DrawOutlineTriangle

`Renderer.DrawOutlineTriangle(points):` `nil`

Draws an outlined triangle\.

## [](#drawfilledtriangle)DrawFilledTriangle

`Renderer.DrawFilledTriangle(points):` `nil`

Draws a filled triangle\.

## [](#drawtexturedpolygon)DrawTexturedPolygon

`Renderer.DrawTexturedPolygon(points, texture):` `nil`

**texture**

Texture handle\.

Draws a textured polygon\.

## [](#loadfont)LoadFont

`Renderer.LoadFont(name, size, flags, weight):` `integer`

**name**

`string`

Name of the font\.

**size**

Size of the font\.

**flags**

Font flags\.

**weight**

Font weight\.

Loads a font\.

## [](#drawtext)DrawText

`Renderer.DrawText(font, x, y, text):` `nil`

**font**

Font handle\.

X coordinate of the text\.

Y coordinate of the text\.

**text**

Text to draw\.

Draws a text\.

## [](#worldtoscreen)WorldToScreen

`Renderer.WorldToScreen(pos):` `integer`\, `integer`\, `boolean`

**pos**

[`Vector`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector)

World coordinates\.

Converts world coordinates to screen coordinates\. Returns x\, y and visible\.

## [](#getscreensize)GetScreenSize

`Renderer.GetScreenSize():` `integer`\, `integer`

Returns screen size\.

## [](#gettextsize)GetTextSize

`Renderer.GetTextSize(font, text):` `integer`\, `integer`

Text to measure\.

Returns text size\.

## [](#loadimage)LoadImage

`Renderer.LoadImage(path):` `integer`

**path**

Path to the image\.

Loads an image\. Returns image handle\.

## [](#drawimage)DrawImage

`Renderer.DrawImage(handle, x, y, w, h):` `nil`

**handle**

Image handle\.

X coordinate of the image\.

Y coordinate of the image\.

Width of the image\.

Height of the image\.

Draws an image\.

## [](#drawimagecentered)DrawImageCentered

`Renderer.DrawImageCentered(handle, x, y, w, h):` `nil`

Draws an image centered\.

## [](#getimagesize)GetImageSize

`Renderer.GetImageSize(handle):` `integer`\, `integer`

Returns image size\.

## [](#drawfilledrectfade)DrawFilledRectFade

`Renderer.DrawFilledRectFade(x0, y0, x1, y1, alpha0, alpha1, bHorizontal):` `nil`

**alpha0**

Alpha of the first point\.

**alpha1**

Alpha of the second point\.

**bHorizontal**

`boolean`

Horizontal fade\.

Draws a filled rectangle with fade\.

## [](#drawfilledgradrect)DrawFilledGradRect

`Renderer.DrawFilledGradRect(x0, y0, x1, y1, r, g, b, a, r2, g2, b2, a2, bHorizontal):` `nil`

Red color of the first point\.

**g**

Green color of the first point\.

**b**

Blue color of the first point\.

**a**

Alpha color of the first point\.

**r2**

Red color of the second point\.

**g2**

Green color of the second point\.

**b2**

Blue color of the second point\.

**a2**

Alpha color of the second point\.

Horizontal gradient\.

Draws a filled gradient rectangle\.

## [](#drawglow)DrawGlow

`Renderer.DrawGlow(x0, y0, w, h, thickness, obj_rounding):` `nil`

**thickness**

Thickness of the glow\.

**obj\_rounding**

Rounding of the glow\.

Draws a glow\.

## [](#drawblur)DrawBlur

`Renderer.DrawBlur(x0, y0, w, h, strength, rounding, alpha):` `nil`

`number`

**strength**

Strength of the blur\.

**rounding**

Rounding of the blur\.

**alpha**

Alpha of the blur\.

Draws a blur\.

## [](#pushclip)PushClip

`Renderer.PushClip(x, y, w, h, intersect):` `nil`

**intersect**

Intersect with the previous clip\.

Pushes a clip rect\.

## [](#popclip)PopClip

`Renderer.PopClip():` `nil`

Pops a clip rect\.

## [](#drawcenterednotification)DrawCenteredNotification

`Renderer.DrawCenteredNotification(text, duration):` `nil`

**duration**

Duration of the notification\.

Draws a centered notification\.

Last updated 19 days ago

