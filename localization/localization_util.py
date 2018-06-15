import numpy as np
import math

# REMEMBER THIS IS IN METERS <3

RADIUS_OF_EARTH = 6371e3
DEGREES = 360
FLOOR_ELLPISOID_ALT = 0

def pixelToDistance(pixelVals, altitude):
    '''convert x, y pixel of image bounding box to distance of object relative
    to plane, returns tuple of obj_xy for use in to_global_system
    altitude needs to be in meters
    '''
    altitude = altitude - FLOOR_ELLPISOID_ALT
    width = 3840. #in pixels of image
    height = 2160.
    pixelX, pixelY = pixelVals #pixel x,y of object of interest
    angleHorizontal = np.deg2rad(23.7/2.) #angle of lens
    angleVertical = np.deg2rad(18./2.)
    centerX = width/2. #in pixels
    centerY = height/2.
    distMetersX = altitude * math.tan(angleHorizontal)
    distMetersY = altitude * math.tan(angleVertical)
    pixToMeterX = distMetersX/centerX #1 pixel = ? meters
    pixToMeterY = distMetersY/centerY
    distX = (pixelX - centerX) * pixToMeterX
    distY = (pixelY - centerY) * pixToMeterY
    return (distX, distY)

def to_global_system(plane_latlong, obj_xy, plane_orientation):
    '''Convert plane latlong, plane_orientation, and object_xy to latlong.

    This function assumes object_xy is a np.array of length 2 containing the
    distance (x,y) pair, in meters, of the object relative to the plane
    (in the frame of the plane's point of view).

    plane_orientation is relative to north

    NOTE: This function assumes the curvature is negligible!
    '''
    obj_latlong = to_latlong(obj_xy)
    world_rm = rot_mat(-to_rad(plane_orientation))

    return plane_latlong + world_rm.dot(obj_latlong)


def to_xy(latlong):
    ''' Converts latlong to xy.

    NOTE: This function assumes the curvature is negligible!
    '''
    return 2*np.pi*RADIUS_OF_EARTH*origin_latlong/DEGREES


def to_latlong(xy):
    ''' Converts latlong to xy.

    NOTE: This function assumes the curvature is negligible!
    '''
    return DEGREES*xy/(2*np.pi*RADIUS_OF_EARTH)


def to_rad(theta):
    return 2*np.pi*theta/DEGREES


def rot_mat(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

pixelToDistance((2, 5), 10)
