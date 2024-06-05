import json

import allure
from allure import attachment_type


def test_attachments():
    allure.attach("Text content", name="Здесь будет - Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="Здесь будет - Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Здесь будет - Json", attachment_type=attachment_type.JSON)