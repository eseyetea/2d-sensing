import qcodes

from qcodes.dataset import (
    LinSweep,
    Measurement,
    dond,
    experiments,
    initialise_or_create_database_at,
    load_by_run_spec,
    load_or_create_experiment,
    plot_dataset,
)

import matplotlib.pyplot as plt
from matplotlib import cm, colors

import numpy as np
import pandas as df
import time

from scipy.optimize import curve_fit
import pathlib

def load_band_2d(ds, name):
    """Return (gate [n], freq [m], s21 [n, m]) for one band."""
    d = ds.get_parameter_data(f"{name}_real", f"{name}_imag")
    re_block, im_block = d[f"{name}_real"], d[f"{name}_imag"]

    gate = re_block["gate"][:, 0]              # setpoint name; see note below
    freq = re_block[f"{name}_freq"][0, :]      # identical for every row
    s21 = re_block[f"{name}_real"] + 1j * im_block[f"{name}_imag"]
    return gate, freq, s21