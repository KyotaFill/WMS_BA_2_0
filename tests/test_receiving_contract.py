"""Check receiving examples against the published OpenAPI schemas."""

import json
from pathlib import Path
import unittest

from jsonschema import RefResolver
from jsonschema.exceptions import ValidationError
from openapi_schema_validator import OAS30Validator


API = json.loads((Path(__file__).resolve().parents[1] / "05_API/openapi_core.json").read_text(encoding="utf-8"))
RESOLVER = RefResolver.from_schema(API)


class ReceivingContractTests(unittest.TestCase):
    def validate_example(self, schema_name, example):
        schema = API["components"]["schemas"][schema_name]
        OAS30Validator(schema, resolver=RESOLVER).validate(example)

    def test_published_examples_match_dtos(self):
        create = API["paths"]["/receipts"]["post"]
        post = API["paths"]["/receipts/{id}/post"]["post"]
        revise = API["paths"]["/receipts/{id}/revise"]["post"]
        purchase_orders = API["paths"]["/purchase-orders"]["get"]
        self.validate_example("ReceiptDraftInput", create["requestBody"]["content"]["application/json"]["example"])
        self.validate_example("PurchaseOrderPage", purchase_orders["responses"]["200"]["content"]["application/json"]["example"])
        self.validate_example("Receipt", create["responses"]["201"]["content"]["application/json"]["example"])
        self.validate_example("ReceiptPostCommand", post["requestBody"]["content"]["application/json"]["example"])
        self.validate_example("ReceiptPostResult", post["responses"]["200"]["content"]["application/json"]["example"])
        self.validate_example("SimpleCommand", revise["requestBody"]["content"]["application/json"]["example"])

    def test_quantities_are_positive_decimal_strings(self):
        create = API["paths"]["/receipts"]["post"]["requestBody"]["content"]["application/json"]["example"]
        for invalid in (80, "0", "0.000000", "1.0000001", "100000000000000", "-1"):
            with self.subTest(invalid=invalid):
                payload = {**create, "lines": [{**create["lines"][0], "quantity": invalid}]}
                with self.assertRaises(ValidationError):
                    self.validate_example("ReceiptDraftInput", payload)

    def test_post_requires_destination_location(self):
        post = API["paths"]["/receipts/{id}/post"]["post"]["requestBody"]["content"]["application/json"]["example"]
        line = {key: value for key, value in post["lines"][0].items() if key != "destination_location_id"}
        with self.assertRaises(ValidationError):
            self.validate_example("ReceiptPostCommand", {**post, "lines": [line]})

    def test_new_serial_can_be_resolved_at_post(self):
        post = API["paths"]["/receipts/{id}/post"]["post"]["requestBody"]["content"]["application/json"]["example"]
        line = {key: value for key, value in post["lines"][0].items() if key != "stock_item_id"}
        line.update(serial_code="SN-001", quantity_base="1")
        self.validate_example("ReceiptPostCommand", {**post, "lines": [line]})
        with self.assertRaises(ValidationError):
            self.validate_example("ReceiptPostCommand", {**post, "lines": [{**line, "stock_item_id": post["lines"][0]["stock_item_id"]}]})


if __name__ == "__main__":
    unittest.main()
