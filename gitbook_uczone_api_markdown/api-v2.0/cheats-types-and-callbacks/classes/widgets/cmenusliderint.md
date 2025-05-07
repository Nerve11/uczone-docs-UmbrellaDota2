# CMenuSliderInt

CMenuSliderInt metatable\.

## [](#update)Update

`:Update(minValue, maxValue, defaultValue):` `nil`

Name

Type

Description

**minValue**

`integer`

**maxValue**

**defaultValue**

Updates the slider values\.

## [](#name)Name

`:Name():` `string`

Returns widget's name\.

## [](#parent)Parent

`:Parent():` [`CMenuGroup`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) \| [`CMenuGearAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent\.

## [](#type)Type

`:Type():` [`Enum.WidgetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type\.

## [](#open)Open

`:Open():` `nil`

Opens parent tabs\.

## [](#forcelocalization)ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

**newText**

`string`

Changes text in the widget\. The path to the widget is not affected\.
May be used for dynamic text customization or recolor\.

## [](#tooltip)ToolTip

`:ToolTip(newText):` `string`

Gets or sets tooltip\. Tooltip is displayed when mouse cursor is over the widget\.
Depends on the argument\.

## [](#tooltip-1)ToolTip

`:ToolTip():` `string`

## [](#visible)Visible

`:Visible(value):` `nil`

**value**

`boolean`

Gets or sets visible state\. Depends on argument\.

#### [](#example)Example

```
-- setter
switch:Visible(false)
```

## [](#visible-1)Visible

`:Visible():` `boolean`

#### [](#example-1)Example

```
-- getter
local isVisible = switch:Visible()
```

## [](#disabled)Disabled

`:Disabled(value):` `nil`

Gets or sets disabled state\. Depends on argument\.

#### [](#example-2)Example

```
-- setter
switch:Disabled( false )
```

## [](#disabled-1)Disabled

`:Disabled():` `boolean`

#### [](#example-3)Example

```
-- getter
local isDisabled = switch:Disabled()
```

## [](#unsafe)Unsafe

`:Unsafe(value):` `nil`

Gets or sets unsafe state\. Unsafe widgets have warning sign\.
Depends on argument\.

## [](#unsafe-1)Unsafe

`:Unsafe():` `boolean`

## [](#get)Get

`:Get():` `integer`

Returns widget's value\.

## [](#set)Set

`:Set(value):` `nil`

Sets widget's value\.

## [](#image)Image

`:Image(imagePath, [offset]):` `nil`

**imagePath**

Path to the image\.

**offset**`[?]`

[`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset\. `(default: {0.0, 0.0})`

Sets widget's image\.

## [](#imagehandle)ImageHandle

`:ImageHandle(imageHandle, [offset]):` `nil`

**imageHandle**

Sets tab's image by already created handle\.

## [](#icon)Icon

`:Icon(icon, [offset]):` `nil`

**icon**

icon unicode\.

Optional icon offset\. `(default: {0.0, 0.0})`

Sets widget's icon\.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### [](#example-4)Example

```
--https://fontawesome.com/icons/user?f=classic&s=solid
switch:Icon("\f{007}")
```

## [](#setcallback)SetCallback

Multiple callbacks could be set\.

\`:SetCallback\(callback\, \[forceCall\]\):\` \*\*\`nil\`\*\*

**callback**

`fun(this: CMenuSliderInt):nil`

function to be called on widget change\.

**forceCall**`[?]`

true if you want to call callback on widget creation\. `(default: false)`

Sets widget's on change callback\.

## [](#unsetcallback)UnsetCallback

`:UnsetCallback(callback):` `nil`

function to be removed from widget's callbacks\.

Removes widget's on change callback\.

## [](#colorpicker)ColorPicker

`:ColorPicker(name, color):` [`CMenuColorPickerAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment)

**name**

Name of the attachment\.

**color**

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Default color\.

Creates `CMenuColorPickerAttachment` and attaches it to the widget\.

## [](#gear)Gear

`:Gear(name, [gearIcon], [useSmallFont]):` [`CMenuGearAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

**gearIcon**`[?]`

Gear FontAwesome icon\. `(default: "\uf013")`

**useSmallFont**`[?]`

Use small font for gear icon\. `(default: true)`

Creates `CMenuGearAttachment` and attaches it to the widget\.

Last updated 19 days ago

