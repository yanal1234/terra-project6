import os
import glob
from typing import List, Dict
from datetime import datetime

class MODISFileLoader:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.files: List[str] = []
        self.month_map: Dict[str, List[str]] = {}

    def load_files(self) -> None:
        # دعم أنواع متعددة من الملفات
        self.files = sorted(
            glob.glob(os.path.join(self.folder_path, "*.hdf")) +
            glob.glob(os.path.join(self.folder_path, "*.h5")) +
            glob.glob(os.path.join(self.folder_path, "*.tif"))
        )

    def group_by_month(self) -> None:
        self.month_map.clear()
        for file in self.files:
            filename = os.path.basename(file)
            if "A" in filename:
                try:
                    date_code = filename.split(".")[1]
                    year = date_code[1:5]
                    day_of_year = int(date_code[5:])
                    month = self._day_to_month(year, day_of_year)
                    key = f"{year}-{month:02d}"
                    self.month_map.setdefault(key, []).append(file)
                except Exception as e:
                    print(f"⚠️ Skipping file due to date parsing error: {filename}\n{e}")

        # تحذير لو فيه شهور فيها عدد قليل من الملفات
        for key, group in self.month_map.items():
            if len(group) < 5:
                print(f"⚠️ Warning: Only {len(group)} files found for {key}")

    def get_available_months(self) -> List[str]:
        return sorted(self.month_map.keys())

    def detect_single_month(self) -> str:
        months = set()
        for file in self.files:
            filename = os.path.basename(file)
            if "A" in filename:
                try:
                    date_code = filename.split(".")[1]
                    year = date_code[1:5]
                    day_of_year = int(date_code[5:])
                    month = self._day_to_month(year, day_of_year)
                    months.add(f"{year}-{month:02d}")
                except:
                    continue
        if len(months) == 1:
            return months.pop()
        elif len(months) == 0:
            raise ValueError("No valid MODIS files found.")
        else:
            raise ValueError(f"Multiple months detected: {months}")

    @staticmethod
    def _day_to_month(year: str, day_of_year: int) -> int:
        date = datetime.strptime(f"{year}{day_of_year:03d}", "%Y%j")
        return date.month