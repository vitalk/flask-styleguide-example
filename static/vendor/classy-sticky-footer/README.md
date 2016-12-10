# Sticky Footer

A sticky footer works great if you can apply a fixed height to the footer. As
per http://css-tricks.com/snippets/css/sticky-footer/.

## Installation

The recommended installation method is a [bower](http://bower.io).

```shell
bower install --save classy-sticky-footer
```

## Usage

```less
@import 'classy-sticky-footer/objects.sticky-footer.less';

// Note, the mixin should be called at document root.
.classy-sticky-footer(42px);
```

```html
<div class="has-sticky-footer">
    Page
</div>
<footer class="sticky-footer">
    I'am sticky!
</footer>
```

Variable | Description
---|---
`@classy-sticky-footer-namespace` | The namespace uses for sticky footer (`sticky-footer` by default).

## License

Licensed under the [MIT license](http://mit-license.org/vitalk).
