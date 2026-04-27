---
layout: default
title: News
description: "Latest news from the Moorabbin Kangaroos Football Club including match reports, events, and announcements."
---

# Latest Club News

<div class="info-cards">
{% for post in site.posts %}
  <a class="info-card" href="{{ post.url | relative_url }}">
    <img class="card-image" src="{{ post.image | default: '/logo-2025.jpg' }}" alt="{{ post.title | escape }}">
    <div class="card-body">
      <h3>{{ post.title }}</h3>
      <p><em>{{ post.date | date: "%B %-d, %Y" }}</em></p>
      <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
    </div>
  </a>
{% endfor %}
</div>

*Subscribe to our newsletter for regular updates*
