## Dependencies

Where provided these are the actual versions bootstrap-treeview has been tested against.

- [Bootstrap v5)](http://getbootstrap.com/)
- [jQuery v3.4.1 (>= 1.9.0)](http://jquery.com/)

### Usage

Add the following resources for the bootstrap-treeview to function correctly.

```html
<!-- Required Stylesheets -->
<link href="bootstrap.css" rel="stylesheet">

<!-- Required Javascript -->
<script src="jquery.js"></script>
<script src="bstreeview.js"></script>
```

The component will bind to any existing DOM element.

```html
<div id="tree"></div>
```

Basic usage may look something like this.

```javascript
function getTree() {
  // Some logic to retrieve, or generate tree structure
  return data;
}

$('#tree').bstreeview({ data: getTree() });
```


## Data Structure

In order to define the hierarchical structure needed for the tree it's necessary to provide a nested array of JavaScript objects.





