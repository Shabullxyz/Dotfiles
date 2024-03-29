# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from spotify import Spotify

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Menu"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="Menu"),
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),
    Key([mod], "b", lazy.spawn("brave"), desc="web browser"),
    Key([mod], "s", lazy.spawn("scrot"), desc="Screenshot"),
    Key([mod], "e", lazy.spawn("thunar"), desc="file explorer"),
    #Switch Focus monitor
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    #Spotify Control
    Key([mod, "control"], "bracketright", lazy.spawn("playerctl --player=spotify next"), desc="nextSpotify"),
    Key([mod, "control"], "bracketleft", lazy.spawn("playerctl --player=spotify previous"), desc="PreviosSpotify"),
    Key([mod, "control"], "backslash", lazy.spawn("playerctl --player=spotify play-pause"), desc="PlaySpotify"),
    #Kenlayout EN ES
    Key([mod], "space", lazy.spawn("kblyt.sh"), desc="chan key layout"),
    #Key([mod], "slash", lazy.spawn("setxkbmap -layout es"), desc="Dist Espa"),
    #Key([mod], "p", lazy.spawn("setxkbmap -layout us"), desc="Dist Englis"),

]

#groups = [Group(i) for i in "123456789"]

#groups = [Group(i) for i in [
   # " 󰄛 "," "," "," "," "," "," "
#]]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

group_labels = ["", "󰇩", "󰄛", "", "󰨞", "", "", "", "", "󰓓",]
#group_labels = ["Web", "Edit", "Ink", "Gimp", "Meld", "Vlc", "VB", "Thunar", "Mail", "Music",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        ))


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_conf = {
    'border_focus':"#ffffff",
    'border_normal':"#aaaaaa",
    'border_width': 1,
    'margin': 11
}

layouts = [
    #layout.Columns(border_focus_stack=["#ffffff", "#aaaaaa"], border_width=6),
    layout.Bsp(**layout_conf),
    layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Matrix(**layout_conf),
    #layout.MonadTall(**layout_conf),
    #layout.MonadWide(**layout_conf),
    #layout.RatioTile(**layout_conf),
    #layout.Tile(**layout_conf),
    #layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#999999", "#999999"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#720000", "#720000"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#773d8e", "#773d8e"], # color 7 #1a2f56 #62FF00
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()


def init_widgets_defaults():
    return dict(font="HackNerdFont Mono",
                fontsize = 12,
                padding = 2,
                background=colors[0])

widget_defaults = init_widgets_defaults()

extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(font="HackNerdFont Mono",
                        fontsize = 30,
                        margin_y = 2,
                        margin_x = 2,
                        padding_y = 6,
                        padding_x = 8,
                        borderwidth = 0,
                        active = colors[5],
                        inactive = colors[9],
                        rounded = False,
                        highlight_method = "block",
                        foreground = colors[9],
                        background = colors[0],
                        this_current_screen_border=colors[8],
                        this_screen_border=colors[1],
                        other_current_screen_border=colors[7],
                        other_screen_border=colors[7],
                        ),
                widget.WindowName(),
                Spotify(),
                #            widget.CurrentLayout(),
                widget.CurrentLayoutIcon(scale=0.65),
                widget.Systray(),
                widget.Clock(format="%d/%m/%Y - %H:%M"),
            ],
            26,
            margin =[10, 10, 0 ,10] ,
        ),
    ),
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(font="HackNerdFont Mono",
                        fontsize = 30,
                        margin_y = 2,
                        margin_x = 2,
                        padding_y = 6,
                        padding_x = 8,
                        borderwidth = 0,
                        active = colors[5],
                        inactive = colors[1],
                        rounded = False,
                        highlight_method = "block",
                        foreground = colors[9],
                        background = colors[0],
                        this_current_screen_border=colors[8],
                        this_screen_border=colors[1],
                        other_current_screen_border=colors[7],
                        other_screen_border=colors[7],
                        
                        ),
                widget.WindowName(),
                #Spotify(),
                #widget.CurrentLayout(),
                widget.CurrentLayoutIcon(scale=0.65),
                widget.Clock(format="%d/%m/%Y - %H:%M"),
            ],
            26,
            margin =[10, 10, 0 ,10] ,
            #margin = 10,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
