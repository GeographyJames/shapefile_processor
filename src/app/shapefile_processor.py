import fiona
from pathlib import Path


def test():
    path = Path("tests/test_data/1_valid_polygon_OSGB36.shp")
    with fiona.open(path) as f:
        print(f.crs)

def open_shapefile(path: Path) -> fiona.collection:
    with fiona.open(path) as f:
        return f
        