# Chinese Commercial Advertisement Archive User Manual

## Getting Started with the Archive Interface

🚀 **Launch the Archive Here**:

🌐 [**Chinese Commercial Advertisement Archive**](https://ccaa-data-server.streamlit.app/)

🕰️ *Note*: The server may take a moment to wake up if it hasn’t been accessed recently. Don't worry—it’s just stretching and getting ready for you!

If the link doesn't load after a couple of minutes, feel free to contact the archive team:
📬 **[positionspress@gmail.com](mailto:positionspress@gmail.com)**

For a detailed technical overview, please refer to the [**Technical Report**](

)

## 1. Introduction to the Archive Access

### 1.1 Accessing the Archive

The Chinese Commercial Advertisement Archive (CCAA) is accessible through a web-based interface. The archive contains 108,244 historical advertisement images from Chinese newspapers (1901-1938), with 44,700 fully cataloged entries.

<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/user_interface.png" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

### 1.2 Interface Overview

The archive interface consists of several key components:
- Search bar for keyword queries
- Filter options for refining results
- Results display area with thumbnail previews
- Individual advertisement viewing upon clicking thumbnails to be redirected to a detailed view


## 2. Search and Navigation

### 2.1 Basic Search
<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/search.gif" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

Enter on full text indices on all text field in the main search bar to search across all indexed advertisement content. The search function queries:
- Advertisement content
- Product descriptions
- Company names
- Brand names

### 2.2 Advanced Filtering Options

<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/filter.gif" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

#### 2.2.1 Date Range Selection
- **Start Year**: Select from dropdown menu (1901-1949)
- **End Year**: Select from dropdown menu (1901-1949)
- Default setting displays all available years

#### 2.2.2 Publisher Selection
Available publishers include:
- Ta Kung Pao [大公報]
- Press of Hankow Times [漢口中西報社]
- Press of Sheng-ching Shih-pao [盛京時報社]
- Press of Yuet Wa Po [越華報社]
- Press of Shen Bao [申報]


#### 2.2.3 Subject Categories
Select from predefined product categories to narrow results by advertisement type.

### 2.3 Results Management

#### 2.3.1 Sorting Options
- **Ascending**: Oldest advertisements first
- **Descending**: Newest advertisements first

#### 2.3.2 Language Toggle
- **English**: Interface and metadata in English
- **Chinese**: Interface and metadata in Chinese

#### 2.3.3 Pagination
- Results display 20 items per page
- Navigate using page numbers at bottom
- Total result count shown above listings

## 3. Viewing Advertisement Details

### 3.1 Search Results Display

Each result shows:
- **Thumbnail**: Small preview image
- **Publisher**: Newspaper source
- **Year**: Publication year
- **Issue #**: Specific issue number
- **Product**: Product category classification
- **Text Preview**: Expandable content preview

### 3.2 Image Viewing Options

Three image types are available for each advertisement:

#### 3.2.1 Cropped Advertisement by clicking on the thumbnail (image.jpg)
- High-resolution image of individual advertisement
- Suitable for detailed content analysis
- Primary research object

#### 3.2.2 Thumbnail View (image_thumbnail.jpg)
- Reduced resolution for quick browsing
- Available for subset of captioned materials
- Useful for initial assessment


## 4. Understanding the Data

### 4.1 Archive Composition

The CCAA contains three collection levels. The primary collection consists of fully captioned advertisements, while the secondary collection contains cropped images without (this is not currently searchable) metadata. The tertiary collection includes early period advertisements from the Shen Bao newspaper. The tertiary collection is auto-captioned with Claude 3.5 Sonnet V2 model, but not fully cataloged.

| Collection Type | Image Count | Description |
|----------------|-------------|-------------|
| Primary (Captioned) | 44,700 | Fully cataloged with metadata |
| Secondary (Uncaptioned) | 63,544 | Cropped images without metadata |
| Tertiary (Shen Bao) | 2,924 | Early period (1901-1907) supplement |

### 4.2 Publisher Distribution

Captioned advertisements by publisher:

| Publisher | Count | Percentage |
|-----------|-------|------------|
| Press of Hankow Times | 15,221 | 37.0% |
| Press of Sheng-ching Shih-pao | 13,488 | 32.8% |
| Ta Kung Pao | 6,263 | 15.2% |
| Press of Yuet Wa Po | 3,488 | 8.5% |
| Press of Shen Bao | 2,914 | 7.1% |


## 5. Data Visualizations Guide


### 5.1 Publisher Advertisement Volume and Company Nations

<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/publisher_and_country.png" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

The combined visualization demonstrates:

**Publisher Advertisement Volumes**:
- **Press of Hankow Times**: ~15,000 advertisements (highest volume)
- **Press of Sheng-ching Shih-pao**: ~13,500 advertisements 
- **Ta Kung Pao**: ~6,500 advertisements
- **Press of Yuet Wa Po**: ~3,500 advertisements
- **Press of Shen Bao**: ~3,000 advertisements

**Company Nation Distribution**:
- **Japan**: 43.1% - Dominant foreign advertiser reflecting strong economic presence
- **Canada**: 19.7% - Significant pharmaceutical sector representation
- **U.S.A**: 16.2% - Diverse product portfolio including tobacco and consumer goods
- **U.K**: 14.3% - Traditional colonial commercial presence
- **Germany**: 3.5% - Specialized pharmaceutical and chemical products
- **Other nations**: <1% each (Switzerland, France, Netherlands, Singapore, India, Russia, Italy)

### 5.2 Brand and Category Distribution

<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/brand_and_category.png" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

Distribution analyses reveal:
- **Top Product Categories**: Pharmaceuticals (>50%), Tobacco (~15%), Food (~10%)
- **Leading Companies**: Dr. Williams Medicine Company (34.6% of pharmaceutical ads)
- **Geographic Concentration**: Treaty ports dominate advertising activity

Key insights:
- Pharmaceutical products dominate the archive
- Jintan (仁丹) is the most frequently advertised brand (13.3%)
- Top 10 brands account for ~60% of advertisements


### 5.3 Top Brands and Company Analysis

<p align="center"> <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/brand_and_company.png" alt="TensorBoard Embedding Projector Demo" width="800"> </p>

The dual pie chart visualization reveals market concentration patterns:

**Top Brand Distribution**:
- **仁丹 (Jintan)**: 13.3% - Japanese pharmaceutical product dominating the market
- **嬰孩自己藥片 (Baby's Own)**: 7.93% - Canadian infant medicine brand
- **如意膏 (She-Ko)**: 7.84% - Popular ointment product
- **味之素 (Ajinomoto)**: 7.6% - Japanese food seasoning company
- **紅錫包香煙 (Ruby Queen)**: 6.51% - Cigarette brand
- **韋廉士吸入止咳片**: 5.62% - Williams' cough remedy products
- **中將湯 (Chujoto)**: 5.06% - Traditional medicine formula
- **韋廉士醫生紅色清導丸 (Pinkettes)**: 5.02% - Williams' laxative product
- **Other brands**: Including various Williams' products and Three Castles Cigarettes

**Top Company Distribution**:
- **韋廉士醫生藥局 (Dr. Williams Medicine Company)**: 34.6% - Overwhelming market leader
- **森下博大藥房 (Morishita &Co.)**: 9.47% - Major Japanese pharmaceutical company
- **惠爾斯公司 (W.D. & H.O. Wills)**: 7.73% - British tobacco company
- **第威德制藥公司 (E.G. DeWitt & CO.)**: 6.4% - American pharmaceutical firm
- **佛安氏西藥公司 (Foster-MacLellan Co.)**: 5.68% - Western medicine distributor
- **S.Suzuki & Co.**: 5.61% - Japanese trading company
- **英美煙公司 (British American Tobacco)**: 5.22% - Major tobacco conglomerate
- **Other companies**: Including various pharmaceutical and trading firms

## 7. Technical Guidelines

### 7.1 Data Access Methods

Current access options:
- Individual image downloading via web interface
- Manual metadata compilation from search results
- No bulk download functionality available on the website, but can be requested for research purposes

### 7.2 Citation Format

Recommended citation:
```
[Advertisement Title]. (Year). In Chinese Commercial Advertisement Archive, 
[Newspaper Name], [Date], [Page Number]. Ephemera Project, Positions.Press. 
Retrieved [Access Date] from [URL]
```

## 8. Research Best Practices

### 8.1 Systematic Documentation

- Record all search parameters used
- Document date ranges and filters applied
- Note total results for each query
- Save URLs for specific advertisements


### 8.2 Copyright and Usage

- Historical materials for research/educational use
- No commercial reproduction without permission
- Attribute the archive in all publications
- Respect cultural sensitivities in historical materials

## 9. Bulk Download and Technical Support

The current archive does not support bulk downloading of images or metadata. Users must download individual images through the web interface. If you require bulk data access for research purposes, please contact the archive administrators. 
For further technical support or research inquiries along with bulk data requests, please reach out via email.
Email: positionspress@gmail.com
