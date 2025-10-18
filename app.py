import streamlit as st
import numpy as np
from skimage import io, filters, measure, color
import matplotlib.pyplot as plt
import pandas as pd

def apply_threshold(image, method, manual_threshold=None):
    if method == 'Isodata':
        threshold_value = filters.threshold_isodata(image)
    elif method == 'Li':
        threshold_value = filters.threshold_li(image)
    elif method == 'Mean':
        threshold_value = filters.threshold_mean(image)
    elif method == 'Minimum':
        threshold_value = filters.threshold_minimum(image)
    elif method == 'Otsu':
        threshold_value = filters.threshold_otsu(image)
    elif method == 'Triangle':
        threshold_value = filters.threshold_triangle(image)
    elif method == 'Yen':
        threshold_value = filters.threshold_yen(image)
    elif method == 'Manual':
        threshold_value = manual_threshold
    else:
        threshold_value = manual_threshold
    thresholded_image = image > threshold_value
    return thresholded_image, threshold_value

def main():
    st.title("Counting Objects in Microscopy Images")
    st.markdown("""
    This workflow counts objects in a microscopy image using image processing techniques.
    * Open image
    * Use filters to suppress noise
    * Segment images using grey level thresholding
    * Count objects
    * Perform basic morphological quantification
    """)

    uploaded_file = st.file_uploader("Choose a microscopy image...", type=["png", "jpg", "jpeg", "tiff"])
    if uploaded_file is not None:
        try:
            image = io.imread(uploaded_file)
            if image.ndim == 3:
                image = color.rgb2gray(image)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            st.write("Image type:", type(image))

            # Filter parameters
            st.sidebar.header("Filter Parameters")
            sigma = st.sidebar.slider("Sigma (Gaussian filter)", 0.0, 10.0, 1.0)

            # Apply Gaussian filter
            filtered_image = filters.gaussian(image, sigma=sigma)
            st.image(filtered_image, caption="Filtered Image", use_container_width=True)

            # Thresholding Method Selection (Radio Buttons)
            st.sidebar.header("Thresholding Method")
            threshold_method = st.sidebar.radio(
                "Select Thresholding Method",
                ["Original", "Manual", "Isodata", "Li", "Mean", "Minimum", "Otsu", "Triangle", "Yen"],
                index=0  # Default to Original
            )

            manual_threshold = st.sidebar.slider("Manual Threshold Value (if applicable)", 0.0, 1.0, 0.5)

            # Thresholding and Visualization
            thresholded_image, threshold_value = apply_threshold(filtered_image, threshold_method, manual_threshold)

            st.image(thresholded_image, caption=f"Thresholded Image ({threshold_method} method)", use_container_width=True)
            if threshold_value is not None:
                st.write(f"Threshold Value ({threshold_method} method):", threshold_value)

            # Count objects
            labels = measure.label(thresholded_image)
            num_objects = labels.max()
            st.write("Number of objects detected:", num_objects)

            # Measure properties using regionprops_table
            props = measure.regionprops_table(labels, properties=['area', 'eccentricity'])
            props_df = pd.DataFrame(props)
            st.write("Properties of detected objects:")
            st.write(props_df.head(200))

            # Statistics for area and eccentricity
            st.write("Average area of objects:", np.mean(props_df['area']))
            st.write("Standard deviation of areas:", np.std(props_df['area']))

            st.write("Average eccentricity of objects:", np.mean(props_df['eccentricity']))
            st.write("Standard deviation of eccentricities:", np.std(props_df['eccentricity']))

            # Enhanced visualization with different colors for each label
            labeled_image = color.label2rgb(labels, image=image, bg_label=0)
            st.image(labeled_image, caption="Labeled Image", use_container_width=True)

        except Exception as e:
            st.error(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
