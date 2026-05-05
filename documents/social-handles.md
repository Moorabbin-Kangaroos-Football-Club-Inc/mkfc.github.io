---
published: false
---

# MKFC Social Media — Status & Action Plan

Working document. Tracks the consolidation of social handles and the actions still outstanding. `published: false` keeps this file out of the live site.

---

## Decision: Option A adopted (2026-05-05)

The committee adopted **Option A — `moorabbinkangas`** as the canonical handle. Instagram and X/Twitter were migrated from `moorabbinroos` to match the existing Facebook handle. Website, JSON-LD structured data, welcome pack, contact page, and the Bunnings flyer have all been updated.

The original options (A/B/C/D) and their pros/cons are preserved in git history (see prior revisions of this file) for posterity.

---

## Current state

| Platform | Handle | URL | Status |
|----------|--------|-----|--------|
| Facebook | `MoorabbinKangas` | facebook.com/MoorabbinKangas | ✅ aligned |
| Instagram | `moorabbinkangas` | instagram.com/moorabbinkangas | ✅ migrated |
| X / Twitter | `moorabbinkangas` | x.com/@moorabbinkangas | ✅ migrated |
| TikTok | *(not claimed)* | — | ⬜ defensive claim pending |
| YouTube | `MoorabbinKangas` | youtube.com/@MoorabbinKangas | ✅ claimed |
| Threads | *(not claimed)* | — | ⬜ defensive claim pending |
| Bluesky | *(not claimed)* | — | ⬜ defensive claim pending |
| LinkedIn | *(no club page)* | — | ⬜ create page |

The three primary platforms are now consistent. Cross-promotion ("follow us @moorabbinkangas everywhere") finally works on the platforms we actually use.

---

## Outstanding actions

### High priority — link FB and IG properly

- [ ] **Convert Instagram to Business or Creator account** if not already. Required before Business Suite linking. Category: Sports Team.
- [ ] **Link Facebook ↔ Instagram via Meta Business Suite.** Step-by-step in [§ Linking FB and IG via Meta Business Suite](#linking-fb-and-ig-via-meta-business-suite) below. ~20 minutes.
- [ ] **Update bios** on FB and IG with the agreed copy in [§ Bio copy ready to paste](#bio-copy-ready-to-paste).
- [ ] **Walk through the [§ Per-profile checklist](#per-profile-checklist)** for both FB and IG and fix anything off-brand.
- [ ] **Assign a Social Media lead** on the committee to own posting cadence, inbox response, and handle hygiene. Without this, the linkage benefits don't compound.

### Defensive handle claims (~30 min, free)

Claim `moorabbinkangas` on:

- [ ] TikTok
- [x] YouTube
- [ ] Threads (auto-creates from Instagram, just confirm)
- [ ] Bluesky

Plus consider reserving `mkfc.au` and `moorabbinkangaroos.com.au` domain variants if not already held.

### Content / activation

- [ ] **TikTok** — claim handle and start posting. Player-of-the-week reels, training highlights, behind-the-scenes. Single biggest reach lever for community sport recruitment under 25.
- [x] **YouTube** — handle `@MoorabbinKangas` claimed. Use for game replays, season highlights. Long-tail discoverability and sponsors love embeddable highlight reels.
- [ ] **Threads** — cross-post from Instagram (free piggyback on IG audience).
- [ ] **LinkedIn** — create a club page (separate from personal profiles). Sponsorship outreach and volunteer / committee recruitment.

### Website integration

- [ ] **Embed an Instagram feed** on the home or news page to replace the "Photos coming soon" placeholder on `gallery/index.md`. Options: native `<blockquote class="instagram-media">` embeds, or a service like SnapWidget for a grid.
- [x] **JSON-LD `sameAs` block** in `_includes/custom-head.html` already lists FB, IG, X — good for Google Knowledge Panel consolidation.
- [x] **Footer social links** in `_config.yml` (`minima.social_links`) already in place across FB, IG, X.
- [ ] Consider building a `/links` page on `mkfc.org.au` as a self-hosted alternative to Linktree (one consolidated landing for all socials), and pointing the IG bio Website field at it. Keeps branding on-brand and analytics first-party.

---

## Linking FB and IG via Meta Business Suite

Do these in order, one sitting:

1. **Make sure Instagram is a Business or Creator account.** IG → Profile → Settings → Account type → switch from Personal. Pick *Sports Team* category.
2. **Open [business.facebook.com](https://business.facebook.com)** with the FB account that admins the MoorabbinKangas page. If the club doesn't have a Business Suite yet, create one and add the page.
3. **Settings → Accounts → Instagram accounts → Add.** Log in as `@moorabbinkangas` and confirm. The Facebook page and Instagram account are now formally linked.
4. **Turn on cross-posting** (Settings → Page settings → Linked accounts → Instagram). Anything posted from Business Suite then publishes to both platforms; Reels created on IG can mirror to FB automatically.
5. **Unified inbox** — Business Suite → Inbox now combines FB Messenger, IG DMs, and comments from both. Critical for inbound enquiries from prospective players/sponsors that we're probably missing today.
6. **Tag-link** — on the IG profile, edit profile → "Page" field → select the Moorabbin Kangaroos FB page. This puts a small "Page" link directly under the IG bio, sending visitors straight to FB.

After step 6 the profiles are *linked* in the technical sense Meta recognises — page badge appears, suggested-follow prompts route IG users to FB and vice versa, and ads run unified.

---

## Bio copy ready to paste

### Instagram bio (150 char limit)

**Pre-linking version** (use until Meta Business Suite linking is complete):

```
Moorabbin Kangaroos Football Club
SFNL Div 4 · Est. 1965
Hampton East, Melbourne
FB: /MoorabbinKangas
```

**Post-linking version** (use once the FB page badge shows under the IG bio — drop the FB line, reuse the space):

```
Moorabbin Kangaroos Football Club
SFNL Div 4 · Est. 1965 🦘
Hampton East, Melbourne
New players welcome ⬇️
```

**Website field** (separate from bio): `https://mkfc.org.au` — don't waste bio characters on it.

### Facebook — three fields

**Page bio** (shows under cover photo, ~101 char limit):

```
SFNL Division 4 men's footy club, est. 1965. Hampton East, Melbourne. IG: @moorabbinkangas
```

**Short description / Description field** (~255 char):

```
Moorabbin Kangaroos Football Club — SFNL Division 4 senior men's club, founded 1965. Home ground: Widdop Crescent, Hampton East. Follow us on Instagram @moorabbinkangas and visit mkfc.org.au for fixtures, news, and join enquiries.
```

**Story / About** (long form, no real limit):

```
The Moorabbin Kangaroos Football Club has been part of the local community since 1965. We compete in the Southern Football and Netball League (SFNL) Division 4 from our home ground at Widdop Crescent, Hampton East.

Whether you're a player looking for a club, a sponsor backing local sport, or a supporter on match day, we'd love to hear from you.

🌐 mkfc.org.au
📷 Instagram: @moorabbinkangas
🐦 X: @moorabbinkangas
```

---

## Per-profile checklist

Walk through both Facebook and Instagram:

| Element | Standard |
|---|---|
| Display name | "Moorabbin Kangaroos Football Club" — verbatim, identical on both |
| Profile picture | Club logo, square, on Deep Navy `#01285E` background. Same image on FB and IG. Test it small (40 px) — does it read? |
| Cover/header image (FB) | Action shot or branded banner using `#01285E` / `#1A5A8E`. Refresh each season. |
| Bio mentions | Full club name · SFNL Division · location · website |
| Category | "Sports Team" or "Sports & Recreation" on FB; "Sports Team" on IG |
| Contact info | Same email/phone on both. Address: ground location (Widdop Crescent, Hampton East) |
| Pinned post (FB) | A current "About / how to join" post. Refresh each season. |
| Story highlights (IG) | Match Days · Training · Players · Sponsors · How to Join. Cover thumbnails on-brand (navy + white). |
| Hashtags | `#GoKangas #MKFC #MoorabbinKangas #SFNL` — agreed bank, used on every post |

---

## Handle conventions (now committed)

- Primary: `@moorabbinkangas` everywhere
- Email signature: "Follow us @moorabbinkangas on Facebook, Instagram, and X"
- Hashtags: `#GoKangas` `#MKFC` `#MoorabbinKangas` `#SFNL`
- Mascot account (optional, low priority): `@kanga_themascot` for fun behind-the-scenes content

---

## Linking the profiles to each other — summary

Once Meta Business Suite linking is done:

- IG profile gets a "Page" link directly under the bio pointing to the FB page
- Posts created in Business Suite publish to both platforms simultaneously
- Reels and stories can mirror automatically
- DMs and comments from both platforms land in one inbox
- Ads run as a single campaign across both audiences

In addition, plain-text cross-references in each bio (`FB: /MoorabbinKangas` on IG, `IG: @moorabbinkangas` on FB) catch users who don't notice the badge.

---

## Open questions

- Do we have admin access for all current accounts? Worth confirming before any further changes — losing access to a verified Facebook page is painful to recover.
- Is anyone currently posting consistently? A unified handle without a content plan won't help recruitment. The Social Media lead role above is the bottleneck.
- Should junior teams have a separate handle, or stay under the main club account? Recommendation: stay unified to consolidate audience.
- Is the X/Twitter URL canonical form (`https://x.com/moorabbinkangas`, no `@`) or with `@` (`https://x.com/@moorabbinkangas`)? Both work — site currently uses the `@` form per the URL provided to the committee.
