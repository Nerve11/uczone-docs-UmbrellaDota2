# ⚒️Config

Table to work with configs that are stored in the `configs` folder with the `.ini` extention\.

## [](#readint)ReadInt

`Config.ReadInt(config, key, [def]):` `integer`

Name

Type

Description

**config**

`string`

The config file name\.

**key**

The key to read\.

**def**`[?]`

`integer`

The default value to return if the key is not found\. `(default: 0)`

Read an integer from a config file\.

## [](#readfloat)ReadFloat

`Config.ReadFloat(config, key, [def]):` `number`

`number`

The default value to return if the key is not found\. `(default: 0.0)`

Read a float from a config file\.

## [](#readstring)ReadString

`Config.ReadString(config, key, [def]):` `string`

The default value to return if the key is not found\. `(default: "")`

Read a string from a config file\.

## [](#writeint)WriteInt

`Config.WriteInt(config, key, value):` `nil`

The key to write\.

**value**

The value to write\.

Write an integer to a config file\.

## [](#writefloat)WriteFloat

`Config.WriteFloat(config, key, value):` `nil`

Write a float to a config file\.

## [](#writestring)WriteString

`Config.WriteString(config, key, value):` `nil`

Write a string to a config file\.

Last updated 19 days ago

