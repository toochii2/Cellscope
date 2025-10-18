# CellScope 🔬

A powerful microscopy image analysis tool built with Streamlit for counting and analyzing objects in microscopy images.

## Features

- **Image Upload**: Support for PNG, JPG, JPEG, and TIFF formats
- **Noise Reduction**: Gaussian filtering with adjustable sigma parameter
- **Multiple Thresholding Methods**:
  - Isodata
  - Li
  - Mean
  - Minimum
  - Otsu
  - Triangle
  - Yen
  - Manual threshold control
- **Object Detection**: Automatic counting of objects in images
- **Morphological Analysis**: 
  - Area measurement
  - Eccentricity calculation
  - Statistical summaries
- **Visualization**: Color-coded labeled images for easy object identification

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/cellscope.git
cd cellscope
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application using Streamlit:
```bash
streamlit run app.py
```

The application will open in your default web browser. From there:

1. Upload a microscopy image using the file uploader
2. Adjust the Gaussian filter sigma value in the sidebar
3. Select a thresholding method to segment your image
4. View the detected objects count and their properties
5. Analyze statistical measurements (area, eccentricity)

## Requirements

- Python 3.7+
- streamlit
- numpy
- scikit-image
- matplotlib
- pandas

## How It Works

1. **Image Processing**: The uploaded image is converted to grayscale if needed
2. **Filtering**: A Gaussian filter reduces noise in the image
3. **Thresholding**: Various algorithms segment the image into foreground (objects) and background
4. **Object Detection**: Connected components are identified and labeled
5. **Quantification**: Morphological properties are measured for each detected object

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - Web application framework
- [scikit-image](https://scikit-image.org/) - Image processing library
- [NumPy](https://numpy.org/) - Numerical computing
- [Pandas](https://pandas.pydata.org/) - Data analysis

---

Made with ❤️ for microscopy image analysis
