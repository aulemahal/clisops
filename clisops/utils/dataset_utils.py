from roocs_utils.xarray_utils.xarray_utils import get_coord_by_type


def calculate_offset(lon):
    """
    Calculate the number of elements to roll the dataset by in order to have
    longitude from -180 to 180 degrees.
    """
    # get resolution of data
    res = lon.values[1] - lon.values[0]  # this doesn't work for test data

    # calculate how many elements to move by to have lon from -180 to 180
    # might need to change this?? - we might need to roll it to something other than -180 to 180
    diff = -180 - lon.values[0]

    # work out how many spaces to roll by to roll data by 1 degree
    index = 1 / res

    # calculate the corresponding offset needed to change data by diff
    offset = int(diff * index)

    return diff, offset


def check_lon_alignment(ds, lon_bnds):
    """
    Check whether the longitude subset requested is within the bounds of the dataset. If not try to roll the dataset so
    that the request is. Raise an exception if rolling is not possible.
    """
    low, high = lon_bnds
    lon = get_coord_by_type(ds, "longitude", ignore_aux_coords=False)
    lon = ds.coords[lon.name]
    lon_min, lon_max = lon.values.min(), lon.values.max()

    # check if the request is in bounds - return ds if it is
    if lon_min <= low and lon_max >= high:
        return ds

    else:
        # check if lon is a dimension
        if lon.name not in ds.dims:
            raise Exception(
                f"The longitude of this dataset runs from {lon_min:.2f} to {lon_max:.2f}, "
                f"and rolling could not be completed successfully. "
                f"Please re-run your request with longitudes between these bounds."
            )
        # roll the dataset and reassign the longitude values
        else:
            diff, offset = calculate_offset(lon)
            ds_roll = ds.roll(shifts={f"{lon.name}": offset}, roll_coords=False)
            ds_roll.coords[lon.name] = ds_roll.coords[lon.name] + diff
            return ds_roll
