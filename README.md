# access-token-validation-governance-pack

Governance for resource-server validation of JWT and opaque access tokens, introspection, revocation, caching, mTLS, DPoP, policy-context mapping, failure, and audit evidence.

## Package identity

- Pack ID: `pack:access-token-validation`
- PyPI distribution: `access-token-validation-governance-pack`
- Python import: `access_token_validation_governance_pack`
- Reservation owner: `extension-pack:access-token-validation-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add access-token-validation-governance-pack
uv run ssot pack sync . access_token_validation_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://www.rfc-editor.org/rfc/rfc9068
- https://www.rfc-editor.org/rfc/rfc7662
- https://www.rfc-editor.org/rfc/rfc9449
- https://www.rfc-editor.org/rfc/rfc8705
