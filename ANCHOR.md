# Anchor — drand round 6669250

Entry: **One Sentence for a Traveler from 1800** — competition
`u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb`, account **@berkahmuse**.

## drand beacon (MAINNET — not quicknet)

Fetched live from the public drand relay (`https://drand.cloudflare.com/public/6669250`
and `https://api.drand.sh/public/6669250`; both relays returned identical values)
at **2026-11-24T08:22:04Z (15:22 WIB)**. Chain info from
`https://drand.cloudflare.com/info`: scheme `pedersen-bls-chained`, period 30 s,
genesis 1595431050, beaconID `default` — this is the **drand mainnet** chain
(the builder's session note calling it "quicknet" was wrong; the chain hash below
is mainnet, not the quicknet hash `52db9ba7…`).

| Field | Value |
|---|---|
| Chain | drand mainnet — hash `8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce` |
| Round | `6669250` |
| Randomness | `41d730f06faa5bdd3d939d9f955333c380c8a8b082d1728243439ee0c33442be` |
| Signature | `861e52bf075c6c575f15fb11411bac9458c01d8f80a8a767d9f1acd3e4f4f5e0684a20463a825415d1fbd1c0a7a4a76a1584d5a2d3c1815c5730c47b9db4475d2f6c9a9e071f7390f366eb412342766a57c68680f96f97cef83b1258e078e6ac` |
| Previous signature | `88d4aa0292fae9d798accba2706e654227e86ee93b18371a4e482293f263c80ffea4368396e17796774c9570686bdcf60868386a5033aceaa1db14b826d004a8e5e48f87955398ea108b38caff6cbe825049113d8a98d4b24f3c456e59d7d661` |
| Wallet | `CnLniiw3PHTymsZvCiMw54wA84dv4ghELdKQMGhB8PbT` |

Same values recorded in `.makefun/freshness.json` (scheme `drand-mainnet`).

## Anchor-before-write sequence

Builder session file:
`~/agents/agent-32c68325-a8c8-4262-b59c-49a818e572c8/sessions/32c68325-a8c8-4262-b59c-49a818e572c8.jsonl`

- **seq 32** (2026-11-24T08:22:04Z): drand relay fetch returns round 6669250 with the
  randomness above.
- **seq 33** (2026-11-24T08:22:15Z): builder quotes the anchor (round, randomness,
  signature) in its reasoning, before drafting the sentence.
- **seq 42**: first write to the entry file (`main.py`).

The anchor was therefore quoted **before the first write** to the entry file.

## Verification

- `main.py` run twice: byte-identical output.
- Output sha256: `a5d6bb32de82854671a6fc9d4b27af6ec911e198d1ec954895798cbde0540159`
- Sentence: 178 characters (gate 1–200).
