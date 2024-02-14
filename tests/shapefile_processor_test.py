from src.app import shapefile_processor
from pathlib import Path
from fiona import Collection

class TestShapefileProcessor:
    def test_should_return_shapefile(self):
        path = Path("tests/test_data/1_valid_polygon_OSGB36.shp")
        assert(path.is_file())
        assert(isinstance(shapefile_processor.open_shapefile(path), Collection))