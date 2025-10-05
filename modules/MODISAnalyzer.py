import rasterio
import numpy as np
from typing import List, Optional

class MODISAnalyzer:
    def __init__(self, file_paths: List[str]):
        self.file_paths = file_paths
        self.cleaned_arrays: List[np.ndarray] = []
        self.mean_array: Optional[np.ndarray] = None
        self.std_array: Optional[np.ndarray] = None
        self.valid_days_array: Optional[np.ndarray] = None

    def extract_and_clean_data(self) -> None:
        self.cleaned_arrays = []
        for path in self.file_paths:
            try:
                with rasterio.open(path) as ds:
                    sub = ds.subdatasets[0]
                    with rasterio.open(sub) as src:
                        arr = src.read(1).astype(float)
                        nodata = src.nodata
                        arr[arr == nodata] = np.nan
                        arr[arr < 7500] = np.nan
                        arr[arr > 65535] = np.nan
                        arr *= 0.02  # تحويل لوحدة Celsius
                        self.cleaned_arrays.append(arr)
            except Exception as e:
                print(f"⚠️ Skipping file due to error: {path}\n{e}")

    def compute_statistics(self) -> None:
        if not self.cleaned_arrays:
            raise ValueError("No valid data arrays to compute statistics.")
        stacked = np.stack(self.cleaned_arrays)
        self.mean_array = np.nanmean(stacked, axis=0)
        self.std_array = np.nanstd(stacked, axis=0)
        self.valid_days_array = np.sum(~np.isnan(stacked), axis=0)