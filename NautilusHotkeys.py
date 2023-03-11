#
# Add further hotkeys on top of the existing ones:
# - use ctrl+tab and ctrl+shift+tab to go to next/previous tabs
# - use backspace to go one folder level up
#
# Parts of code written by @jesusferm, used with permission:
# https://github.com/jesusferm/Nautilus-43-BackSpace/issues/1#issuecomment-1464625632
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

import gi
from gi.repository import GObject, Gtk, GLib
gi.require_version("Gtk", "4.0")


def idle_callback(*args):
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.up", ["BackSpace", "<alt>Up"])
    app.set_accels_for_action("win.tab-previous", ["<shift><control>Tab", "<control>Page_Up"])
    app.set_accels_for_action("win.tab-next", ["<control>Tab", "<control>Page_Down"])
    return False


def window_added(*args):
    GLib.idle_add(idle_callback, None)


class NautilusHotkeys(GObject.GObject):
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.up", ["BackSpace", "<alt>Up"])
    app.set_accels_for_action("win.tab-previous", ["<shift><control>Tab", "<control>Page_Up"])
    app.set_accels_for_action("win.tab-next", ["<control>Tab", "<control>Page_Down"])
    app.connect("window-added", window_added)
