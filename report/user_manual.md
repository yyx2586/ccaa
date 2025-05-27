# Chinese Commercial Advertisement Archive User Manual

## Getting Started with the Archive Interface

🚀 **Launch the Archive Here**:

🌐 [**Chinese Commercial Advertisement Archive**](https://ccaa-data-server.streamlit.app/)

🕰️ *Note*: The server may take a moment to wake up if it hasn’t been accessed recently. Don't worry—it’s just stretching and getting ready for you!

If the link doesn't load after a couple of minutes, feel free to contact the archive team:
📬 **[positionspress@gmail.com](mailto:positionspress@gmail.com)**

For a detailed technical overview, please refer to the [**Technical Report**](https://github.com/yyx2586/ccaa/blob/main/report/technical_report.md)

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

## 2.2 Dataset Filtering Options

To facilitate efficient exploration and scholarly analysis of the Chinese Commercial Advertisement Archive (CCAA), the user interface includes several dynamic filtering options. These filters enable users to narrow down search results by date, publisher, and product category. The default settings are optimized to display the most content-rich subset of the archive.

---

### 2.2.1 Date Range Filter

**Variable Name**: `dc_date_issued`
**Filter Type**: Dropdown (Start Year / End Year)
**Available Range**: 1901–1949
**Default Range Displayed**: 1907–1938

**Description**:
Users can select a specific date range to limit the dataset to advertisements published within the chosen years. This is particularly useful for studying temporal trends in commercial culture or tracking the development of specific industries over time.

* Both *Start Year* and *End Year* must be selected from dropdown lists.
* If no selection is made, the interface defaults to the most content-rich period: **1907 to 1938**.
* Dates correspond to the issue date of the newspaper in which the advertisement was printed.

---

### 2.2.2 Publisher Filter

**Variable Name**: `publisher`
**Filter Type**: Dropdown (single select)
**Available Values**:

**Ta Kung Pao (大公報)**
Founded in 1902 in Tianjin, *Ta Kung Pao* was a prominent Chinese-language newspaper known for its reformist and nationalist stance. It played a critical role in shaping public discourse in Republican China and was widely respected for its editorial independence.

**Press of Hankow Times (漢口中西報社)**
Operating in the treaty port of Hankow (now part of Wuhan), this bilingual press catered to both Chinese and Western readers. It served as a key platform for commercial advertising and cultural exchange in central China during the early 20th century.

**Press of Sheng-ching Shih-pao (盛京時報社)**
Based in Fengtian (modern-day Shenyang), *Sheng-ching Shih-pao* was a semi-official newspaper under Japanese influence in Manchuria. It reflected regional political dynamics and was instrumental in disseminating commercial and governmental information in Northeast China.

**Press of Yuet Wa Po (越華報社)**
*Yuet Wa Po* was a Chinese-language newspaper serving the Cantonese-speaking community in southern China and Southeast Asia. It documented local commerce and diaspora networks, making it an important source for studying transregional trade and advertising.

**Press of Shen Bao (申報)**
Established in 1872 in Shanghai, *Shen Bao* was one of the most influential and longest-running newspapers in modern Chinese history. It set the standard for commercial advertising and journalistic professionalism, providing a rich archive of urban culture and market activity.

**Description**:
Filters records based on the original newspaper in which the advertisement appeared. This option allows researchers to focus on regional or institutional editorial trends and provides a foundation for comparative press studies.

---

### 2.2.3 Product Category Filter

**Variable Name**: `dc_subject_product`
**Filter Type**: Multi-select Dropdown
**Description**:
This filter allows users to narrow results based on the type of product or service being advertised. Categories are based on a modified version of the United Nations Central Product Classification (CPC), adapted for historical accuracy and relevance. Users can select multiple categories to include a broader range of products in their query.

**Available Product Categories**:

| Category (EN)                                                             | Category (ZH) |
| ------------------------------------------------------------------------- | ------------- |
| Pharmaceutical products                                                   | 藥品            |
| Tobacco products                                                          | 煙草製品          |
| Soap, cleaning preparations, perfumes and toilet preparations             | 日化用品          |
| Food products n.e.c.                                                      | 食品            |
| Other dairy products                                                      | 乳製品           |
| Motor vehicles, trailers and semi-trailers; parts and accessories thereof | 機械車           |
| Glass and glass products                                                  | 玻璃製品          |
| Beverages                                                                 | 飲品            |
| Fertilizers and pesticides                                                | 化肥及殺蟲劑        |
| Radio and Television or Sound Equipment                                   | 音響設備          |
| Accumulators, primary cells and primary batteries                         | 蓄電池           |
| Furniture; Other manufactured articles n.e.c.                             | 傢俱及其它製成品      |
| Photographic equipment                                                    | 攝影器材          |
| Optical instruments and photographic equipment                            | 光學儀器          |
| Grain mill products                                                       | 穀物研磨品         |
| Daily Necessities                                                         | 日用品           |
| Insurance and pension services                                            | 保險和養老金服務      |
| Consumables                                                               | 耗材            |
| Engines and turbines and parts thereof                                    | 發動機及其配件       |
| Office and accounting machinery                                           | 辦公設備及其部件      |
| Radio, television and communication equipment                             | 廣播電視通訊設備及部件   |
| Domestic appliances                                                       | 家用設備          |
| Watches and clocks                                                        | 鐘錶及其部件        |
| Chemical products n.e.c.                                                  | 化工產品          |
| Rubber tyres and tubes                                                    | 橡膠輪胎及橡膠管      |
| Petroleum Products                                                        | 原油及提煉油        |
| Textile, apparel and leather production machinery                         | 布料皮革製品機器及其配件  |
| Cocoa, chocolate and sugar confectionery                                  | 糖果            |
| Textiles n.e.c.                                                           | 織物            |
| Musical instruments                                                       | 樂器            |
| Other transport equipment                                                 | 其它運輸工具及其配件    |
| Medical Devices                                                           | 醫療器械          |
| Other manufactured articles n.e.c.                                        | 其他工業製品        |
| Woven fabrics of natural fibres (excluding cotton)                        | 紡織品           |
| Sports goods                                                              | 體育用品          |
| Trademark                                                                 | 商標            |
| Construction                                                              | 建築工程          |
| Clothing                                                                  | 服飾            |
| Materials / Consumables                                                   | 原料 / 耗材       |

**Note**:

* Selecting multiple categories will display any advertisement that matches *at least one* of the selected product types.

## 2.3 Results Management

The Chinese Commercial Advertisement Archive (CCAA) platform supports robust results navigation through various user-configurable options. These tools assist researchers in customizing the display of advertisements according to temporal, linguistic, and browsing preferences.

---

### 2.3.1 Sorting Options

**Variable Name**: `sort_order`
**Filter Type**: Radio button (single select)
**Available Values**:

* **Ascending** – Displays advertisements in chronological order, starting with the earliest
* **Descending** – Displays advertisements in reverse chronological order, starting with the latest

**Default Behavior**:
The default sort order is **Ascending** to support historical analysis from earlier to later periods. This sorting logic is applied in conjunction with other active filters, such as year range or publisher.

**Use Case**:
This option is especially useful for longitudinal studies of commercial culture and temporal trend analysis in early 20th-century China.

---

### 2.3.2 Language Toggle

**Variable Name**: `language`
**Filter Type**: Radio button (single select)
**Available Values**:

* **English** – Displays metadata fields (e.g., title, preview text) in English
* **Chinese** – Displays metadata fields in Traditional Chinese

**Functionality**:
This toggle affects only the **Text Preview** field. All other fields (e.g., publisher, year, product classification) remain **bilingual**, preserving their original Chinese and transliterated English representations.

**Use Case**:
Facilitates cross-cultural research and supports both monolingual and bilingual users. It also allows for side-by-side linguistic comparison of advertisement content.

---

### 2.3.3 Pagination

**Pagination Limit**: 20 results per page
**Navigation Options**:

* Use the **increment (+/-)** buttons to move page-by-page
* Use the **numeric input box** to jump directly to a desired page

**Total Result Display**:
The total number of matching entries is shown at the top of the search results panel, providing users with a sense of dataset scope for their current query.

**Use Case**:
Supports efficient review of large datasets while maintaining load performance and readability. Researchers can sample early, middle, or late entries with minimal friction.

---

## 3. Viewing Advertisement Details

Search results in the CCAA platform are rendered in a structured table, optimized for browsing, inspection, and eventual deep access to source imagery. Each result provides essential metadata and an image preview to help guide scholarly inquiry.

---

### 3.1 Search Results Display

Each individual advertisement listing includes the following elements:

* **Thumbnail**
  A small preview image of the advertisement. Clicking the thumbnail opens the **high-resolution cropped image** in a new browser tab.

* **Publisher**
  The name of the newspaper press where the advertisement appeared. Displayed in English and Traditional Chinese for transparency and citation accuracy.

* **Year**
  The year of publication as derived from the newspaper issue date.

* **Issue #**
  A unique identifier corresponding to the specific issue of the newspaper in which the advertisement was printed.

* **Product**
  A classified category label indicating the advertised product’s industry (e.g., Pharmaceuticals, Tobacco, Domestic Appliances).

* **Text Preview**
  An expandable snippet of the advertisement content in either English or Chinese, depending on the interface language setting (see Section 2.3.2).

---

### 3.2 Image Viewing Options

Each advertisement in the archive is available in two visual formats to support both preliminary review and detailed content analysis.

---

#### 3.2.1 Cropped Advertisement (`image.jpg`)

* **Description**: A high-resolution image showing only the advertisement portion, cropped from the original newspaper page.
* **Use Case**: This is the primary visual object for research, suitable for close reading, annotation, or inclusion in scholarly outputs.
* **Access Method**: Click the thumbnail in the result table to open this image in a new tab.

---

#### 3.2.2 Thumbnail View (`image_thumbnail.jpg`)

* **Description**: A reduced-resolution version of the advertisement, optimized for fast rendering and bulk browsing.
* **Availability**: Present for most entries with full metadata; not all uncatalogued items include this format.
* **Use Case**: Useful for quick content skimming and comparative review across multiple records.

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


## 5. Data Statistics and Visualization Charts


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

## 6. Computational Visualization with TensorBoard Embedding Projector

The Chinese Commercial Advertisement Archive (CCAA) incorporates a TensorBoard Embedding Projector to support exploratory analysis of high-dimensional representations of historical advertisements. This interactive visualization tool enables researchers to navigate, cluster, and interpret image embeddings generated from the archive’s visual and textual features.

---

### 6.1 Overview of Embedding Projection

The embedding projector visualizes precomputed vectors derived from the archived advertisements using deep learning models. These vectors encode semantic and stylistic patterns captured from advertisement images, including layout, typography, and iconography, and optionally integrate textual metadata such as product categories or publication dates.

Researchers can explore this latent space to uncover:

* **Visual affinities across product types**
* **Temporal clusters indicating design evolution**
* **Cross-publication similarities in advertising style**
* **Outlier analysis highlighting unique or innovative advertisements**

---

### 6.2 Interactive Interface Features

The TensorBoard interface provides intuitive controls for manipulating and filtering the embedding space:

* **Label By**: Assigns label text to each data point. Common choices include `Publisher`, `Product`, or `Date`.
* **Color By**: Applies color mapping based on metadata (e.g., date range, category) to aid in visual clustering.
* **Edit By / Tag Selection**: Allows users to create custom tags or organize subsets of advertisements for further analysis.
* **Spherize Data**: Normalizes the vector distribution for optimal UMAP/PCA/T-SNE projection.

Learn more about the Dimension Reduction techniques: [UMAP](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html).

---

### 6.3 Dimensionality Reduction: UMAP Configuration

The default projection is computed using **UMAP (Uniform Manifold Approximation and Projection)** with configurable parameters:

* **Dimension**: Select between **2D** or **3D** space for visual rendering.
* **Neighbors**: Adjusts local neighborhood size; higher values reveal broader structure, lower values emphasize local clustering.
* **Sampling**: For performance, the interface automatically samples down to 5,000 points if the dataset is large.

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/spinning.gif" alt="UMAP Spinning Preview" width="600">
</p>

---

### 6.4 Metadata-Driven Filtering and Exploration

Users can navigate the embedding space using metadata controls:

* Filter by **Publisher**, **Product Category**, or **Publication Date**
* Explore bilingual metadata (English/Chinese) for cross-lingual comparison
* Hover or click on individual points to retrieve image thumbnails and corresponding metadata

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/navigation.gif" alt="Interactive Metadata Filtering" width="600">
</p>

---

### 6.5 Analytical Potential

This tool enhances the archive's utility for visual analytics and computational humanities by enabling:

* **Cluster detection** – Identify groupings of advertisements with similar design or theme.
* **Outlier analysis** – Spot unique formats or foreign-influenced advertising styles.
* **Temporal pattern discovery** – Reveal changes in visual form across decades.
* **Visual hypothesis generation** – Complement metadata-based queries with latent-space navigation.

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/move.gif" alt="Cluster Exploration" width="600">
</p>

How to use the UMAP visualization:
1. **UMAP Projection**: Click the "UMAP" button to generate a 2D or 3D projection of the advertisement embeddings.
2. **Select Number of Neighbors**: Adjust the number of neighbors to control local clustering granularity (in this example, we set 50 neighbors).
<p align="center">
  <img src="umap.gif" alt="Cluster Exploration" width="600">
</p>

---

### 6.6 Use Cases

This embedded tool supports a variety of scholarly workflows:

* **Media historians** tracing visual style shifts by decade or product class
* **Design researchers** identifying typographic or compositional conventions
* **Digital humanists** conducting exploratory clustering or similarity search
* **Educators** creating visual narratives from selected advertisement clusters

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

## 8. Copyright, Usage and Support

### 8.1 Copyright and Usage

- Historical materials for research/educational use
- No commercial reproduction without permission
- Attribute the archive in all publications
- Respect cultural sensitivities in historical materials

### 8.2. Bulk Download and Technical Support

The current archive does not support bulk downloading of images or metadata. Users must download individual images through the web interface. If you require bulk data access for research purposes, please contact the archive administrators. 

For further technical support or research inquiries along with bulk data requests, please reach out via email.
Email: positionspress@gmail.com
