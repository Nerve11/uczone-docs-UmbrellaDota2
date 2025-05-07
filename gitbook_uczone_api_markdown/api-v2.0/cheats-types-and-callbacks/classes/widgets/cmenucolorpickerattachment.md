# CMenuColorPickerAttachment

CMenuColorPickerAttachment metatable\.

## [](#name)Name

`:Name():` `string`

Returns widget's name\.

## [](#parent)Parent

`:Parent():` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) \| [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) \| [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) \| [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) \| [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) \| [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) \| [`CMenuGroup`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup) \| [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

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

Name

Type

Description

**newText**

`string`

Changes text in the widget\. The path to the widget is not affected\.
May be used for dynamic text customization or recolor\.

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

## [](#get)Get

`:Get():` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Returns widget's value\.

## [](#set)Set

`:Set(value):` `nil`

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Sets widget's value\.

## [](#setcallback)SetCallback

Multiple callbacks could be set\.

\`:SetCallback\(callback\, \[forceCall\]\):\` \*\*\`nil\`\*\*

**callback**

`fun(this: CMenuColorPickerAttachment):nil`

function to be called on widget change\.

**forceCall**`[?]`

true if you want to call callback on widget creation\. `(default: false)`

Sets widget's on change callback\.

## [](#unsetcallback)UnsetCallback

`:UnsetCallback(callback):` `nil`

function to be removed from widget's callbacks\.

Removes widget's on change callback\.

Last updated 19 days ago

