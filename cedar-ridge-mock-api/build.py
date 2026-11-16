"""Rebuilds the mock API files from data/members.json.

The "API" is just folders of small JSON files. A lookup is a web address:
  api/verify/<member_id>/<date_of_birth>.json   -> identity check
  api/claims/<member_id>/<date_of_birth>.json   -> that member's claims
A file only exists when the member ID and date of birth match, so a wrong
combination finds nothing (and the voice agent treats that as "not verified").
"""
import json, shutil
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / "data" / "members.json").read_text())
api = root / "api"
if api.exists():
    shutil.rmtree(api)

def id_variants(member_id):
    # Accept the ID with or without hyphens, upper or lower case.
    plain = member_id.replace("-", "")
    return sorted({member_id, plain, member_id.lower(), plain.lower()})

count = 0
for m in data["members"]:
    verify = {"verified": True, "member_id": m["member_id"], "first_name": m["first_name"],
              "plan": data["plan"], "preferred_language": m["preferred_language"]}
    claims = {"verified": True, "member_id": m["member_id"], "claims": m["claims"]}
    for mid in id_variants(m["member_id"]):
        for kind, body in (("verify", verify), ("claims", claims)):
            p = api / kind / mid / f'{m["date_of_birth"]}.json'
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(body, indent=2) + "\n")
            count += 1
print(f"Wrote {count} files for {len(data['members'])} members")
