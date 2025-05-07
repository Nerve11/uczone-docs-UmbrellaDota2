# 🖼️Panorama

Table to work with Dota Panorama system\.

## [](#getpanelinfo)GetPanelInfo

`Panorama.GetPanelInfo(path, [bLogError], [useJsFunc]):` `{x:number, y:number, w:number, h:number}`

Name

Type

Description

**path**

`string[]`

Path to the panel\.

**bLogError**`[?]`

`boolean` \| `nil`

`(default: false)`

**useJsFunc**`[?]`

Use js GetPositionWithinWindow function to get position\. `(default: false)`

Get panel info\. GetPanelByName for first argument then FindChild others and accumulate x and y\.

## [](#getpanelbypath)GetPanelByPath

`Panorama.GetPanelByPath(path, [bLogError]):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

`boolean`

Log error if panel not found\. `(default: false)`

Get panel by path\.

## [](#getpanelbyname)GetPanelByName

`Panorama.GetPanelByName(id, is_type_name):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel) \| `nil`

**id**

`string`

Id of the panel\.

**is\_type\_name**

Check type name instead of names\.

Get panel by id\.

## [](#createpanel)CreatePanel

`Panorama.CreatePanel(type, id, parent, classes, styles):` [`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

**type**

panel type to create

`string` \| `nil`

id of the panel

**parent**

[`UIPanel`](https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel)

parent panel

**classes**

space separated classes to add

**styles**

styles to set

Creates a new panorama panel

#### [](#example)Example

```
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

Last updated 19 days ago

