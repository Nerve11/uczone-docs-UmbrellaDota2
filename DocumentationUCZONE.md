# UCZONE API v2.0 - Полная документация

*Сгенерировано из 85 страниц GitBook*

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

<!-- Source: https://uczone.gitbook.io/api-v2.0/getting-started/getting_started.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Cheats Types and Callbacks

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/callbacks.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

### Classes - Color

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color.md -->

# Color

Color metatable

### Fields

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **r** | <mark style="color:purple;">**`number`**</mark> | red         |
| **g** | <mark style="color:purple;">**`number`**</mark> | green       |
| **b** | <mark style="color:purple;">**`number`**</mark> | blue        |
| **a** | <mark style="color:purple;">**`number`**</mark> | alpha       |

## <sub>\_\_eq</sub>

`:__eq(other):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                    | Description |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |             |

Compares two colors for equality.

## <sub>Set</sub>

`:Set(r, g, b, [a]):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name                                                    | Type                                            | Description      |
| ------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **r**                                                   | <mark style="color:purple;">**`number`**</mark> |                  |
| **g**                                                   | <mark style="color:purple;">**`number`**</mark> |                  |
| **b**                                                   | <mark style="color:purple;">**`number`**</mark> |                  |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |

Sets r, g, b, a components. Returns self for chaining.

## <sub>LerpInPlace</sub>

`:LerpInPlace(other, t):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name      | Type                                                                                                    | Description |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |             |
| **t**     | <mark style="color:purple;">**`number`**</mark>                                                         |             |

Linearly interpolates this color towards other in-place. Returns self for chaining.

## <sub>IsZero</sub>

`:IsZero([tolerance]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                            | Type                                            | Description       |
| --------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| **tolerance&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.01)` |

Returns true if all components are near zero within tolerance.

## <sub>Color</sub>

`Color([r], [g], [b], [a]):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name                                                    | Type                                            | Description      |
| ------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **r&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **g&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **b&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |
| **a&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 255)` |

Create a new Color.

## <sub>Color</sub>

`Color(hex):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name    | Type                                            | Description                        |
| ------- | ----------------------------------------------- | ---------------------------------- |
| **hex** | <mark style="color:purple;">**`string`**</mark> | Hex string. Do not use "#" symbol. |

Create a new Color from hex string.

## <sub>AsFraction</sub>

`:AsFraction(r, g, b, a):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name  | Type                                            | Description                                                |
| ----- | ----------------------------------------------- | ---------------------------------------------------------- |
| **r** | <mark style="color:purple;">**`number`**</mark> | New R color range as a percentage in the range \[0.0, 1.0] |
| **g** | <mark style="color:purple;">**`number`**</mark> | New G color range as a percentage in the range \[0.0, 1.0] |
| **b** | <mark style="color:purple;">**`number`**</mark> | New B color range as a percentage in the range \[0.0, 1.0] |
| **a** | <mark style="color:purple;">**`number`**</mark> | New A color range as a percentage in the range \[0.0, 1.0] |

Overwrites the color's ranges using the fraction values. Returns itself.

## <sub>AsInt</sub>

`:AsInt(value):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name      | Type                                            | Description     |
| --------- | ----------------------------------------------- | --------------- |
| **value** | <mark style="color:purple;">**`number`**</mark> | int color value |

Overwrites the color's ranges converting the int value to RGBA values. Returns\
itself.

## <sub>AsHsv</sub>

`:AsHsv(h, s, v, a):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name  | Type                                            | Description                        |
| ----- | ----------------------------------------------- | ---------------------------------- |
| **h** | <mark style="color:purple;">**`number`**</mark> | Hue color range \[0.0, 1.0]        |
| **s** | <mark style="color:purple;">**`number`**</mark> | Saturation color range \[0.0, 1.0] |
| **v** | <mark style="color:purple;">**`number`**</mark> | Value color range \[0.0, 1.0]      |
| **a** | <mark style="color:purple;">**`number`**</mark> | Alpha color range \[0.0, 1.0]      |

Overwrites the color's ranges converting the HSV to RGBA values. Returns itself.

## <sub>AsHsl</sub>

`:AsHsl(h, s, l, a):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

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

`:Lerp(other, weight):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name       | Type                                                                                                    | Description                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **other**  | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | The color to interpolate to                                    |
| **weight** | <mark style="color:purple;">**`number`**</mark>                                                         | A value between 0 and 1 that indicates the weight of **other** |

Returns the linearly interpolated color between two colors by the specified weight.

## <sub>Grayscale</sub>

`:Grayscale(weight):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name       | Type                                            | Description                                                        |
| ---------- | ----------------------------------------------- | ------------------------------------------------------------------ |
| **weight** | <mark style="color:purple;">**`number`**</mark> | A value between 0 and 1 that indicates the weight of **grayscale** |

Returns the grayscaled color.

## <sub>AlphaModulate</sub>

`:AlphaModulate(alpha):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

| Name      | Type                                            | Description                   |
| --------- | ----------------------------------------------- | ----------------------------- |
| **alpha** | <mark style="color:purple;">**`number`**</mark> | Alpha color range \[0.0, 1.0] |

Returns the alpha modulated color.

## <sub>Clone</sub>

`:Clone():` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

Creates and returns a copy of the color object.

## <sub>Unpack</sub>

`:Unpack():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns the r, g, b, and a values of the color. Note that these fields can be\
accessed by indexing r, g, b, and a.

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

Returns hex string representing the color.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.


--------------------------------------------------------------------------------

### Classes - Menu System

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu.md -->

# Menu

Table to work with Menu.

## <sub>Find</sub>

`Menu.Find(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName, widgetName, attachmentName, widgetInGearName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md) | [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md) | [<mark style="color:purple;">**`CMenuButton`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md) | <mark style="color:purple;">**`nil`**</mark>

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

`Menu.Create(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md)

| Name              | Type                                            | Description |
| ----------------- | ----------------------------------------------- | ----------- |
| **firstTabName**  | <mark style="color:purple;">**`string`**</mark> |             |
| **sectionName**   | <mark style="color:purple;">**`string`**</mark> |             |
| **secondTabName** | <mark style="color:purple;">**`string`**</mark> |             |
| **thirdTabName**  | <mark style="color:purple;">**`string`**</mark> |             |
| **groupTabName**  | <mark style="color:purple;">**`string`**</mark> |             |

Creates tab/section/group. Returns menu item.

## <sub>Style</sub>

`Menu.Style(styleColor):` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

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

`Menu.Pos():` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

Returns current menu pos.

## <sub>Size</sub>

`Menu.Size():` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

Returns current menu size.

## <sub>Scale</sub>

`Menu.Scale():` <mark style="color:purple;">**`integer`**</mark>

Returns current menu scale percentage.

## <sub>AnimDuration</sub>

`Menu.AnimDuration():` <mark style="color:purple;">**`number`**</mark>

Returns current menu animation duration.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection.md -->

# CTabSection

CTabSection metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CFirstTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab.md)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(sectionName):` [<mark style="color:purple;">**`CSecondTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab.md)

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CSecondTab`.

## <sub>Find</sub>

`:Find(sectionName):` [<mark style="color:purple;">**`CSecondTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab.md) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CSecondTab` by name.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab.md -->

# CFirstTab

CFirstTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` <mark style="color:purple;">**`nil`**</mark>

Returns parent. It's `nil` for CFirstTab.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(sectionName):` [<mark style="color:purple;">**`CTabSection`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection.md)

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CTabSection`.

## <sub>Find</sub>

`:Find(sectionName):` [<mark style="color:purple;">**`CTabSection`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection.md) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                            | Description |
| --------------- | ----------------------------------------------- | ----------- |
| **sectionName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CTabSection` by name.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab.md -->

# CSecondTab

CSecondTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CTabSection`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection.md)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(tabName):` [<mark style="color:purple;">**`CThirdTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab.md)

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **tabName** | <mark style="color:purple;">**`string`**</mark> |             |

Creates new `CThirdTab`.

## <sub>Find</sub>

`:Find(tabName):` [<mark style="color:purple;">**`CThirdTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab.md) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **tabName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CThirdTab` by name.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets tab's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
-- https://fontawesome.com/icons/user?f=classic&s=solid
tab:Icon( "\u{f007}" )
```

## <sub>LinkHero</sub>

`:LinkHero(heroId, attribute):` <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                                                                                                                                                              | Description                  |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **heroId**    | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                  | See `Engine.GetHeroIDByName` |
| **attribute** | [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.attributes) |                              |

Links tab to hero and attribute.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab.md -->

# CThirdTab

CThirdTab metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns tab's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CSecondTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab.md)

Returns tab's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Create</sub>

`:Create(groupName, [side]):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md)

| Name                                                       | Type                                                                                                                                                                            | Description                         |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **groupName**                                              | <mark style="color:purple;">**`string`**</mark>                                                                                                                                 |                                     |
| **side&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.GroupSide`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.groupside) | `(default: Enum.GroupSide.Default)` |

Creates new `CMenuGroup`.

## <sub>Find</sub>

`:Find(groupName):` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | <mark style="color:purple;">**`nil`**</mark>

| Name          | Type                                            | Description |
| ------------- | ----------------------------------------------- | ----------- |
| **groupName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the `CMenuGroup` by name.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

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

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets tab's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
-- https://fontawesome.com/icons/user?f=classic&s=solid
tab:Icon( "\u{f007}")
```

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md -->

# CMenuGroup

CMenuGroup metatable

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns group's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CThirdTab`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab.md)

Returns group's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>Find</sub>

`:Find(widgetName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md) | [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md) | [<mark style="color:purple;">**`CMenuButton`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **widgetName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the widget by name.

## <sub>Switch</sub>

`:Switch(switchName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md)

| Name                                                               | Type                                             | Description                                                |
| ------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------- |
| **switchName**                                                     | <mark style="color:purple;">**`string`**</mark>  |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | `(default: false)`                                         |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>  | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuSwitch`.

## <sub>Bind</sub>

`:Bind(bindName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md)

| Name                                                               | Type                                                                                                                                                                              | Description                                                |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **bindName**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                                                                                   |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode) | `(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`           |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                                                                                   | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuBind`.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

\`:ForceLocalization(newText):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the group header. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md)

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

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md)

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

`:ColorPicker(colorPickerName, color, [imageIcon]):` [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md)

| Name                                                            | Type                                                                                                    | Description                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **colorPickerName**                                             | <mark style="color:purple;">**`string`**</mark>                                                         |                                                            |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark>                                                         | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuColorPicker`.

## <sub>Button</sub>

`:Button(buttonName, callback, [altStyle], [widthPercent]):` [<mark style="color:purple;">**`CMenuButton`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md)

| Name                                                               | Type                                                                | Description                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------ |
| **buttonName**                                                     | <mark style="color:purple;">**`string`**</mark>                     |                                                        |
| **callback**                                                       | <mark style="color:purple;">**`fun(this: CMenuButton):nil`**</mark> | function to call on button click.                      |
| **altStyle&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`boolean`**</mark>                    | Use alternative button style. `(default: false)`       |
| **widthPercent&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                     | Button width in percents. \[0.0, 1.0] `(default: 1.0)` |

Creates new `CMenuButton`.

#### Example

```lua
group:Button( "button", function( this )
	Log.Write( "Button '" .. this:Name() .. "' has been clicked."  )
end )
```

## <sub>Combo</sub>

`:Combo(comboName, items, [defaultValue]):` [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md)

| Name                                                               | Type                                              | Description                                           |
| ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **comboName**                                                      | <mark style="color:purple;">**`string`**</mark>   |                                                       |
| **items**                                                          | <mark style="color:purple;">**`string[]`**</mark> |                                                       |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>  | Index of default item. (starts from 0) `(default: 0)` |

Creates new `CMenuComboBox`.

## <sub>MultiCombo</sub>

`:MultiCombo(multiComboName, items, enabledItems):` [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md)

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

`:MultiSelect(multiSelectName, items, [expanded]):` [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md)

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

`:Input(inputName, defaultValue, [imageIcon]):` [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md)

| Name                                                            | Type                                            | Description                                                |
| --------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **inputName**                                                   | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **defaultValue**                                                | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuInputBox`.

## <sub>Label</sub>

`:Label(labelText, [imageIcon]):` [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md)

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.


--------------------------------------------------------------------------------

### Classes - UI Widgets

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md -->

# CMenuSwitch

CMenuSwitch metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md -->

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

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md -->

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

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md -->

# CMenuColorPicker

CMenuColorPicker metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

`:Get():` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                    | Description |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| **value** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |             |

Sets widget's value.

## <sub>Image</sub>

`:Image(imagePath, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md -->

# CMenuColorPickerAttachment

CMenuColorPickerAttachment metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md) | [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

`:Get():` [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)

Returns widget's value.

## <sub>Set</sub>

`:Set(value):` <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                                    | Description |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| **value** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |             |

Sets widget's value.

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md -->

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

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md -->

# CMenuGearAttachment

CMenuGearAttachment metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md) | [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

\`:ForceLocalization(newText):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Changes text in the widget. The path to the widget is not affected.\
May be used for dynamic text customization or recolor.

## <sub>Find</sub>

`:Find(widgetName):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md) | [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md) | [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md) | [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md) | [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md) | [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md) | [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md) | [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md) | [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md) | [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                            | Description |
| -------------- | ----------------------------------------------- | ----------- |
| **widgetName** | <mark style="color:purple;">**`string`**</mark> |             |

Finds the widget by name.

## <sub>Switch</sub>

`:Switch(switchName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuSwitch`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch.md)

| Name                                                               | Type                                             | Description                                                |
| ------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------- |
| **switchName**                                                     | <mark style="color:purple;">**`string`**</mark>  |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | `(default: false)`                                         |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>  | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuSwitch`.

## <sub>Bind</sub>

`:Bind(bindName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuBind`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md)

| Name                                                               | Type                                                                                                                                                                                 | Description                                                |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **bindName**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                                                                                      |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode) | `(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`           |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                                                                                                      | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuBind`.

## <sub>Slider</sub>

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderInt`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint.md)

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

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [<mark style="color:purple;">**`CMenuSliderFloat`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat.md)

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

`:ColorPicker(colorPickerName, color, [imageIcon]):` [<mark style="color:purple;">**`CMenuColorPicker`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker.md)

| Name                                                            | Type                                                                                                    | Description                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **colorPickerName**                                             | <mark style="color:purple;">**`string`**</mark>                                                         |                                                            |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) |                                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark>                                                         | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuColorPicker`.

## <sub>Button</sub>

`:Button(buttonName, callback, [altStyle], [widthPercent]):` [<mark style="color:purple;">**`CMenuButton`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton.md)

| Name                                                               | Type                                                                | Description                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------ |
| **buttonName**                                                     | <mark style="color:purple;">**`string`**</mark>                     |                                                        |
| **callback**                                                       | <mark style="color:purple;">**`fun(this: CMenuButton):nil`**</mark> | function to call on button click.                      |
| **altStyle&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`boolean`**</mark>                    | Use alternative button style. `(default: false)`       |
| **widthPercent&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                     | Button width in percents. \[0.0, 1.0] `(default: 1.0)` |

Creates new `CMenuButton`.

#### Example

```lua
gear:Button( "button", function( this )
	Log.Write( "Button '" .. this:Name() .. "' has been clicked."  )
end )
```

## <sub>Combo</sub>

`:Combo(comboName, items, [defaultValue]):` [<mark style="color:purple;">**`CMenuComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox.md)

| Name                                                               | Type                                              | Description                                           |
| ------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| **comboName**                                                      | <mark style="color:purple;">**`string`**</mark>   |                                                       |
| **items**                                                          | <mark style="color:purple;">**`string[]`**</mark> |                                                       |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>  | Index of default item. (starts from 0) `(default: 0)` |

Creates new `CMenuComboBox`.

## <sub>MultiCombo</sub>

`:MultiCombo(multiComboName, items, enabledItems):` [<mark style="color:purple;">**`CMenuMultiComboBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md)

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

`:MultiSelect(multiSelectName, items, [expanded]):` [<mark style="color:purple;">**`CMenuMultiSelect`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md)

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

`:Input(inputName, [defaultValue], [imageIcon]):` [<mark style="color:purple;">**`CMenuInputBox`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md)

| Name                                                               | Type                                            | Description                                                |
| ------------------------------------------------------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| **inputName**                                                      | <mark style="color:purple;">**`string`**</mark> |                                                            |
| **defaultValue&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`string`**</mark> | `(default: "")`                                            |
| **imageIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark> | Path to image or FontAwesome icon unicode. `(default: "")` |

Creates new `CMenuInputBox`.

## <sub>Label</sub>

`:Label(labelText, [imageIcon]):` [<mark style="color:purple;">**`CMenuLabel`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md)

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md -->

# CMenuInputBox

CMenuInputBox metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md -->

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

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md -->

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

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md -->

# CMenuBind

CMenuBind metatable.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

Returns widget's name.

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget's type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

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

`:Get([idx]):` [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode)

| Name                                                      | Type                                                                                     | Description                                          |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **idx&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`0`**</mark> \| <mark style="color:purple;">**`1`**</mark> | index of the button to get value from `(default: 0)` |

Returns widget's value. To get both of the buttons use `Buttons` method.

## <sub>Set</sub>

`:Set(key1, [key2]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                       | Type                                                                                                                                                                                 | Description                                                 |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **key1**                                                   | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode) | primary button code                                         |
| **key2&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode) | secondary button code `(default: Enum.ButtonCode.KEY_NONE)` |

Sets widget's value.

## <sub>Buttons</sub>

`:Buttons():` [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode), [<mark style="color:purple;">**`Enum.ButtonCode`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.buttoncode)

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\u{f007}")
```

## <sub>SetCallback</sub>

Multiple callbacks could be set.

`:SetCallback(callback, [forceCall]):` <mark style="color:purple;">**`nil`**</mark>

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

## <sub>SetKeyCallback</sub>

Multiple callbacks could be set.

\`:SetKeyCallback(callback):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name         | Type                                                                                                           | Description                                 |
| ------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuBind, key: Enum.ButtonCode, event: Enum.EKeyEvent):nil`**</mark> | function to be called on key press/release. |

Sets widget's on key press/release callback.

## <sub>UnsetKeyCallback</sub>

`:UnsetKeyCallback(callback):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                           | Description             |
| ------------ | -------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **callback** | <mark style="color:purple;">**`fun(this: CMenuBind, key: Enum.ButtonCode, event: Enum.EKeyEvent):nil`**</mark> | function to be removed. |

Removes widget's on key press/release callback.

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md -->

# CMenuLabel

CMenuLabel metatable.

## <sub>Name</sub>

`:Name(newText):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                            | Description |
| ----------- | ----------------------------------------------- | ----------- |
| **newText** | <mark style="color:purple;">**`string`**</mark> |             |

Returns widget's name.

## <sub>Name</sub>

`:Name():` <mark style="color:purple;">**`string`**</mark>

## <sub>Parent</sub>

`:Parent():` [<mark style="color:purple;">**`CMenuGroup`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup.md) | [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

Returns widget's parent.

## <sub>Type</sub>

`:Type():` [<mark style="color:purple;">**`Enum.WidgetType`**</mark>](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/pages/VwVljl88Qnl7u9hhqRdw#enum.widgettype)

Returns widget type.

## <sub>Open</sub>

`:Open():` <mark style="color:purple;">**`nil`**</mark>

Opens parent tabs.

## <sub>ForceLocalization</sub>

Not recommended for use due to its complexity

\`:ForceLocalization(newText):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

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

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imagePath**                                                | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.                             |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets widget's image.

## <sub>ImageHandle</sub>

`:ImageHandle(imageHandle, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                    |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **imageHandle**                                              | <mark style="color:purple;">**`integer`**</mark>                                                           |                                                |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional image offset. `(default: {0.0, 0.0})` |

Sets tab's image by already created handle.

## <sub>Icon</sub>

`:Icon(icon, [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                       | Description                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **icon**                                                     | <mark style="color:purple;">**`string`**</mark>                                                            | icon unicode.                                 |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Optional icon offset. `(default: {0.0, 0.0})` |

Sets widget's icon.\
[Icons list](https://fontawesome.com/search?o=r\&s=solid\&f=classic)

#### Example

```lua
--https://fontawesome.com/icons/user?f=classic&s=solid
widget:Icon("\u{f007}")
```

## <sub>ColorPicker</sub>

`:ColorPicker(name, color):` [<mark style="color:purple;">**`CMenuColorPickerAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment.md)

| Name      | Type                                                                                                    | Description             |
| --------- | ------------------------------------------------------------------------------------------------------- | ----------------------- |
| **name**  | <mark style="color:purple;">**`string`**</mark>                                                         | Name of the attachment. |
| **color** | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md) | Default color.          |

Creates `CMenuColorPickerAttachment` and attaches it to the widget.

## <sub>Gear</sub>

`:Gear(name, [gearIcon], [useSmallFont]):` [<mark style="color:purple;">**`CMenuGearAttachment`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment.md)

| Name                                                               | Type                                             | Description                                     |
| ------------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- |
| **name**                                                           | <mark style="color:purple;">**`string`**</mark>  | Name of the attachment.                         |
| **gearIcon&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>  | Gear FontAwesome icon. `(default: "\uf013")`    |
| **useSmallFont&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Use small font for gear icon. `(default: true)` |

Creates `CMenuGearAttachment` and attaches it to the widget.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenulabel.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.


--------------------------------------------------------------------------------

### Classes - Math

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md -->

# Angle

Angle metatable

### Fields

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **pitch** | <mark style="color:purple;">**`number`**</mark> |             |
| **yaw**   | <mark style="color:purple;">**`number`**</mark> |             |
| **roll**  | <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_eq</sub>

`:__eq(other):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md) |             |

Compares two angles for equality.

## <sub>\_\_add</sub>

`:__add(other):` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md) |             |

Adds two angles together. Returns a new Angle.

## <sub>\_\_sub</sub>

`:__sub(other):` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md) |             |

Subtracts one angle from another. Returns a new Angle.

## <sub>Set</sub>

`:Set(pitch, yaw, roll):` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

| Name      | Type                                            | Description |
| --------- | ----------------------------------------------- | ----------- |
| **pitch** | <mark style="color:purple;">**`number`**</mark> |             |
| **yaw**   | <mark style="color:purple;">**`number`**</mark> |             |
| **roll**  | <mark style="color:purple;">**`number`**</mark> |             |

Sets pitch, yaw, roll. Returns self for chaining.

## <sub>CopyFrom</sub>

`:CopyFrom(other):` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **other** | [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md) |             |

Copies values from another angle without allocating. Returns self for chaining.

## <sub>Clone</sub>

`:Clone():` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

Creates a new angle with the same values as the original.

## <sub>Get</sub>

`:Get():` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

Returns pitch, yaw, roll as three numbers.

## <sub>IsZero</sub>

`:IsZero([tolerance]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                            | Type                                            | Description       |
| --------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| **tolerance&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.01)` |

Returns true if all components are near zero within tolerance.

## <sub>Angle</sub>

`Angle([pitch], [yaw], [roll]):` [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)

| Name                                                        | Type                                            | Description      |
| ----------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| **pitch&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **yaw&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |
| **roll&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark> | `(default: 0.0)` |

Create a new Angle.

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>GetForward</sub>

`:GetForward():` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

Returns the forward vector from a given Angle.

## <sub>GetVectors</sub>

`:GetVectors():` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md), [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md), [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md -->

# Vec2

Vec2 metatable

### Fields

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

## <sub>AddInPlace</sub>

`:AddInPlace(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

Adds other to this Vec2 in-place. Returns self for chaining.

## <sub>SubInPlace</sub>

`:SubInPlace(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

Subtracts other from this Vec2 in-place. Returns self for chaining.

## <sub>MulInPlace</sub>

`:MulInPlace(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

Multiplies this Vec2 by other in-place. Returns self for chaining.

## <sub>DivInPlace</sub>

`:DivInPlace(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

Divides this Vec2 by other in-place. Returns self for chaining.

## <sub>CopyFrom</sub>

`:CopyFrom(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                       | Description |
| --------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) |             |

Copies values from another Vec2 without allocating. Returns self for chaining.

## <sub>Clone</sub>

`:Clone():` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

Creates a new Vec2 with the same values as the original.

## <sub>Set</sub>

`:Set(x, y):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

Sets x, y components. Returns self for chaining.

## <sub>IsZero</sub>

`:IsZero([tolerance]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                            | Type                                            | Description       |
| --------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| **tolerance&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | `(default: 0.01)` |

Returns true if all components are near zero within tolerance.

## <sub>Vec2</sub>

`Vec2(x, y):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name  | Type                                            | Description |
| ----- | ----------------------------------------------- | ----------- |
| **x** | <mark style="color:purple;">**`number`**</mark> |             |
| **y** | <mark style="color:purple;">**`number`**</mark> |             |

Create a new Vec2.

## <sub>Vec2</sub>

`Vec2():` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

Create a new Vec2(0,0).

## <sub>\_\_tostring</sub>

`:__tostring():` <mark style="color:purple;">**`string`**</mark>

## <sub>\_\_add</sub>

Overload for operator +

`:__add(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_sub</sub>

Overload for operator -

`:__sub(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_div</sub>

Overload for operator /

`:__div(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_mul</sub>

Overload for operator \*

`:__mul(other):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name      | Type                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_eq</sub>

Overload for operator ==

\`:\_\_eq(other):\` <mark style="color:purple;">\*\*\`boolean\`\*\*</mark>

| Name      | Type                                                                                                       | Description |
| --------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) |             |

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md -->

# Vertex

Vertex metatable

### Fields

| Name    | Type                                                                                                       | Description |
| ------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| **pos** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | screen pos  |
| **uv**  | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | texture uv  |

## <sub>Vertex</sub>

`Vertex(pos, uv):` [<mark style="color:purple;">**`Vertex`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md)

| Name    | Type                                                                                                       | Description |
| ------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| **pos** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) |             |
| **uv**  | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) |             |

Create a new Vertex.

## <sub>Vertex</sub>

`Vertex(posx, posy, uvx, uvy):` [<mark style="color:purple;">**`Vertex`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md)

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

Overload for operator +

`:__add(other):` [<mark style="color:purple;">**`Vertex`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md)

| Name      | Type                                                                                                                                                              | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vertex`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md) \| <mark style="color:purple;">**`number`**</mark> |             |

## <sub>\_\_sub</sub>

Overload for operator -

\`:\_\_sub(other):\` \[<mark style="color:purple;">\*\*\`Vertex\`\*\*</mark>]\(Vertex.md)

| Name      | Type                                                                                                                                                              | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **other** | [<mark style="color:purple;">**`Vertex`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md) \| <mark style="color:purple;">**`number`**</mark> |             |

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.


--------------------------------------------------------------------------------

## Game Components - Entity Lists

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/abilities.md -->

# Abilities

Table to work with ability list.

## <sub>Count</sub>

`Abilities.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of ability list.

## <sub>Get</sub>

`Abilities.Get(index):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                     |
| --------- | ------------------------------------------------ | ------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of ability in cheat list. |

Return ability by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Abilities.GetAll():` [<mark style="color:purple;">**`CAbility[]`**</mark>](/api-v2.0/game-components/core/ability.md)

Return all abilities in cheat list.

## <sub>Contains</sub>

`Abilities.Contains(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description       |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | Ability to check. |

Check ability in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/abilities.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/couriers.md -->

# Couriers

Table to work with courier list.

## <sub>Count</sub>

`Couriers.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of courier list.

## <sub>Get</sub>

`Couriers.Get(index):` [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                     |
| --------- | ------------------------------------------------ | ------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of courier in cheat list. |

Return courier by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Couriers.GetAll():` [<mark style="color:purple;">**`CCourier[]`**</mark>](/api-v2.0/game-components/core/courier.md)

Return all couriers in cheat list.

## <sub>Contains</sub>

`Couriers.Contains(courier):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description       |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | Courier to check. |

Check courier in cheat list.

## <sub>GetLocal</sub>

`Couriers.GetLocal():` [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | <mark style="color:purple;">**`nil`**</mark>

Return local courier.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/couriers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/customentities.md -->

# CustomEntities

Table to work with specific abilities.

## <sub>GetSpiritBear</sub>

`CustomEntities.GetSpiritBear(spiritBear):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name           | Type                                                                                           | Description              |
| -------------- | ---------------------------------------------------------------------------------------------- | ------------------------ |
| **spiritBear** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | The Spirit Bear ability. |

Accept the Spirit Bear ability and return linked Bear.

## <sub>GetVengeIllusion</sub>

`CustomEntities.GetVengeIllusion(commandAura):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name            | Type                                                                                           | Description               |
| --------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| **commandAura** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | The Command Aura ability. |

Accept the Vengeful Spirit's Command Aura ability and return scepter linked illusion.

## <sub>GetTetheredUnit</sub>

`CustomEntities.GetTetheredUnit(tether):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                           | Description         |
| ---------- | ---------------------------------------------------------------------------------------------- | ------------------- |
| **tether** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | The Tether ability. |

Accept the Wisp's Tether ability and return linked unit.

## <sub>GetTempestDouble</sub>

`CustomEntities.GetTempestDouble(tempestDouble):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                                                                           | Description                 |
| ----------------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **tempestDouble** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | The Tempest Double ability. |

Accept the Arc Warden's Tempest Double ability and return linked clone.

## <sub>GetMeepoIndex</sub>

`CustomEntities.GetMeepoIndex(dividedWeStand):` <mark style="color:purple;">**`integer`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                           | Description                   |
| ------------------ | ---------------------------------------------------------------------------------------------- | ----------------------------- |
| **dividedWeStand** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | The Divided We Stand ability. |

Accept the Meepo's Divided We Stand ability and return index of Meepo.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/customentities.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/entities.md -->

# Entities

Table to work with entity list.

## <sub>GetAll</sub>

`Entities.GetAll():` [<mark style="color:purple;">**`CEntity[]`**</mark>](/api-v2.0/game-components/core/entity.md)

Get all entities on the map.

## <sub>Contains</sub>

`Entities.Contains(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                         | Description      |
| ---------- | -------------------------------------------------------------------------------------------- | ---------------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | Entity to check. |

Check entity in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/entities.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/heroes.md -->

# Heroes

Table to work with hero list.

## <sub>Count</sub>

`Heroes.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of hero list.

## <sub>Get</sub>

`Heroes.Get(index):` [<mark style="color:purple;">**`CHero`**</mark>](/api-v2.0/game-components/core/hero.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of hero in cheat list. |

Return hero by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Heroes.GetAll():` [<mark style="color:purple;">**`CHero[]`**</mark>](/api-v2.0/game-components/core/hero.md)

Return all heroes in cheat list.

## <sub>Contains</sub>

`Heroes.Contains(hero):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description    |
| -------- | ---------------------------------------------------------------------------------------- | -------------- |
| **hero** | [<mark style="color:purple;">**`CHero`**</mark>](/api-v2.0/game-components/core/hero.md) | Hero to check. |

Check hero in cheat list.

## <sub>InRadius</sub>

`Heroes.InRadius(pos, radius, teamNum, teamType, [omitIllusions], [omitDormant]):` [<mark style="color:purple;">**`CHero[]`**</mark>](/api-v2.0/game-components/core/hero.md)

| Name                                                                | Type                                                                                                                                                        | Description                                                             |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **pos**                                                             | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)                                              | Position to check.                                                      |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                                             | Radius to check.                                                        |
| **teamNum**                                                         | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/lists/pages/VwVljl88Qnl7u9hhqRdw#enum.teamnum)   | Team number to check.                                                   |
| **teamType**                                                        | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/lists/pages/VwVljl88Qnl7u9hhqRdw#enum.teamtype) | Team type to filter by. Relative to teamNum param.                      |
| **omitIllusions&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                            | `true` if you want to get table without illusions `(default: false)`    |
| **omitDormant&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`boolean`**</mark>                                                                                                            | `true` if you want to get table without dormant units `(default: true)` |

Return all heroes in radius.

## <sub>GetLocal</sub>

`Heroes.GetLocal():` [<mark style="color:purple;">**`CHero`**</mark>](/api-v2.0/game-components/core/hero.md)

Return local hero.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/heroes.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/npcs.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/camps.md -->

# Camps

Table to work with list of neutral spawners.

## <sub>Count</sub>

`Camps.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of neutral spawner list.

## <sub>Get</sub>

`Camps.Get(index):` [<mark style="color:purple;">**`CCamp`**</mark>](/api-v2.0/game-components/core/camp.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                             |
| --------- | ------------------------------------------------ | --------------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of neutral spawner in cheat list. |

Return neutral spawner by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Camps.GetAll():` [<mark style="color:purple;">**`CCamp[]`**</mark>](/api-v2.0/game-components/core/camp.md)

Return all neutral spawners in cheat list.

## <sub>InRadius</sub>

`Camps.InRadius(pos, radius):` [<mark style="color:purple;">**`CCamp[]`**</mark>](/api-v2.0/game-components/core/camp.md)

| Name       | Type                                                                                                           | Description        |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| **pos**    | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Position to check. |
| **radius** | <mark style="color:purple;">**`number`**</mark>                                                                | Radius to check.   |

Return all neutral spawners in radius.

## <sub>Contains</sub>

`Camps.Contains(camp):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description               |
| -------- | ---------------------------------------------------------------------------------------- | ------------------------- |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](/api-v2.0/game-components/core/camp.md) | Neutral spawner to check. |

Check neutral spawner in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/camps.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/players.md -->

# Players

Table to work with player list.

## <sub>Count</sub>

`Players.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of player list.

## <sub>Get</sub>

`Players.Get(index):` [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                    |
| --------- | ------------------------------------------------ | ------------------------------ |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of player in cheat list. |

Return player by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Players.GetAll():` [<mark style="color:purple;">**`CPlayer[]`**</mark>](/api-v2.0/game-components/core/player.md)

Return all players in cheat list.

## <sub>Contains</sub>

`Players.Contains(player):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                         | Description      |
| ---------- | -------------------------------------------------------------------------------------------- | ---------------- |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | Player to check. |

Check player in cheat list.

## <sub>GetLocal</sub>

`Players.GetLocal():` [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md)

Return local player.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/players.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/runes.md -->

# Runes

Table to work with rune list.

## <sub>Count</sub>

`Runes.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of rune list.

## <sub>Get</sub>

`Runes.Get(index):` [<mark style="color:purple;">**`CRune`**</mark>](/api-v2.0/game-components/core/rune.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of rune in cheat list. |

Return rune by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Runes.GetAll():` [<mark style="color:purple;">**`CRune[]`**</mark>](/api-v2.0/game-components/core/rune.md)

Return all runes in cheat list.

## <sub>Contains</sub>

`Runes.Contains(rune):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description    |
| -------- | ---------------------------------------------------------------------------------------- | -------------- |
| **rune** | [<mark style="color:purple;">**`CRune`**</mark>](/api-v2.0/game-components/core/rune.md) | Rune to check. |

Check rune in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/runes.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/temptrees.md -->

# TempTrees

Table to work with list of temp trees.

## <sub>Count</sub>

`TempTrees.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of temp trees list.

## <sub>Get</sub>

`TempTrees.Get(index):` [<mark style="color:purple;">**`CTree`**</mark>](/api-v2.0/game-components/core/tree.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                       |
| --------- | ------------------------------------------------ | --------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of temp tree in cheat list. |

Return temp tree by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`TempTrees.GetAll():` [<mark style="color:purple;">**`CTree[]`**</mark>](/api-v2.0/game-components/core/tree.md)

Return all temp trees in cheat list.

## <sub>InRadius</sub>

`TempTrees.InRadius(pos, radius):` [<mark style="color:purple;">**`CTree[]`**</mark>](/api-v2.0/game-components/core/tree.md)

| Name       | Type                                                                                                           | Description        |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| **pos**    | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Position to check. |
| **radius** | <mark style="color:purple;">**`number`**</mark>                                                                | Radius to check.   |

Return all temp trees in radius.

## <sub>Contains</sub>

`TempTrees.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description         |
| -------- | ---------------------------------------------------------------------------------------- | ------------------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](/api-v2.0/game-components/core/tree.md) | Temp tree to check. |

Check temp tree in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/temptrees.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/towers.md -->

# Towers

Table to work with tower list.

## <sub>Count</sub>

`Towers.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of tower list.

## <sub>Get</sub>

`Towers.Get(index):` [<mark style="color:purple;">**`CTower`**</mark>](/api-v2.0/game-components/core/tower.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                   |
| --------- | ------------------------------------------------ | ----------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of tower in cheat list. |

Return tower by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Towers.GetAll():` [<mark style="color:purple;">**`CTower[]`**</mark>](/api-v2.0/game-components/core/tower.md)

Return all towers in cheat list.

## <sub>InRadius</sub>

`Towers.InRadius(pos, radius, teamNum, [teamType]):` [<mark style="color:purple;">**`CTower[]`**</mark>](/api-v2.0/game-components/core/tower.md)

| Name                                                           | Type                                                                                                                                                        | Description                                                 |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **pos**                                                        | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)                                              | Position to check.                                          |
| **radius**                                                     | <mark style="color:purple;">**`number`**</mark>                                                                                                             | Radius to check.                                            |
| **teamNum**                                                    | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/lists/pages/VwVljl88Qnl7u9hhqRdw#enum.teamnum)   | Team number to check.                                       |
| **teamType&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/lists/pages/VwVljl88Qnl7u9hhqRdw#enum.teamtype) | Team number to check. `(default: Enum.TeamType.TEAM_ENEMY)` |

Return all towers in radius.

## <sub>Contains</sub>

`Towers.Contains(tower):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                       | Description     |
| --------- | ------------------------------------------------------------------------------------------ | --------------- |
| **tower** | [<mark style="color:purple;">**`CTower`**</mark>](/api-v2.0/game-components/core/tower.md) | Tower to check. |

Check tower in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/towers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/trees.md -->

# Trees

Table to work with list of trees.

## <sub>Count</sub>

`Trees.Count():` <mark style="color:purple;">**`integer`**</mark>

Return size of tree list.

## <sub>Get</sub>

`Trees.Get(index):` [<mark style="color:purple;">**`CTree`**</mark>](/api-v2.0/game-components/core/tree.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                  |
| --------- | ------------------------------------------------ | ---------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of tree in cheat list. |

Return tree by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Trees.GetAll():` [<mark style="color:purple;">**`CTree[]`**</mark>](/api-v2.0/game-components/core/tree.md)

Return all trees in cheat list.

## <sub>InRadius</sub>

`Trees.InRadius(pos, radius, [active]):` [<mark style="color:purple;">**`CTree[]`**</mark>](/api-v2.0/game-components/core/tree.md)

| Name                                                         | Type                                                                                                           | Description                              |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **pos**                                                      | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Position to check.                       |
| **radius**                                                   | <mark style="color:purple;">**`number`**</mark>                                                                | Radius to check.                         |
| **active&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                               | Active state to check. `(default: true)` |

Return all trees in radius.

## <sub>Contains</sub>

`Trees.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description    |
| -------- | ---------------------------------------------------------------------------------------- | -------------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](/api-v2.0/game-components/core/tree.md) | Tree to check. |

Check tree in cheat list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/trees.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/physicalitems.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/modifiers.md -->

# Modifiers

Table to work with list of modifiers.

## <sub>Count</sub>

`Modifiers.Count():` <mark style="color:purple;">**`integer`**</mark>

Returns size of modifiers list.

## <sub>Get</sub>

`Modifiers.Get(index):` [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                             | Description                       |
| --------- | ------------------------------------------------ | --------------------------------- |
| **index** | <mark style="color:purple;">**`integer`**</mark> | Index of temp tree in cheat list. |

Returns modifiers by index in cheat list. Not the same as in-game index.

## <sub>GetAll</sub>

`Modifiers.GetAll():` [<mark style="color:purple;">**`CModifier[]`**</mark>](/api-v2.0/game-components/core/modifier.md)

Returns all modifiers in cheat list.

## <sub>Contains</sub>

`Modifiers.Contains(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                             | Description         |
| -------- | ------------------------------------------------------------------------------------------------ | ------------------- |
| **tree** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | Temp tree to check. |

Checks if modifiers is in list.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/lists/modifiers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/lists/linearprojectiles.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Game Components - Core Objects

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/player.md -->

# Player

Table to work with `CPlayer`. <mark style="color:purple;">**`CPlayer`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>PrepareUnitOrders</sub>

`Player.PrepareUnitOrders(player, type, target, pos, ability, issuer, issuer_npc, [queue], [show_effects], [callback], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                                                                                               | Description                                                                                       |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **player**                                                           | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md)                                                                                       | The player issuing the order.                                                                     |
| **type**                                                             | [<mark style="color:purple;">**`Enum.UnitOrder`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.unitorder)                       | The type of order to be issued.                                                                   |
| **target**                                                           | [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) \| <mark style="color:purple;">**`nil`**</mark>                                       | The target entity, if applicable.                                                                 |
| **pos**                                                              | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)                                                                     | The positional coordinates for the order.                                                         |
| **ability**                                                          | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) \| <mark style="color:purple;">**`nil`**</mark>                                     | The ability for order.                                                                            |
| **issuer**                                                           | [<mark style="color:purple;">**`Enum.PlayerOrderIssuer`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.playerorderissuer)       | The issuer capture mode.                                                                          |
| **issuer\_npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) \| [<mark style="color:purple;">**`CNPC[]`**</mark>](/api-v2.0/game-components/core/npc.md) | The specific NPC or group of NPC that will issue the order.                                       |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                   | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **show\_effects&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                   | If true, visual effects will indicate the position of the order. `(default: false)`               |
| **callback&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                   | If true, the order will be pushed to the `OnPrepareUnitOrders` callback. `(default: false)`       |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                   | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                                                                                    | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                   | If true, the order will be forced by the minimap if possible. `(default: true)`                   |

Provides ability to execute such game actions as moving, attacking, or casting spells etc.

## <sub>HoldPosition</sub>

`Player.HoldPosition(player, issuer_npc, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                         | Description                                                                                       |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **player**                                                          | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The player issuing the order.                                                                     |
| **issuer\_npc**                                                     | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)       | The specific NPC that will issue the order.                                                       |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`         |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                              | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |

Sends the hold position action.

## <sub>AttackTarget</sub>

`Player.AttackTarget(player, issuer_npc, target, [queue], [push], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                         | Description                                                                                       |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **player**                                                           | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The player issuing the order.                                                                     |
| **issuer\_npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)       | The specific NPC that will issue the order.                                                       |
| **target**                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)       | The target NPC.                                                                                   |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will be added to the Dota cast queue. `(default: false)`                       |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will be pushed to the OnPrepareUnitOrders callback. `(default: false)`         |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will bypass internal safety delays for immediate execution. `(default: false)` |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                              | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)`           |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                             | If true, the order will be forced by the minimap if possible. `(default: true)`                   |

Sends the attack target position.

## <sub>GetPlayerID</sub>

`Player.GetPlayerID(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the player ID within the current game session.\
If the player ID is not valid, it will return -1.

## <sub>GetPlayerSlot</sub>

`Player.GetPlayerSlot(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the player slot number within the current game session.

## <sub>GetPlayerTeamSlot</sub>

`Player.GetPlayerTeamSlot(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the team slot number assigned to the player within their respective team.

## <sub>GetName</sub>

`Player.GetName(player):` <mark style="color:purple;">**`string`**</mark>, <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the player nickname and his proname

## <sub>GetProName</sub>

`Player.GetProName(steamId):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                             | Description |
| ----------- | ------------------------------------------------ | ----------- |
| **steamId** | <mark style="color:purple;">**`integer`**</mark> |             |

Returns cached player's proname. Works only in game callbacks

## <sub>GetPlayerData</sub>

`Player.GetPlayerData(player, [output]):` <mark style="color:purple;">**`{valid:boolean, fullyJoined:boolean, fakeClient:boolean, connectionState:integer, steamid:integer, PlusSubscriber:boolean, MVPLastGame:boolean, PlayerName:string, ProName:string}`**</mark>

| Name                                                         | Type                                                                                         | Description                                                                         |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **player**                                                   | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player.                                                                  |
| **output&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`table`**</mark>                                               | Optional reusable table to populate instead of creating a new one. `(default: nil)` |

Returns the player data table.

## <sub>GetTeamData</sub>

`Player.GetTeamData(player):` <mark style="color:purple;">**`{selected_hero_id:integer, kills:integer, assists:integer, deaths:integer, streak:integer, respawnTime:integer, selected_hero_variant:integer, lane_selection_flags:integer, last_buyback_time:number}`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the player team data table.\
Team data is only available for players on the local team.

## <sub>GetNeutralStashItems</sub>

`Player.GetNeutralStashItems(player):` <mark style="color:purple;">**`{item: CItem }[]`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns table with `CItem`s available in the neutral stash.

## <sub>GetTeamPlayer</sub>

`Player.GetTeamPlayer(player, [output]):` <mark style="color:purple;">**`{reliable_gold:integer, unreliable_gold:integer, starting_position:integer, totalearned_gold:integer, totalearned_xp:integer, shared_gold:integer, hero_kill_gold:integer, creep_kill_gold:integer, neutral_kill_gold:integer, courier_gold:integer, bounty_gold:integer, roshan_gold:integer, building_gold:integer, other_gold:integer, comeback_gold:integer, experimental_gold:integer, experimental2_gold:integer, creepdeny_gold:integer, tp_scrolls_purchased:integer, custom_stats:number, income_gold:integer, ward_kill_gold:integer, ability_gold:integer, networth:integer, deny_count:integer, lasthit_count:integer, lasthit_streak:integer, lasthit_multikill:integer, nearby_creep_death_count:integer, claimed_deny_count:integer, claimed_miss_count:integer, miss_count:integer, possible_hero_selection:integer, meta_level:integer, meta_experience:integer, meta_experience_awarded:integer, buyback_cooldown_time:number, buyback_gold_limit_time:number, buyback_cost_time:number, custom_buyback_cooldown:number, stuns:number, healing:number, tower_Kills:integer, roshan_kills:integer, camera_target:CEntity, override_selection_entity:CEntity, observer_wards_placed:integer, sentry_wards_placed:integer, creeps_stacked:integer, camps_stacked:integer, rune_pickups:integer, gold_spent_on_support:integer, hero_damage:integer, wards_purchased:integer, wards_destroyed:integer, commands_issued:integer, gold_spent_on_consumables:integer, gold_spent_on_items:integer, gold_spent_on_buybacks:integer, gold_lost_to_death:integer, is_new_player:boolean, is_guide_player:boolean, acquired_madstone:integer, current_madstone:integer, possible_hero_facet_selection:integer}`**</mark>

| Name                                                         | Type                                                                                         | Description                                                                         |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **player**                                                   | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player.                                                                  |
| **output&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`table`**</mark>                                               | Optional reusable table to populate instead of creating a new one. `(default: nil)` |

Returns **Team Player Data** table

## <sub>GetPlayerNeutralInfo</sub>

`Player.GetPlayerNeutralInfo(player):` <mark style="color:purple;">**`nil`**</mark> | <mark style="color:purple;">**`{acquired_madstone:integer, current_madstone:integer, trinket_choices:integer[], enhancement_choices:integer[], selected_trinkets:integer[], selected_enhancements:integer[], times_crafted:integer[]}`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns info about player's neutral items

## <sub>IsMuted</sub>

`Player.IsMuted(player):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns the player mute status.

## <sub>GetSelectedUnits</sub>

`Player.GetSelectedUnits(player):` [<mark style="color:purple;">**`CNPC[]`**</mark>](/api-v2.0/game-components/core/npc.md)

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns table of selected units by player.

## <sub>AddSelectedUnit</sub>

`Player.AddSelectedUnit(player, NPC):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |
| **NPC**    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)       | To select.         |

Adds unit to player selection.

## <sub>ClearSelectedUnits</sub>

`Player.ClearSelectedUnits(player):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Clears player selection.

## <sub>GetQuickBuyInfo</sub>

`Player.GetQuickBuyInfo(player):` <mark style="color:purple;">**`{m_quickBuyItems:integer[], m_quickBuyIsPurchasable:boolean[]}`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns table with m\_quickBuyItems(item ids) and m\_quickBuyIsPurchasable(table of booleans).

## <sub>GetCourierControllerInfo</sub>

`Player.GetCourierControllerInfo(player):` <mark style="color:purple;">**`{state:integer, shop:integer}`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns table with m\_CourierController structure

## <sub>GetTotalGold</sub>

`Player.GetTotalGold(player):` <mark style="color:purple;">**`integer`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns total gold of player.

## <sub>GetAssignedHero</sub>

`Player.GetAssignedHero(player):` [<mark style="color:purple;">**`CHero`**</mark>](/api-v2.0/game-components/core/hero.md) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns player's assigned hero.

## <sub>GetActiveAbility</sub>

`Player.GetActiveAbility(player):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                         | Description        |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------ |
| **player** | [<mark style="color:purple;">**`CPlayer`**</mark>](/api-v2.0/game-components/core/player.md) | The target player. |

Returns player's active ability.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/player.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/modifier.md -->

# Modifier

Table to work with `CModifier`. You can get modifiers from `NPC.GetModifier`function.

## <sub>GetName</sub>

`Modifier.GetName(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                             | Description             |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get name of |

Returns the name of the modifier.

## <sub>GetClass</sub>

`Modifier.GetClass(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                             | Description |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) |             |

Returns the name of the modifier's class.

## <sub>GetModifierAura</sub>

Deprecated.

`Modifier.GetModifierAura(modifier):` <mark style="color:purple;">**`string`**</mark>

| Name         | Type                                                                                             | Description             |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get aura of |

Should return the name of the modifier's aura, but instead, it returns an empty string in all\
the cases I have tested.

## <sub>GetSerialNumber</sub>

Deprecated.

`Modifier.GetSerialNumber(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                      |
| ------------ | ------------------------------------------------------------------------------------------------ | -------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get serial number of |

Should return the serial number of the modifier, but instead, it returns 0 in all the cases I\
have tested.

## <sub>GetStringIndex</sub>

Deprecated.

`Modifier.GetStringIndex(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                     |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get string index of |

Should return the string index of the modifier, but instead, it returns 0 in all the cases I\
have tested.

## <sub>GetIndex</sub>

`Modifier.GetIndex(modifier):` <mark style="color:purple;">**`GetIndex`**</mark>

| Name         | Type                                                                                             | Description              |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get index of |

Returns the hero's modifier index. The index is an incrementable value with each new modifier\
the NPC gets

## <sub>GetCreationTime</sub>

`Modifier.GetCreationTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                      |
| ------------ | ------------------------------------------------------------------------------------------------ | -------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get creation time of |

Returns the game time when the modifier was created.

## <sub>GetCreationFrame</sub>

`Modifier.GetCreationFrame(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                       |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get creation frame of |

Returns the frame when the modifier was created. You could get current frame count from\
`GlobalVars.GetFrameCount` function.

## <sub>GetLastAppliedTime</sub>

`Modifier.GetLastAppliedTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                          |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get last applied time of |

Returns the game time when the modifier was last applied. Don't know cases when it can be\
different from `GetCreationTime`.

## <sub>GetDuration</sub>

`Modifier.GetDuration(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                 |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get duration of |

Returns the duration of the modifier.

## <sub>GetDieTime</sub>

`Modifier.GetDieTime(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                        |
| ------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get expiration time of |

Returns the game time when the modifier will expire.

## <sub>GetStackCount</sub>

`Modifier.GetStackCount(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                    |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get stack count of |

If there are stacks of the modifier, it returns the amount of stacks; otherwise, it returns\
0\.

## <sub>GetAuraSearchTeam</sub>

Deprecated.

`Modifier.GetAuraSearchTeam(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                         |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get aura search team of |

Returns aura search team of the modifier.

## <sub>GetAuraSearchType</sub>

Deprecated.

`Modifier.GetAuraSearchType(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                         |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get aura search type of |

Returns aura search type of the modifier.

## <sub>GetAuraSearchFlags</sub>

Deprecated.

`Modifier.GetAuraSearchFlags(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                          |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get aura search flags of |

Returns aura search flags of the modifier.

## <sub>GetAuraRadius</sub>

Deprecated.

`Modifier.GetAuraRadius(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                    |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get aura radius of |

Returns aura radius of the modifier.

## <sub>GetTeam</sub>

`Modifier.GetTeam(modifier):` [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.teamnum)

| Name         | Type                                                                                             | Description             |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get team of |

Returns team of the modifier.

## <sub>GetAttributes</sub>

Deprecated.

`Modifier.GetAttributes(modifier):` <mark style="color:purple;">**`integer`**</mark>

| Name         | Type                                                                                             | Description                   |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get attributes of |

Returns the attributes of the modifier.

## <sub>IsAura</sub>

Deprecated.

`Modifier.IsAura(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if the modifier is an aura.

## <sub>IsAuraActiveOnDeath</sub>

Deprecated.

`Modifier.IsAuraActiveOnDeath(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if the modifier aura active on death.

## <sub>GetMarkedForDeletion</sub>

Deprecated.

`Modifier.GetMarkedForDeletion(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if the modifier is marked for deletion.

## <sub>GetAuraIsHeal</sub>

Deprecated.

`Modifier.GetAuraIsHeal(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if aura is heal.

## <sub>GetProvidedByAura</sub>

`Modifier.GetProvidedByAura(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if modifier is provided by an aura.

## <sub>GetPreviousTick</sub>

`Modifier.GetPreviousTick(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                       |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get last tick time of |

Returns the game time of the last modifier tick (\~0.033 seconds).

## <sub>GetThinkInterval</sub>

Deprecated.

`Modifier.GetThinkInterval(modifier):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description                       |
| ------------ | ------------------------------------------------------------------------------------------------ | --------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get think interval of |

Returns the modifier's think interval.

## <sub>GetThinkTimeAccumulator</sub>

Deprecated.

\`Modifier.GetThinkTimeAccumulator(modifier):\` <mark style="color:purple;">\*\*\`number\`\*\*</mark>

| Name         | Type                                                                                             | Description                               |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get think time accumulator of |

Return the modifier's think interval time accumulator.

## <sub>IsCurrentlyInAuraRange</sub>

`Modifier.IsCurrentlyInAuraRange(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if is in aura range.

## <sub>GetAbility</sub>

`Modifier.GetAbility(modifier):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                             | Description                |
| ------------ | ------------------------------------------------------------------------------------------------ | -------------------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get ability of |

Returns the modifier's ability or nil if ability not in the cheat's ability list

## <sub>GetAuraOwner</sub>

`Modifier.GetAuraOwner(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                             | Description |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier    |

Returns the owner of aura

## <sub>GetParent</sub>

`Modifier.GetParent(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                             | Description |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier    |

Returns the parent of modifier

## <sub>GetCaster</sub>

`Modifier.GetCaster(modifier):` [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                             | Description |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier    |

Returns caster of modifier

## <sub>GetState</sub>

`Modifier.GetState(modifier):` <mark style="color:purple;">**`number`**</mark>, <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                             | Description              |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------ |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get state of |

Returns the modifier state masks. See the example.

#### Example

```lua
local m_nEnabledStateMask, m_nDisabledStateMask = Modifier.GetState(mod)
local mod_is_hex = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_HEXED & 1) > 0
local mod_is_stun = (m_nEnabledStateMask >> Enum.ModifierState.MODIFIER_STATE_STUNNED & 1) > 0
```

## <sub>IsDebuff</sub>

`Modifier.IsDebuff(modifier):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                             | Description       |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------------- |
| **modifier** | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to check |

Returns `true` if the modifier is a debuff.

## <sub>GetField</sub>

`Modifier.GetField(modifier, fieldName, [dbgPrint]):` <mark style="color:purple;">**`any`**</mark>

| Name                                                           | Type                                                                                             | Description                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **modifier**                                                   | [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | modifier to get field from               |
| **fieldName**                                                  | <mark style="color:purple;">**`string`**</mark>                                                  | field name                               |
| **dbgPrint&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                 | print possible errors `(default: false)` |

Returns value of the field.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/modifier.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/entity.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/npc.md -->

# NPC

Table to work with `CNPC`. <mark style="color:purple;">**`CNPC`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetOwnerNPC</sub>

`NPC.GetOwnerNPC(npc):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                   | Description           |
| ------- | -------------------------------------------------------------------------------------- | --------------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to get owner from |

Returns owner of the `CNPC`. Works for spirit bear.

## <sub>GetItem</sub>

`NPC.GetItem(npc, name, [isReal]):` [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                   | Description                                                                                                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to get item from                                                                                                           |
| **name**                                                     | <mark style="color:purple;">**`string`**</mark>                                        | name of the item                                                                                                               |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `CItem` by name.

## <sub>HasItem</sub>

`NPC.HasItem(npc, name, [isReal]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                         | Type                                                                                   | Description                                                                                                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check                                                                                                                   |
| **name**                                                     | <mark style="color:purple;">**`string`**</mark>                                        | name of the item                                                                                                               |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `true` if the `CNPC` has item with specified name.

## <sub>HasModifier</sub>

`NPC.HasModifier(npc, name):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                   | Description          |
| -------- | -------------------------------------------------------------------------------------- | -------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check         |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | name of the modifier |

Returns `true` if the `CNPC` has modifier with specified name.

## <sub>GetModifier</sub>

`NPC.GetModifier(npc, name):` [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                   | Description              |
| -------- | -------------------------------------------------------------------------------------- | ------------------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to get modifier from |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | name of the modifier     |

Returns `CModifier` by name.

## <sub>GetModifiers</sub>

\`poperty\_filter\` doesn\`t filter all modifiers every call, it uses already prefiltered list.  \`NPC.GetModifiers(npc, \[poperty\_filter]):\` \[<mark style="color:purple;">\*\*\`CModifier\[]\`\*\*</mark>]\(Modifier.md)

| Name                                                                  | Type                                                                                                                                                                       | Description                                                                                         |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **npc**                                                               | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                                     | npc to get modifiers from                                                                           |
| **poperty\_filter&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.modifierfunction) | Filter modifiers by specified property `(default: Enum.ModifierFunction.MODIFIER_FUNCTION_INVALID)` |

Returns an array of all NPC's `CModifier`s.

## <sub>HasAnyModifier</sub>

`NPC.HasAnyModifier(npc, names):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                 | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                               |             |
| **names** | <mark style="color:purple;">**`string[]`**</mark> \| <mark style="color:purple;">**`table<string, boolean>`**</mark> |             |

Returns `true` if the NPC has any modifier from the given set.\
Accepts either an array `{"mod_a", "mod_b"}` or a hash set `{mod_a = true, mod_b = true}`.\
The hash set form is faster: O(M) hash lookups vs O(M\*N) strcmp, where M = modifier count, N = names count.

## <sub>GetModifierByIndex</sub>

`NPC.GetModifierByIndex(npc, index):` [<mark style="color:purple;">**`CModifier`**</mark>](/api-v2.0/game-components/core/modifier.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                   | Description   |
| --------- | -------------------------------------------------------------------------------------- | ------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) |               |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                       | 1-based index |

Returns the modifier at the given 1-based index, or nil if out of range.\
Use with `NPC.GetModifiers` count or iterate until nil.

## <sub>HasInventorySlotFree</sub>

`NPC.HasInventorySlotFree(npc, [isReal]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                         | Type                                                                                   | Description                                                                                                                    |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **npc**                                                      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check                                                                                                                   |
| **isReal&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | if true, returns only 1-6 slots and neutral item, otherwise returns all items (including backpack and stash) `(default: true)` |

Returns `true` if the `CNPC` has free inventory slot.

## <sub>HasState</sub>

`NPC.HasState(npc, state):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                                                                                                 | Description    |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                               | npc to check   |
| **state** | [<mark style="color:purple;">**`Enum.ModifierState`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.modifierstate) | state to check |

Returns `true` if the `CNPC` has state. The best way to check if the `CNPC` is stunned, silenced, hexed, has BKB immune etc.

## <sub>GetStatesDuration</sub>

`NPC.GetStatesDuration(npc, states, [only_active_states]):` <mark style="color:purple;">**`table`**</mark>

| Name                                                                       | Type                                                                                   | Description                                                                                                                         |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **npc**                                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check                                                                                                                        |
| **states**                                                                 | <mark style="color:purple;">**`integer[]`**</mark>                                     | states to check                                                                                                                     |
| **only\_active\_states&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | if `true` then check only states that active on unit, otherwise check all states. e.g. rooted while debuff immune `(default: true)` |

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

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if waiting to spawn. For example, creeps are waiting to spawn under the ground near the barracks.

## <sub>IsIllusion</sub>

`NPC.IsIllusion(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is illusion.

## <sub>IsVisible</sub>

`NPC.IsVisible(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is visible to local player.

## <sub>IsVisibleToEnemies</sub>

`NPC.IsVisibleToEnemies(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is visible enemies.

## <sub>IsCourier</sub>

`NPC.IsCourier(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a courier.

## <sub>IsRanged</sub>

`NPC.IsRanged(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a ranged unit.

## <sub>IsCreep</sub>

`NPC.IsCreep(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a creep.

## <sub>IsLaneCreep</sub>

`NPC.IsLaneCreep(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a lane creep.

## <sub>IsStructure</sub>

`NPC.IsStructure(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a structure.

## <sub>IsTower</sub>

`NPC.IsTower(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a tower.

## <sub>GetUnitType</sub>

`NPC.GetUnitType(npc):` [<mark style="color:purple;">**`Enum.UnitTypeFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.unittypeflags)

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns unit type flags.

## <sub>IsConsideredHero</sub>

`NPC.IsConsideredHero(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if it is unit a considered a hero for targeting purposes.

## <sub>IsBarracks</sub>

`NPC.IsBarracks(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a barracks.

## <sub>IsAncient</sub>

`NPC.IsAncient(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is an ancient creeps.

## <sub>IsRoshan</sub>

`NPC.IsRoshan(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a Roshan.

## <sub>IsNeutral</sub>

`NPC.IsNeutral(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a neutral. Neutral creeps, ancient creeps.

## <sub>IsHero</sub>

`NPC.IsHero(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a hero.

## <sub>IsWard</sub>

`NPC.IsWard(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a ward.

## <sub>IsMeepoClone</sub>

`NPC.IsMeepoClone(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is a meepo clone.

## <sub>IsEntityInRange</sub>

`NPC.IsEntityInRange(npc, npc2, range):` <mark style="color:purple;">**`boolean`**</mark>

| Name      | Type                                                                                   | Description    |
| --------- | -------------------------------------------------------------------------------------- | -------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check   |
| **npc2**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check   |
| **range** | <mark style="color:purple;">**`number`**</mark>                                        | range to check |

Returns `true` if the `CNPC` in range of other `CNPC`.

## <sub>IsPositionInRange</sub>

`NPC.IsPositionInRange(npc, pos, range, [hull]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                       | Type                                                                                                           | Description                               |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **npc**                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                         | npc to check                              |
| **pos**                                                    | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | position to check                         |
| **range**                                                  | <mark style="color:purple;">**`number`**</mark>                                                                | range to check                            |
| **hull&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                | hull just added to range `(default: 0.0)` |

Returns `true` if the `CNPC` in range of position.

## <sub>IsLinkensProtected</sub>

`NPC.IsLinkensProtected(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is protected by Linkens Sphere.

## <sub>IsMirrorProtected</sub>

`NPC.IsMirrorProtected(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is protected by Mirror Shield.

## <sub>IsChannellingAbility</sub>

Do not work for items.

`NPC.IsChannellingAbility(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description  |
| ------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |

Returns `true` if the `CNPC` is channeling ability. Black Hole, Life Drain, etc.

## <sub>GetChannellingAbility</sub>

`NPC.GetChannellingAbility(npc):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the currently channelling `CAbility`.

## <sub>IsRunning</sub>

`NPC.IsRunning(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` is running.

## <sub>IsAttacking</sub>

`NPC.IsAttacking(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` is attacking.

## <sub>IsSilenced</sub>

`NPC.IsSilenced(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` is silenced.

## <sub>IsStunned</sub>

`NPC.IsStunned(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` is stunned.

## <sub>HasAegis</sub>

`NPC.HasAegis(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` has aegis.

## <sub>IsKillable</sub>

`NPC.IsKillable(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns `true` if the `CNPC` has killable. Example: false if affected by Eul.

## <sub>GetActivity</sub>

`NPC.GetActivity(npc):` [<mark style="color:purple;">**`Enum.GameActivity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.gameactivity)

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the `CNPC` activity, such as running, attacking, casting, etc.

## <sub>GetAnimationInfo</sub>

`NPC.GetAnimationInfo(npc):` <mark style="color:purple;">**`{sequence:integer, cycle:number, name:string, mdl_name:string}`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns information about the current animation of the `CNPC`.

## <sub>GetAttackRange</sub>

`NPC.GetAttackRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the base attack range of the `CNPC`.

## <sub>GetAttackRangeBonus</sub>

`NPC.GetAttackRangeBonus(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the bonus attack range of the `CNPC`.

## <sub>GetCastRangeBonus</sub>

`NPC.GetCastRangeBonus(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the bonus cast range of the `CNPC`.

## <sub>GetPhysicalArmorValue</sub>

`NPC.GetPhysicalArmorValue(npc, [excludeWhiteArmor]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                    | Type                                                                                   | Description                           |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------- |
| **npc**                                                                 | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                            |
| **excludeWhiteArmor&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | exclude white armor `(default: true)` |

Returns the physical armor value of the `CNPC`.

## <sub>GetPhysicalDamageReduction</sub>

`NPC.GetPhysicalDamageReduction(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the physical damage reduction value of the `CNPC`.

## <sub>GetArmorDamageMultiplier</sub>

`NPC.GetArmorDamageMultiplier(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the physical damage multiplier value of the `CNPC`.

## <sub>GetMagicalArmorValue</sub>

`NPC.GetMagicalArmorValue(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the magical armor value of the `CNPC`.

## <sub>GetMagicalArmorDamageMultiplier</sub>

`NPC.GetMagicalArmorDamageMultiplier(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the magical damage multiplier value of the `CNPC`.

## <sub>GetIncreasedAttackSpeed</sub>

`NPC.GetIncreasedAttackSpeed(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                   | Description                                      |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | ignore temporary attack speed `(default: false)` |

Returns increased attack speed of the `CNPC`.

## <sub>GetAttacksPerSecond</sub>

`NPC.GetAttacksPerSecond(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                   | Description                                      |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | ignore temporary attack speed `(default: false)` |

Returns the number of attacks per second that the `CNPC` can deal.

## <sub>GetAttackTime</sub>

`NPC.GetAttackTime(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the amount of time needed for the `CNPC` to perform an attack.

## <sub>GetAttackSpeed</sub>

`NPC.GetAttackSpeed(npc, [ignore_temp_attack_speed]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                              | Type                                                                                   | Description                                      |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **npc**                                                                           | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                                       |
| **ignore\_temp\_attack\_speed&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | ignore temporary attack speed `(default: false)` |

Returns the attack speed of the `CNPC`.

## <sub>GetBaseAttackSpeed</sub>

`NPC.GetBaseAttackSpeed(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the base attack speed of the `CNPC`.

## <sub>GetHullRadius</sub>

`NPC.GetHullRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the model interaction radius of the `CNPC`.

## <sub>GetPaddedCollisionRadius</sub>

`NPC.GetPaddedCollisionRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the collision hull radius (including padding) of this `NPC`.

## <sub>GetCollisionPadding</sub>

`NPC.GetCollisionPadding(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the collision including padding of this `NPC`.

## <sub>GetPaddedCollisionRadius</sub>

`NPC.GetPaddedCollisionRadius(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the ring radius of this `NPC`.

## <sub>GetProjectileCollisionSize</sub>

see: <https://dota2.fandom.com/wiki/Unit\\_Size#Collision\\_Size>

`NPC.GetProjectileCollisionSize(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the collision size of the `CNPC`. Collision size is the internal size that prevents other units from passing through.

## <sub>GetTurnRate</sub>

see: <https://dota2.fandom.com/wiki/Turn\\_rate>

`NPC.GetTurnRate(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the turn rate, which is the speed at which the `CNPC` can turn.

## <sub>GetAttackAnimPoint</sub>

see: <https://dota2.fandom.com/wiki/Attack\\_animation>

`NPC.GetAttackAnimPoint(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the attack animation point, `nil` if not found.

## <sub>GetAttackProjectileSpeed</sub>

see: <https://dota2.fandom.com/wiki/Projectile\\_Speed>

`NPC.GetAttackProjectileSpeed(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the attack projectile speed, `nil` if not found.

## <sub>IsTurning</sub>

`NPC.IsTurning(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns true if the `CNPC` is turning.

## <sub>GetAngleDiff</sub>

doesn't work for creeps

`NPC.GetAngleDiff(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the remaining degree angle needed to complete the turn of the `CNPC`.

## <sub>GetPhysicalArmorMainValue</sub>

`NPC.GetPhysicalArmorMainValue(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the (main) white armor of the `CNPC`.

## <sub>GetTimeToFace</sub>

`NPC.GetTimeToFace(npc, target):` <mark style="color:purple;">**`number`**</mark>

| Name       | Type                                                                                   | Description |
| ---------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc**    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | source npc  |
| **target** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the amount of time needed for the source `CNPC` to face the target `CNPC`.

## <sub>FindRotationAngle</sub>

`NPC.FindRotationAngle(npc, pos):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                           | Description                         |
| ------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                         | source npc                          |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | position to find the rotation angle |

Returns the rotation angle of the `CNPC`.

## <sub>GetTimeToFacePosition</sub>

`NPC.GetTimeToFacePosition(npc, pos):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                                           | Description     |
| ------- | -------------------------------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                         | source npc      |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | target position |

Returns the amount of time needed for the source `CNPC` to face a specific position.

## <sub>FindFacingNPC</sub>

`NPC.FindFacingNPC(npc, ignoreNpc, [team_type], [angle], [distance]):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                                                                       | Description                            |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **npc**                                                          | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                     | source npc                             |
| **ignoreNpc**                                                    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                     | ignore npc                             |
| **team\_type&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.teamtype) | team type `(default: TEAM_BOTH)`       |
| **angle&#x20;**<mark style="color:orange;">**`[?]`**</mark>      | <mark style="color:purple;">**`number`**</mark>                                                                                                            | max angle to check `(default: 0.0)`    |
| **distance&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                                                                            | max distance to check `(default: 0.0)` |

Returns the `CNPC` that the source `CNPC` is currently facing.

## <sub>GetBaseSpeed</sub>

`NPC.GetBaseSpeed(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the base move speed of the `CNPC`.

## <sub>GetMoveSpeed</sub>

`NPC.GetMoveSpeed(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the move speed of the `CNPC`.

## <sub>GetMinDamage</sub>

`NPC.GetMinDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the minumum attack damage of the `CNPC`.

## <sub>GetBonusDamage</sub>

`NPC.GetBonusDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the bonus attack damage of the `CNPC`.

## <sub>GetTrueDamage</sub>

`NPC.GetTrueDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the minumum attack damage + bonus damage of the `CNPC`.

## <sub>GetTrueMaximumDamage</sub>

`NPC.GetTrueMaximumDamage(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the maximum attack damage + bonus damage of the `CNPC`.

## <sub>GetItemByIndex</sub>

`NPC.GetItemByIndex(npc, index):` [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                   | Description |
| --------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                       | item index  |

Returns the `CItem` by index.

## <sub>GetAbilityByIndex</sub>

`NPC.GetAbilityByIndex(npc, index):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                   | Description   |
| --------- | -------------------------------------------------------------------------------------- | ------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc    |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                       | ability index |

Returns the `CAbility` by index.

## <sub>GetAbilityByActivity</sub>

`NPC.GetAbilityByActivity(npc, activity):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                                                                               | Description             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                             | npc to get ability from |
| **activity** | [<mark style="color:purple;">**`Enum.GameActivity`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.gameactivity) | game activity           |

Returns the `CAbility` by game activity.

## <sub>GetAbility</sub>

`NPC.GetAbility(npc, name):` [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) | <mark style="color:purple;">**`nil`**</mark>

| Name     | Type                                                                                   | Description  |
| -------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc   |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | ability name |

Returns the `CAbility` by name.

## <sub>HasAbility</sub>

`NPC.HasAbility(npc, name):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                   | Description  |
| -------- | -------------------------------------------------------------------------------------- | ------------ |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc   |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | ability name |

Returns `true` if the `CNPC` has this ability.

## <sub>GetMana</sub>

`NPC.GetMana(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the current mana of the `CNPC`.

## <sub>GetMaxMana</sub>

`NPC.GetMaxMana(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the maximum mana of the `CNPC`.

## <sub>GetManaRegen</sub>

`NPC.GetManaRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the mana regeneration rate of the `CNPC`.

## <sub>GetHealthRegen</sub>

`NPC.GetHealthRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the health regeneration rate of the `CNPC`.

## <sub>CalculateHealthRegen</sub>

Works for creeps but really slow.

`NPC.CalculateHealthRegen(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Iterate over all modifiers and returns the health regeneration rate of the `CNPC`.

## <sub>GetCurrentLevel</sub>

`NPC.GetCurrentLevel(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the current level of the `CNPC`.

## <sub>GetDayTimeVisionRange</sub>

`NPC.GetDayTimeVisionRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the day-time vision range of the `CNPC`.

## <sub>GetNightTimeVisionRange</sub>

`NPC.GetNightTimeVisionRange(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the night-time vision range of the `CNPC`.

## <sub>GetUnitName</sub>

`NPC.GetUnitName(npc):` <mark style="color:purple;">**`string`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the unit-name of the `CNPC`.

## <sub>GetHealthBarOffset</sub>

`NPC.GetHealthBarOffset(npc, [checkOverride]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                                | Type                                                                                   | Description                                            |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **npc**                                                             | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                                             |
| **checkOverride&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                       | returns override offset if it exists `(default: true)` |

Returns the health bar offset of the `CNPC`.

## <sub>GetUnitNameIndex</sub>

index can change when new unit are added

`NPC.GetUnitNameIndex(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns unit-name index of the `CNPC`.

## <sub>GetAttachment</sub>

`NPC.GetAttachment(npc, name):` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

| Name     | Type                                                                                   | Description                            |
| -------- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                             |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | attachment name. e.g. "attach\_hitloc" |

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

`NPC.GetAttachmentByIndex(npc, index):` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

| Name      | Type                                                                                   | Description      |
| --------- | -------------------------------------------------------------------------------------- | ---------------- |
| **npc**   | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc       |
| **index** | <mark style="color:purple;">**`integer`**</mark>                                       | attachment index |

Returns the attachment position of the `CNPC` by the specified index.

## <sub>GetAttachmentIndexByName</sub>

`NPC.GetAttachmentIndexByName(npc, name):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                   | Description                            |
| -------- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| **npc**  | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc                             |
| **name** | <mark style="color:purple;">**`string`**</mark>                                        | attachment name. e.g. "attach\_hitloc" |

Returns the attachment index of the `CNPC` by the name.

## <sub>GetBountyXP</sub>

`NPC.GetBountyXP(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the amount of experience points (XP) you can earn for killing the `CNPC`.

## <sub>GetGoldBountyMin</sub>

`NPC.GetGoldBountyMin(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the minimum amount gold you can earn for killing the `CNPC`.

## <sub>GetGoldBountyMax</sub>

`NPC.GetGoldBountyMax(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description |
| ------- | -------------------------------------------------------------------------------------- | ----------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | target npc  |

Returns the maximum amount gold you can earn for killing the `CNPC`.

## <sub>MoveTo</sub>

`NPC.MoveTo(npc, position, [queue], [show], [callback], [executeFast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                           | Description                                                                             |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **npc**                                                              | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                         | The target NPC.                                                                         |
| **position**                                                         | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | The destination position.                                                               |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                               | Add the order to the Dota queue. `(default: false)`                                     |
| **show&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                                               | Show the order position. `(default: false)`                                             |
| **callback&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | <mark style="color:purple;">**`boolean`**</mark>                                                               | Push the order to the OnPrepareUnitOrders callback. `(default: false)`                  |
| **executeFast&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`boolean`**</mark>                                                               | Place the order at the top of the queue. `(default: false)`                             |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                               | If true, the order will be forced by the minimap if possible. `(default: true)`         |

Initiates an order for the `CNPC` to move to a specified position.

## <sub>SetZDelta</sub>

`NPC.SetZDelta(npc, z):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |
| **z**   | <mark style="color:purple;">**`number`**</mark>                                        | Z pos           |

Sets the Z position of the `CNPC` model.

## <sub>HasScepter</sub>

`NPC.HasScepter(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns `true` if the `CNPC` has or consumed Aghanim Scepter.

## <sub>HasShard</sub>

`NPC.HasShard(npc):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns `true` if the `CNPC` has or consumed Aghanim Shard.

## <sub>GetScepterUpgradeID</sub>

`NPC.GetScepterUpgradeID(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns index of selected scepter upgrade.

## <sub>GetShardUpgradeID</sub>

`NPC.GetShardUpgradeID(npc):` <mark style="color:purple;">**`integer`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns index of selected shard upgrade.

## <sub>SequenceDuration</sub>

`NPC.SequenceDuration(npc, sequence):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                   | Description         |
| ------------ | -------------------------------------------------------------------------------------- | ------------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC.     |
| **sequence** | <mark style="color:purple;">**`integer`**</mark>                                       | The sequence index. |

Returns sequence duration of the npc with the specified sequence index.

## <sub>GetSecondsPerAttack</sub>

`NPC.GetSecondsPerAttack(npc, bIgnoreTempAttackSpeed):` <mark style="color:purple;">**`number`**</mark>

| Name                       | Type                                                                                   | Description                    |
| -------------------------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| **npc**                    | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC.                |
| **bIgnoreTempAttackSpeed** | <mark style="color:purple;">**`boolean`**</mark>                                       | Ignore temporary attack speed. |

Returns the seconds per attack of the npc.

## <sub>GetBarriers</sub>

`NPC.GetBarriers(npc):` <mark style="color:purple;">**`{physical:{total:number, current:number}, magic:{total:number, current:number}, all:{total:number, current:number}}`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns a table with information about the barriers of the `CNPC`.

## <sub>GetGlow</sub>

`NPC.GetGlow(npc):` <mark style="color:purple;">**`{m_bSuppressGlow:boolean, m_bFlashing:boolean, m_bGlowing:boolean, m_iGlowType:integer, r:integer, g:integer, b:integer}`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns a table with information about the current glow effect of the `CNPC`.

## <sub>SetGlow</sub>

`NPC.SetGlow(npc, suppress_glow, flashing, glowing, glow_type, r, g, b):` <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                   | Description     |
| ------------------ | -------------------------------------------------------------------------------------- | --------------- |
| **npc**            | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |
| **suppress\_glow** | <mark style="color:purple;">**`boolean`**</mark>                                       | suppress\_glow  |
| **flashing**       | <mark style="color:purple;">**`boolean`**</mark>                                       | flashing        |
| **glowing**        | <mark style="color:purple;">**`boolean`**</mark>                                       | glowing         |
| **glow\_type**     | <mark style="color:purple;">**`integer`**</mark>                                       | glow type       |
| **r**              | <mark style="color:purple;">**`integer`**</mark>                                       | r factor        |
| **g**              | <mark style="color:purple;">**`integer`**</mark>                                       | g factor        |
| **b**              | <mark style="color:purple;">**`integer`**</mark>                                       | b factor        |

Sets the `CNPC` glow effect.

## <sub>SetColor</sub>

`NPC.SetColor(npc, r, g, b):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |
| **r**   | <mark style="color:purple;">**`integer`**</mark>                                       | r factor        |
| **g**   | <mark style="color:purple;">**`integer`**</mark>                                       | g factor        |
| **b**   | <mark style="color:purple;">**`integer`**</mark>                                       | b factor        |

Sets the `CNPC` model color.

## <sub>IsInRangeOfShop</sub>

`NPC.IsInRangeOfShop(npc, shop_type, [specific]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                           | Type                                                                                                                                                       | Description                              |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **npc**                                                        | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                     | The target NPC.                          |
| **shop\_type**                                                 | [<mark style="color:purple;">**`Enum.ShopType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.shoptype) | Shop type to check.                      |
| **specific&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                                                                           | No idea what is that. `(default: false)` |

Checks if the `CNPC` is in range of a shop.

## <sub>GetBaseSpellAmp</sub>

`NPC.GetBaseSpellAmp(npc):` <mark style="color:purple;">**`number`**</mark>

| Name    | Type                                                                                   | Description     |
| ------- | -------------------------------------------------------------------------------------- | --------------- |
| **npc** | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | The target NPC. |

Returns the base spell amplification of the `CNPC`.

## <sub>GetModifierProperty</sub>

`NPC.GetModifierProperty(npc, property):` <mark style="color:purple;">**`number`**</mark>

| Name         | Type                                                                                                                                                                       | Description     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                                     | The target NPC. |
| **property** | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.modifierfunction) | Property enum.  |

Returns the property value for the `CNPC`.

## <sub>IsControllableByPlayer</sub>

`NPC.IsControllableByPlayer(npc, playerId):` <mark style="color:purple;">**`boolean`**</mark>

| Name         | Type                                                                                   | Description  |
| ------------ | -------------------------------------------------------------------------------------- | ------------ |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | npc to check |
| **playerId** | <mark style="color:purple;">**`integer`**</mark>                                       | player id    |

Returns `true` if npc is controllable by player.

## <sub>GetModifierPropertyHighest</sub>

Fixes the issue when you have multiple Kaya items that actually don't stack.

\`NPC.GetModifierPropertyHighest(npc, property):\` <mark style="color:purple;">\*\*\`number\`\*\*</mark>

| Name         | Type                                                                                                                                                                       | Description     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **npc**      | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)                                                                                     | The target NPC. |
| **property** | [<mark style="color:purple;">**`Enum.ModifierFunction`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.modifierfunction) | Property enum.  |

Returns the hieghest property value for the `CNPC`.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/npc.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/hero.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/ability.md -->

# Ability

Table to work with `CAbility`.

<mark style="color:purple;">**`CAbility`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetOwner</sub>

`Ability.GetOwner(ability):` [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability owner.

## <sub>IsBasic</sub>

`Ability.IsBasic(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is basic.

## <sub>IsUltimate</sub>

`Ability.IsUltimate(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is an ultimate.

## <sub>IsAttributes</sub>

`Ability.IsAttributes(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is an attribute or a talent.

## <sub>GetType</sub>

`Ability.GetType(ability):` [<mark style="color:purple;">**`Enum.AbilityTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.abilitytypes)

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability type.

## <sub>GetBehavior</sub>

`Ability.GetBehavior(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.AbilityBehavior`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.abilitybehavior)

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns the ability type.

## <sub>IsPassive</sub>

`Ability.IsPassive(ability, [from_static_data]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns `true` if the ability is passive.

## <sub>GetTargetTeam</sub>

`Ability.GetTargetTeam(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.TargetTeam`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.targetteam)

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns the target team of this Ability.

## <sub>GetTargetType</sub>

`Ability.GetTargetType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.TargetType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.targettype)

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns the target type of this Ability.

## <sub>GetTargetFlags</sub>

`Ability.GetTargetFlags(ability):` [<mark style="color:purple;">**`Enum.TargetFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.targetflags)

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the target flags of this Ability.

## <sub>GetDamageType</sub>

`Ability.GetDamageType(ability):` [<mark style="color:purple;">**`Enum.DamageTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.damagetypes)

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the damage type of this Ability.

## <sub>GetImmunityType</sub>

`Ability.GetImmunityType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.ImmunityTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.immunitytypes)

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns the immunity type of this Ability.

## <sub>GetDispellableType</sub>

`Ability.GetDispellableType(ability, [from_static_data]):` [<mark style="color:purple;">**`Enum.DispellableTypes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.dispellabletypes)

| Name                                                                     | Type                                                                                           | Description                                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                  |
| **from\_static\_data&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | if `true` will check from ability static data `(default: false)` |

Returns the dispel type of this Ability.

## <sub>GetLevelSpecialValueFor</sub>

`Ability.GetLevelSpecialValueFor(ability, name, [lvl]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                      | Type                                                                                           | Description                                                                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **ability**                                               | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                                             |
| **name**                                                  | <mark style="color:purple;">**`string`**</mark>                                                | Special value name. Can be found in the ability KV file. (`assets/data/npc_abilities.json`) |
| **lvl&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>                                               | Ability level, if -1 will automatically get lvl. `(default: -1)`                            |

WRONG API FIX ME IT MUST BE GetSpecialValueFor.

## <sub>IsReady</sub>

`Ability.IsReady(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is ready to use.

## <sub>SecondsSinceLastUse</sub>

`Ability.SecondsSinceLastUse(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the number of seconds passed from the last usage of the ability. Will return -1 if\
the ability is not on the cooldown.

## <sub>GetDamage</sub>

`Ability.GetDamage(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability damage from assets/data/npc\_abilities.json field. Will return 0.0 if the\
ability doesn't contain this field.

## <sub>GetHealthCost</sub>

`Ability.GetHealthCost(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability's health cost.

## <sub>GetLevel</sub>

`Ability.GetLevel(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the current ability level.

## <sub>GetCastPoint</sub>

`Ability.GetCastPoint(ability, [include_modifiers]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                                     | Type                                                                                           | Description       |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ----------------- |
| **ability**                                                              | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                   |
| **include\_modifiers&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | `(default: true)` |

Gets the cast delay of this Ability.

## <sub>GetCastPointModifier</sub>

`Ability.GetCastPointModifier(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Gets the cast delay modifier of this Ability.

## <sub>IsCastable</sub>

`Ability.IsCastable(ability, [mana]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                       | Type                                                                                           | Description      |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------- |
| **ability**                                                | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                  |
| **mana&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                | `(default: 0.0)` |

Returns `true` if the ability is currently castable. Checks for mana cost, cooldown, level,\
and slot for items.

## <sub>IsChannelling</sub>

`Ability.IsChannelling(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is in channeling state. Example: teleport, rearm, powershot\
etc.

## <sub>GetName</sub>

`Ability.GetName(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability name or empty string.

## <sub>GetBaseName</sub>

`Ability.GetBaseName(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability base name or empty string.

## <sub>IsInnate</sub>

`Ability.IsInnate(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is innate.

## <sub>IsInnatePassive</sub>

`Ability.IsInnatePassive(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is passive innate.

## <sub>GetMaxLevel</sub>

`Ability.GetMaxLevel(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns ability's max level.

## <sub>IsGrantedByFacet</sub>

`Ability.IsGrantedByFacet(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` when abiliti is granted by facet.

## <sub>CanBeExecuted</sub>

`Ability.CanBeExecuted(ability):` [<mark style="color:purple;">**`Enum.AbilityCastResult`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.abilitycastresult)

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `-1` if ability can be executed.

## <sub>IsOwnersManaEnough</sub>

`Ability.IsOwnersManaEnough(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if enough mana for cast.

## <sub>CastNoTarget</sub>

`Ability.CastNoTarget(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                           | Description                                                                             |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                               | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Casts the ability that doesn't require a target or position.

## <sub>CastPosition</sub>

`Ability.CastPosition(ability, pos, [queue], [push], [execute_fast], [identifier], [force_minimap]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                 | Type                                                                                                           | Description                                                                             |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                          | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md)                 |                                                                                         |
| **pos**                                                              | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Order position.                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                                               | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>           | <mark style="color:purple;">**`boolean`**</mark>                                                               | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`boolean`**</mark>                                                               | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`string`**</mark>                                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |
| **force\_minimap&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                               | If true, the order will be forced by the minimap if possible. `(default: true)`         |

Casts the ability at a specified position.

## <sub>CastTarget</sub>

`Ability.CastTarget(ability, target, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                           | Description                                                                             |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                                         |
| **target**                                                          | [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md)         | Order target.                                                                           |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                               | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Casts the ability on a specified target.

## <sub>Toggle</sub>

`Ability.Toggle(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                           | Description                                                                             |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                               | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Toggles the ability. Example: Armlet.

## <sub>ToggleMod</sub>

`Ability.ToggleMod(ability, [queue], [push], [execute_fast], [identifier]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                           | Description                                                                             |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ability**                                                         | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |                                                                                         |
| **queue&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | <mark style="color:purple;">**`boolean`**</mark>                                               | Will add order to the cast queue. `(default: false)`                                    |
| **push&#x20;**<mark style="color:orange;">**`[?]`**</mark>          | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to the OnPrepareUnitOrders callback. `(default: false)`                 |
| **execute\_fast&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                               | Will push order to start of the order's list. `(default: false)`                        |
| **identifier&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`string`**</mark>                                                | The identifier which will be passed to `OnPrepareUnitOrders` callback. `(default: nil)` |

Toggles the ability modifier. Example: Frost Arrows, Medusa's Shield.

## <sub>GetDefaultName</sub>

`Ability.GetDefaultName(ability_name):` <mark style="color:purple;">**`string`**</mark> | <mark style="color:purple;">**`nil`**</mark>

| Name              | Type                                            | Description |
| ----------------- | ----------------------------------------------- | ----------- |
| **ability\_name** | <mark style="color:purple;">**`string`**</mark> |             |

Returns the default ability icon name from items\_game.txt

## <sub>CanBeUpgraded</sub>

`Ability.CanBeUpgraded(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns if the ability is upgradable with a specific reason.

## <sub>GetAbilityID</sub>

`Ability.GetAbilityID(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns ability id

## <sub>GetIndex</sub>

`Ability.GetIndex(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the index of the ability in the ability owner's list. The index can be used in\
NPC.GetAbilityByIndex later.

## <sub>GetCastRange</sub>

`Ability.GetCastRange(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the cast range of the ability.

## <sub>IsHidden</sub>

`Ability.IsHidden(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if ability is hidden. Example: Zeus's Nimbus before purchasing agh.

## <sub>IsActivated</sub>

`Ability.IsActivated(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is in an activated state.

## <sub>GetDirtyButtons</sub>

`Ability.GetDirtyButtons(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns we don't know what :).

## <sub>GetToggleState</sub>

`Ability.GetToggleState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns if the ability is toggled. Example: Medusa's Shield.

## <sub>IsInAbilityPhase</sub>

`Ability.IsInAbilityPhase(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is in the cast state. Examples: Nature's Prophet's Teleport,\
Meepo's Poof.

## <sub>GetCooldown</sub>

`Ability.GetCooldown(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the amount of time before the ability can be cast.

## <sub>GetCooldownLength</sub>

`Ability.GetCooldownLength(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the amount of time the ability couldn't be cast after being used.

## <sub>GetManaCost</sub>

`Ability.GetManaCost(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the ability mana cost.

## <sub>GetAutoCastState</sub>

`Ability.GetAutoCastState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the autocast state of the ability.

## <sub>GetAltCastState</sub>

`Ability.GetAltCastState(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the alt cast state of the ability. Example: Doom's Devour.

## <sub>GetChannelStartTime</sub>

`Ability.GetChannelStartTime(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the gametime the channeling of the ability will start. Requires the ability to be in\
the cast state when called.

## <sub>GetCastStartTime</sub>

`Ability.GetCastStartTime(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the gametime the ability will be casted. Requires the ability to be in the cast state\
when called.

## <sub>IsInIndefinateCooldown</sub>

`Ability.IsInIndefinateCooldown(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the cooldown of the ability is indefinite.

## <sub>IsInIndefinateCooldown</sub>

`Ability.IsInIndefinateCooldown(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the cooldown of the ability is frozen.

## <sub>GetOverrideCastPoint</sub>

`Ability.GetOverrideCastPoint(ability):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the overridden cast point. Example: Arcane Blink.

## <sub>IsStolen</sub>

`Ability.IsStolen(ability):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns `true` if the ability is stolen.

## <sub>GetCurrentCharges</sub>

`Ability.GetCurrentCharges(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the number of charges available.

## <sub>ChargeRestoreTimeRemaining</sub>

`Ability.ChargeRestoreTimeRemaining(ability):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the remaining time for the next charge to restore.

## <sub>GetKeybind</sub>

`Ability.GetKeybind(ability):` <mark style="color:purple;">**`string`**</mark>

| Name        | Type                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **ability** | [<mark style="color:purple;">**`CAbility`**</mark>](/api-v2.0/game-components/core/ability.md) |             |

Returns the keybind of the ability.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/ability.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/item.md -->

# Item

Table to work with `CItem`.

<mark style="color:purple;">**`CItem`**</mark> extends <mark style="color:purple;">**`CAbility`**</mark>

## <sub>IsCombinable</sub>

`Item.IsCombinable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is combinable. I'm not sure if non-combinable items even exist.

## <sub>IsPermanent</sub>

`Item.IsPermanent(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is permanent. I'm not sure what permanent items is, but for items with stacks this function returns `false`.

## <sub>IsStackable</sub>

`Item.IsStackable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is stackable. e.g tangoes, wards, etc.

## <sub>IsRecipe</sub>

`Item.IsRecipe(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is recipe.

## <sub>GetSharability</sub>

`Item.GetSharability(item):` [<mark style="color:purple;">**`Enum.ShareAbility`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.shareability)

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns item's sharability type.

## <sub>IsDroppable</sub>

`Item.IsDroppable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is droppable.

## <sub>IsPurchasable</sub>

`Item.IsPurchasable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is purchasable.

## <sub>IsSellable</sub>

`Item.IsSellable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item is sellable.

## <sub>RequiresCharges</sub>

`Item.RequiresCharges(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if the item requires charges. e.g. urn, vessel etc.

## <sub>IsKillable</sub>

`Item.IsKillable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item is destroyable by autoatack.

## <sub>IsDisassemblable</sub>

`Item.IsDisassemblable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item is disassemblable.

## <sub>IsAlertable</sub>

`Item.IsAlertable(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item is alertable. e.g. smoke, mekansm, arcane boots etc.

## <sub>GetInitialCharges</sub>

`Item.GetInitialCharges(item):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns initial charges of the item. e.g. 3 for bottle, 1 for dust etc.

## <sub>CastsOnPickup</sub>

`Item.CastsOnPickup(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

No idea what this function does.

## <sub>GetCurrentCharges</sub>

`Item.GetCurrentCharges(item):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns amount of current charges.

## <sub>GetSecondaryCharges</sub>

`Item.GetSecondaryCharges(item):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns amount of secondary charges. e.g. pack of both type of wards.

## <sub>IsCombineLocked</sub>

`Item.IsCombineLocked(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item locked for combining.

## <sub>IsMarkedForSell</sub>

`Item.IsMarkedForSell(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item is marked for sell.

## <sub>GetPurchaseTime</sub>

`Item.GetPurchaseTime(item):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns the game time when the item was purchased. If the item was assembled from other items, It returns the purchase time of the item that had the lowest\
index at the moment of assembling.

## <sub>GetAssembledTime</sub>

`Item.GetAssembledTime(item):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns the game time when the item was assembled. If the item was not assembled, returns time when the item was purchased.

## <sub>PurchasedWhileDead</sub>

`Item.PurchasedWhileDead(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `true` if item was purchased while dead.

## <sub>CanBeUsedOutOfInventory</sub>

`Item.CanBeUsedOutOfInventory(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

No idea which specific item example could be used out of inventory.

## <sub>IsItemEnabled</sub>

`Item.IsItemEnabled(item):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns `false` if item has CD after moving from stash.

## <sub>GetEnableTime</sub>

Could be less than current game time if item is already enabled.

`Item.GetEnableTime(item):` <mark style="color:purple;">**`number`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns game time when item will be enabled.

## <sub>GetPlayerOwnerID</sub>

`Item.GetPlayerOwnerID(item):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns player ID who owns the item.

## <sub>GetCost</sub>

`Item.GetCost(item):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **item** | [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) |             |

Returns item cost.

## <sub>GetStockCount</sub>

Item id can be found in \`assets/data/items.json\` file in cheat folder.

\`Item.GetStockCount(item\_id, \[team]):\` <mark style="color:purple;">\*\*\`integer\`\*\*</mark>

| Name                                                       | Type                                                                                                                                                     | Description                                                                        |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **item\_id**                                               | <mark style="color:purple;">**`integer`**</mark>                                                                                                         |                                                                                    |
| **team&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.TeamNum`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.teamnum) | - Optional. Default is local player's team. `(default: Enum.TeamNum.TEAM_RADIANT)` |

Returns amount of remaining items in shop by item id.

#### Example

```lua
-- "item_ward_observer": {
--     "ID": "42",
Log.Write("Observers available: " .. Item.GetStockCount(42))
```

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/item.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/rune.md -->

# Rune

Table to work with `CRune`.<mark style="color:purple;">**`CRune`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetRuneType</sub>

`Rune.GetRuneType(rune):` [<mark style="color:purple;">**`Enum.RuneType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.runetype)

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **rune** | [<mark style="color:purple;">**`CRune`**</mark>](/api-v2.0/game-components/core/rune.md) |             |

Returns `Enum.RuneType` the rune type.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/rune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tower.md -->

# Tower

Table to work with `CTower`.<mark style="color:purple;">**`CTower`**</mark> extends <mark style="color:purple;">**`CNPC`**</mark>

## <sub>GetAttackTarget</sub>

`Tower.GetAttackTarget(tower):` [<mark style="color:purple;">**`CNPC`**</mark>](/api-v2.0/game-components/core/npc.md) | <mark style="color:purple;">**`nil`**</mark>

| Name      | Type                                                                                       | Description |
| --------- | ------------------------------------------------------------------------------------------ | ----------- |
| **tower** | [<mark style="color:purple;">**`CTower`**</mark>](/api-v2.0/game-components/core/tower.md) |             |

Returns `CNPC` that is attacked by the tower now.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/tower.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tree.md -->

# Tree

Table to work with `CTree`.<mark style="color:purple;">**`CTree`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>IsActive</sub>

`Tree.IsActive(tree):` <mark style="color:purple;">**`boolean`**</mark>

| Name     | Type                                                                                     | Description |
| -------- | ---------------------------------------------------------------------------------------- | ----------- |
| **tree** | [<mark style="color:purple;">**`CTree`**</mark>](/api-v2.0/game-components/core/tree.md) |             |

Returns if the tree is not cut.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/tree.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace.md -->

# Vambrace

Table to work with `CVambrace`.<mark style="color:purple;">**`CVambrace`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetStats</sub>

`Vambrace.GetStats(vambrace):` [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.attributes)

| Name         | Type                                                                                             | Description |
| ------------ | ------------------------------------------------------------------------------------------------ | ----------- |
| **vambrace** | [<mark style="color:purple;">**`CVambrace`**</mark>](/api-v2.0/game-components/core/vambrace.md) |             |

Returns selected `Enum.Attributes` attribute.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/camp.md -->

# Camp

Table to work with `CCamp`.<mark style="color:purple;">**`CCamp`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetType</sub>

`Camp.GetType(camp):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                     | Description        |
| -------- | ---------------------------------------------------------------------------------------- | ------------------ |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](/api-v2.0/game-components/core/camp.md) | The camp to check. |

Returns the camp type.

## <sub>GetCampBox</sub>

`Camp.GetCampBox(camp):` <mark style="color:purple;">**`{min:Vector, max:Vector}`**</mark>

| Name     | Type                                                                                     | Description        |
| -------- | ---------------------------------------------------------------------------------------- | ------------------ |
| **camp** | [<mark style="color:purple;">**`CCamp`**</mark>](/api-v2.0/game-components/core/camp.md) | The camp to check. |

Returns camp box as a table with **min** and **max** fields(**Vector**).

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/camp.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/bottle.md -->

# Bottle

Table to work with `CBottle`.

<mark style="color:purple;">**`CBottle`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetRuneType</sub>

`Bottle.GetRuneType(bottle):` [<mark style="color:purple;">**`Enum.RuneType`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.runetype)

| Name       | Type                                                                                         | Description |
| ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| **bottle** | [<mark style="color:purple;">**`CBottle`**</mark>](/api-v2.0/game-components/core/bottle.md) |             |

Returns the rune inside the bottle.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/bottle.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/courier.md -->

# Courier

Table to work with `CCourier`.<mark style="color:purple;">**`CCourier`**</mark> extends <mark style="color:purple;">**`CNPC`**</mark>

## <sub>IsFlyingCourier</sub>

`Courier.IsFlyingCourier(courier):` <mark style="color:purple;">**`boolean`**</mark>

| Name        | Type                                                                                           | Description           |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | The courier to check. |

Returns `true` if the courier is flying.

## <sub>GetRespawnTime</sub>

`Courier.GetRespawnTime(courier):` <mark style="color:purple;">**`number`**</mark>

| Name        | Type                                                                                           | Description           |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | The courier to check. |

Returns the game time when the courier will respawn.

## <sub>GetCourierState</sub>

`Courier.GetCourierState(courier):` [<mark style="color:purple;">**`Enum.CourierState`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.courierstate)

| Name        | Type                                                                                           | Description           |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | The courier to check. |

Returns the courier state.

## <sub>GetPlayerID</sub>

`Courier.GetPlayerID(courier):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                           | Description           |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | The courier to check. |

Returns owner's player id.

## <sub>GetCourierStateEntity</sub>

`Courier.GetCourierStateEntity(courier):` [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) | <mark style="color:purple;">**`nil`**</mark>

| Name        | Type                                                                                           | Description           |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **courier** | [<mark style="color:purple;">**`CCourier`**</mark>](/api-v2.0/game-components/core/courier.md) | The courier to check. |

Returns the entity that the courier is currently interacting with.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/courier.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler.md -->

# DrunkenBrawler

Table to work with `CDrunkenBrawler`.<mark style="color:purple;">**`CDrunkenBrawler`**</mark> extends <mark style="color:purple;">**`CAbility`**</mark>

## <sub>GetState</sub>

`DrunkenBrawler.GetState(ability):` [<mark style="color:purple;">**`Enum.DrunkenBrawlerState`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.drunkenbrawlerstate)

| Name        | Type                                                                                                         | Description |
| ----------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| **ability** | [<mark style="color:purple;">**`CDrunkenBrawler`**</mark>](/api-v2.0/game-components/core/drunkenbrawler.md) |             |

Returns the state of the CDrunkenBrawler ability.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem.md -->

# PhysicalItem

Table to work with `CPhysicalItem`.<mark style="color:purple;">**`CPhysicalItem`**</mark> extends <mark style="color:purple;">**`CEntity`**</mark>

## <sub>GetItem</sub>

`PhysicalItem.GetItem(physical_item):` [<mark style="color:purple;">**`CItem`**</mark>](/api-v2.0/game-components/core/item.md) | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                                                                                     | Description |
| ------------------ | -------------------------------------------------------------------------------------------------------- | ----------- |
| **physical\_item** | [<mark style="color:purple;">**`CPhysicalItem`**</mark>](/api-v2.0/game-components/core/physicalitem.md) |             |

Returns `CItem` object from `CPhysicalItem`.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads.md -->

# PowerTreads

Table to work with `CPowerTreads`.<mark style="color:purple;">**`CTower`**</mark> extends <mark style="color:purple;">**`CItem`**</mark>

## <sub>GetStats</sub>

`PowerTreads.GetStats(power_tread):` [<mark style="color:purple;">**`Enum.Attributes`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/core/pages/VwVljl88Qnl7u9hhqRdw#enum.attributes)

| Name             | Type                                                                                                   | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| **power\_tread** | [<mark style="color:purple;">**`CPowerTreads`**</mark>](/api-v2.0/game-components/core/powertreads.md) |             |

Returns selected `Enum.Attributes` attribute.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Game Engine

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/engine.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gamerules.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/globalvars.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gridnav.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/input.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/world.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/fogofwar.md -->

An unexpected error occurred

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Networking and APIs

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi.md -->

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http.md -->

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi.md -->

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

This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.

`Steam.GetProfilePictureBySteamId(steamID64, [large]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                        | Type                                             | Description                                                 |
| ----------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| **steamID64**                                               | <mark style="color:purple;">**`integer`**</mark> | The Steam ID of the player                                  |
| **large&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Whether to get the large profile picture `(default: false)` |

Returns the handle of the profile picture of the given Steam ID.

## <sub>GetProfilePictureByAccountId</sub>

This function works only if you already got player's user information (EMsg\_ClientRequestFriendData). That means you should be in the same game with the player or he should be in your friend list.

\`Steam.GetProfilePictureByAccountId(steamID64, \[large]):\` <mark style="color:purple;">\*\*\`integer\`\*\*</mark>

| Name                                                        | Type                                             | Description                                                 |
| ----------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| **steamID64**                                               | <mark style="color:purple;">**`integer`**</mark> | The account id of the player                                |
| **large&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark> | Whether to get the large profile picture `(default: false)` |

Returns the handle of the profile picture of the given account id.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel.md -->

# NetChannel

Table to work with game's net channel.

## <sub>GetLatency</sub>

`NetChannel.GetLatency([flow]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                       | Type                                                                                                                                                              | Description                                                 |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **flow&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.Flow`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/pages/VwVljl88Qnl7u9hhqRdw#enum.flow) | flow to get latency of `(default: Enum.Flow.FLOW_OUTGOING)` |

Returns the latency/ping of the net channel in seconds.

## <sub>GetAvgLatency</sub>

`NetChannel.GetAvgLatency([flow]):` <mark style="color:purple;">**`number`**</mark>

| Name                                                       | Type                                                                                                                                                              | Description                                                         |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **flow&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.Flow`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/pages/VwVljl88Qnl7u9hhqRdw#enum.flow) | flow to get average latency of `(default: Enum.Flow.FLOW_OUTGOING)` |

Returns the average latency/ping of the net channel in seconds.

## <sub>SendNetMessage</sub>

You can repeat the same message from OnSendNetMessage if you want to know the format of the message.

\`NetChannel.SendNetMessage(name, json):\` <mark style="color:purple;">\*\*\`boolean\`\*\*</mark>

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
    channel_type = 11, -- 11 - all chat
    roll_min = 11,
    roll_max = 222
}));

```

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/gc.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Rendering and Visuals

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle.md -->

# Particle

Table to work with particles.

## <sub>Create</sub>

`Particle.Create(particle, [attach_type], [entity]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                               | Type                                                                                                                                                                                            | Description                                                                                                   |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **particle**                                                       | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                 | Particle path                                                                                                 |
| **attach\_type&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.particleattachment) | attach\_type Attach type `(default: Enum.ParticleAttachment.PATTACH_WORLDORIGIN)`                             |
| **entity&#x20;**<mark style="color:orange;">**`[?]`**</mark>       | [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md)                                                                                                    | Entity to own of the particle. If not specified, the local hero will be used. `(default: Players.GetLocal())` |

Creates a particle and returns its index.

## <sub>SetControlPoint</sub>

`Particle.SetControlPoint(particle_index, control_point, value):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                                                                                           | Description         |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark>                                                               | Particle index      |
| **control\_point**  | <mark style="color:purple;">**`integer`**</mark>                                                               | Control point       |
| **value**           | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Control point value |

Sets the control point value of a particle.

## <sub>SetShouldDraw</sub>

`Particle.SetShouldDraw(particle_index, value):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                             | Description    |
| ------------------- | ------------------------------------------------ | -------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark> | Particle index |
| **value**           | <mark style="color:purple;">**`boolean`**</mark> | set value      |

Enables or disables the drawing of a particle.

## <sub>SetControlPointEnt</sub>

`Particle.SetControlPointEnt(particle_index, control_point, entity, attach_type, attach_name, position, lock_orientation):` <mark style="color:purple;">**`nil`**</mark>

| Name                  | Type                                                                                                                                                                                            | Description                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **particle\_index**   | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                                | Particle index                                |
| **control\_point**    | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                                | Control point                                 |
| **entity**            | [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md)                                                                                                    | Entity to attach                              |
| **attach\_type**      | [<mark style="color:purple;">**`Enum.ParticleAttachment`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.particleattachment) | Attach type                                   |
| **attach\_name**      | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                                                                                 | Attach name. See `NPC.GetAttachment` function |
| **position**          | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)                                                                                  | Control point position                        |
| **lock\_orientation** | <mark style="color:purple;">**`boolean`**</mark>                                                                                                                                                | Lock orientation. No idea what it does        |

Sets the control point entity value of a particle.

## <sub>SetParticleControlTransform</sub>

`Particle.SetParticleControlTransform(particle_index, control_point, position, angle):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                                                                                           | Description            |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark>                                                               | Particle index         |
| **control\_point**  | <mark style="color:purple;">**`integer`**</mark>                                                               | Control point          |
| **position**        | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | Control point position |
| **angle**           | [<mark style="color:purple;">**`Angle`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/angle.md)   | Control point angle    |

Sets the control point's position and angle.

## <sub>Destroy</sub>

`Particle.Destroy(particle_index):` <mark style="color:purple;">**`nil`**</mark>

| Name                | Type                                             | Description    |
| ------------------- | ------------------------------------------------ | -------------- |
| **particle\_index** | <mark style="color:purple;">**`integer`**</mark> | Particle index |

Destroys the particle by index.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1.md -->

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

| Name    | Type                                                                                                           | Description        |
| ------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | World coordinates. |

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2.md -->

# Render

Table to work with render v2.

## <sub>FilledRect</sub>

`Render.FilledRect(start, end_, color, [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                                                          | Description                                                    |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the rectangle.                           |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the rectangle.                             |
| **color**                                                      | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the rectangle.                                    |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |

Draws a filled rectangle.

## <sub>Rect</sub>

`Render.Rect(start, end_, color, [rounding], [flags], [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                                                          | Description                                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the rectangle.                           |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the rectangle.                             |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the rectangle's border.                           |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the rectangle's border. `(default: 1.0)`      |

Draws an unfilled rectangle.

## <sub>RoundedProgressRect</sub>

`Render.RoundedProgressRect(start, end_, color, percent, rounding, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                       | Description                                               |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The starting point of the rectangle.                      |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The ending point of the rectangle.                        |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color of the rectangle.                               |
| **percent**                                                     | <mark style="color:purple;">**`number`**</mark>                                                            | The percentage of the rectangle to fill \[0..1].          |
| **rounding**                                                    | <mark style="color:purple;">**`number`**</mark>                                                            | The rounding radius of the rectangle corners.             |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                            | The thickness of the rectangle's border. `(default: 1.0)` |

Draw a progress rectangle.

## <sub>DonutChart</sub>

`Render.DonutChart(center, radius, thickness, segments, [options]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                          | Type                                                                                                                                                                                                                                                                                                             | Description                                                  |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **center**                                                    | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                                                                                                                                                       | The center position of the chart.                            |
| **radius**                                                    | <mark style="color:purple;">**`number`**</mark>                                                                                                                                                                                                                                                                  | The outer radius of the chart.                               |
| **thickness**                                                 | <mark style="color:purple;">**`number`**</mark>                                                                                                                                                                                                                                                                  | The thickness of the donut ring.                             |
| **segments**                                                  | <mark style="color:purple;">**`{value: number, color: Color, icon: number`**</mark> \| <mark style="color:purple;">**`nil, icon_color: Color`**</mark> \| <mark style="color:purple;">**`nil, font_icon: {font: number, size: number, text: string}`**</mark> \| <mark style="color:purple;">**`nil}[]`**</mark> | List of data segments.                                       |
| **options&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`{separator_color:Color`**</mark> \| <mark style="color:purple;">**`nil, separator_thickness:number`**</mark> \| <mark style="color:purple;">**`nil}`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                                                                     | Optional settings for the chart appearance. `(default: nil)` |

Draw a donut chart.

## <sub>Line</sub>

`Render.Line(start, end_, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                       | Description                                 |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The starting point of the line.             |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The ending point of the line.               |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color of the line.                      |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                            | The thickness of the line. `(default: 1.0)` |

Draws a line between two points.

## <sub>PolyLine</sub>

`Render.PolyLine(points, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                         | Description                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vec2[]`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | A table of Vec2 points to connect with lines.   |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)      | The color of the polyline.                      |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                              | The thickness of the polyline. `(default: 1.0)` |

Draws a series of connected lines (polyline).

## <sub>Circle</sub>

`Render.Circle(pos, radius, color, [thickness], [startDeg], [percentage], [rounded], [segments]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                       | Description                                                                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                            | The radius of the circle.                                                                                            |
| **color**                                                        | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color of the circle.                                                                                             |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                            | The thickness of the circle's outline. `(default: 1.0)`                                                              |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                            | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                            | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |
| **rounded&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`boolean`**</mark>                                                           | Whether the circle is rounded. `(default: false)`                                                                    |
| **segments&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                           | The number of segments used for drawing the circle. `(default: 32)`                                                  |

Draws a circle.

## <sub>FilledCircle</sub>

`Render.FilledCircle(pos, radius, color, [startDeg], [percentage], [segments]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                       | Description                                                                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                            | The radius of the circle.                                                                                            |
| **color**                                                        | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color of the circle.                                                                                             |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                            | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                            | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |
| **segments&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                           | The number of segments used for drawing the circle. `(default: 32)`                                                  |

Draws a filled circle.

## <sub>CircleGradient</sub>

`Render.CircleGradient(pos, radius, colorOuter, colorInner, [startDeg], [percentage]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                             | Type                                                                                                       | Description                                                                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **pos**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The center position of the circle.                                                                                   |
| **radius**                                                       | <mark style="color:purple;">**`number`**</mark>                                                            | The radius of the circle.                                                                                            |
| **colorOuter**                                                   | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The outer color of the gradient.                                                                                     |
| **colorInner**                                                   | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The inner color of the gradient.                                                                                     |
| **startDeg&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`number`**</mark>                                                            | The starting degree for drawing the circle. 0 is right side, 90 is bottom, 180 is left, 270 is top. `(default: 0.0)` |
| **percentage&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                            | The percentage of the circle to draw, in the range \[0.0-1.0]. `(default: 1.0)`                                      |

Draws a circle with a gradient.

## <sub>Triangle</sub>

`Render.Triangle(points, color, [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                         | Description                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vec2[]`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | A table of three Vec2 points defining the vertices of the triangle. |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)      | The color of the triangle's outline.                                |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                              | The thickness of the triangle's outline. `(default: 1.0)`           |

Draws a triangle outline.

## <sub>FilledTriangle</sub>

`Render.FilledTriangle(points, color):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                                                                                         | Description                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **points** | [<mark style="color:purple;">**`Vec2[]`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | A table of three Vec2 points defining the vertices of the triangle. |
| **color**  | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)      | The color of the triangle.                                          |

Draws a filled triangle.

## <sub>TexturedPoly</sub>

`Render.TexturedPoly(points, textureHandle, color, [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                             | Description                                                                                                                            |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **points**                                                      | [<mark style="color:purple;">**`Vertex[]`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vertex.md) | A table of Vertex points defining the vertices of the polygon. Each Vertex contains a position (Vec2) and a texture coordinate (Vec2). |
| **textureHandle**                                               | <mark style="color:purple;">**`integer`**</mark>                                                                 | The handle to the texture to be applied to the polygon.                                                                                |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)          | The color to apply over the texture. This can be used to tint the texture.                                                             |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                  | The grayscale of the image. `(default: 0.0)`                                                                                           |

Draws a textured polygon.

## <sub>LoadFont</sub>

`Render.LoadFont(fontName, [fontFlag], [weight]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                           | Type                                                                                                                                                                                                                                | Description                                                                               |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **fontName**                                                   | <mark style="color:purple;">**`string`**</mark>                                                                                                                                                                                     | The name of the font to load.                                                             |
| **fontFlag&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Enum.FontCreate`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.fontcreate) \| <mark style="color:purple;">**`integer`**</mark> | Flags for font creation, such as antialiasing. `(default: Enum.FontCreate.FONTFLAG_NONE)` |
| **weight&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | <mark style="color:purple;">**`integer`**</mark>                                                                                                                                                                                    | The weight (thickness) of the font. Typically, 0 means default weight. `(default: 400)`   |

Loads a font and returns its handle. Returns handle to the loaded font.

## <sub>Text</sub>

`Render.Text(font, fontSize, text, pos, color):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                                                                                       | Description                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **font**     | <mark style="color:purple;">**`integer`**</mark>                                                           | The handle to the font used for drawing the text. |
| **fontSize** | <mark style="color:purple;">**`number`**</mark>                                                            | The size of the font.                             |
| **text**     | <mark style="color:purple;">**`string`**</mark>                                                            | The text to be drawn.                             |
| **pos**      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The position where the text will be drawn.        |
| **color**    | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color of the text.                            |

Draws text at a specified position.

## <sub>WorldToScreen</sub>

`Render.WorldToScreen(pos):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md), <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                           | Description                            |
| ------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | The 3D world position to be converted. |

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

`Render.ScreenSize():` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

Retrieves the current screen size, returning it as a Vec2 where x is the width and y is the height of the screen.

## <sub>TextSize</sub>

`Render.TextSize(font, fontSize, text):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

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

## <sub>LoadSvg</sub>

`Render.LoadSvg(path, size):` <mark style="color:purple;">**`integer`**</mark>

| Name     | Type                                                                                                       | Description             |
| -------- | ---------------------------------------------------------------------------------------------------------- | ----------------------- |
| **path** | <mark style="color:purple;">**`string`**</mark>                                                            | Path to the image.      |
| **size** | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Size of image to scale. |

Loads svg image and returns its handle.

## <sub>LoadSvgString</sub>

`Render.LoadSvgString(svg, size, cacheId):` <mark style="color:purple;">**`integer`**</mark>

| Name        | Type                                                                                                       | Description                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **svg**     | <mark style="color:purple;">**`string`**</mark>                                                            | Svg text itself.                                             |
| **size**    | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | Size of image to scale.                                      |
| **cacheId** | <mark style="color:purple;">**`string`**</mark>                                                            | Texture of image creates only once for every unique cache id |

Loads svg image from string and returns its handle.

## <sub>Image</sub>

`Render.Image(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                                                          | Description                                                             |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **imageHandle**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                                                                              | The handle to the image.                                                |
| **pos**                                                         | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The position to draw the image.                                         |
| **size**                                                        | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The size of the image.                                                  |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color to tint the image.                                            |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the image corners. `(default: 0.0)`              |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`              |
| **uvMin&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})` |
| **uvMax&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})` |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The grayscale of the image. `(default: 0.0)`                            |

Draws an image at a specified position and size.

## <sub>ImageCentered</sub>

`Render.ImageCentered(imageHandle, pos, size, color, [rounding], [flags], [uvMin], [uvMax], [grayscale]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                                                          | Description                                                             |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **imageHandle**                                                 | <mark style="color:purple;">**`integer`**</mark>                                                                                                                              | The handle to the image.                                                |
| **pos**                                                         | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The center position to draw the image.                                  |
| **size**                                                        | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The size of the image.                                                  |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color to tint the image.                                            |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the image corners. `(default: 0.0)`              |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`              |
| **uvMin&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The minimum UV coordinates for texture mapping. `(default: {0.0, 0.0})` |
| **uvMax&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The maximum UV coordinates for texture mapping. `(default: {1.0, 1.0})` |
| **grayscale&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The grayscale of the image. `(default: 0.0)`                            |

Draws an image centered at a specified position and size.

## <sub>ImageSize</sub>

`Render.ImageSize(imageHandle):` [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)

| Name            | Type                                             | Description              |
| --------------- | ------------------------------------------------ | ------------------------ |
| **imageHandle** | <mark style="color:purple;">**`integer`**</mark> | The handle to the image. |

Retrieves the size of an image. Returns the size of the image as a Vec2.

## <sub>OutlineGradient</sub>

`Render.OutlineGradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags], [thickness]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                                                                                          | Description                                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the gradient rectangle.                  |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the gradient rectangle.                    |
| **topLeft**                                                     | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the top-left corner.                              |
| **topRight**                                                    | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the top-right corner.                             |
| **bottomLeft**                                                  | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the bottom-left corner.                           |
| **bottomRight**                                                 | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the bottom-right corner.                          |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |
| **thickness&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the outline. `(default: 1.0)`                 |

Draws a outlined gradient rectangle.

## <sub>Gradient</sub>

`Render.Gradient(start, end_, topLeft, topRight, bottomLeft, bottomRight, [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                                                          | Description                                                    |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the gradient rectangle.                  |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the gradient rectangle.                    |
| **topLeft**                                                    | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the top-left corner.                              |
| **topRight**                                                   | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the top-right corner.                             |
| **bottomLeft**                                                 | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the bottom-left corner.                           |
| **bottomRight**                                                | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the bottom-right corner.                          |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing. `(default: Enum.DrawFlags.None)`     |

Draws a filled gradient rectangle.

## <sub>Shadow</sub>

`Render.Shadow(start, end_, color, thickness, [obj_rounding], [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **start**                                                           | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the shadow rectangle.                                                  |
| **end\_**                                                           | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the shadow rectangle.                                                    |
| **color**                                                           | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the shadow.                                                                     |
| **thickness**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the shadow.                                                                 |
| **obj\_rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the shadow rectangle corners. `(default: 0.0)`                        |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark>        | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The offset of the shadow from the original rectangle. `(default: {0.0, 0.0})`                |

Draws a shadow effect within a specified rectangular area.

## <sub>ShadowCircle</sub>

`Render.ShadowCircle(center, radius, color, thickness, [num_segments], [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                | Type                                                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **center**                                                          | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The center point of the circle.                                                              |
| **radius**                                                          | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The radius of the circle.                                                                    |
| **color**                                                           | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the shadow.                                                                     |
| **thickness**                                                       | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the shadow.                                                                 |
| **num\_segments&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`integer`**</mark>                                                                                                                              | The number of segments for drawing the circle. `(default: 12)`                               |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>         | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark>        | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The offset of the shadow from the circle. `(default: {0.0, 0.0})`                            |

Draws a circle shadow effect.

## <sub>ShadowConvexPoly</sub>

`Render.ShadowConvexPoly(points, color, thickness, [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **points**                                                   | [<mark style="color:purple;">**`Vec2[]`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                  | Table of Vec2 points defining the convex polygon. Should be more than 2 points.              |
| **color**                                                    | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the shadow.                                                                     |
| **thickness**                                                | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the shadow.                                                                 |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The offset of the shadow from the polygon. `(default: {0.0, 0.0})`                           |

Draws a shadow convex polygon effect.

## <sub>ShadowNGon</sub>

`Render.ShadowNGon(center, radius, color, thickness, num_segments, [flags], [offset]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                         | Type                                                                                                                                                                          | Description                                                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **center**                                                   | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The center point of the n-gon.                                                               |
| **radius**                                                   | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The radius of the n-gon.                                                                     |
| **color**                                                    | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)                                                                       | The color of the shadow.                                                                     |
| **thickness**                                                | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The thickness of the shadow.                                                                 |
| **num\_segments**                                            | <mark style="color:purple;">**`integer`**</mark>                                                                                                                              | The number of segments (sides) of the n-gon.                                                 |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>  | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for drawing the shadow. `(default: Enum.DrawFlags.ShadowCutOutShapeBackground)` |
| **offset&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The offset of the shadow from the n-gon. `(default: {0.0, 0.0})`                             |

Draws a shadow n-gon (polygon with n sides) effect.

## <sub>Blur</sub>

`Render.Blur(start, end_, [strength], [alpha], [rounding], [flags]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                           | Type                                                                                                                                                                          | Description                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **start**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The starting point of the blur rectangle.                           |
| **end\_**                                                      | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md)                                                                    | The ending point of the blur rectangle.                             |
| **strength&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The strength of the blur effect. `(default: 1.0)`                   |
| **alpha&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The alpha value of the blur effect. `(default: 1.0)`                |
| **rounding&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>                                                                                                                               | The rounding radius of the blur rectangle corners. `(default: 0.0)` |
| **flags&#x20;**<mark style="color:orange;">**`[?]`**</mark>    | [<mark style="color:purple;">**`Enum.DrawFlags`**</mark>](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/pages/VwVljl88Qnl7u9hhqRdw#enum.drawflags) | Custom flags for the blur effect. `(default: Enum.DrawFlags.None)`  |

Applies a blur effect within a specified rectangular area.

## <sub>PushClip</sub>

`Render.PushClip(start, end_, [intersect]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                                                                                       | Description                                                                                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **start**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The starting point of the clipping rectangle.                                                    |
| **end\_**                                                       | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The ending point of the clipping rectangle.                                                      |
| **intersect&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>                                                           | If true, the new clipping area is intersected with the current clipping area. `(default: false)` |

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

Do not forget to reset the global alpha value after your rendering.

\`Render.SetGlobalAlpha(alpha):\` <mark style="color:purple;">\*\*\`nil\`\*\*</mark>

| Name      | Type                                            | Description                    |
| --------- | ----------------------------------------------- | ------------------------------ |
| **alpha** | <mark style="color:purple;">**`number`**</mark> | The alpha value to set \[0..1] |

Set the global alpha value for rendering.

## <sub>ResetGlobalAlpha</sub>

`Render.ResetGlobalAlpha():` <mark style="color:purple;">**`nil`**</mark>

Reset the global alpha value for rendering to 1.0.

## <sub>CenteredNotification</sub>

`Render.CenteredNotification(text, duration):` <mark style="color:purple;">**`nil`**</mark>

| Name         | Type                                            | Description                   |
| ------------ | ----------------------------------------------- | ----------------------------- |
| **text**     | <mark style="color:purple;">**`string`**</mark> | Text to draw.                 |
| **duration** | <mark style="color:purple;">**`number`**</mark> | Duration of the notification. |

Draws a centered notification.

## <sub>Logo</sub>

`Render.Logo(center, radius, [angle], [primary_color], [secondary_color]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                                   | Type                                                                                                       | Description                        |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **center**                                                             | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) |                                    |
| **radius**                                                             | <mark style="color:purple;">**`number`**</mark>                                                            |                                    |
| **angle&#x20;**<mark style="color:orange;">**`[?]`**</mark>            | <mark style="color:purple;">**`number`**</mark>                                                            | rotation angle `(default: -45)`    |
| **primary\_color&#x20;**<mark style="color:orange;">**`[?]`**</mark>   | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | `(default: Menu.Style("primary"))` |
| **secondary\_color&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | `(default: {227, 227, 227, 255})`  |

Draws umbrella logo

## <sub>FindOrCreateRT</sub>

`Render.FindOrCreateRT(name, [w], [h]):` <mark style="color:purple;">**`integer`**</mark>

| Name                                                    | Type                                            | Description                                                 |
| ------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------- |
| **name**                                                | <mark style="color:purple;">**`string`**</mark> | The unique name of the render target.                       |
| **w&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The width of the render target. Optional. `(default: nil)`  |
| **h&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark> | The height of the render target. Optional. `(default: nil)` |

Creates a new render target or retrieves an existing one by name.\
If width or height are not provided, the render target will be full screen size.

## <sub>MarkDirtyRT</sub>

`Render.MarkDirtyRT(handle):` <mark style="color:purple;">**`nil`**</mark>

| Name       | Type                                             | Description                      |
| ---------- | ------------------------------------------------ | -------------------------------- |
| **handle** | <mark style="color:purple;">**`integer`**</mark> | The handle of the render target. |

Marks a render target as dirty, causing the next Render.RenderRT call to re-bake it.\
Safe across frame drops: the dirty state is only cleared once the bake is actually processed.

## <sub>RenderRT</sub>

`Render.RenderRT(callback, handle, pos, color, [scale], [uvSizeMin], [uvSizeMax]):` <mark style="color:purple;">**`boolean`**</mark>

| Name                                                            | Type                                                                                                       | Description                                                                |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **callback**                                                    | <mark style="color:purple;">**`fun():boolean?`**</mark>                                                    | The function containing rendering commands to bake into the render target. |
| **handle**                                                      | <mark style="color:purple;">**`integer`**</mark>                                                           | The handle of the render target (from Render.FindOrCreateRT).              |
| **pos**                                                         | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The screen position where the render target texture will be drawn.         |
| **color**                                                       | [<mark style="color:purple;">**`Color`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/color.md)    | The color tint to apply when drawing the render target texture.            |
| **scale&#x20;**<mark style="color:orange;">**`[?]`**</mark>     | <mark style="color:purple;">**`number`**</mark>                                                            | The scale factor for the render target. `(default: 1.0)`                   |
| **uvSizeMin&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The minimum UV offset for texture mapping. `(default: {0.0, 0.0})`         |
| **uvSizeMax&#x20;**<mark style="color:orange;">**`[?]`**</mark> | [<mark style="color:purple;">**`Vec2`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vec2.md) | The maximum UV offset for texture mapping. `(default: {0.0, 0.0})`         |

Renders a cached render target texture at the given position.\
If the render target is dirty (see Render.MarkDirtyRT), the callback is invoked once\
inside a push/pop RT context to re-bake the texture content, then the baked texture\
is drawn at `pos`. If the render target is clean, only the cached texture is drawn.\
\
The callback receives no arguments and may return a boolean: returning `true` signals\
that the content is still updating (e.g. animation in progress).

#### Example

```lua
-- render_target.lua
local rt_w, rt_h = 256, 80
local rt_handle = Render.FindOrCreateRT("example_rt", rt_w, rt_h)

local font = Render.LoadFont("MuseoSansEx", Enum.FontCreate.FONTFLAG_ANTIALIAS | Enum.FontCreate.FONTFLAG_DROPSHADOW, 500)

local white  = Color(255, 255, 255, 255)
local bg     = Color(20, 20, 20, 220)
local accent = Color(80, 200, 120, 255)
local dim    = Color(160, 160, 160, 200)
local rt_pos = Vec2(100, 100)

-- Animation state
local anim_start = 0
local anim_duration = 0.6 -- seconds
local is_animating = false
local click_count = 0

-- Draw callback is invoked ONLY when the RT is dirty.
-- Returning true  tells the caller "content is still changing" (animation in progress).
-- Returning false tells the caller "content is now static" (bake is final).
-- The engine itself does NOT use this value — it is passed through as RenderRT's return.
local function draw_rt_content()
    local t = is_animating
        and math.min((os.clock() - anim_start) / anim_duration, 1.0)
        or 0

    Render.FilledRect(Vec2(0, 0), Vec2(rt_w, rt_h), bg)
    Render.FilledRect(Vec2(0, rt_h - 8), Vec2(t * rt_w, rt_h), accent)
    Render.Text(font, 14, "Clicks: " .. click_count, Vec2(10, 10), white)

    if t >= 1.0 then
        is_animating = false
    end

    return is_animating
end

return {
    OnDraw = function()
        -- Click inside the RT rect -> start a new animation
        if Input.IsKeyDownOnce(Enum.ButtonCode.KEY_MOUSE1)
            and Input.IsCursorInRect(rt_pos.x, rt_pos.y, rt_w, rt_h) then
            click_count = click_count + 1
            anim_start = os.clock()
            is_animating = true
            Render.MarkDirtyRT(rt_handle)
        end

        -- RenderRT returns true when it baked AND the callback returned true.
        -- That means the animation is still playing, so mark dirty again
        -- to force another bake next frame.
        local still_updating = Render.RenderRT(draw_rt_content, rt_handle, rt_pos, white)
        if still_updating then
            Render.MarkDirtyRT(rt_handle)
        end

        -- Print current state below the RT rect
        local state = still_updating and "Redrawing (animation)" or "Cached (using RT)"
        Render.Text(font, 12, state, Vec2(rt_pos.x, rt_pos.y + rt_h + 4), dim)
    end
}

```

## <sub>ResizeRT</sub>

`Render.ResizeRT(handle, [w], [h]):` <mark style="color:purple;">**`nil`**</mark>

| Name                                                    | Type                                             | Description                                                           |
| ------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------- |
| **handle**                                              | <mark style="color:purple;">**`integer`**</mark> | The handle of the render target to resize.                            |
| **w&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>  | The new width, or a Vec2 containing both dimensions. `(default: nil)` |
| **h&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`number`**</mark>  | The new height. Not used when Vec2 is provided. `(default: nil)`      |

Resizes an existing render target.\
If width and height are not provided, it changes the render target to be full screen size.\
Accepts (handle, w, h), (handle, vec2), or (handle) for full screen.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/minimap.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

### Rendering - Panorama UI

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama.md -->

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

`Panorama.GetPanelByPath(path, [bLogError]):` [<mark style="color:purple;">**`UIPanel`**</mark>](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md) | <mark style="color:purple;">**`nil`**</mark>

| Name                                                            | Type                                              | Description                                      |
| --------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| **path**                                                        | <mark style="color:purple;">**`string[]`**</mark> | Path to the panel.                               |
| **bLogError&#x20;**<mark style="color:orange;">**`[?]`**</mark> | <mark style="color:purple;">**`boolean`**</mark>  | Log error if panel not found. `(default: false)` |

Get panel by path.

## <sub>GetPanelByName</sub>

`Panorama.GetPanelByName(id, is_type_name):` [<mark style="color:purple;">**`UIPanel`**</mark>](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md) | <mark style="color:purple;">**`nil`**</mark>

| Name               | Type                                             | Description                       |
| ------------------ | ------------------------------------------------ | --------------------------------- |
| **id**             | <mark style="color:purple;">**`string`**</mark>  | Id of the panel.                  |
| **is\_type\_name** | <mark style="color:purple;">**`boolean`**</mark> | Check type name instead of names. |

Get panel by id.

## <sub>CreatePanel</sub>

`Panorama.CreatePanel(type, id, parent, classes, styles):` [<mark style="color:purple;">**`UIPanel`**</mark>](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md)

| Name        | Type                                                                                                                    | Description                    |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **type**    | <mark style="color:purple;">**`string`**</mark>                                                                         | panel type to create           |
| **id**      | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                         | id of the panel                |
| **parent**  | [<mark style="color:purple;">**`UIPanel`**</mark>](/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md) | parent panel                   |
| **classes** | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                         | space separated classes to add |
| **styles**  | <mark style="color:purple;">**`string`**</mark> \| <mark style="color:purple;">**`nil`**</mark>                         | styles to set                  |

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel.md -->

An unexpected error occurred


--------------------------------------------------------------------------------

## Configuration and Utilities

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config.md -->

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer.md -->

# Humanizer

Table to work with humanizer.

## <sub>IsInServerCameraBounds</sub>

`Humanizer.IsInServerCameraBounds(pos):` <mark style="color:purple;">**`boolean`**</mark>

| Name    | Type                                                                                                           | Description       |
| ------- | -------------------------------------------------------------------------------------------------------------- | ----------------- |
| **pos** | [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md) | position to check |

Returns `true` if the world position is in server camera bounds.

## <sub>GetServerCameraPos</sub>

`Humanizer.GetServerCameraPos():` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

Returns server camera position.

## <sub>GetClientCameraPos</sub>

`Humanizer.GetClientCameraPos():` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

Returns client camera position.

## <sub>GetServerCursorPos</sub>

`Humanizer.GetServerCursorPos():` [<mark style="color:purple;">**`Vector`**</mark>](/api-v2.0/cheats-types-and-callbacks/classes/math/vector.md)

Returns the server cursor position.

## <sub>GetOrderQueue</sub>

`Humanizer.GetOrderQueue():` <mark style="color:purple;">**`{player: CPlayer, orderType: Enum.UnitOrder, targetIndex: integer, position: Vector, abilityIndex: integer, orderIssuer: Enum.PlayerOrderIssuer, unit: CNPC, orderQueueBehavior: integer, showEffects: boolean, triggerCallBack: boolean, isByMiniMap: boolean, addTime: number }[]`**</mark>

Returns information about the current humanizer order queue.

## <sub>IsSafeTarget</sub>

`Humanizer.IsSafeTarget(entity):` <mark style="color:purple;">**`boolean`**</mark>

| Name       | Type                                                                                         | Description |
| ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| **entity** | [<mark style="color:purple;">**`CEntity`**</mark>](/api-v2.0/game-components/core/entity.md) |             |

Returns information about the current humanizer order queue.

## <sub>ForceUserOrderByMinimap</sub>

`Humanizer.ForceUserOrderByMinimap():` <mark style="color:purple;">**`nil`**</mark>

Forces current user order by minimap. Must be called in OnPrepareUnitOrder

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log.md -->

# Log

Table to log.

## <sub>Write</sub>

`Log.Write(arg):` <mark style="color:purple;">**`nil`**</mark>

| Name    | Type                                         | Description      |
| ------- | -------------------------------------------- | ---------------- |
| **arg** | <mark style="color:purple;">**`any`**</mark> | Message to write |

Writes a message to the console.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer.md -->

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

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

<!-- Source: https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/gamelocalizer.md -->

An unexpected error occurred

