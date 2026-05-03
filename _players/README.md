# Adding a Player Profile

Each player on the roster is a single Markdown file in this folder
(`_players/`). When you add a file here, Jekyll automatically:

- generates a profile page at `/players/<filename>/`
- adds a row to the roster table on `/players/`
- links the player's name in that table to their profile page

You only need to **get the player's written consent** before publishing,
then add a Markdown file. No code changes required.

## 1. Get consent

Before publishing any real player's name, photo, or biographical details,
get explicit written consent from the player. For under-18s, get
parental consent as well. Keep a record of the consent — a signed form
or an email reply is fine.

## 2. Create the Markdown file

Create a new file in `_players/` named after the player using
**lowercase-with-hyphens**. The filename becomes the URL.

```
_players/john-smith.md   →   https://www.mkfc.org.au/players/john-smith/
```

## 3. Fill in the frontmatter

Copy the template below into the new file and fill it in. Everything
between the two `---` lines is **frontmatter** (structured data); the
content underneath is the player's bio (free-form Markdown).

```markdown
---
name: John Smith
number: 23
position: Midfielder
team: seniors
photo: /assets/players/john-smith.jpg
joined: 2021
---

A short bio paragraph about John — where he grew up, how he came to
MKFC, his playing style, and what he brings to the team.

## Career Highlights

- Best and Fairest 2024
- Premiership team 2023

## Off the Field

What John does outside footy — work, study, family, hobbies.
```

### Frontmatter fields

| Field      | Required | Notes                                                |
|------------|----------|------------------------------------------------------|
| `name`     | yes      | Full name as displayed on the profile and roster.    |
| `number`   | yes      | Jersey number. Used to sort the roster table.        |
| `position` | yes      | E.g. *Midfielder*, *Forward*, *Defender*, *Ruck*.    |
| `team`     | yes      | Either `seniors` or `reserves` (lowercase, exact).   |
| `photo`    | no       | Path to a player photo (see step 4). Falls back to the club logo if omitted. |
| `joined`   | no       | Year they joined MKFC.                               |

## 4. Add the photo (optional)

If you have a photo:

1. Save it as a square JPG or PNG (recommended: 600 × 600 px or larger).
2. Place it in `assets/players/` — create that folder if it doesn't
   exist yet.
3. Name it to match the Markdown filename: `john-smith.jpg`.
4. Reference it in the frontmatter:
   `photo: /assets/players/john-smith.jpg`.

If you skip the photo, the club logo is used as a placeholder.

## 5. Preview locally (optional)

```bash
bundle exec jekyll serve
```

Visit <http://localhost:4000/players/> to see the roster, and click the
player's name to view their profile page.

## 6. Commit and push

Commit the new Markdown file (and photo, if any) and push to `main`.
GitHub Pages will rebuild and publish the new profile within a minute.

## Removing a player

Delete the file from `_players/` (and the photo from `assets/players/`,
if any), then commit and push. The profile page and roster row both
disappear automatically.

## Reference

- Example profile: [`example-player.md`](example-player.md)
- Example reserve: [`example-reserve.md`](example-reserve.md)
- Profile layout: [`../_layouts/player.html`](../_layouts/player.html)
- Roster page source: [`../players/index.md`](../players/index.md)
