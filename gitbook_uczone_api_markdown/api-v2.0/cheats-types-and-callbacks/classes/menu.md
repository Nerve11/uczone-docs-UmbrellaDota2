# 📋Menu

Table to work with Menu\.

## [](#find)Find

`Menu.Find(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName, widgetName, attachmentName, widgetInGearName):` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) \| [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) \| [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) \| [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) \| [`CMenuColorPicker`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) \| [`CMenuComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) \| [`CMenuButton`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) \| [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) \| [`CMenuMultiSelect`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) \| [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) \| [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) \| `nil`

Name

Type

Description

**firstTabName**

`string`

**sectionName**

**secondTabName**

**thirdTabName**

**groupTabName**

**widgetName**

**attachmentName**

**widgetInGearName**

Returns menu item\.

## [](#create)Create

`Menu.Create(firstTabName, sectionName, secondTabName, thirdTabName, groupTabName):` [`CMenuGroup`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup)

Creates tab/section/group\. Returns menu item\.

## [](#style)Style

`Menu.Style(styleColor):` [`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

**styleColor**

Creates tab/section/group\. Returns color of specified style var or table of all style colors
depends on param\.

## [](#opened)Opened

`Menu.Opened():` `boolean`

Returns current menu open state\.

## [](#alpha)Alpha

`Menu.Alpha():` `number`

Returns current menu alpha\.

## [](#pos)Pos

`Menu.Pos():` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu pos\.

## [](#size)Size

`Menu.Size():` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns current menu size\.

## [](#scale)Scale

`Menu.Scale():` `integer`

Returns current menu scale percentage\.

## [](#animduration)AnimDuration

`Menu.AnimDuration():` `number`

Returns current menu animation duration\.

Last updated 19 days ago

