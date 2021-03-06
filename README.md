# Living Styleguide

Example of living Styleguide made with [Flask-Styleguide](https://github.com/vitalk/flask-styleguide)
and [Frozen-Flask](https://github.com/SimonSapin/Frozen-Flask/). This guide
describes how to generate your own styleguide for any flask application.

- Use [KSS](http://warpspire.com/kss/) to document your stylesheets. KSS is
  documentation syntax for any flavor CSS. It's human readable, machine
  parsable, and easy to remember. [Flask-Styleguide](https://github.com/vitalk/flask-styleguide)
  looks for any KSS formated documentation in static directories of your
  application and registered blueprints (if any). 

  ```less
  // A standard, but classy, button used widely for submit forms and
  // to complete other app actions.
  //
  // :hover - Hover state.
  // :active - When the button is pressed.
  // :focus - When the button is focused.
  // :disabled - Disabled state.
  // .is-disabled - Same as above.
  //
  // Styleguide 2.1.
  ```

- Define endpoint for your styleguide in application:

  ```python
  @app.route('/styleguide/')
  def styleguide():
      return render_template('styleguide.html')
  ```

- The new jinja tag `styleguide` becomes available when `flask_styleguide` is
  initialized. Let's write some html examples for our buttons:

  ```jinja
  {% extends 'layout.html' %}
  {% block main %}
    {% styleguide "2.1" %}
      <button class="button$modifier_class">Button</button>
      <a class="button$modifier_class">A button link</a>
    {% endstyleguide %}
  {% endblock %}
  ```

- The `styleguide/section.html` template will be used for each section in your
  styleguide (like `2.1` in the previous step). Let's define it:

  ```jinja
  <article class="style-guide" id="{{ section.section }}">
    <h4 class="style-guide-reference">{{ section.section }}</h4>

    <div class="style-guide-description">
      <p>{{ section.description|safe }}</p>
      {% if section.modifiers %}
        <ul class="style-guide-modifiers">
          {% for m in section.modifiers %}
            <li><strong>{{ m.name }}</strong> - {{ m.description }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    </div>

    <div class="style-guide-element">
      {{ section.example|safe }}
    </div>

    {% for m in section.modifiers %}
      <div class="style-guide-element">
        <small class="style-guide-modifier">{{ m.name }}</small>
        {{ m.example|safe }}
      </div>
    {% endfor %}

    <div class="style-guide-html">
      <pre>{{ section.example|forceescape }}</pre>
    </div>
  </article>
  ```

- Prettify styleguide. Without styles styleguide looks not so great. Apply
  some styling to it or reuse this one:

  ```bash
  bower install --save classy-style-guide
  ```

  ```less
  @import 'classy-style-guide/components.style-guide.less';
  ```

- Now that you’re up and running. Fire up a browser and go to the
  [brand new styleguide...](https://vitalk.github.io/flask-styleguide-example)
