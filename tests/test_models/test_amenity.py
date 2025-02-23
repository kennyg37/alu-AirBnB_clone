from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity

class TestAmenity(TestBaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
