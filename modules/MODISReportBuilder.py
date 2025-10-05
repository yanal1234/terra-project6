import numpy as np
from typing import List, Optional

class MODISReportBuilder:
    def __init__(self, month: str):
        self.month = month
        self.lines: List[str] = []

    def add_summary(self, global_avg: float, max_temp: float, min_temp: float) -> None:
        self.lines.append(f"📅 Month: {self.month}")
        self.lines.append(f"🌡️ Global Average Temperature: {global_avg:.2f} °C")
        self.lines.append(f"🔥 Max Temperature: {max_temp:.2f} °C")
        self.lines.append(f"❄️ Min Temperature: {min_temp:.2f} °C")

    def add_valid_days_info(self, valid_days_array: np.ndarray) -> None:
        total_pixels = valid_days_array.size
        fully_covered = np.sum(valid_days_array >= 28)
        partially_covered = np.sum((valid_days_array > 0) & (valid_days_array < 28))
        missing = np.sum(valid_days_array == 0)
        self.lines.append(f"✅ Pixels with full coverage (≥28 days): {fully_covered}/{total_pixels}")
        self.lines.append(f"🟡 Partially covered pixels: {partially_covered}")
        self.lines.append(f"❌ Missing pixels: {missing}")

    def add_category_breakdown(self, category_array: np.ndarray) -> None:
        unique, counts = np.unique(category_array, return_counts=True)
        self.lines.append("📊 Temperature Categories:")
        for cat, count in zip(unique, counts):
            self.lines.append(f"  - {cat}: {count} pixels")

    def add_delta_summary(self, delta_array: np.ndarray) -> None:
        mean_delta = np.nanmean(delta_array)
        max_delta = np.nanmax(delta_array)
        min_delta = np.nanmin(delta_array)
        self.lines.append("📈 Monthly Temperature Change:")
        self.lines.append(f"  - Mean Δ: {mean_delta:.2f} °C")
        self.lines.append(f"  - Max Δ: {max_delta:.2f} °C")
        self.lines.append(f"  - Min Δ: {min_delta:.2f} °C")

    def add_note(self, note: str) -> None:
        self.lines.append(f"📝 Note: {note}")

    def build(self) -> str:
        return "\n".join(self.lines)