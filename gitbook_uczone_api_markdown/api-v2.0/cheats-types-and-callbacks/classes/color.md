# 🎨Color

Color metatable

### [](#fields)Fields

Name

Type

Description

**r**

`number`

red

**g**

green

**b**

blue

**a**

alpha

## [](#color)Color

`Color([r], [g], [b], [a]):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**r**`[?]`

`(default: 255)`

**g**`[?]`

**b**`[?]`

**a**`[?]`

Create a new Color\.

## [](#color-1)Color

`Color(hex):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**hex**

`string`

Hex string\. Do not use "\#" symbol\.

Create a new Color from hex string\.

## [](#asfraction)AsFraction

`:AsFraction(r, g, b, a):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

New R color range as a percentage in the range \[0\.0\, 1\.0\]

New G color range as a percentage in the range \[0\.0\, 1\.0\]

New B color range as a percentage in the range \[0\.0\, 1\.0\]

New A color range as a percentage in the range \[0\.0\, 1\.0\]

Overwrites the color's ranges using the fraction values\. Returns itself\.

## [](#asint)AsInt

`:AsInt(value):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**value**

int color value

Overwrites the color's ranges converting the int value to RGBA values\. Returns
itself\.

## [](#ashsv)AsHsv

`:AsHsv(h, s, v, a):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**h**

Hue color range \[0\.0\, 1\.0\]

**s**

Saturation color range \[0\.0\, 1\.0\]

**v**

Value color range \[0\.0\, 1\.0\]

Alpha color range \[0\.0\, 1\.0\]

Overwrites the color's ranges converting the HSV to RGBA values\. Returns itself\.

## [](#ashsl)AsHsl

`:AsHsl(h, s, l, a):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**l**

Lightness color range \[0\.0\, 1\.0\]

Overwrites the color's ranges converting the HSL to RGBA values\. Returns itself\.

## [](#tofraction)ToFraction

`:ToFraction():` `number`\, `number`\, `number`\, `number`

Returns the r\, g\, b\, and a ranges of the color as a percentage in the range of
\[0\.0\, 1\.0\]\.

## [](#toint)ToInt

`:ToInt():` `number`

Returns the int value representing the color\.

## [](#tohsv)ToHsv

`:ToHsv():` `number`\, `number`\, `number`

Returns the HSV representation of the color\.

## [](#tohsl)ToHsl

`:ToHsl():` `number`\, `number`\, `number`

Returns the ToHsl representation of the color\.

## [](#tohex)ToHex

`:ToHex():` `string`

Returns the hex string representing the color\.

## [](#lerp)Lerp

`:Lerp(other, weight):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**other**

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

The color to interpolate to

**weight**

A value between 0 and 1 that indicates the weight of **other**

Returns the linearly interpolated color between two colors by the specified weight\.

## [](#grayscale)Grayscale

`:Grayscale(weight):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

A value between 0 and 1 that indicates the weight of **grayscale**

Returns the grayscaled color\.

## [](#alphamodulate)AlphaModulate

`:AlphaModulate(alpha):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**alpha**

Returns the alpha modulated color\.

## [](#clone)Clone

`:Clone():` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Creates and returns a copy of the color object\.

## [](#unpack)Unpack

`:Unpack():` `number`\, `number`\, `number`\, `number`

Returns the r\, g\, b\, and a values of the color\. Note that these fields can be
accessed by indexing r\, g\, b\, and a\.

## [](#tostring)\_\_tostring

`:__tostring():` `string`

Returns hex string representing the color\.

Last updated 19 days ago

