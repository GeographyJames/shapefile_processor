from src.app import shapefile_processor
from pathlib import Path
from fiona import Collection
import pytest
import attrs
import shapely
from shapely.geometry import Polygon, Point, LineString

@attrs.define
class Case:
    path: Path
    crs: str
    feature_count: int
    geometry_type: str

test_cases = [
    Case(Path("1_valid_polygon_OSGB36.shp"), "EPSG:27700", 1, "Polygon"),
    Case(Path("2_valid_polygons_WGS84.shp"), "EPSG:4326", 2, "Polygon"),
    Case(Path("3_valid_points_OSGB36.shp"), "EPSG:27700", 3, "Point"),
    Case(Path("3_valid_linestrings_OSGB36.shp"), "EPSG:27700", 3, "LineString"),
        ]

for case in test_cases:
    case.path = Path("tests/test_data/" / case.path)

@pytest.mark.parametrize("test_case", test_cases)
class TestShapefileProcessor:
    def test_should_return_CRS(self, test_case: Case) -> None:
        assert shapefile_processor.crs(test_case.path) == test_case.crs

    def test_should_return_feature_count(self, test_case: Case) -> None:
        assert shapefile_processor.number_of_features(test_case.path) == test_case.feature_count

    def should_return_list_of_shapely_geometries(self, test_case: Case) -> None:
        for geom in shapefile_processor.to_shapely(test_case.path):
            assert isinstance(geom, shapely.Geometry)

    def test_should_return_shapely_multigeometry(self, test_case: Case) -> None:
        assert isinstance(shapefile_processor.to_shapely_multipolygon(
            shapefile_processor.to_shapely(test_case.path)), shapely.Geometry)

    def test_should_return_geometry_type(self, test_case: Case) -> None:
        assert shapefile_processor.geom_type(test_case.path) == test_case.geometry_type