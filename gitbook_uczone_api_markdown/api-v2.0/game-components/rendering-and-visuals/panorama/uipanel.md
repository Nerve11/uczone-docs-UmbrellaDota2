# 🖼️UIPanel

UIPanel metatable

## [](#tostring)\_\_tostring

`:__tostring():` `nil`

## [](#eq)\_\_eq

Overload for operator ==\.

`:__eq(other):` `boolean`

Name

Type

Description

**other**

[`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

## [](#findchild)FindChild

`:FindChild(id):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

**id**

`string`

id of the child\.

Finds child by name\.

## [](#isvisible)IsVisible

`:IsVisible():` `boolean`

Returns visible state\.

## [](#setvisible)SetVisible

`:SetVisible(newState):` `nil`

**newState**

`boolean`

Sets visible state\.

## [](#getclasslist)GetClassList

`:GetClassList():` `string[]`

Returns class name list\.

## [](#findchildinlayoutfile)FindChildInLayoutFile

`:FindChildInLayoutFile(id):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

???\.

## [](#findpanelinlayoutfile)FindPanelInLayoutFile

`:FindPanelInLayoutFile(id):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

## [](#findchildtraverse)FindChildTraverse

`:FindChildTraverse(id):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

Recursive find child by id\.

## [](#getchildcount)GetChildCount

`:GetChildCount():` `integer`

Returns child by count\.

## [](#getchild)GetChild

`:GetChild(index):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

**index**

`number`

Returns child by index\.

## [](#getchildbypath)GetChildByPath

`:GetChildByPath(path, [bLogError]):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

**path**

`string[]`

**bLogError**`[?]`

Log error if panel not found\. `(default: false)`

Returns child by path using FindChild\.

## [](#getchildindex)GetChildIndex

`:GetChildIndex():` `integer`

Returns index in parent children list\. Starts from 0\.

## [](#getfirstchild)GetFirstChild

`:GetFirstChild():` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

Returns first child\.

## [](#getlastchild)GetLastChild

`:GetLastChild():` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

Returns last child\.

## [](#hasid)HasID

`:HasID():` `boolean`

Returns `true` if the panel has an id\.

## [](#getid)GetID

`:GetID():` `string`

Returns id of panel\.

## [](#setid)SetID

`:SetID(id):` `nil`

Sets the panel's id\.

## [](#getlayoutheight)GetLayoutHeight

`:GetLayoutHeight():` `integer`

Returns the panel height\.

## [](#getlayoutwidth)GetLayoutWidth

`:GetLayoutWidth():` `integer`

Returns the panel width\.

## [](#getparent)GetParent

`:GetParent():` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

Returns the panel's parent\.

## [](#getrootparent)GetRootParent

`:GetRootParent():` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

Returns the panel's root parent\. ???

## [](#getxoffset)GetXOffset

`:GetXOffset():` `integer`

Returns the panel's relative X offset\.

## [](#getyoffset)GetYOffset

`:GetYOffset():` `integer`

Returns the panel's relative Y offset\.

## [](#getbounds)GetBounds

`:GetBounds([useJsFunc]):` `{x:number, y:number, w:number, h:number}`

**useJsFunc**`[?]`

`boolean` \| `nil`

Use js GetPositionWithinWindow function to get position\. `(default: false)`

Returns the panel's bounds\. Iterate over the parent hierarchy to get the absolute bounds\.

## [](#getimagesrc)GetImageSrc

`:GetImageSrc():` `string`

Return the panel source image\.

## [](#getpaneltype)GetPanelType

`:GetPanelType():` `string`

Returns the panel's type\.

## [](#bsetproperty)BSetProperty

`:BSetProperty(key, value):` `boolean`

**key**

**value**

Sets the panel property\.

## [](#setstyle)SetStyle

`:SetStyle(cssString):` `boolean`

**cssString**

Sets the panel style\.

#### [](#example)Example

```
-- set_style.lua
local css_like_table = {
    ["horizontal-align"] = "center",
	["vertical-align"] = "center",
    ["transform"] = "translate3d( 0px, -0px, 0px ) scale3d(1, 1, 1)",
    ["padding-left"] = "0px",
    ["margin"] = "0px",
    ["border-radius"] = "4px",
    ["background-color"] = "none",
    ["box-shadow"] = "none",
    ["color"] = "gradient( linear, 0% 100%, 0% 0%, from( #ff00FF ), to( #5C9C68 ) )",
    ["font-size"] = "20px",
    ["text-align"] = "center",
    ["text-decoration"] = "none",
    ["background-size"] = "0% 0%",
    ["opacity-mask"] = 'url("s2r://panorama/images/masks/hudchat_mask_psd.vtex") 1.0',
    ["hue-rotation"] = "-10deg",
    ["text-shadow"] = "2px 2px #111111b0",
    ["blur"] = "gaussian(0px)",
    ["line-height"] = "120%",
    ["font-family"] = "Radiance",
    ["border-brush"] = "gradient( linear, 0% 0%, 0% 100%, from( #96c5ff96 ), to( #12142d2d ) )",
}


local function css_to_string(tbl)
    local str = ""
    for k, v in pairs(tbl) do
        str = str .. k .. ": " .. v .. "; "
    end
    return str;
end

local health_label = Panorama.GetPanelByName("HealthLabel");
if (health_label) then
    health_label:SetStyle(css_to_string(css_like_table))
end
```

## [](#setattribute)SetAttribute

`:SetAttribute(key, value):` `nil`

Sets the panel's attribute\.

## [](#getattribute)GetAttribute

`:GetAttribute(key, default):` `string` \| `nil`

**default**

Returns the panel's attribute\.

## [](#getpositionwithinwindow)GetPositionWithinWindow

`:GetPositionWithinWindow():` [`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Returns the panel's window position\. Not sure about optimization\.

## [](#gettext)GetText

This method is only available for Label panels\.

`:GetText():` `string`

Returns the label panel's text\.

## [](#settext)SetText

`:SetText(text):` `nil`

**text**

Sets the label panel's text\.

## [](#gettexttype)GetTextType

`:GetTextType():` `integer`

Gets the label panel's text type\. \(2 = plain\, 3 = html\)

## [](#settexttype)SetTextType

\`:SetTextType\(new\):\` \*\*\`nil\`\*\*

**new**

`integer`

value

Sets the label panel's text type\. \(2 = plain\, 3 = html\)\. Should always set text type before setting the text

#### [](#example-1)Example

```
label_panel:SetTextType(3)
label_panel:SetText("<font color='#8BFFD8'>Vitória</font>")
```

## [](#hasclass)HasClass

`:HasClass(className):` `boolean`

**className**

Class name\.

Checks if the panel has a class\.

## [](#addclasses)AddClasses

`:AddClasses(classNames):` `nil`

**classNames**

Could be a space separated list of classes\.

Adds a class to the panel\.

## [](#removeclasses)RemoveClasses

`:RemoveClasses(classNames):` `nil`

Removes a class to the panel\.

Last updated 19 days ago

