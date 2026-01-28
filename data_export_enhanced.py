# ENHANCED DATA EXPORT TAB WITH INDIVIDUAL PROPERTY CHECKBOXES

import streamlit as st
import pandas as pd
from core.excel_exporter import ExcelExporter

def show_data_export_tab():
    """Data Export tab with individual property selection"""
    
    st.header("Data Export")
    st.markdown("Export IFC data to Excel for editing.")
    
    # Check if file is uploaded
    if not st.session_state.ifc_file_path:
        st.warning("Please upload an IFC file in the File Analysis tab first.")
        return
    
    if not st.session_state.analysis_result:
        st.warning("Please analyze your IFC file first in the File Analysis tab.")
        return
    
    st.success(f"Working with file: {st.session_state.ifc_file_name}")
    st.info("See full implementation for export functionality")
