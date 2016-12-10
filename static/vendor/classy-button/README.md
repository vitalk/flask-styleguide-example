# Classy Button

A standart, but classy, button.

## Installation

The recommended installation method is a [bower](http://bower.io).

```shell
bower install --save classy-button
```

## Usage

Buttons have a few required constraints for proper functionality,
accessibility, and styling:

- Whenever possible, use `button` over `a`.
- Never set `tabindex` on buttons - let the browser automatically set that.

```html
<button class="button">Button</button>
<a class="button">A button link</a>
```

Variable | Description
---|---
`@classy-button-namespace` | The namespace uses for classy button (`button` by default).
`@classy-button-padding` | The vertical padding for buttons; the left and right values are doubled (`.6em` by default).
`@classy-button-padding-mini` | The vertical padding for mini buttons (a half of `@classy-button-padding` by default).

## License

Licensed under the [MIT license](http://mit-license.org/vitalk).
