---
layout: default
title: Calendar
description: "Season 2026 fixtures, training schedule, and key dates for the Moorabbin Kangaroos Football Club."
---

# Season 2026 Calendar

## Training

- **Tuesday**: 6:00pm - 8:00pm
- **Thursday**: 6:00pm - 8:00pm
- **Location**: Widdop Crescent Oval, Hampton East 3188

## Season 2026 Fixtures

All home games are played at [**Moorabbin Reserve**](https://maps.app.goo.gl/DhGiLHBnpMiHvNTu5). Game times are 12 PM for Reserves and 2 PM for Seniors.

**[Download Full Season Calendar (.ics)](/calendar/mkfc-season-2026.ics)** — Import all 18 rounds into Apple Calendar, Google Calendar, or Outlook.

<table>
  <thead>
    <tr>
      <th>Rnd</th>
      <th>Date</th>
      <th>Opponent</th>
      <th>H/A</th>
      <th>Venue</th>
      <th>Add to Calendar</th>
    </tr>
  </thead>
  <tbody>
  {% for game in site.data.fixtures.games %}
    <tr>
      <td>{{ game.round }}</td>
      <td>{{ game.date | date: "%a %-d %b" }}</td>
      <td>{{ game.opponent }}</td>
      <td>{{ game.home_away }}</td>
      <td>{{ game.venue }}</td>
      <td>
        <small>
          <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=MKFC%20vs%20{{ game.opponent | url_encode }}&dates={{ game.date | date: '%Y%m%d' }}T040000Z/{{ game.date | date: '%Y%m%d' }}T070000Z&location={{ game.venue | url_encode }}&details=Round%20{{ game.round }}%20-%20{{ game.home_away }}%20%7C%20SFNL" target="_blank" rel="noopener">Google</a>
          &middot;
          <a href="#" class="ical-btn" data-round="{{ game.round }}" data-date="{{ game.date | date: '%Y%m%d' }}" data-opponent="{{ game.opponent }}" data-venue="{{ game.venue }}" data-homeaway="{{ game.home_away }}">iCal</a>
        </small>
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

### Finals Series

| Week | Date |
|---|---|
| Week 1 Finals | 15-16 August |
| Week 2 Finals | 22-23 August |
| Week 3 Finals | 29 August |
| Grand Final | 5 September |

## Results & Ladders

Full results and ladders are available on the [SportsTG / GameDay website](https://websites.mygameday.app/assoc_page.cgi?assoc=24578).

## Key Dates

Check our [Facebook page](https://www.facebook.com/MoorabbinKangaroos) for upcoming social events, fundraisers, and club functions.

<script>
document.querySelectorAll('.ical-btn').forEach(function(el) {
  el.addEventListener('click', function(e) {
    e.preventDefault();
    var d = el.dataset;
    var now = new Date().toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
    var lines = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//MKFC//Season 2026//EN',
      'BEGIN:VEVENT',
      'UID:mkfc-2026-r' + d.round + '@mkfc.org.au',
      'DTSTAMP:' + now,
      'DTSTART;TZID=Australia/Melbourne:' + d.date + 'T140000',
      'DTEND;TZID=Australia/Melbourne:' + d.date + 'T170000',
      'SUMMARY:MKFC vs ' + d.opponent,
      'LOCATION:' + d.venue,
      'DESCRIPTION:Round ' + d.round + ' - ' + d.homeaway + ' | SFNL',
      'STATUS:CONFIRMED',
      'END:VEVENT',
      'END:VCALENDAR'
    ];
    var blob = new Blob([lines.join('\r\n')], {type: 'text/calendar;charset=utf-8'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'mkfc-round-' + d.round + '.ics';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  });
});
</script>
