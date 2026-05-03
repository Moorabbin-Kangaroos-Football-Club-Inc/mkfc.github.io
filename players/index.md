---
layout: default
title: Players
description: "Moorabbin Kangaroos player roster for the 2026 SFNL Division 4 season. Senior and Reserves teams."
---

# Players

The Moorabbin Kangaroos field two teams in the **SFNL Division 4** competition each season.

{% assign seniors = site.players | where: "team", "seniors" | sort: "number" %}
{% assign reserves = site.players | where: "team", "reserves" | sort: "number" %}

## Senior Team

{% if seniors.size > 0 %}
| # | Player | Position |
|---|--------|----------|
{% for player in seniors %}| {{ player.number }} | [{{ player.name }}]({{ player.url | relative_url }}) | {{ player.position }} |
{% endfor %}
{% else %}
*Senior team roster coming soon.*
{% endif %}

## Reserves Team

{% if reserves.size > 0 %}
| # | Player | Position |
|---|--------|----------|
{% for player in reserves %}| {{ player.number }} | [{{ player.name }}]({{ player.url | relative_url }}) | {{ player.position }} |
{% endfor %}
{% else %}
*Reserves roster coming soon.*
{% endif %}

*Roster last updated: March 2026. For match-day team sheets, see our [Facebook page](https://www.facebook.com/MoorabbinKangaroos).*

## Interested in Playing?

We welcome new players of all experience levels. Come down to training or get in touch:

- **Training**: Tuesday & Thursday, 6:00pm - 8:00pm
- **Location**: Widdop Crescent Oval, Hampton East 3188
- **Contact**: [info@mkfc.org.au](mailto:info@mkfc.org.au)
