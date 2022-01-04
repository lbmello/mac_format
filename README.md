
# mac-format

CLI tool to format any possible mac address input text to some pretermined mac formats.

By defaul, the tool will clean the MAC address delimiters and reformat the address in lower and upper case, using two chars by group notation (xx:xx:xx:xx:xx:xx).

Only the follow delimiters will be added to the final addresses:

- Nothing.
- Single space.
- `:`
- `-`
- `_`
- `.`

---
# Installation

To install the tool, run the follow [pip](https://pypi.org/project/pip/) command:

```shell
    $ python3 -m pip install mac-format
```

To check if the tool is availabe, run:

```shell
    $ python3 -m pip freeze | grep mac-format
```

To simply run the tool, you can execute it calling the python module follow by the mac address:

```shell
    $ python3 -m mac_format 77:62:76:5F:B0:85
    
    |  | M |: 7762765FB08
    |  | m |: 7762765fb08
    | : | M |: 77:62:76:5F:B0:85
    | : | m |: 77:62:76:5f:b0:85
    | - | M |: 77-62-76-5F-B0-85
    | - | m |: 77-62-76-5f-b0-85
    | _ | M |: 77_62_76_5F_B0_85
    | _ | m |: 77_62_76_5f_b0_85
    | . | M |: 77.62.76.5F.B0.85
    | . | m |: 77.62.76.5f.b0.85
    |   | M |: 77 62 76 5F B0 85
    |   | m |: 77 62 76 5f b0 85
    ------------------------------
    The 7762765FB085's vendor is: Dell Inc.
```

If you just run the tool withou the MAC (`$ python3 -m mac_format`) an input field will be opened:

```shell
    $ py -m mac_format
    
    Type the MAC address: 77.62.76-5f.b0.85 

    |  | M |: 7762765FB08
    |  | m |: 7762765fb08
    | : | M |: 77:62:76:5F:B0:85
    ...
    The 7762765FB085's vendor is: Dell Inc.
```

To became easy to run, you can create an alias, the follow command:

```sudo echo 'alias macf="python3 -m mac_format"' >> ~/.zshrc```

* I'm using zsh in my shell, please change to your favorite shell rc file.

Then simply run `macf` in your shell to run the tool.
