#!/bin/bash

pkill lemonbar
python3 ~/.config/theme_bot/custom.py | lemonbar -f "Source Code Pro:size=10" -f "Font Awesome:size=10" -f "xft:DejaVu:size=12" -g 1920x12+0+0
