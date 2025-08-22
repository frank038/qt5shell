# qt5shell
A desktop shell (desktop and panel) for Xorg and Linux.

Use the version in the Releases page.

Required:
- python3
- pyqt5 (and some other pyqt5 modules)
- gir1.2-glib-2.0
- python3-xlib
- python3-xdg

For mass storage devices (optional):
- udisk2
- dbus
- pyudev
- notify-send (for desktop notifications)

For custom actions (option):
- 7z
- tar
- zip
- md5sum - sha256sum
- xterm

For thumbnailers (option):
- pdftocairo
- ffmpegthumbnailer

For webcam:
- pyudev
- lsof (command line program)
- pyinotify

Maybe also others not listed above.

How to launch the qt5shell:
the folder qt5shell must be copied into the /opt folder; then launch the file qt5shell_launch.sh (must be made executable); however, any location is valid, unless you modify the file qt5shell_launch.sh accordingly; other bash files maybe need to be modified to match the user programs or options. 

The panel:
- menu, virtual desktops, taskbar, tray (both versions, xlib and dbus), clipboard (text and images), clock, audio manager, microphone indicator, webcam indicator, battery indicator, calendar, notification history (a notificaition server is needed), timer, internal menu modificator, internal calendar events manager (double click on a date to add an event or on an event to modify or remove it), menu bookmarks, applications can be pinned into the panel; window event sounds; some options are available by using the right mouse button; etc.
- the desktop: trash-bin, usb devices, usb devices insertion, wallpaper, custom item position, thumbails, custom actions, trash-bin event sounds, etc.

All the available options and customizations are in the cfg files.

To do:
- notification server.

Pros:
- too many options, almost for everything.

Cons:
- too many options.

![My image](https://github.com/frank038/qt5shell/blob/main/screenshot1.jpg)
