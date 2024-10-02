# Previews and instructions

## Login page
![alt text](https://github.com/Richardbarbosasilva/Datacom-automate-config-L2-L3/blob/main/loginpage.png)

## Main page
![alt text](https://github.com/Richardbarbosasilva/Datacom-automate-config-L2-L3/blob/main/mainpage.png)

## Topology page
![alt text](https://github.com/Richardbarbosasilva/Datacom-automate-config-L2-L3/blob/main/topologypage.png)

## script page
![alt text](https://github.com/Richardbarbosasilva/Datacom-automate-config-L2-L3/blob/main/scriptpagegif.gif)

# Dependencies and enviroment

I provided these packet links that are needed to replicate my actual development enviroment:

- [Bootstrap v5](http://getbootstrap.com/)
- [jQuery v3.4.1 (>= 1.9.0)](http://jquery.com/)
- [Python v3.12.6)](http://www.python.org/)
- [Chrome v129.0.6668.70)](https://www.google.pt/intl/pt-PT/chrome/?brand=OZZY&ds_kid=43700080663033589&gad_source=1&gclid=Cj0KCQjwr9m3BhDHARIsANut04Ze-cxBa8X7gW9GnJZwEchmEKV5FjVR5CuHXZ4XFJB2wq_6AP-QfDQaAugREALw_wcB&gclsrc=aw.ds)
- [Vscode v1.93)(recommended to always use the most recent release)](https://code.visualstudio.com/download)
- [fontawesome v?)](https://kit.fontawesome.com/64d58efce2.js)
- [flowbite v1.0 (>=1.0.0)](https://flowbite.com/docs/getting-started/introduction/)
- [flask v3.0.3) (>=2.3.0)](https://flask.palletsprojects.com/en/3.0.x/)

# CMD Packets

In order to correctly install the enviroment you also need to install some libraries using pip packet manager:

- Flask
- Jquery
- Bootstrap
- Flowbite
- Pyautogui
- jinja2

## Usage

Add the following steps:

```Starting
start the loginpage.html with live server (or any other localhost server you wish)
the GUI configuration is only set on dm4370 page!
```

## html CDN bootstrap an jquery index
<!-- Required Stylesheets -->
<link href="bootstrap.css" rel="stylesheet">

<!-- Required Javascript -->
<script src="jquery.js"></script>
<script src="bstreeview.js"></script>


## Call python API (before open script page)
```
host= '127.0.0.1', port = '5000'

```

## Default front-end port
```
host= '127.0.0.1', port = '1010'

```

``` live server settings.json model

{
    "liveServer.settings.file": "loginpage.html",
    "liveServer.settings.port": 1010,
    "liveServer.settings.ChromeDebuggingAttachment": false,
    "liveServer.settings.CustomBrowser": "chrome"
}

```









