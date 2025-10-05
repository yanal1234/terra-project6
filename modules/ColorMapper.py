import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple

class ColorMapper:
    def __init__(self, colormap_name: str = "coolwarm", nan_color: Tuple[float, float, float, float] = (0, 0, 0, 0)):
        self.colormap_name = colormap_name
        self.colormap = plt.get_cmap(colormap_name)
        self.nan_color = nan_color  # لون القيم المفقودة

    def map_array_to_colors(
        self,
        array: np.ndarray,
        vmin: Optional[float] = None,
        vmax: Optional[float] = None,
        output_mode: str = "rgba"  # خيارات: "rgba", "rgb", "gray"
    ) -> np.ndarray:
        # تحديد نطاق التلوين
        vmin = vmin if vmin is not None else np.nanmin(array)
        vmax = vmax if vmax is not None else np.nanmax(array)
        norm = plt.Normalize(vmin=vmin, vmax=vmax)

        # تطبيق التدرج اللوني
        mapped = self.colormap(norm(array))

        # التعامل مع القيم المفقودة
        mapped[np.isnan(array)] = self.nan_color

        # اختيار نوع الإخراج
        if output_mode == "rgb":
            return mapped[:, :, :3]
        elif output_mode == "gray":
            gray = norm(array)
            gray[np.isnan(array)] = 0
            return np.stack([gray] * 3, axis=-1)
        else:
            return mapped  # RGBA