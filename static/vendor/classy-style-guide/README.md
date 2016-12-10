# Classy Styleguide

Base Styleguide layout inspired by the [GitHub Styleguide](https://github.com/styleguide).


## Installation

The recommended installation method is a [bower](http://bower.io).

```shell
bower install --save classy-style-guide
```


## Usage

```jinja
<article class="style-guide" id="{{ section.section }}">
  <h3 class="style-guide__reference">{{ section.section }}</h3>

  <div class="style-guide__description">
    <p>{{ section.description|safe }}</p>
    {% if section.modifiers %}
      <ul class="style-guide__modifiers">
        {% for m in section.modifiers %}
          <li><strong>{{ m.name }}</strong> - {{ m.description }}</li>
        {% endfor %}
      </ul>
    {% endif %}
  </div>

  <div class="style-guide__element">
    {{ section.example|safe }}
  </div>

  {% for m in section.modifiers %}
    <div class="style-guide__element">
      <small class="style-guide__modifier">{{ m.name }}</small>
      {{ m.example|safe }}
    </div>
  {% endfor %}

  <div class="style-guide__html">
    <pre>{{ section.example|forceescape }}</pre>
  </div>
</article>
```

Variable | Description
---|---
`@classy-style-guide-namespace` | The namespace uses for classy style guide class names (`style-guide` by default).
`#classy-style-guide-vars` | The custom namespace for related variables.


## License

Licensed under the [MIT license](http://mit-license.org/vitalk).
