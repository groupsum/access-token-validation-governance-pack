"""Inspect the installed pack identity."""

from access_token_validation_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:access-token-validation"
print(metadata["origin"]["id"])
