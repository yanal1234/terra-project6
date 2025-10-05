import streamlit as st
import numpy as np
from modules.MODISFileLoader import MODISFileLoader
from modules.MODISAnalyzer import MODISAnalyzer
from modules.TemperatureStats import TemperatureStats
from modules.ColorMapper import ColorMapper
from modules.DataExporter import DataExporter
from modules.MODISReportBuilder import MODISReportBuilder

st.set_page_config(page_title="MODIS Analyzer", layout="wide")
st.title("🌍 MODIS Temperature Analyzer")

# إدخال المسارات
folder_path = st.text_input("📁 MODIS folder path:", "C:/Users/omar/Downloads/MODIS")
output_folder = st.text_input("📤 Output folder:", "C:/Users/omar/Desktop/output")

# اختيار التدرج اللوني والدقة (اختياري للتوسع لاحقًا)
colormap_name = st.selectbox("🎨 Colormap:", ["coolwarm", "jet", "viridis", "plasma"], index=0)

if st.button("🔍 Analyze"):
    try:
        # تحميل الملفات
        loader = MODISFileLoader(folder_path)
        loader.load_files()
        loader.group_by_month()
        month_key = loader.detect_single_month()
        file_paths = loader.month_map.get(month_key, [])

        if not file_paths:
            st.error(f"No files found for {month_key}")
        else:
            st.success(f"✅ Detected month: {month_key}")
            st.info(f"🔢 Found {len(file_paths)} files for analysis")

            # تحليل البيانات مباشرة من الملفات باستخدام rasterio
            analyzer = MODISAnalyzer(file_paths)
            analyzer.extract_and_clean_data()

            if not analyzer.cleaned_arrays:
                st.error("❌ No valid MODIS files could be read.")
            else:
                analyzer.compute_statistics()

                # إحصائيات
                stats = TemperatureStats(analyzer.mean_array)
                stats.compute_basic_stats()
                stats.categorize_temperatures()

                # تحويل إلى ألوان
                mapper = ColorMapper(colormap_name)
                color_array = mapper.map_array_to_colors(analyzer.mean_array)

                # عرض الخريطة
                st.subheader("🌡️ Mean Temperature Map (15km resolution)")
                st.image(color_array, caption=f"Mean Temperature - {month_key}", use_column_width=True)

                # تصدير النتائج
                exporter = DataExporter(output_folder)
                exporter.export_image(color_array, f"temp_map_{month_key}")
                exporter.export_csv(analyzer.mean_array, f"mean_temp_{month_key}")

                # بناء التقرير
                report = MODISReportBuilder(month_key)
                report.add_summary(stats.global_avg, stats.max_temp, stats.min_temp)
                report.add_valid_days_info(analyzer.valid_days_array)
                report.add_category_breakdown(stats.category_array)
                report.add_note("Data downsampled to 15km resolution for memory optimization.")

                # عرض التقرير
                st.subheader("📄 Report")
                st.text(report.build())

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")