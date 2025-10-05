import os
import numpy as np
import matplotlib.pyplot as plt
import csv
from typing import Optional, List

class DataExporter:
    def __init__(self, output_folder: str):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def export_image(self, color_array: np.ndarray, filename: str, mode: str = "auto") -> None:
        path = os.path.join(self.output_folder, f"{filename}.png")
        if mode == "rgb":
            plt.imsave(path, color_array[:, :, :3])
        else:
            plt.imsave(path, color_array)

    def export_csv(self, array: np.ndarray, filename: str, headers: Optional[List[str]] = None, fmt: str = "%.2f") -> None:
        path = os.path.join(self.output_folder, f"{filename}.csv")
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)
            for row in array:
                formatted = [fmt % val if isinstance(val, float) else val for val in row]
                writer.writerow(formatted)

    def export_categories(self, category_array: np.ndarray, filename: str) -> None:
        path = os.path.join(self.output_folder, f"{filename}_categories.csv")
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            for row in category_array:
                writer.writerow(row)
                