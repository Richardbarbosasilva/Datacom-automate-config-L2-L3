## Dependencies

I provided all the packet links that are needed to replicate my actual development enviroment (not tested with other IDEs like pycharm or browsers like firefox and so on):

- [Bootstrap v5](http://getbootstrap.com/)
- [jQuery v3.4.1 (>= 1.9.0)](http://jquery.com/)
- [Python v3.12.6)](http://www.python.org/)
- [Chrome v129.0.6668.70)](https://www.google.pt/intl/pt-PT/chrome/?brand=OZZY&ds_kid=43700080663033589&gad_source=1&gclid=Cj0KCQjwr9m3BhDHARIsANut04Ze-cxBa8X7gW9GnJZwEchmEKV5FjVR5CuHXZ4XFJB2wq_6AP-QfDQaAugREALw_wcB&gclsrc=aw.ds)
- [Vscode v1.93)(recommended to always use the most recent release)](https://code.visualstudio.com/download)
- [fontawesome v?)](https://kit.fontawesome.com/64d58efce2.js)
- [flowbite v1.0 (>=1.0.0)](https://flowbite.com/docs/getting-started/introduction/)
- [flask v3.0.3) (>=2.3.0)](https://flask.palletsprojects.com/en/3.0.x/)

### Usage

Add the following resources for the bootstrap-treeview to function correctly.

```html CDN
<!-- Required Stylesheets -->
<link href="bootstrap.css" rel="stylesheet">

<!-- Required Javascript -->
<script src="jquery.js"></script>
<script src="bstreeview.js"></script>
```

The component will bind to any existing DOM element.

```html login page
loginpage.html
```

Basic usage may look something like this.

```javascript

function getTree() {
  // Some logic to retrieve, or generate tree structure
  return data;
}

$('#tree').bstreeview({ data: getTree() });
```

```python API

host= '127.0.0.1', port = '5000'

```







