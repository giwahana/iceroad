# Gain lookup  look up for radiometric calibration
# source: https://dg-cms-uploads-production.s3.amazonaws.com/uploads/document/file/209/ABSRADCAL_FLEET_2016v0_Rel20170606.pdf
values = {
    'worldview-3': {
        'pan':      0.950,
        'coastal':   0.905,
        'blue':     0.940,
        'green':    0.938,
        'yellow':   0.962,
        'red':      0.964,
        'rededge':  1.000,
        'nir1':     0.961,
        'nir2':     0.978,
        'swir1':    1.200,
        'swir2':    1.227,
        'swir3':    1.199,
        'swir4':    1.196,
        'swir5':    1.262,
        'swir6':    1.314,
        'swir7':    1.346,
        'swir8':    1.376,
    },
    'worldview-2': {
        'pan':      0.942,
        'coastal':   1.151,
        'blue':     0.988,
        'green':    0.936,
        'yellow':   0.949,
        'red':      0.952,
        'rededge':  0.974,
        'nir1':     0.961,
        'nir2':     1.002,
    },
    'geoeye-1': {
        'pan':      0.970, 
        'blue':     1.053, 
        'green':    0.994, 
        'red':      0.998, 
        'nir1':     0.994,
    },
    'quickbird': {
        'pan':      0.870, 
        'blue':     1.105, 
        'green':    1.071, 
        'red':      1.060, 
        'nir1':     1.020,
    },
    'worldview-1': {
        'pan':      1.016,
    }, 
    'ikonos': {
        'pan':      0.907, 
        'blue':     1.073, 
        'green':    0.990, 
        'red':      0.940, 
        'nir1':     1.043,
    },
}
