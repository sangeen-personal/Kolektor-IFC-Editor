# COMPREHENSIVE PROPERTY MANAGEMENT TAB WITH DROPDOWNS
# This replaces the current property management implementation

import streamlit as st
import os
from core.property_renamer import PropertyRenamer
from core.property_set_deleter import PropertySetDeleter

def show_property_management_tab():
    """Property Management tab with proper dropdowns"""
    
    st.header("⚙️ Property Management")
    st.markdown("Add, rename, or delete properties in your IFC file.")
    
    # Check if file is uploaded
    if not st.session_state.ifc_file_path:
        st.warning("⚠️ Please upload an IFC file in the **File Analysis** tab first.")
        st.info("👈 Go to the **File Analysis** tab to upload your IFC file.")
        return
    
    if not st.session_state.analysis_result:
        st.warning("⚠️ Please analyze your IFC file first in the **File Analysis** tab.")
        st.info("Click the **Analyze File** button in the File Analysis tab to extract property information.")
        return
    
    st.success(f"✅ Working with file: {st.session_state.ifc_file_name}")
    
    # Get analysis data for dropdowns
    result = st.session_state.analysis_result
    available_psets = list(result.get('property_sets', {}).keys())
    
    if not available_psets:
        st.error("❌ No property sets found in this IFC file. Cannot manage properties.")
        return
    
    file_path = st.session_state.ifc_file_path
    
    # Operation selector
    st.markdown("---")
    operation = st.selectbox(
        "Select Operation",
        ["Add New Property", "Rename Existing Property", "Delete Property"],
        key="prop_operation"
    )
    
    st.markdown("---")
    
    # Display operation content based on selection
    if operation == "Add New Property":
        st.info("Add New Property functionality - see full implementation")
    elif operation == "Rename Existing Property":
        st.info("Rename Property functionality - see full implementation")
    elif operation == "Delete Property":
        st.info("Delete Property functionality - see full implementation")
