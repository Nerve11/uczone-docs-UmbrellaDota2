# CMenuGroup

CMenuGroup metatable

## [](#name)Name

`:Name():` `string`

Returns group's name\.

## [](#parent)Parent

`:Parent():` [`CThirdTab`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Returns group's parent\.

## [](#type)Type

`:Type():` [`Enum.WidgetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type\.

## [](#open)Open

`:Open():` `nil`

Opens parent tabs\.

## [](#find)Find

`:Find(widgetName):` [`CMenuSwitch`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch) \| [`CMenuBind`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind) \| [`CMenuSliderFloat`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat) \| [`CMenuSliderInt`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint) \| [`CMenuColorPicker`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker) \| [`CMenuComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox) \| [`CMenuButton`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton) \| [`CMenuMultiComboBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox) \| [`CMenuMultiSelect`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect) \| [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox) \| [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md) \| `nil`

Name

Type

Description

**widgetName**

`string`

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
group:Slider( "slider", 0, 100, 50, "%d" )
-- Create slider with integer values and custom format function
group:Slider( "slider", 0, 100, 50, function( value ) return "%d%%" end ) -- turns into
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

## [](#colorpicker)ColorPicker

`:ColorPicker(colorPickerName, color, [imageIcon]):` [`CMenuColorPicker`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker)

**colorPickerName**

**color**

[`Color`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color)

Creates new `CMenuColorPicker`\.

## [](#button)Button

`:Button(buttonName, callback, [altStyle], [widthPercent]):` [`CMenuButton`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton)

**buttonName**

**callback**

`function`

`func(this: CMenuButton):nil` function to call on button click\.

**altStyle**`[?]`

Use alternative button style\. `(default: false)`

**widthPercent**`[?]`

Button width in percents\. \[0\.0\, 1\.0\] `(default: 1.0)`

Creates new `CMenuButton`\.

#### [](#example-2)Example

```
group:Button( "button", function( this )
	Log.Write( "Button '" .. this:Name() .. "' has been clicked."  )
end )
```

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

#### [](#example-3)Example

```
group:MultiCombo( "multiCombo", { "item1", "item2", "item3" }, { "item1", "item3" } )
```

## [](#multiselect)MultiSelect

`:MultiSelect(multiSelectName, items, [expanded]):` [`CMenuMultiSelect`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect)

**multiSelectName**

`{nameId: string, imagePath: string, isEnabled: boolean}[]`

See example\.

**expanded**`[?]`

false if you want to create MultiSelect in collapsed state\. `(default: false)`

Creates new `CMenuMultiSelect`\.

#### [](#example-4)Example

```
group:MultiSelect( "multiSelect", {
 	{ "1", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
 	{ "2", "panorama/images/heroes/icons/npc_dota_hero_antimage_png.vtex_c", false },
}, true )
```

## [](#input)Input

`:Input(inputName, defaultValue, [imageIcon]):` [`CMenuInputBox`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox)

**inputName**

Creates new `CMenuInputBox`\.

## [](#label)Label

`:Label(labelText, [imageIcon]):` [`CMenuLabel`](https://github.com/Boyarinov/gitbook-doc-parser/blob/main/generated/menu/CMenuLabel.md)

**labelText**

Creates new `CMenuLabel`\.

## [](#disabled)Disabled

`:Disabled(value):` `nil`

**value**

Gets or sets group's disabled state\. Depends on argument\.

#### [](#example-5)Example

```
-- setter
group:Disabled( false )
```

## [](#disabled-1)Disabled

`:Disabled():` `boolean`

#### [](#example-6)Example

```
-- getter
local isDisabled = group:Disabled()
```

## [](#visible)Visible

`:Visible(value):` `nil`

Gets or sets group's visible state\. Depends on argument\.

#### [](#example-7)Example

```
-- setter
group:Visible(false)
```

## [](#visible-1)Visible

`:Visible():` `boolean`

#### [](#example-8)Example

```
-- getter
local isVisible = group:Visible()
```

## [](#searchhidden)SearchHidden

`:SearchHidden(value):` `nil`

Gets or sets group's search state\. Depends on argument\.

#### [](#example-9)Example

```
-- setter
group:SearchHidden(false)
```

## [](#searchhidden-1)SearchHidden

`:SearchHidden():` `boolean`

#### [](#example-10)Example

```
-- getter
local isSearchHidden = group:SearchHidden()
```

Last updated 19 days ago

