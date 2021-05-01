Adwaita Highlight Cursor Theme
==============================

This is a hacky way to create RPMs for the highlight variant of the Adwaita
cursor theme.  The necessary changes were sent upstream but are not (yet)
accepted.

In the meantime I use this hacky setup to create the RPMs to install the
files in a controlled way.  It uses my clone of the `adwaita-cursors`
repository to build the files, creates a local SRPM file from it, and
then builds the `.noarch.rpm` file which can be installed.

I'm using the cursor theme for screen sharing sessions or for recording.
This simple shell script is used to toggle between the normal and the
highlight version of the Adwaita cursors:

     #!/bin/bash
     current=$(gsettings get org.gnome.desktop.interface cursor-theme)
     if [ $current = "'Adwaita'" ]; then
       gsettings set org.gnome.desktop.interface cursor-theme Adwaita-highlight
       gsettings set org.gnome.desktop.interface cursor-size 96
     else
       gsettings set org.gnome.desktop.interface cursor-theme Adwaita
       gsettings set org.gnome.desktop.interface cursor-size 36
     fi

With this scripts available through a hotkey one can quickly switch back and
forth from and to the highlight theme.  In my case the script is triggered by
a key on the StreamDeck which makes it vary convenient.  The sizes chosen
might have to be adjusted.  With the 4k screens I use this is needed when
the entire screen is shared/recorded because otherwise the cursor is too
small.


Prerequisites
-------------

To create the cursor binaries varies compile time dependencies are needed.

* `xcursorgen`
* `python2`
* `python3`
* `inkscape`

as well as several python modules.  In addition to the modules needed by the
original cursors packages the highlight theme also need `python3-pypng`.
