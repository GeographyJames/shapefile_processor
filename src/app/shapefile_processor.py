import fiona
from pathlib import Path
from fiona.crs import CRS
import shapely
from shapely.geometry import Polygon, Point, LineString, shape, MultiPolygon, MultiPoint, MultiLineString


def crs(path: Path) -> str:
    with fiona.open(path) as f:
        return CRS.to_string(f.crs) # type: ignore

def number_of_features(path: Path) -> int:
    with fiona.open(path) as f:
        return len(f)

def to_shapely(path: Path) -> list[shapely.Geometry]:
    with fiona.open(path) as f:
        shapes = [shape(feature.geometry) for feature in f]
    return shapes

def to_shapely_multipolygon(shapes: list[Polygon | Point | LineString]) -> shapely.Geometry:
    if isinstance(shapes[0], Polygon):
       return MultiPolygon(shapes)
    if isinstance(shapes[0], Point):
        return MultiPoint(shapes)
    if isinstance(shapes[0], LineString):
        return MultiLineString(shapes)

def geom_type(path: Path):
    with fiona.open(path) as f: 
        return f.schema["geometry"]

if __name__ == "__main__":
    path = Path("tests/test_data/1_valid_polygon_OSGB36.shp")
    print(type(crs(path)))
    print(crs(path))
    print(to_shapely(path))
    print(to_shapely_multipolygon(to_shapely(path)))
    print(type(geom_type(path)))