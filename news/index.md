---
layout: default
title: News
description: "Latest news from the Moorabbin Kangaroos Football Club including match reports, events, and announcements."
---

# Latest Club News

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %-d, %Y" }}*

{{ post.excerpt }}

[Read more]({{ post.url }})

---
{% endfor %}

*Subscribe to our newsletter for regular updates*
