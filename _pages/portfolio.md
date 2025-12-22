---
layout: archive
title: "Portfolio"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}

{% assign shown = site.portfolio | where: "include_on_website", true %}

{% for slug in site.portfolio.portfolio_order %}
  {% assign post = shown | where: "slug", slug | first %}
  {% if post %}
    {% include portfolio-single.html %}
  {% endif %}
{% endfor %}

{# Optional: render anything not listed at the end #}
{% for post in shown %}
  {% unless site.data.portfolio_order contains post.slug %}
    {% include portfolio-single.html %}
  {% endunless %}
{% endfor %}
