#!/bin/bash
thisdir=$(dirname "$0")
cd $thisdir

# desktop
/opt/qt5shell/qt5desktop/qt5desktop.sh &
# panel
/opt/qt5shell/qt5dock/qt5dock.sh &
# notification daemon
/opt/qt5shell/gtk3notification/gtk3notification.sh &
