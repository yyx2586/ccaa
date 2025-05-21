# 📰 Chinese Commercial Advertisement Archive (CCAA)

This interactive dashboard showcases digitized Chinese commercial advertisements published between 1901 and 1938. Built with **Streamlit** and **Plotly**, the application allows users to search, view, and analyze historical ephemera metadata and images stored in S3.

## 📦 Features

- 🔍 Full-text search of historical ads
- 🗓 Date-range filtering (1901–1938)
- 📸 Thumbnail and full image viewer (presigned S3 URLs)
- 📊 Data visualizations of:
  - Advertisement volume over time
  - Top brands and product categories
  - Geographic and publisher distributions
  - Heatmaps and sunburst charts
- 📁 Supports CSV-based metadata and S3-based images

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ccaa-dashboard.git
cd ccaa-dashboard
````

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run ccaa_data.py
```

## 🌐 Project Structure

```
.
├── ccaa_data.py            # Main Streamlit app
├── ccaa_final.csv          # Metadata file (ads from 1901–1938)
├── images/
│   └── index.png           # Logo image
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 📬 Contact

* Project: **Ephemera Project**
* Source: [Positions.Press](https://positionspress.org)
* Contact: [positionspress@gmail.com](mailto:positionspress@gmail.com)

## 🧾 License

Rights to this material belong to the Ephemera Project. This digital version is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.1 Unported

---
