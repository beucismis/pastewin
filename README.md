# pastewin

A light and fast static front-end for users of countries where Pastebin is banned. It was created with Python and Flask.

Official instance: https://pastewin.up.railway.app

![Screenshot](https://user-images.githubusercontent.com/40023234/164679737-ed4ad861-c215-4faf-b327-dffca21fd6ed.png)

It is recommended to use it with the [Redirector](https://einaregilsson.com/redirector) browser plugin. Example configuration:
```
Description: Pastebin to Pastewin
Example URL: https://pastewin.up.railway.app/B5EfdLF6
Include pattern: ^https?://(?:.*\.)*(?<!link.)pastebin\.com(/.*)?$
Redirect to: https://pastewin.up.railway.app$1
Pattern type: Regular Expression
Pattern Description: ?
Example result: https://pastewin.up.railway.app/B5EfdLF6
```

## Install and Run

Clone the reporistrory:
```shell
git clone https://github.com/beucismis/pastewin
```

Install dependencies:
```shell
cd pastewin
pip3 install --user -r requirements.txt
```

Running:
```shell
python3 pastewin/app.py
```

Check the `https://0.0.0.0:5000` address.

## License

This project lisanced under GPL-3.0 - for details check [LICENSE](LICENSE) file.
