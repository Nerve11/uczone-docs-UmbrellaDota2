# CMenuMultiSelect

CMenuMultiSelect metatable\.

## [](#name)Name

`:Name():` `string`

Returns widget's name\.

## [](#update)Update

`:Update(items, [expanded]):` `nil`

Name

Type

Description

**items**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See `CMenuGroup:MultiSelect`\.

**expanded**`[?]`

`boolean`

false if you want to create MultiSelect in collapsed state\. `(default: false)`

Updates the multiselect values\.

## [](#oneitemselection)OneItemSelection

`:OneItemSelection(newState):` `boolean`

**newState**

Gets or sets one item selection state\. One item selection allows only one item to be
selected\. Depends on the argument\.

## [](#oneitemselection-1)OneItemSelection

`:OneItemSelection():` `boolean`

## [](#dragallowed)DragAllowed

`:DragAllowed(newState):` `boolean`

Gets or sets drag allowed state\. Drag allows items to be ordered by cursor\.
Depends on the argument\.

## [](#dragallowed-1)DragAllowed

`:DragAllowed():` `boolean`

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

`:Get(itemId):` `boolean`

**itemId**

Returns enable state of the item in multiselect\.

## [](#set)Set

`:Set(enabledItems):` `nil`

**enabledItems**

`string[]`

A table of enabled items; other items will be disabled\.

Sets a new value for the item by itemId or sets a new list of enabled items

## [](#set-1)Set

`:Set(itemId, value):` `nil`

## [](#list)List

`:List():` `string[]`

Returns array of itemIds\.

## [](#listenabled)ListEnabled

`:ListEnabled():` `string[]`

Returns array of enabled itemIds\.

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
widget:Icon("\f{007}")
```

## [](#setcallback)SetCallback

Multiple callbacks could be set\.

\`:SetCallback\(callback\, \[forceCall\]\):\` \*\*\`nil\`\*\*

**callback**

`fun(this: CMenuMultiSelect):nil`

function to be called on widget change\.

**forceCall**`[?]`

true if you want to call callback on widget creation\. `(default: false)`

Sets widget's on change callback\.

## [](#unsetcallback)UnsetCallback

`:UnsetCallback(callback):` `nil`

function to be removed from widget's callbacks\.

Removes widget's on change callback\.

## [](#updatebackgroundcolors)UpdateBackgroundColors

`:UpdateBackgroundColors(colors):` `nil`

**colors**

`table<string>`

Table with background colors\.

Updates widget's background colors\.

## [](#updateimagecolors)UpdateImageColors

`:UpdateImageColors(colors):` `nil`

Table with image colors\.

Updates widget's image colors\.

## [](#updatetooltips)UpdateToolTips

`:UpdateToolTips(colors):` `nil`

Table with new tooltips

Updates widget's tooltips

Last updated 11 days ago

