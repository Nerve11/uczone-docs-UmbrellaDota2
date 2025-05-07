# CSecondTab

CSecondTab metatable

## [](#name)Name

`:Name():` `string`

Returns tab's name\.

## [](#parent)Parent

`:Parent():` [`CTabSection`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection)

Returns tab's parent\.

## [](#type)Type

`:Type():` [`Enum.WidgetType`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.widgettype)

Returns widget type\.

## [](#open)Open

`:Open():` `nil`

Opens parent tabs\.

## [](#create)Create

`:Create(tabName):` [`CThirdTab`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab)

Name

Type

Description

**tabName**

`string`

Creates new `CThirdTab`\.

## [](#find)Find

`:Find(tabName):` [`CThirdTab`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab) \| `nil`

Finds the `CThirdTab` by name\.

## [](#image)Image

`:Image(imagePath, [offset]):` `nil`

**imagePath**

Path to the image\.

**offset**`[?]`

[`Vec2`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2)

Optional image offset\. `(default: {0.0, 0.0})`

Sets tab's image\.

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

Sets tab's icon\.
[Icons list](https://fontawesome.com/search?o=r&s=solid&f=classic)

#### [](#example)Example

```
-- https://fontawesome.com/icons/user?f=classic&s=solid
tab:Icon( "\f{007}" )
```

## [](#linkhero)LinkHero

`:LinkHero(heroId, attribute):` `nil`

**heroId**

See `Engine.GetHeroIDByName`

**attribute**

[`Enum.Attributes`](https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums#enum.attributes)

Links tab to hero and attribute\.

Last updated 19 days ago

