# Access Token Validation Governance pack guide

Governance for resource-server validation of JWT and opaque access tokens, introspection, revocation, caching, mTLS, DPoP, policy-context mapping, failure, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `access-token-validation-governance-pack` is an installable SSOT governance pack for Access Token Validation. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for access token validation, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`access-token-validation-governance-pack`](https://pypi.org/project/access-token-validation-governance-pack/)
- GitHub package repository: [`groupsum/access-token-validation-governance-pack`](https://github.com/groupsum/access-token-validation-governance-pack)
- Import package: `access_token_validation_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:access-token-validation`
- PyPI package: `access-token-validation-governance-pack`
- Import package: `access_token_validation_governance_pack`
- GitHub repository: [groupsum/access-token-validation-governance-pack](https://github.com/groupsum/access-token-validation-governance-pack)
- Reservation owner: `extension-pack:access-token-validation-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Access Token Validation

## Authority Sources

- [RFC 9068: JWT Profile for OAuth 2.0 Access Tokens](https://www.rfc-editor.org/rfc/rfc9068)
- [RFC 7662: OAuth 2.0 Token Introspection](https://www.rfc-editor.org/rfc/rfc7662)
- [RFC 9449: Demonstrating Proof of Possession](https://www.rfc-editor.org/rfc/rfc9449)
- [RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication](https://www.rfc-editor.org/rfc/rfc8705)

## Included ADRs

- [`adr:resource-servers-own-access-token-validation`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/adr/ADR-1000-resource-servers-own-access-token-validation.yaml) - Resource Servers Own Access Token Validation
- [`adr:token-claims-are-validated-authority-inputs-not-permissions`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/adr/ADR-1001-token-claims-are-validated-authority-inputs-not-permissions.yaml) - Token Claims Are Validated Authority Inputs Not Permissions
- [`adr:sender-constrained-token-policy-is-explicit`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/adr/ADR-1002-sender-constrained-token-policy-is-explicit.yaml) - Sender Constrained Token Policy Is Explicit

## Included SPECs

- [`spc:jwt-access-token-validation-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2000-jwt-access-token-validation-contract.yaml) - JWT Access Token Validation Contract
- [`spc:opaque-token-introspection-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2001-opaque-token-introspection-contract.yaml) - Opaque Token Introspection Contract
- [`spc:token-revocation-expiration-and-cache-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2002-token-revocation-expiration-and-cache-contract.yaml) - Token Revocation Expiration And Cache Contract
- [`spc:mtls-and-dpop-sender-constraint-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2003-mtls-and-dpop-sender-constraint-contract.yaml) - mTLS And DPoP Sender Constraint Contract
- [`spc:token-to-policy-context-mapping-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2004-token-to-policy-context-mapping-contract.yaml) - Token To Policy Context Mapping Contract
- [`spc:token-validation-audit-and-failure-contract`](https://github.com/groupsum/access-token-validation-governance-pack/blob/master/src/access_token_validation_governance_pack/templates/specs/SPEC-2005-token-validation-audit-and-failure-contract.yaml) - Token Validation Audit And Failure Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect access_token_validation_governance_pack
uvx --from ssot-registry ssot pack preflight . access_token_validation_governance_pack --all
uvx --from ssot-registry ssot pack sync . access_token_validation_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from access_token_validation_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-jwt-access-token-validation-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/access-token-validation-governance-pack](https://github.com/groupsum/access-token-validation-governance-pack)
- PyPI package: [access-token-validation-governance-pack](https://pypi.org/project/access-token-validation-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the access token validation governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
