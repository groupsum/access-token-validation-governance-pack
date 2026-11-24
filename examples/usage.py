"""Find a specification and its downstream path in the installed manifest."""

from access_token_validation_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:jwt-access-token-validation-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-jwt-access-token-validation-contract.yaml"
