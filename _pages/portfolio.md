---
layout: archive
title: "Portfolio"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

{% for post in site.portfolio reversed %}
  {% if post.include_on_website %}
    {% include portfolio-single.html %}
  {% endif %}
{% endfor %}