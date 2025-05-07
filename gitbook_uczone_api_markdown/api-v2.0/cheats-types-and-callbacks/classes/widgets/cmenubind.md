# CMenuBind

CMenuBind metatable\.

## [](#name)Name

`:Name():` `string`

Returns widget's name\.

## [](#parent)Parent

`:Parent():` [`CMenuGroup`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) \| [`CMenuGearAttachment`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment)

Returns widget's parent\.

## [](#type)Type

`:Type():` [`Enum.WidgetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget's type\.

## [](#open)Open

`:Open():` `nil`

Opens parent tabs\.

## [](#forcelocalization)ForceLocalization

Not recommended for use due to its complexity

`:ForceLocalization(newText):` `nil`

Name

Type

Description

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
widget:Visible(false)
```

## [](#visible-1)Visible

`:Visible():` `boolean`

#### [](#example-1)Example

```
-- getter
local isVisible = widget:Visible()
```

## [](#disabled)Disabled

`:Disabled(value):` `nil`

Gets or sets disabled state\. Depends on argument\.

#### [](#example-2)Example

```
-- setter
widget:Disabled( false )
```

## [](#disabled-1)Disabled

`:Disabled():` `boolean`

#### [](#example-3)Example

```
-- getter
local isDisabled = widget:Disabled()
```

## [](#unsafe)Unsafe

`:Unsafe(value):` `nil`

Gets or sets unsafe state\. Unsafe widgets have warning sign\.
Depends on argument\.

## [](#unsafe-1)Unsafe

`:Unsafe():` `boolean`

## [](#get)Get

`:Get([idx]):` [`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

**idx**`[?]`

`0` \| `1`

index of the button to get value from `(default: 0)`

Returns widget's value\. To get both of the buttons use `Buttons` method\.

## [](#set)Set

`:Set(key1, [key2]):` `nil`

**key1**

[`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

primary button code

**key2**`[?]`

secondary button code `(default: Enum.ButtonCode.KEY_NONE)`

Sets widget's value\.

## [](#buttons)Buttons

`:Buttons():` [`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)\, [`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

Returns widget's buttons value\.

## [](#isdown)IsDown

`:IsDown():` `boolean`

Returns `true` when the key or both keys is down\.

## [](#ispressed)IsPressed

`:IsPressed():` `boolean`

Returns `true` when the key or both keys is pressed for the first time\.

## [](#istoggled)IsToggled

`:IsToggled():` `boolean`

Bind stores it's toggle state and switches it when the key is pressed\. This method
returns this state\.

## [](#settoggled)SetToggled

`:SetToggled(value):` `nil`

Sets the toggle state manually\.

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

`integer`

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

`fun(this: CMenuBind):nil`

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

## [](#properties)Properties

`:Properties([name], [value], [markAsToggle]):` `nil`

**name**`[?]`

Overridden name to display in bind list\. `(default: nil)`

**value**`[?]`

Overridden value to display alongside the name in the bind list\. This can be used to provide additional context about the bind\. `(default: nil)`

**markAsToggle**`[?]`

Indicates whether the bind should be marked as a toggle\, which is particularly useful if the bind's functionality includes toggling states\. Recommended to be used in conjunction with the IsToggled\(\)\. `(default: false)`

Updates the properties of a widget for display in the bind list\.

## [](#showinbindisland)ShowInBindIsland

`:ShowInBindIsland(newStatus):` `boolean`

**newStatus**

Gets or sets the visibility of the bind in the bind island\.

## [](#showinbindisland-1)ShowInBindIsland

`:ShowInBindIsland():` `boolean`

## [](#mousebinding)MouseBinding

`:MouseBinding(newStatus):` `boolean`

Gets or sets the ability to bind the mouse button\.

## [](#mousebinding-1)MouseBinding

`:MouseBinding():` `boolean`

Last updated 19 days ago

