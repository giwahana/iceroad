"""
Raster
------

Tools for raster I/o and manipulation

Some code originates from https://github.com/rwspicer/spicebox
which is licensed under the MIT License

"""
from osgeo import gdal
import numpy as np


def load_raster (filename,  return_dataset = False):
    """Load a raster file and it's metadata

    TAKEN FROM SPICEBOX v0.5.0
    
    Parameters
    ----------
    filename: str
        path to raster file to read
    return_dataset: bool
        if true return gdal.dataset
        
    Returns 
    -------
    gdal.dataset
        or 
    np.array
        2d raster data
    RASTER_METADATA
        metadata on raster file read
    """
    dataset = gdal.Open(filename, gdal.GA_ReadOnly)
    # (X, deltaX, rotation, Y, rotation, deltaY) = dataset.GetGeoTransform()
    if return_dataset:
        return dataset

    metadata = {
        'transform': dataset.GetGeoTransform(),
        'projection': dataset.GetProjection(),
        'x_size': dataset.RasterXSize,
        'y_size': dataset.RasterYSize,
    }

    data = dataset.GetRasterBand(1).ReadAsArray()
    return data, metadata


def clip_polygon_raster (
    in_raster, out_raster, vector, **warp_options
    ):
    """clips raster from shape using gdal warp

    TAKEN FROM SPICEBOX v0.5.0

    Parameters
    ----------
    in_raster: path or gdal.Dataset
        input rater 
    out_raster: path
        file to save clipped data to
    vector: path
        path to vector file with shape to clip to
    warp_options:
        keyword options for gdal warp as formated for gdal.WarpOptions
        see https://gdal.org/python/osgeo.gdal-module.html#WarpOptions
        Default options use 'cropToCutline' = True, 'targetAlignedPixels' = True
        and xRes and yRes from input raster.

    Returns
    -------
    gdal.Dataset
    """
    if type(in_raster) is str:
        in_raster = load_raster(in_raster, True)
    gt = in_raster.GetGeoTransform()
     
    
    options = {
        'xRes': gt[1],'yRes': gt[5],
        'targetAlignedPixels':True,
        'cutlineDSName': vector,
        'cropToCutline':True
    }
    options.update(warp_options)
    
    options = gdal.WarpOptions(**options)
    
    rv = gdal.Warp(out_raster, in_raster, options=options )
    if not rv is None:
        rv.FlushCache()
    return rv


def is_bad_data(dataset, bad_value = np.nan, band = 1):
    """Test if all pixels are bad data

    Parameters
    ----------
    dataset: Gdal.Dataset
        input data.
    bad_value: any, default np.nan
        type of bad_value must be compatible with dataset type
    band: int, default 1
        band of dataset to use for testing.  
    

    Returns
    -------
    bool:
        True if all pixels equal bad_value, else false.
    """
    pixels = dataset.GetRasterBand(band).ReadAsArray()
    if np.isnan(bad_value):
        if np.isnan(pixels).all():
            return True
    else:
        if (pixels == bad_value).all():
            return True
    
    return False


def orthorectify_rpc(input, output, dem, crs):
    """orthorectify raster with RPC information using a dem 

    Parameters
    ----------
    input: path or gdal.Dataset
        in raster
    output: path or gdal.Dataset
        out raster 
    dem: path
        dem raster (this has to be a file path)
    crs: string
        WKT crs 

    Returns
    -------
    gdal.Dataset
    """

    warp_options = gdal.WarpOptions(
        dstSRS = crs, 
        srcNodata = 0, 
        dstNodata=0, 
        rpc=True, 
        transformerOptions='RPC_DEM=%s' % dem
    )  
    return gdal.Warp(output, input, options= warp_options)