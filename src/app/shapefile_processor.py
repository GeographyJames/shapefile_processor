import fiona
from pathlib import Path
from fiona.crs import CRS

path = Path("tests/test_data/1_valid_polygon_OSGB36.shp")

def open_shapefile(path: Path) -> fiona.collection:
    with fiona.open(path) as f:
        return f
        
def crs(path: Path) -> str:
    with fiona.open(path) as f:
        return CRS.to_string(f.crs)
    
if __name__ == "__main__":
    print(type(crs(path)))
    print(crs(path))