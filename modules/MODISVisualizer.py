import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple

class MODISVisualizer:
    def __init__(self, figsize: Tuple[int, int] = (8, 6)):
        self.figsize = figsize

    def show_temperature_map(
        self,
        array: np.ndarray,
        title: str = "Temperature Map",
        cmap: str = "coolwarm",
        show_axis: bool = False,
        save_path: Optional[str] = None
    ) -> None:
        plt.figure(figsize=self.figsize)
        im = plt.imshow(array, cmap=cmap)
        plt.colorbar(im, label="°C")
        plt.title(title)
        if not show_axis:
            plt.axis("off")
        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
        plt.show()

    def show_difference_map(
        self,
        delta_array: np.ndarray,
        title: str = "Monthly Temperature Difference",
        cmap: str = "bwr",
        vmin: float = -5,
        vmax: float = 5,
        show_axis: bool = False,
        save_path: Optional[str] = None
    ) -> None:
        plt.figure(figsize=self.figsize)
        im = plt.imshow(delta_array, cmap=cmap, vmin=vmin, vmax=vmax)
        plt.colorbar(im, label="Δ°C")
        plt.title(title)
        if not show_axis:
            plt.axis("off")
        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
        plt.show()

    def show_category_map(
        self,
        category_array: np.ndarray,
        title: str = "Temperature Categories",
        category_colors: Optional[dict] = None,
        show_axis: bool = False,
        save_path: Optional[str] = None
    ) -> None:
        if category_colors is None:
            category_colors = {
                "Cold": "#1f77b4",
                "Mild": "#ff7f0e",
                "Hot": "#d62728",
                "Unknown": "#cccccc"
            }

        # تحويل التصنيفات إلى ألوان
        color_array = np.empty(category_array.shape + (3,), dtype=np.uint8)
        for label, hex_color in category_colors.items():
            mask = category_array == label
            rgb = tuple(int(hex_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
            color_array[mask] = rgb

        plt.figure(figsize=self.figsize)
        plt.imshow(color_array)
        plt.title(title)
        if not show_axis:
            plt.axis("off")
        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
        plt.show()