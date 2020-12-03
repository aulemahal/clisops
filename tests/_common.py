import os
import tempfile
from pathlib import Path

from jinja2 import Template

ROOCS_CFG = str(Path(tempfile.gettempdir()).joinpath("roocs.ini").absolute())
TESTS_HOME = Path(__file__).absolute().parent
XCLIM_TESTS_DATA = TESTS_HOME.joinpath("xclim-testdata/testdata")
DEFAULT_CMIP5_ARCHIVE_BASE = TESTS_HOME.joinpath(
    "mini-esgf-data/test_data/badc/cmip5/data"
)
REAL_C3S_CMIP5_ARCHIVE_BASE = Path("/group_workspaces/jasmin2/cp4cds1/vol1/data/")
DEFAULT_CMIP6_ARCHIVE_BASE = TESTS_HOME.joinpath(
    "mini-esgf-data/test_data/badc/cmip6/data"
)


def write_roocs_cfg():
    cfg_templ = """
    [project:cmip5]
    base_dir = {{ base_dir }}/mini-esgf-data/test_data/badc/cmip5/data

    [project:cmip6]
    base_dir = {{ base_dir }}/mini-esgf-data/test_data/badc/cmip6/data

    [project:cordex]
    base_dir = {{ base_dir }}/mini-esgf-data/test_data/badc/cordex/data

    [project:c3s-cmip5]
    base_dir = {{ base_dir }}/mini-esgf-data/test_data/group_workspaces/jasmin2/cp4cds1/vol1/data

    [project:c3s-cmip6]
    base_dir = NOT DEFINED YET

    [project:c3s-cordex]
    base_dir = {{ base_dir }}/mini-esgf-data/test_data/group_workspaces/jasmin2/cp4cds1/vol1/data
    """
    cfg = Template(cfg_templ).render(base_dir=TESTS_HOME)
    with open(ROOCS_CFG, "w") as fp:
        fp.write(cfg)
    # point to roocs cfg in environment
    os.environ["ROOCS_CONFIG"] = ROOCS_CFG


def cmip5_archive_base():
    if "CMIP5_ARCHIVE_BASE" in os.environ:
        return Path(os.environ["CMIP5_ARCHIVE_BASE"])
    return DEFAULT_CMIP5_ARCHIVE_BASE


def cmip6_archive_base():
    if "CMIP6_ARCHIVE_BASE" in os.environ:
        return Path(os.environ["CMIP6_ARCHIVE_BASE"])
    return DEFAULT_CMIP6_ARCHIVE_BASE


CMIP5_ARCHIVE_BASE = cmip5_archive_base()

CMIP5_ZOSTOGA = CMIP5_ARCHIVE_BASE.joinpath(
    "cmip5/output1/INM/inmcm4/rcp45/mon/ocean/Omon/r1i1p1/latest/zostoga/*.nc",
)

CMIP5_TAS = CMIP5_ARCHIVE_BASE.joinpath(
    "cmip5/output1/MOHC/HadGEM2-ES/rcp85/mon/atmos/Amon/r1i1p1/latest/tas/*.nc",
)

CMIP5_RH = CMIP5_ARCHIVE_BASE.joinpath(
    "cmip5/output1/MOHC/HadGEM2-ES/historical/mon/land/Lmon/r1i1p1/latest/rh/*.nc",
)

CMIP5_TAS_FILE = CMIP5_ARCHIVE_BASE.joinpath(
    "cmip5/output1/MOHC/HadGEM2-ES/rcp85/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp85_r1i1p1_200512-203011.nc",  # noqa
)

CMIP6_ARCHIVE_BASE = cmip6_archive_base()

CMIP6_O3 = XCLIM_TESTS_DATA.joinpath(
    "cmip6",
    "o3_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc",
)

C3S_CMIP5_TSICE = REAL_C3S_CMIP5_ARCHIVE_BASE.joinpath(
    "c3s-cmip5/output1/NCC/NorESM1-ME/rcp60/mon/seaIce/OImon/r1i1p1/tsice/v20120614/*.nc",
)


C3S_CMIP5_TOS = REAL_C3S_CMIP5_ARCHIVE_BASE.joinpath(
    "c3s-cmip5/output1/BCC/bcc-csm1-1-m/historical/mon/ocean/Omon/r1i1p1/tos/v20120709/*.nc",
)
