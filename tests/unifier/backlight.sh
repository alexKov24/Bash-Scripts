#!/bin/sh

# find all connected screens
NAMES=$( xrandr | grep "connected" | cut --delimiter=' ' -f 1 )

# find and isolate current brightness
BL=$( xrandr --verbose --current | grep "BACKLIGHT" | awk '{print $2}')

while IFS=" " read -ra name; do
	case $1 in
		+)

			BL=`echo "scale=4 ; $BL+100" | bc`
			xrandr --output $name --set "BACKLIGHT" $BL
			;;
		-)

			BL=`echo "scale=4 ; $BL-100" | bc`
			xrandr --output $name --set "BACKLIGHT" $BL
			;;
		*)
			;;
	esac
done <<< "$NAMES"
