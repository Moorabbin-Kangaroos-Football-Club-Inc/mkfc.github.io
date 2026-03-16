---
layout: default
title: Players
description: "Moorabbin Kangaroos player roster for the 2026 SFNL Division 4 season. Senior and Reserves teams."
---

# Players

The Moorabbin Kangaroos field two teams in the **SFNL Division 4** competition each season.

## Senior Team

| # | Player | Position |
|---|--------|----------|
{% for player in site.data.players.seniors %}| {{ player.number }} | {{ player.name }} | {{ player.position }} |
{% endfor %}

## Reserves Team

| # | Player | Position |
|---|--------|----------|
{% for player in site.data.players.reserves %}| {{ player.number }} | {{ player.name }} | {{ player.position }} |
{% endfor %}

*Roster last updated: March 2026. For match-day team sheets, see our [Facebook page](https://www.facebook.com/MoorabbinKangaroos).*

## Interested in Playing?

We welcome new players of all experience levels. Come down to training or get in touch:

- **Training**: Tuesday & Thursday, 6:00pm - 8:00pm
- **Location**: Widdop Crescent Oval, Hampton East 3188
- **Contact**: [info@mkfc.org.au](mailto:info@mkfc.org.au)
