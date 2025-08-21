# qt5shell
A desktop shell (desktop and panel) for Xorg and Linux.

Use the version in the Releases page.

Required:
- python3
- pyqt5 (and some other pyqt5 modules)
- gir1.2-glib-2.0
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

Maybe also other not listed above.

The panel:
- menu, virtual desktops, taskbar, tray (both versions, xlib and dbus), clipboard (text and images), clock, audio manager, microphone indicator, webcam indicator, battery indicator, calendar, notification history (a notificaition server is needed), timer, internal menu modificator, internal calendar events manager, menu bookmarks, applications can be pinned into the panel; the available option can be selected by using the right mouse button; etc.
- the desktop: trash-bin, usb devices, usb devices insertion, wallpaper, custom item position, etc.

All the available options and customizations are in the cfg files.

To do:
- notification server.

Pros:
- too many options, almost for everything.

Cons:
- too many options.

![My image](https://github.com/frank038/qt5shell/blob/main/screenshot1.jpg)
