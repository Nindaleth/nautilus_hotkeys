# Nautilus Hotkeys

Adds a few more hotkeys to Nautilus (GNOME Files) to improve the user experience:

* Switch tabs via `Ctrl+Shift+Tab` and `Ctrl+Tab` in addition to the existing `Ctrl+PageUp` and `Ctrl+PageDown` hotkeys
* Go one directory level up via `Backspace` in addition to the existing `Alt+Up` hotkey

Supports GNOME 43 and newer.

## Acknowledgements

Parts of code written by @jesusferm, used [with permission](https://github.com/jesusferm/Nautilus-43-BackSpace/issues/1#issuecomment-1464625632)

## Installation

1. Install [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython)

  * Fedora: `dnf install nautilus-python`
  * Ubuntu family: `apt install python3-nautilus`
  * Arch Linux: `pacman -S python-nautilus`
  * openSUSE: `zypper install python-nautilus`
  * Solus: `eopkg install nautilus-python`

2. Get NautilusHotkeys and install it

```
git clone https://github.com/Nindaleth/nautilus_hotkeys
mkdir -p ~/.local/share/nautilus-python/extensions/
ln -s $(pwd)/nautilus_hotkeys/NautilusHotkeys.py ~/.local/share/nautilus-python/extensions/
```

### 3) Restart Nautilus

```
killall nautilus
```
