mc_xclip
========

**NEW:**

Don't use `mc_xclip`! Instead:

* `sudo apt-get install xclip`
* Make sure `mc` is NOT running, or it will overwrite the next changes.
* Find `clipboard_store` in `~/.config/mc/ini`
* Set `clipboard_store=xclip -i -selection clipboard`
* Set `clipboard_paste=xclip -o -selection clipboard`
* Thanks to https://github.com/IvanAli

**OLD:**

Syncs clipboards of Midnight Commander and X Window System.

Install:

    sudo apt-get install xclip
    sudo pip install mc_xclip

    # If you use Display Manager:
    echo 'mc_xclip &' >> ~/.xprofile

    # Else:
    echo 'mc_xclip &' >> ~/.xinitrc

    # Reboot.

mc_xclip version 0.3.0  
Copyright (C) 2011-2017 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
