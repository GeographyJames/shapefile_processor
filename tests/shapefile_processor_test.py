from src.app import shapefile_processor
from pathlib import Path
from fiona import Collection
import pytest
import attrs

@attrs.define
class Case:
    path: Path
    crs: str
    feature_count: int

test_cases = [
    Case(Path("1_valid_polygon_OSGB36.shp"), "EPSG:27700", 1,),
    Case(Path("2_valid_polygons_WGS84.shp"), "EPSG:4326", 2,),
        ]

for case in test_cases:
    case.path = Path("tests/test_data/" / case.path)

@pytest.mark.parametrize("test_case", test_cases)
class TestShapefileProcessor:
    def test_should_return_CRS(self, test_case: Case):
        assert shapefile_processor.crs(test_case.path) == test_case.crs
 
    def test_should_return_feature_count(self, test_case: Case):
        assert shapefile_processor.number_of_features(test_case.path) == test_case.feature_count