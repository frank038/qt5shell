# position: 0 top - 1 bottom
dock_position=1
# icon button max size to get from application (even number)
button_size=36
# padding - space between button and icon (size icon: button_size - button_padding)
button_padding=2
# the height of the dock - useless: use button_size (first)
dock_height=button_size+2
# program launchers button size
pbutton_size=34
# show virtual desktops: 0 no - 1 yes
virtual_desktops=1
# use the builtin tray (server x): 0 no - 1 yes
use_tray=0
# use the builtin tray (dbus - preferred; implies use_tray=0): 0 no - 1 yes
use_tray_dbus=1
# tray icon size (even number)
tbutton_size = button_size-4
# tasklist position (with CENTRALIZE_EL=0): 0 left - 1 center
tasklist_position=0
# tasklist minimun size when tasklist_position=1
# tasklist_minimum_size=200
# theme style: "" to use the default theme
theme_style=""
# icon theme: "" to use the default theme
icon_theme=""
# the colour of the pressed menu and bookmark button: "" for the default or in the form #7F7F7F
button_menu_selected_color="#7F7F7F"
# the background colour of each button in the tasklist or "" for default #DF5E0B
button_background_color="#C9912B"
# application to be skipped from the dock (executables between double quotes with comma separator)
SKIP_APP=[]
# centralize all the elements: 0 no (traditional taskbar) - 2 only tasklist - 1 yes (except label0 and notification - do not use)
# do not use
CENTRALIZE_EL=0
# close the menu and the clock applet if focus is lost on another window: 0 no - 1 yes
LOST_FOCUS_CLOSE=1
# play sounds: 0 no - 1 use external player - 2 internal player QSound - 3 internal player GSound
PLAY_SOUND=2
# audio player: "NAME" or "" (PLAY_SOUND=1 required)
A_PLAYER="aplay"
# play sounds as a window opens or closes: 0 no - 1 yes (PLAY_SOUND=1/2 required)
PLAY_SOUND_WIN=0
# alarm sound: 0 disabled - 1 enabled (use_clock>0 and PLAY_SOUND=1 are required)
# right click in the time
PLAY_ALARM=1
# use internal clipboard
USE_CLIPBOARD=1
# use internal audio control - experimental
USE_AUDIO=1
# volume step: %
AUDIO_STEP=5
# starting audio level: 0-100
AUDIO_START_LEVEL=30
# show the microphone icon - experimental - USE_AUDIO is required
USE_MICROPHONE=1
# audio control panel command
MIXER_CONTROL="pavucontrol-qt"
# custom widgets at left
USE_CUSTOM_WIDGET_LEFT=0
# custom widgets at right
USE_CUSTOM_WIDGET_RIGHT=0
######### MENU ##########
# show the application menu: 0 no - 1 left - 2 right (clock/calendar to left)
use_menu=1
# view mode: 0 list - 1 icons
icon_mode = 1
# in icon mode, the grid size
icon_mode_width = 240
icon_mode_height = 128
# this window width
menu_width=1050
# menu position pad - bottom
menu_padx=4
menu_pady=4
# menu category icon size
menu_icon_size=48
# application icon size in the view
menu_app_icon_size=48
# service menu icon size
service_icon_size=20
# service menu border colour
service_border_color="gray"
# program used to add applications OR "" - full path
app_prog="./appmenu.py"
# program used to modify a desktop file OR ""
app_mod_prog=app_prog
# search field background colour: colour (in the form "#xxxxxx") OR ""
search_field_bg=""
# in the form "#XXXXXX" or "rgb(X, X, X)" or "colour name"
scroll_handle_col="#B5B5B5"
# highlight color - in the form "#rrggbb or "" for default #DF5E0B
item_highlight_color=""
# show this action in the menu: 0 no - 1 yes
SEND_TO_DESKTOP=0
# desktop name
DESKTOP_NAME="Desktop"
# terminal program
USER_TERMINAL="xterm"
#########
########## CLOCK - CALENDAR ##########
# show the clock - calendar: 0 no - 2 yes - [1 left (do not use)]
use_clock=2
# clock font
clock_font="Digital-7"
clock_font_size=12
# Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
clock_font_weight=50
# 0 no - 1 yes
clock_font_italic=0
# show the name of the day: 0 no - 1 yes
day_name=0
# time in AM/PM format: 0 no - 1 yes
USE_AP = 0
# the calendar ics file to read/write or leave ""
calendar_file=""
# in the form "#XXXXXX" or "colour name"
calendar_appointment_day_color="#00AA00"
# highlight color - in the form "#rrggbb or "" for default
citem_highlight_color=""
# border thickness
appointment_border_size=3
# in the form "#XXXXXX" or "colour name"
appointment_border_color="gray"
#
appointment_border_radius="15"
# calendar window width
calendar_width=800
# calendar window height
calendar_heidht=600
# left calendar window size
appointment_window_size=600
# font to be used in the label
calendar_label_font=""
# font size
calendar_label_font_size=18
# font weight: Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
calendar_label_font_weight=75
# font italic: 0 no - 1 yes
calendar_label_font_italic=0
# in the form "#XXXXXX" or "colour name"
calendar_label_font_color=""
# font to use in the calendar: "" not to set it
calendar_cal_font=""
# font size to use in the calendar: number or 0 not to set it
calendar_cal_font_size=0
#
appointment_char="✔"
# commad to launch after a double click on an event, or leave "" empty
# use "internal" for the internal application
event_command="internal"
# command to execute after double clicking a date in the calendar
# use "internal" for the internal application
date_command=event_command
# more pixels from panel or screen border
clock_gapx=menu_padx
clock_gapy=menu_pady
############
######## NOTIFICATIONS
# qt5notification manager: 0 no - 'full directory path' e.g. "mynots"
USE_NOTIFICATION="mynots"
# listen to another server only (implies USE_NOTIFICATION="mynots"): 0 no - 1 yes
USE_NOTIFICATION_SERVER=1
# list of application names to not save on disc (comma separated) - require USE_NOTIFICATION_SERVER=1
SKIP_APPS = ["Applet NetworkManager"]
# hyperlinks are clickable: 0 no - 1 yes - 2 opens the link (use with caution)
# 1 the link is copied to the clipboard - 2 opens the link with a program
HYPER_CLICK=1
# #  icon size of the notifications (pixels)
# NOTIFICATION_ICON_SIZE=160
#### do not disturb mode
# mandatory: folder in wich to create the file notificationdonotuse_3: path or ""
DO_NOT_DISTURB="."
# type of notifications not to display: 1 only urgency low - 2 only urgency normal and low - 3 all type (default)
# only 3 - do not change
DO_NOT_DISTURB_TYPE=3
#### notification window width and height
# not_width=800
# not_height=600
# notification content window width
# not_win_content=0
# window position pad - bottom
not_padx=menu_padx
not_pady=menu_pady
# notification icon size in the history
not_icon_size=96
# play sound events in not disturb mode: 0 no - 1 yes
NOT_PLAY_SOUND=1
#########
######### label0 - at far left
# exec label1 script: 0 to disable - 1 yes
label0_script=0
# seconds to wait for executing the script again
label0_interval=30
# use html tags instead of plain text - override the next label1 options
label0_use_richtext=0
# label2 color: "" to default or in the form "#XXXXXX" "colour name"
label0_color="green"
# font to be used in the label
label0_font=""
# font size
label0_font_size=12
# font weight: Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
label0_font_weight=75
# font italic: 0 no - 1 yes
label0_font_italic=0
# command to execute
label0_command1=""
# command to execute - center mouse button
label0_command2=""
######### label1 - at right
# exec label1 script: 0 to disable - 1 yes
label1_script=0
# seconds to wait for executing the script again
label1_interval=1
# use html tags instead of plain text - override the next label1 options
label1_use_richtext=0
# label2 color: "" to default or in the form "#XXXXXX" "colour name"
label1_color="red"
# font to be used in the label
label1_font=""
# font size
label1_font_size=12
# font weight: Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
label1_font_weight=75
# font italic: 0 no - 1 yes
label1_font_italic=0
# command to execute
label1_command1=""
# command to execute - center mouse button
label1_command2=""
######### label2 - at right
# execute label2 script: 0 to disable - 1 yes
label2_script=0
# seconds to wait for executing the script again
label2_interval=3
# use html tags instead of plain text - override the next label2 options
label2_use_richtext=0
# label2 color: "" to default or in the form "#XXXXXX" or "colour name"
label2_color="gray"
# font to be used in the label
label2_font=""
# font size
label2_font_size=12
# font weight: Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
label2_font_weight=75
# font italic: 0 no - 1 yes
label2_font_italic=0
# command to execute - left mouse button
label2_command1=""
# command to execute - center mouse button
label2_command2=""
######### label3 - at left
# exec label1 script: 0 to disable - 1 yes
label3_script=0
# seconds to wait for executing the script again
label3_interval=30
# use html tags instead of plain text - override the next label1 options
label3_use_richtext=0
# label2 color: "" to default or in the form "#XXXXXX" "colour name"
label3_color="black"
# font to be used in the label
label3_font=""
# font size
label3_font_size=10
# font weight: Thin 0 - ExtraLight 12 - Light 25 - Normal 50 - Medium 57 - DemiBold 63 - Bold 75 - ExtraBold 81 - Black 87
label3_font_weight=50
# font italic: 0 no - 1 yes
label3_font_italic=0
# command to execute
label3_command1=""
# command to execute - center mouse button
label3_command2=""
########## service commands
# one word or script - /usr/bin/systemctl poweroff
shutdown_command="./poweroff.sh"
# one word or script - /usr/bin/systemctl reboot
restart_command="./reboot.sh"
# one word or script
logout_command="./logout.sh"
##### custom commands
# one word command - with full path eventually
# command and name mandatory
COMM1_COMMAND="xterm"
COMM1_ICON=""
COMM1_NAME="XTERM"
COMM1_TOOLTIP=""
#
COMM2_COMMAND=""
COMM2_ICON=""
COMM2_NAME=""
COMM2_TOOLTIP=""
#
COMM3_COMMAND=""
COMM3_ICON=""
COMM3_NAME=""
COMM3_TOOLTIP=""
############ webcam
# show webcams, even not in use state: 0 no - 1 yes
use_webcam=1
# do not show the following cameras by "idvendor:idproduct" : eg ["0123:4567"] - if attached but not in use it will not be shown
show_webcam_skip=[]
# only if in use state: 0 no - 1 yes
show_only_active=0
# same as above but only if in use: this implies show_webcam_skip: the webcam will not be shown at all
show_only_active_skip=[]
################ battery
# use_clock=1 is required
# 0 no - 1 yes : one minute check
use_battery_info=0
################
# # # DO NOT CHANGE
# increase the value to better centralize elements (L left, R right): 1 or > 1
CENTRALIZE_GAP_L=1
CENTRALIZE_GAP_R=1
# # border radius
# border_radius=15
# # amount of effect
# blur_radius=15
