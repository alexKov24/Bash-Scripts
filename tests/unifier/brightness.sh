#!/bin/sh

# find all connected screens
NAMES=$( xrandr | grep "connected" | cut --delimiter=' ' -f 1 )

# find and isolate current brightness
BRI=$( xrandr --verbose --current | grep -E -m1 "Brightness" | awk '{print $2}')

while IFS=" " read -ra name; do
	case $1 in
		+)

			#echo "scale=4 ; $BRI+0.1" | bc | xargs -r xrandr --output $name --brightness
			BRI=`echo "scale=4 ; $BRI+0.1" | bc`
			xrandr --output $name --brightness $BRI
			;;
		-)

			BRI=`echo "scale=4 ; $BRI-0.1" | bc`
			xrandr --output $name --brightness $BRI
			;;
		*)
			;;
	esac
done <<< "$NAMES"
