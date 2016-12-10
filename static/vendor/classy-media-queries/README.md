# Classy media queries

Defines a few variables to simplify usage of media queries.

```less
.main {
    color: orangered;

    @media @laptop {
        color: red;
    }
}
```

## Installation

The recommended installation method is a [bower](http://bower.io).

```shell
bower install --save classy-media-queries
```

## Usage

Breakpoint | Value
---|---
`@classy-palm-to` | `30em`
`@classy-tablet-from` | `30.0625em`
`@classy-tablet-to` | `48em`
`@classy-laptop-from` | `48.0625em`
`@classy-laptop-to` | `67.5em`
`@classy-tablet-from` | `67.5625em`


Media query | Description
---|---
`@classy-portrait` | Portrait orientation.
`@classy-landspace` | Landspace orientation.
`@classy-retina` | Retina support.
`@classy-mobile` | Only mobile screen.
`@classy-tablet` | Only tablet screen.
`@classy-tablet-and-up` | Tablets and above.
`@classy-laptop` | Only laptop.
`@classy-laptop-and-up` | Laptop screen and above.
`@classy-desktop` | Only desktop screen.

## License

Licensed under the [MIT license](http://mit-license.org/vitalk).
