import fiona
from pathlib import Path
from fiona.crs import CRS

path = Path("tests/test_data/1_valid_polygon_OSGB36.shp")
        
def crs(path: Path) -> str:
    with fiona.open(path) as f:
        return CRS.to_string(f.crs)

def number_of_features(path: Path) -> str:
    with fiona.open(path) as f:
        return len(f)
        
if __name__ == "__main__":
    print(type(crs(path)))
    print(crs(path))