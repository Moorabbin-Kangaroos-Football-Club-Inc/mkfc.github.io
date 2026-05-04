---
layout: default
title: Players
description: "Moorabbin Kangaroos player roster for the 2026 SFNL Division 4 season."
---

# Players

The Moorabbin Kangaroos field two teams in the **SFNL Division 4** competition each season. Players move between the Seniors and Reserves through the year, so we list our full squad together.

{% assign squad = site.players | sort: "number" %}

## Squad

{% if squad.size > 0 %}
| # | Player | Position |
|---|--------|----------|
{% for player in squad %}| {{ player.number }} | [{{ player.name }}]({{ player.url | relative_url }}) | {{ player.position }} |
{% endfor %}
{% else %}
*Squad roster coming soon.*
{% endif %}

*Roster last updated: March 2026. For match-day team sheets, see our [Facebook page](https://www.facebook.com/MoorabbinKangas).*

## Interested in Playing?

We welcome new players of all experience levels. Come down to training or get in touch:

- **Training**: Tuesday & Thursday, 6:00pm - 8:00pm
- **Location**: Widdop Crescent Oval, Hampton East 3188
- **Contact**: [info@mkfc.org.au](mailto:info@mkfc.org.au)
