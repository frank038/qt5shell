#!/usr/bin/env python3

# V. 0.9.53

import os,sys,time
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, Gio, GLib, Pango
from gi.repository import GdkPixbuf
import dbus
import dbus.service as Service

from cfg_not import *

_curr_dir = os.getcwd()

from dbus.mainloop.glib import DBusGMainLoop
mainloop = DBusGMainLoop(set_as_default=True)

# # deactivated
# SOUND_PLAYER = 0
# if SOUND_PLAYER == 1:
    # gi.require_version('GSound', '1.0')
    # from gi.repository import GSound

def dbus_to_python(data):
    if isinstance(data, dbus.String):
        data = str(data)
    elif isinstance(data, dbus.Boolean):
        data = bool(data)
    elif isinstance(data, dbus.Int64):
        data = int(data)
    elif isinstance(data, dbus.Double):
        data = float(data)
    elif isinstance(data, dbus.Byte):
        data = int(data)
    elif isinstance(data, dbus.UInt32):
        data = int(data)
    elif isinstance(data, dbus.Array):
        data = [dbus_to_python(value) for value in data]
    elif isinstance(data, dbus.Dictionary):
        new_data = dict()
        for key in data.keys():
            new_data[dbus_to_python(key)] = dbus_to_python(data[key])
        data = new_data
    return data

class mainProg():
    def __init__(self):
        
        # notification icon size
        self.not_icon_size = NOT_ICON_SIZE
        # notifications to skip
        self.not_skip_apps = APP_LIST_SKIPPED
        # notification width
        self.not_width = NOT_WIDTH
        # notification height
        self.not_height = NOT_HEIGHT
        # notification max height
        self.not_height_max = NOT_HEIGHT_MAX
        # # 0 no - 1 yes - 2 yes/with external player
        # self.not_sounds = 0 # deactivated
        # do not disturbe mode
        self.not_dnd = DO_NOT_DISTURBE
        #
        self.qt5dock_location = QTDOCK_FOLDER
        # bottom screen limin
        self.not_bottom_limit = BOTTOM_LIMIT
        # pad between notifications
        self.not_pad = PAD_NOT
        # top margin + _pad
        self.starting_y = NOT_STARTING_Y
        
        self._monitor = Gdk.Display.get_default().get_monitor(0)
        self.screen_width = self._monitor.get_geometry().width
        self.screen_height = self._monitor.get_geometry().height
        
        conn = dbus.SessionBus(mainloop = mainloop)
        Notifier(conn, "org.freedesktop.Notifications", self)
        
        
class notificationWin(Gtk.Window):
    def __init__(self, _parent, args):
        super().__init__()
        #
        self.set_title("gtk3notification")
        self._notifier = _parent
        # disable the window decoration
        self.set_decorated(False)
        # No influence is made on placement.
        self.set_position(Gtk.WindowPosition.NONE)
        #
        self.set_focus_on_map(False)
        #
        self.set_focus_visible(False)
        #
        self.set_keep_above(True)
        #
        self.set_skip_pager_hint(True)
        #
        self.set_skip_taskbar_hint(True)
        #
        self.set_type_hint(Gdk.WindowTypeHint.NOTIFICATION)
        
        _x = args[0]
        _y = args[1]
        _appname = dbus_to_python(args[2])
        _pixbuf = args[3] # pixbuf or None
        _summary = dbus_to_python(args[4])
        _body = dbus_to_python(args[5])
        _timeout = dbus_to_python(args[6])
        _hints = args[7]
        _actions = args[8]
        _replaceid = args[9]
        
        self.__y = _y
        self.not_width = self._notifier.not_width
        self.not_height = self._notifier.not_height
        
        self._pad = 4
        
        # # hints: "desktop-entry" "image-path" "transient" "urgency" "value"
        # #  "suppress-sound" "sound-file" "sound-name"
        
        self.style_provider = Gtk.CssProvider()
        self.SC = Gtk.StyleContext.new()
        self.self_style_context = self.get_style_context()
        self.self_style_context.add_class("notificationwin")
        css = ".notificationwin { border: 1px solid gray; }"
        self.style_provider.load_from_data(css.encode('utf-8'))
        self.SC.add_provider_for_screen(
        Gdk.Screen.get_default(),
        self.style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        self.connect('show', self.on_show)
        
        self.set_resizable(True)
        self.set_vexpand(True)
        self.set_size_request(self.not_width, self.not_height)
        
        self.main_box = Gtk.Box.new(1,0)
        self.add(self.main_box)
        
        self.btn_icon_box = Gtk.Box.new(0,0)
        # self.btn_icon_box.set_halign(2)
        self.main_box.pack_start(self.btn_icon_box,True,True,0)
        
        if _pixbuf:
            _img = Gtk.Image.new_from_pixbuf(_pixbuf)
            self.btn_icon_box.pack_start(_img,False,True,4)
        
        self.second_box = Gtk.Box.new(1,0)
        self.btn_icon_box.pack_start(self.second_box,True,True,0)
        
        # app - summary - body : in second_box vertical
        if _summary:
            _lbl_summary = Gtk.Label(label="<b>"+_summary+"</b>")
            _lbl_summary.set_use_markup(True)
            _lbl_summary.set_halign(1)
            _lbl_summary.set_line_wrap(True)
            _lbl_summary.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
            if _body:
                _lbl_summary.set_valign(2)
            else:
                _lbl_summary.set_valign(3)
            self.second_box.pack_start(_lbl_summary,True,True,self._pad)
        #
        if _body:
            _lbl_body = Gtk.Label(label=_body)
            _lbl_body.set_halign(1)
            _lbl_body.set_use_markup(True)
            _lbl_body.set_line_wrap(True)
            _lbl_body.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
            if _summary:
                _lbl_body.set_valign(1)
            else:
                _lbl_body.set_valign(3)
            self.second_box.pack_start(_lbl_body,True,True,self._pad)
        
        self.close_btn = Gtk.Button.new()
        self.close_btn.set_name("closebtn")
        conf_img = Gtk.Image.new_from_icon_name("stock_close", 1)
        self.close_btn.set_image(conf_img)
        self.close_btn.set_relief(Gtk.ReliefStyle.NONE)
        self.close_btn.set_halign(2)
        self.close_btn.set_valign(1)
        # self.conf_btn.props.hexpand = True
        # self.conf_btn.halign = Gtk.Align.FILL
        # self.conf_btn.valign = Gtk.Align.START
        self.close_btn.connect('clicked', self.on_close_btn)
        self.btn_icon_box.pack_start(self.close_btn,False,False,0)
        self.main_box.set_margin_start(self._pad)
        # self.main_box.set_margin_end(self._pad)
        
        # action buttons in main_box
        if _actions:
            _actions_box = Gtk.Box.new(0,0)
            self.main_box.add(_actions_box)
            _actions_box.set_halign(3)
            for _ee in _actions[::2]:
                btn_name = _actions[_actions.index(_ee)+1]
                _btn = Gtk.Button(label=btn_name)
                _btn.set_relief(Gtk.ReliefStyle.NONE)
                _btn.connect('clicked',self._on_button_callback, _replaceid, _ee)
                _actions_box.add(_btn)
        
        self.connect('delete-event', self.on_close_win,_replaceid)
        self.connect('destroy-event', self.on_close_win,_replaceid)
        
        # the geometry of this window
        self._value = None
        
        #
        # _x = self._notifier._parent.screen_width - self.get_size_request().width - self._pad
        # self.move(_x,_y)
        #
        self.show_all()
        #
        self.stick()

    # action button pressed
    def _on_button_callback(self, _btn, _replaceid, _action):
        self._notifier.ActionInvoked(_replaceid, _action)
        self.close()
    
    def on_close(self,_replaceid):
        self._notifier.NotificationClosed(_replaceid, 3)
        for el in self._notifier.list_notifications[:]:
            if el[0] == self:
                self._notifier.list_notifications.remove(el)
                break
    
    def on_close_win(self,w,e,_replaceid):
        self.on_close(_replaceid)
        self.close()
    
    def on_close_btn(self, btn):
        self.close()
        
    def on_show(self, widget):
        self._win = self.get_window()
        
        _geometry = Gdk.Geometry()
        # _geometry.min_width = self.not_width
        # _geometry.min_height = self.not_height
        _geometry.max_width = self.not_width
        _geometry.max_height = self._notifier._parent.not_height_max
        # _geometry.width_inc = 10
        # _geometry.height_inc = 10
        self._win.set_geometry_hints(_geometry, Gdk.WindowHints.MAX_SIZE)
        
        _x = self._notifier._parent.screen_width - self.not_width - self._pad
        self._win.move(_x,self.__y)
        
        self._value = self.get_window().get_geometry()


class Notifier(Service.Object):
    
    def __init__(self, conn, bus, _parent):
        Service.Object.__init__(self, object_path = "/org/freedesktop/Notifications", bus_name = Service.BusName(bus, conn))
        self._parent = _parent
        self.list_notifications = []
        self._not_path = os.path.join(_curr_dir,"mynots")
        # top margin and _pad
        self.starting_y = self._parent.starting_y
        self.not_pad = self._parent.not_pad
        # top margin + _pad
        self.__y = self.starting_y+self.not_pad # static value
        self._y = self.__y # variable value
        self._not_counter = 1
    
    @Service.method("org.freedesktop.Notifications", out_signature="as")
    def GetCapabilities(self):
        return ["actions", "action-icons", "body", "body-markup", "body-hyperlinks", "body-images", "icon-static", "sound"]
        
    @Service.method("org.freedesktop.Notifications", in_signature="susssasa{sv}i", out_signature="u")
    def Notify(self, appName, replacesId, appIcon, summary, body, actions, hints, expireTimeout):
        replacesId = dbus_to_python(replacesId)
        
        # skip these applications
        if appName in self._parent.not_skip_apps:
            return replacesId
        
        # # skipped
        # x-canonical-private-synchronous - e.g. volume
        # replacesId = self._on_hints(hints, "x-canonical-private-synchronous")
        if "x-canonical-private-synchronous" in hints:
            # if self._parent.not_vol_change:
                # replacesId = 5000
            # else:
            return replacesId
        
        if self._not_counter == 4000:
            self._not_counter = 1
        if replacesId == 0 or not replacesId:
            replacesId = self._not_counter
            self._not_counter +=1
        elif replacesId == self._not_counter:
            self._not_counter += 1
        
        action_1 = dbus_to_python(actions)
        
        if not dbus_to_python(appIcon):
            appIcon = ""
        if action_1:
            if expireTimeout == -1:
                expireTimeout = 10000
            self._qw(appName, summary, body, replacesId, action_1, hints, expireTimeout, appIcon)
        else:
            action_1 = []
            if expireTimeout == -1:
                expireTimeout = 6000
            self._qw(appName, summary, body, replacesId, action_1, hints, expireTimeout, appIcon)
        
        return replacesId

    @Service.method("org.freedesktop.Notifications", in_signature="u")
    def CloseNotification(self, id):
        # reasons: 1 expired - 2 dismissed by the user - 3 from here - 4 other
        self.NotificationClosed(id, 3)

    @Service.method("org.freedesktop.Notifications", out_signature="ssss")
    def GetServerInformation(self):
        return ("gtk3notification-server", "Calculon", "1.0", "0.666")

    @Service.signal("org.freedesktop.Notifications", signature="uu")
    def NotificationClosed(self, id, reason):
        pass

    @Service.signal("org.freedesktop.Notifications", signature="us")
    def ActionInvoked(self, id, actionKey):
        pass
    
    @Service.signal("org.freedesktop.Notifications", signature="us")
    def ActivationToken(self, id, actionKey):
        pass
    
    # find and return the hint
    def _on_hints(self, _hints, _value):
        if _value in _hints:
            # return _hints[_value]
            return dbus_to_python(_hints[_value])
        return None
    
    def _qw(self, _appname, _summ, _body, _replaceid, _actions, _hints, _timeout, _icon):
        # hints: "desktop-entry" "image-path" "transient" "urgency" "value"
        #  "suppress-sound" "sound-file" "sound-name"
        _ICON_SIZE = self._parent.not_icon_size
        self.not_width = self._parent.not_width
        self.not_height = self._parent.not_height
        # # 0 no - 1 yes - 2 yes/with external player
        # self.no_sound = self._parent.not_sounds # deactivated
        self.not_dnd = self._parent.not_dnd
        # notification icon
        _desktop_entry = self._on_hints(_hints, "desktop-entry")
        ret_icon = None
        #
        if _desktop_entry:
            ret_icon = self._on_desktop_entry(os.path.basename(_desktop_entry))
        _not_name =  str(int(time.time()))
        _notification_path = os.path.join(self._not_path, _not_name)
        _pix = self._find_icon(ret_icon, _icon, _hints, _ICON_SIZE)
        #
        _found_same_id = 0
        if _replaceid != 0:
            for _el in self.list_notifications:
                if _el[1] == _replaceid:
                    _found_same_id = 1
                    _el[0].close()
                    break
        # 
        if _found_same_id == 0:
            if self.list_notifications:
                self._y = self.list_notifications[-1][2]+self.not_pad
            else:
                self._y = self.__y
        #
        if self._y > self._parent.screen_height - self._parent.not_bottom_limit:
            self._y = self.__y
        
        # 0 low - 1 normal - 2 critical
        _urgency = self._on_hints(_hints, "urgency")
        
        NW = None
        # _dnd_file = os.path.join(_curr_dir,"do_not_disturb_mode")
        _dnd_file = os.path.join(self._parent.qt5dock_location,"notificationdonotuse_3")
        #
        if os.path.exists(_dnd_file):
            # never show the notification
            if self.not_dnd == 0:
                return
        if ( os.path.exists(_dnd_file) == False ) or ( (os.path.exists(_dnd_file) == True) and (self.not_dnd == 1 and _urgency == 2)):
            NW = notificationWin(self, (0, self._y, _appname, _pix, _summ, _body, _timeout, _hints, _actions, _replaceid))
            #
            # _NW_height = NW.get_size_request().height
            _NW_height = NW._value.height
            self._y += _NW_height
            #
            self.list_notifications.append([NW,_replaceid, self._y])
            self._close_notification(_timeout,NW)
        #
        # _is_transient = self._on_hints(_hints, "transient")
        #
        ############ deactivated
        # # send signal for storing and playing sound
        # if not _is_transient:
            # _no_sound = self._on_hints(_hints, "suppress-sound")
            # try:
                # # self._signal.propList = ["not-write", _appname, _summ, _body, _urgency, _pix, _hints]
                # self._signal.propList = ["not-write", _appname, _summ, _body, _urgency, _pix, _no_sound]
            # except:
                # pass
        # else:
            # _no_sound = self._on_hints(_hints, "suppress-sound")
            # try:
                # # self._signal.propList = ["not-write", _appname, _summ, _body, _urgency, _pix, _hints]
                # self._signal.propList = ["not-sound", None, None, None, _urgency, None, _no_sound]
            # except:
                # pass
        #####
        # deactivated
        # # write the notification content
        # if not _is_transient:
            # try:
                # if os.access(self._not_path,os.W_OK):
                    # os.makedirs(_notification_path)
                    # ff = open(os.path.join(_notification_path,"notification"), "w")
                    # ff.write(_appname+"\n\n\n@\n\n\n"+_summ+"\n\n\n@\n\n\n"+_body)
                    # ff.close()
                    # #
                    # _pb = _pix.get_paintable()
                    # _pb.save_to_png(os.path.join(_notification_path,"image.png"))
            # except:
                # pass
        
        # deactivated
        # # sounds
        # if self.no_sound != 0 and not os.path.exists(_dnd_file):
            # if self.not_dnd == 0 or (self.not_dnd == 1 and _urgency == 2):
                # _no_sound = self._on_hints(_hints, "suppress-sound")
                # _soundfile = self._on_hints(_hints, "sound-file")
                # if not _soundfile:
                    # _soundfile = self._on_hints(_hints, "sound-name")
                
                # if not _no_sound:
                    # if _soundfile:
                        # self.play_sound(_soundfile)
                    # else:
                        # if _urgency == 1 or _urgency == None:
                            # self.play_sound(os.path.join(_curr_dir, "sounds/urgency-normal.wav"))
                        # elif _urgency == 2:
                            # self.play_sound(os.path.join(_curr_dir, "sounds/urgency-critical.wav"))
        
    def on_close_notification(self, nw):
        nw.close()
        
    def _close_notification(self,_t,nw):
        GLib.timeout_add(_t, self.on_close_notification, nw)
    
    # find the icon from the desktop file
    def _on_desktop_entry(self, _desktop):
        app_dirs_user = [os.path.join(os.path.expanduser("~"), ".local/share/applications")]
        app_dirs_system = ["/usr/share/applications", "/usr/local/share/applications"]
        _ddir = app_dirs_user+app_dirs_system
        _icon = None
        for dd in _ddir:
            if os.path.exists(dd):
                for ff in os.listdir(dd):
                    if os.path.basename(ff) == _desktop+".desktop":
                        try:
                            _ap = Gio.DesktopAppInfo.new_from_filename(os.path.join(dd,ff))
                            _icon = _ap.get_icon()
                            if _icon:
                                if isinstance(_icon,Gio.ThemedIcon):
                                    _icon = _icon.to_string()
                                elif isinstance(_icon,Gio.FileIcon):
                                    _icon = _icon.get_file().get_path()
                                return _icon
                            else:
                                return None
                        except:
                            return None
        
        return None
    
    # desktop_icon _icon _hints user_icon_size
    # priority: image-data image-path/application_icon
    def _find_icon(self, ret_icon, _icon, _hints, ICON_SIZE):
        _image_data = self._on_hints(_hints, "image-data")
        _icon_data = self._on_hints(_hints, "icon_data")
        pixbuf = None
        #
        if _image_data or _icon_data:
            if _image_data:
                _image_data = _image_data
            else:
                _image_data = _icon_data
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_bytes(
                        width=_image_data[0],
                        height=_image_data[1],
                        has_alpha=_image_data[3],
                        data=GLib.Bytes.new(_image_data[6]),
                        colorspace=GdkPixbuf.Colorspace.RGB,
                        rowstride=_image_data[2],
                        bits_per_sample=_image_data[4],
                        )
            except:
                pass
            if pixbuf:
                pixbuf = pixbuf.scale_simple(ICON_SIZE,ICON_SIZE,GdkPixbuf.InterpType.BILINEAR)
                return pixbuf
        #
        _image_path = self._on_hints(_hints, "image-path")
        if _image_path:
            if _image_path[0:7] == "file://":
                _image_path = _image_path[7:]
            _base_dir = os.path.dirname(_image_path)
            _base_name = os.path.basename(_image_path)
            if os.path.exists(_base_dir) and os.path.exists(_image_path):
                try:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(_image_path, ICON_SIZE, ICON_SIZE, 1)
                except:
                    pass
                if pixbuf:
                    return pixbuf
            else:
                try:
                    pixbuf = Gtk.IconTheme().load_icon(_image_path, ICON_SIZE, Gtk.IconLookupFlags.FORCE_SVG)
                    pixbuf = pixbuf.scale_simple(ICON_SIZE, ICON_SIZE, GdkPixbuf.InterpType.BILINEAR)
                except:
                    pass
                if pixbuf:
                    return pixbuf
        #
        if _icon:
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(_icon, ICON_SIZE, ICON_SIZE, 1)
            except:
                try:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(os.path.join(_curr_dir,"icons","wicon.png"), ICON_SIZE, ICON_SIZE, 1)
                except:
                    pass
            if pixbuf:
                return pixbuf
        #
        if ret_icon:
            try:
                pixbuf = Gtk.IconTheme().load_icon(ret_icon, ICON_SIZE, Gtk.IconLookupFlags.FORCE_SVG)
            except:
                try:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(os.path.join(_curr_dir,"icons","wicon.png"), ICON_SIZE, ICON_SIZE, 1)
                except:
                    pass
            if pixbuf:
                return pixbuf
        #
        try:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(os.path.join(_curr_dir,"icons","wicon.png"), ICON_SIZE, ICON_SIZE, 1)
            return pixbuf
        except:
            pass
        
        return None
    
    # deactivated
    # def play_sound(self, _sound):
        # if self.no_sound == 1 and SOUND_PLAYER == 1:
            # try:
                # ctx = GSound.Context()
                # ctx.init()
                # ret = ctx.play_full({GSound.ATTR_EVENT_ID: _sound})
                # if ret == None:
                    # ret = ctx.play_full({GSound.ATTR_MEDIA_FILENAME: _sound})
            # except:
                # pass
        # elif self.no_sound not in [1,2] and SOUND_PLAYER == 1:
            # _player = self.no_sound
            # try:
                # os.system("{0} {1} &".format(_player, _sound))
            # except:
                # pass

if __name__ == '__main__':
    _prog = mainProg()
    Gtk.main()