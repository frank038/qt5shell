# the folder to set as desktop in the home directory
USER_DESKTOP="Desktop"
# the terminal to use or leave "" for the default one if setted
USER_TERMINAL = ""
## viewport margins
# left margin
M_LEFT=0
# top margin
M_TOP=0
# right margin
M_RIGHT=0
# bottom margin
M_BOTTOM=0
# multi items drag picture: 0 use simple icon - 1 extended icons - 2 very extended icons
USE_EXTENDED_DRAG_ICON=1
# icon size if USE_EXTENDED_DRAG_ICON=1
mini_icon_size=32
# x offset of each icon if USE_EXTENDED_DRAG_ICON is enabled
X_EXTENDED_DRAG_ICON=40
# y offset of each icon if USE_EXTENDED_DRAG_ICON is enabled
Y_EXTENDED_DRAG_ICON=20
# limit the number of icon overlays if USE_EXTENDED_DRAG_ICON is enabled
NUM_OVERLAY=20
# thumbnailers: 0 no - 1 yes
USE_THUMB=0
# use custom icons for folders: 0 no - 1 yes
USE_FOL_CI=0
# space between items
ITEM_SPACE=10
# icon cell width - greater than ICON_SIZE
ITEM_WIDTH=160
# icon cell height
ITEM_HEIGHT=120
# icon size
ICON_SIZE=80
# thumb size: greater than ICON_SIZE - same size of ICON_SIZE to disable bigger thumbnailers
THUMB_SIZE=120
# item text shrinking - in the case the item text takes three lines when not selected increase this value
TEXT_SHRINK=0
# other icons size: link and permissions
ICON_SIZE2=36
# text colour in the form #AARRGGBB - "" to use default
TEXT_COLOR="#FFFFFFFF"
# draw the shadow back the text: 0 no - 1 yes
TEXT_SHADOW=0
TEXT_SHADOW_SHIFT=2
# text shadow colour in the form #AARRGGBB
TEXT_SHADOW_COLOR="#FF999999"
# draw a rouded rectangle back the text: 0 no - 1 yes
TEXT_BACKGROUND=1
# text background colors
TRED=167
TGREEN=167
TBLUE=167
TALPHA=185
# menu highlight color: "" to use the default style
# a color is mandatory
MENU_H_COLOR="#FFa7a7a7"
# the size of the circle at top-left of each item
CIRCLE_SIZE=30
# the circle color in the form #AARRGGBB
CIRCLE_COLOR="#FF476cba"
# tick symbol
TICK_CHAR="✓"
# tick size in pixels
TICK_SIZE=30
# tick symbol color
TICK_COLOR="white"
# Open with... dialog: 0 simple - 1 list installed applications
OPEN_WITH=1
# show delete context menu entry that bypass the trashcan: 0 no - 1 yes
USE_DELETE=1
# load the trash module: 0 no - 1 yes
USE_TRASH=1
# trash event sounds: 0 no - 1 in and out and empty - 2 empty only
TRASH_EVENT_SOUNDS=2
# recycle bin name
TRASH_NAME="Recycle Bin"
# load the media: 0 no - 1 yes
USE_MEDIA=1
# use desktop notification throu notify-send for storage devices: 0 not - 1 only ejected - 2 also after inserted
# do not use both USE_MEDIA_NOTIFICATION and USE_USB_DEVICES
USE_MEDIA_NOTIFICATION=0
# notify any usb device added or removed: 0 no - 1 yes - 2 play sound (implies 2)
# 3 try to use specific icon - 4 play sound (implies 3)
# do not use both USE_MEDIA_NOTIFICATION and USE_USB_DEVICES
USE_USB_DEVICES=3
# player to play event sounds: 0 no - 1 use qsound - "player_name"
SOUND_PLAYER=1
# media to skip, comma separated values in the form "/dev/xxx" - not reccomanded for removable ones
MEDIA_SKIP=["/dev/sda1"]
# Paste and Merge, how to backup the new files: 0 add progressive number
# in the form _(#) - 1 add date and time (without checking eventually
# existing file at destination with same date and time suffix) 
# in the form _yy.mm.dd_hh.mm.ss
USE_DATE=1
# creation data and time of the item in the property dialog: 0 use os.stat - 1 use functions from bash (should be precise)
DATE_TIME=1
# dialog windows width
DIALOGWIDTH=600
# can use: 1 - the user mimeapps.list (in $HOME/.config/mimeapps.list) or 0 - that in the program
USER_MIMEAPPSLIST=1
# icon theme name - if the qt5ct program overrides this use ""
ICON_THEME=""
# theme style: "" to use the default theme
THEME_STYLE=""
# use background colour in the listview widgets: 0 no - 1 yes
USE_BACKGROUND_COLOUR=0
BACKGROUND_COLOR="#878787"
# show the exit button: 0 no - 1 yes
SHOW_EXIT=1
# track screen resolution changes: 0 no - 1 yes
SCRN_RES = 1
### needed for qt5archiver
# usually 7z - or 7za
COMMAND_EXTRACTOR="7z"
### needed by pythumb
# use thumbnailer in the home dir only: 0 no - 1 yes
USE_THUMB_HOME_ONLY=1
# use borders: 0 no - 1 yes
USE_BORDERS=1
# 
BORDER_WIDTH=2
# border color of the thumbnails
BORDER_COLOR_R = 0
BORDER_COLOR_G = 0
BORDER_COLOR_B = 0
# thumbnail images cache
XDG_CACHE_LARGE = "sh_thumbnails/large/"
