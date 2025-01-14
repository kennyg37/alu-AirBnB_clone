from tests.test_models.test_base_model import TestBaseModel
from models.state import State

class TestState(TestBaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
