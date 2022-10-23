#!/bin/sh

BL=$( xrandr --verbose | grep "BACKLIGHT" )
[ -z $BL ] && brightness $1 || backlight $1
