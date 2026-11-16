# Cedar Ridge mock member API

Fictional demo data for a voice-agent demo. Cedar Ridge Health Plan is not a
real health plan and the members here are not real people.

## What this is

A stand-in for a health plan's member and claims system. Instead of a running
server, it is a set of small files. Each lookup is a web address:

| Lookup | Address ends with | Returns |
|---|---|---|
| Identity check | `api/verify/<member_id>/<date_of_birth>.json` | `verified: true` and the member's first name |
| Claim status | `api/claims/<member_id>/<date_of_birth>.json` | That member's claims |

A file only exists when the member ID and date of birth match. A wrong
combination finds nothing, and the agent treats that as "not verified."
Dates are written YYYY-MM-DD, for example `1954-03-14`.

## How to change the data

1. Edit `data/members.json` (add a member, change a claim).
2. Run `python3 build.py` to rebuild the `api` folder.
3. Commit and push.

Or ask Claude: "add a member named ... with a denied claim for ..." and it
will do all three steps.

## Test members

| Member | Member ID | Date of birth |
|---|---|---|
| Maria | CR-204-881 | 1954-03-14 |
| Harold | CR-118-402 | 1949-11-02 |
