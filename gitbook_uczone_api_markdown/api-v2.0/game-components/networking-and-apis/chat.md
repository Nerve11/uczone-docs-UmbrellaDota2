# 💬Chat

Table to work with chat\.

## [](#getchannels)GetChannels

`Chat.GetChannels():` `string[]`

Returns an array of channel names\.

## [](#print)Print

`Chat.Print(channel, text):` `nil`

Name

Type

Description

**channel**

`string`

The channel name to say the message in\.

**text**

The message to say\.

Print a message in a channel\. This message will not be sent to the server\.

## [](#say)Say

`Chat.Say(channel, text):` `nil`

Say a message in a channel\.

## [](#flip)Flip

`Chat.Flip(channel):` `nil`

The channel name to flip the coin in\.

Flip the coin in a channel\.

## [](#roll)Roll

`Chat.Roll(channel, [min], [max]):` `nil`

The channel name to roll the dice in\.

**min**`[?]`

`number`

The minimum number to roll\. `(default: 0)`

**max**`[?]`

The maximum number to roll\. `(default: 100)`

Roll a dice in a channel\.

Last updated 19 days ago

