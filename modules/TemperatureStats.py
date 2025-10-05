import numpy as np
from typing import Optional, Tuple

class TemperatureStats:
    def __init__(self, mean_array: np.ndarray, previous_mean_array: Optional[np.ndarray] = None):
        self.mean_array = mean_array
        self.previous_mean_array = previous_mean_array

        self.max_temp: Optional[float] = None
        self.min_temp: Optional[float] = None
        self.global_avg: Optional[float] = None

        self.delta_array: Optional[np.ndarray] = None
        self.delta_category_array: Optional[np.ndarray] = None

        self.category_array: Optional[np.ndarray] = None

    def compute_basic_stats(self) -> None:
        self.max_temp = np.nanmax(self.mean_array)
        self.min_temp = np.nanmin(self.mean_array)
        self.global_avg = np.nanmean(self.mean_array)

    def compute_delta(self) -> None:
        if self.previous_mean_array is not None:
            self.delta_array = self.mean_array - self.previous_mean_array
            self._categorize_delta()

    def categorize_temperatures(self, thresholds: Tuple[float, float] = (10.0, 25.0)) -> None:
        low, high = thresholds
        categories = np.full(self.mean_array.shape, "Unknown", dtype=object)
        categories[self.mean_array < low] = "Cold"
        categories[(self.mean_array >= low) & (self.mean_array <= high)] = "Mild"
        categories[self.mean_array > high] = "Hot"
        self.category_array = categories

    def _categorize_delta(self, tolerance: float = 0.5) -> None:
        """تصنيف التغيرات الحرارية بين الشهرين"""
        categories = np.full(self.delta_array.shape, "Stable", dtype=object)
        categories[self.delta_array > tolerance] = "Warmer"
        categories[self.delta_array < -tolerance] = "Cooler"
        self.delta_category_array = categories