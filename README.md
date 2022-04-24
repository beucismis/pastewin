# pastewin

No Flash, No Java, No Websocket, No Bullshit. This is for countries where Pastebin is banned or for those who want a light and fast static front-end. It was created with Python and Flask.

Official instance: https://pastewin.herokuapp.com

![Screenshot](https://user-images.githubusercontent.com/40023234/164679737-ed4ad861-c215-4faf-b327-dffca21fd6ed.png)

It is recommended to use it with the [Redirector](https://einaregilsson.com/redirector) browser plugin. Example configuration:
```
Description: Pastebin to Pastewin
Example URL: https://pastebin.com/B5EfdLF6
Include pattern: ^https?://(?:.*\.)*(?<!link.)pastebin\.com(/.*)?$
Redirect to: https://pastewin.herokuapp.com$1
Pattern type: Regular Expression
Pattern Description: ?
Example result: https://pastewin.herokuapp.com/B5EfdLF6
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