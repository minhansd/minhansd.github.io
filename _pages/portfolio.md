---
layout: archive
title: "Portfolio"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

{% assign items = site.portfolio | where: "include_on_website", true | sort: "weight" %}
{% for post in items %}
  {% include portfolio-single.html %}
{% endfor %}
