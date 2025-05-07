# CMenuGearAttachment

CMenuGearAttachment metatable\.

## [](#name)Name

`:Name():` `string`

Returns widget's name\.

## [](#parent)Parent

`:Parent():` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) \| [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) \| [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) \| [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) \| [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) \| [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) \| [`CMenuComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) \| [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

Returns widget's parent\.

## [](#type)Type

`:Type():` [`Enum.WidgetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type\.

## [](#open)Open

`:Open():` `nil`

Opens parent tabs\.

## [](#forcelocalization)ForceLocalization

Not recommended for use due to its complexity

\`:ForceLocalization\(newText\):\` \*\*\`nil\`\*\*

Name

Type

Description

**newText**

`string`

Changes text in the widget\. The path to the widget is not affected\.
May be used for dynamic text customization or recolor\.

## [](#find)Find

`:Find(widgetName):` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) \| [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) \| [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) \| [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) \| [`CMenuColorPicker`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) \| [`CMenuComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) \| [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) \| [`CMenuMultiSelect`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) \| [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) \| [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) \| `nil`

**widgetName**

Finds the widget by name\.

## [](#switch)Switch

`:Switch(switchName, [defaultValue], [imageIcon]):` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch)

**switchName**

**defaultValue**`[?]`

`boolean`

`(default: false)`

**imageIcon**`[?]`

Path to image or FontAwesome icon unicode\. `(default: "")`

Creates new `CMenuSwitch`\.

## [](#bind)Bind

`:Bind(bindName, [defaultValue], [imageIcon]):` [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind)

**bindName**

[`Enum.ButtonCode`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.buttoncode)

`(default: Enum.ButtonCode.BUTTON_CODE_INVALID)`

Creates new `CMenuBind`\.

## [](#slider)Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint)

**sliderName**

**minValue**

`integer`

**maxValue**

**defaultValue**

**format**`[?]`

`string` \| `fun(value: integer):string`

Format string or function to format value\. See example\. `(default: "%d")`

Creates new `CMenuSliderInt` or `CMenuSliderFloat` depents on arg types\.
`minValue`\, `maxValue` and `defaultValue` should be integer to create `CMenuSliderInt`\.

#### [](#example)Example

```
-- Create slider with integer values
gear:Slider( "slider", 0, 100, 50, "%d" )
-- Create slider with integer values and custom format function
gear:Slider( "slider", 0, 100, 50, function( value ) return "%d%%" end ) -- turns into
"50%"
```

## [](#slider-1)Slider

`:Slider(sliderName, minValue, maxValue, defaultValue, [format]):` [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat)

`number`

`string` \| `fun(value: number):string`

Format string or function to format value\. See example\. `(default: "%f")`

Creates new `CMenuSliderFloat`\.

#### [](#example-1)Example

```
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

## [](#colorpicker)ColorPicker

`:ColorPicker(colorPickerName, color, [imageIcon]):` [`CMenuColorPicker`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

**colorPickerName**

**color**

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Creates new `CMenuColorPicker`\.

## [](#combo)Combo

`:Combo(comboName, items, [defaultValue]):` [`CMenuComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox)

**comboName**

**items**

`string[]`

Index of default item\. \(starts from 0\) `(default: 0)`

Creates new `CMenuComboBox`\.

## [](#multicombo)MultiCombo

`:MultiCombo(multiComboName, items, enabledItems):` [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox)

**multiComboName**

**enabledItems**

table of enabled items

Creates new `CMenuMultiComboBox`\.

#### [](#example-2)Example

```
gear:MultiCombo( "multiCombo", { "item1", "item2", "item3" }, { "item1", "item3" } )
```

## [](#multiselect)MultiSelect

`:MultiSelect(multiSelectName, items, [expanded]):` [`CMenuMultiSelect`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

**multiSelectName**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See example\.

**expanded**`[?]`

false if you want to create MultiSelect in collapsed state\. `(default: false)`

Creates new `CMenuMultiSelect`\.

#### [](#example-3)Example

```
gear:MultiSelect( "multiSelect", {
 	{ "1", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
 	{ "2", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
}, true )
```

## [](#input)Input

`:Input(inputName, [defaultValue], [imageIcon]):` [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

**inputName**

`(default: "")`

Creates new `CMenuInputBox`\.

## [](#label)Label

`:Label(labelText, [imageIcon]):` [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md)

**labelText**

Creates new `CMenuLabel`\.

## [](#visible)Visible

`:Visible(value):` `nil`

**value**

Gets or sets visible state\. Depends on argument\.

#### [](#example-4)Example

```
-- setter
widget:Visible(false)
```

## [](#visible-1)Visible

`:Visible():` `boolean`

#### [](#example-5)Example

```
-- getter
local isVisible = widget:Visible()
```

## [](#disabled)Disabled

`:Disabled(value):` `nil`

Gets or sets disabled state\. Depends on argument\.

#### [](#example-6)Example

```
-- setter
widget:Disabled( false )
```

## [](#disabled-1)Disabled

`:Disabled():` `boolean`

#### [](#example-7)Example

```
-- getter
local isDisabled = widget:Disabled()
```

Last updated 19 days ago

