# Digital Platform of the Chinese Commercial Advertisement Archive (CCAA): 
## A Comprehensive Detailed Technical User Manual on Data Acquisition, Preprocessing, and Infrastructure

## Abstract

This report presents a comprehensive analysis of the data processing pipeline developed for the Chinese Commercial Advertisement Archive (CCAA), a substantial digital humanities collection containing historical Chinese newspaper advertisements from the early twentieth century. The archive encompasses 108,244 images totaling approximately 198.28 GB of data across five major newspaper publishers: Ta Kung Pao (大公報), Hankow Times (漢口中西報社), Sheng-ching Shih-pao (盛京時報社), Yuet Wa Po (越華報社), and Shen Bao (申報). Of these, 44,700 images contain comprehensive metadata and captions, while 66,468 remain uncaptioned but cropped for analysis. This study documents the technical challenges encountered in data acquisition, preprocessing methodologies employed, and infrastructure considerations necessary for large-scale historical image processing projects. The findings contribute to best practices in digital humanities data management and provide methodological insights into the complexities of processing multilingual historical advertisement collections for scholarly research.

## 1. Introduction

### 1.1 Background and Historical Significance

The Chinese Commercial Advertisement Archive (CCAA) represents a significant digital humanities resource documenting the commercial landscape of early twentieth-century China through newspaper advertisements. This collection provides unprecedented access to the material culture, consumer practices, and economic transformations that characterized China's engagement with global markets during a period of profound social and political change.

The archive encompasses five prominent Chinese newspapers spanning the period from 1901 to 1938:
- **Ta Kung Pao (大公報)**: Premier national newspaper with broad circulation across multiple Chinese cities
- **Hankow Times (漢口中西報社)**: Bilingual publication serving the foreign concession community in Hankou
- **Sheng-ching Shih-pao (盛京時報社)**: Regional newspaper documenting commercial activities in Northeast China
- **Yuet Wa Po (越華報社)**: Publication serving overseas Chinese communities and international trade networks
- **Shen Bao (申報)**: Shanghai-based newspaper representing the commercial heart of modern China's economic transformation

### 1.2 Dataset Composition and Quantitative Overview

The CCAA dataset presents a complex multi-tiered structure comprising 108,244 total images organized across three distinct collection levels:

**Primary Collection (Captioned Data): 44,700 images**
- Comprehensively cataloged advertisement images with complete bilingual metadata
- Full-text transcriptions in both Traditional and Simplified Chinese
- English translations of titles and descriptions for international research accessibility
- Complete bibliographic information including publisher attribution, precise dating, and geographic location data
- Systematic product categorization and brand identification

**Secondary Collection (Uncaptioned Data): 63,544 images**
- Systematically cropped advertisement images lacking comprehensive metadata
- Predominantly sourced from Ta Kung Pao archives
- Represents significant untapped potential for future OCR and content analysis projects

**Tertiary Collection (Shen Bao Supplement): 2,924 images**
- Specialized collection covering Shen Bao advertisements from 1901-1907
- Documents critical early period of modern Chinese commercial advertising
- Cropped but requires future captioning for full research utility

**Captioned Advertisement Distribution by Publisher:**

| Publisher | Publisher Name | Advertisement Count | Percentage of Total |
|-----------|----------------|-------------------|-------------------|
| Press of Hankow Times | 漢口中西報社 | 15,221 | 37.0% |
| Press of Sheng-ching Shih-pao | 盛京時報社 | 13,488 | 32.8% |
| Ta Kung Pao | 大公報 | 6,263 | 15.2% |
| Press of Yuet Wa Po | 越華報社 | 3,488 | 8.5% |
| Press of Shen Bao | 申報 | 2,914 | 7.1% |
| **Total** | | **41,374** | **100.0%** |

**Total Storage (Un-captioned Included) Distribution by Publisher:**

| Publisher Abbreviation | Publisher Name | Data Volume | Percentage of Total |
|----------------------|----------------|-------------|-------------------|
| dgb | Ta Kung Pao (大公報) | 106.97 GB | 53.9% |
| sjsb | Sheng-ching Shih-pao (盛京時報社) | 40.36 GB | 20.4% |
| hkts | Hankow Times (漢口中西報社) | 28.21 GB | 14.2% |
| yhb | Yuet Wa Po (越華報社) | 18.16 GB | 9.2% |
| sjxb | Shen Bao (申報) | 4.58 GB | 2.3% |

**File Structure Architecture:**
Each complete advertisement entry consists of three distinct image components designed to support multiple research methodologies:
- `image.jpg`: High-resolution cropped advertisement image serving as the primary analytical object for content analysis, visual studies, and material culture research
- `image_thumbnail.jpg`: Optimized preview image (available for subset of captioned materials) enabling rapid browsing and preliminary assessment
- `image_page.jpg`: Complete newspaper page providing essential contextual information including surrounding advertisements, editorial content, and page layout for understanding advertisement placement strategies

### 1.3 Research Significance and Scholarly Applications

This archive addresses several critical gaps in the historiography of modern Chinese commercial culture and provides unprecedented primary source access for multiple scholarly disciplines:

**Economic History Applications:**
- Quantitative analysis of foreign product penetration in Chinese markets across different geographical regions and time periods
- Documentation of price trends, product availability, and market expansion patterns during China's integration into global commercial networks
- Evidence of changing consumer preferences and purchasing power across different social strata

**Cultural and Social History Research:**
- Evolution of visual advertising techniques and their adaptation to Chinese cultural contexts
- Analysis of gender representation, family structures, and social aspirations as reflected in commercial messaging
- Documentation of lifestyle changes and material culture transformation in urban Chinese society

**Business and Marketing History Studies:**
- Corporate strategies of foreign companies entering Chinese markets, including localization of products and marketing messages
- Development of modern advertising agencies and professional marketing practices in early twentieth-century China
- Analysis of brand development, trademark registration, and intellectual property practices

**Digital Humanities Methodologies:**
- Large-scale image analysis using computer vision and machine learning techniques for pattern recognition in visual advertising elements
- Natural language processing applications for systematic content analysis of multilingual advertisement texts
- Network analysis of commercial relationships between foreign corporations and Chinese distributors or agents

### 1.4 Technical and Methodological Challenges

The project confronts several significant challenges that impact both technical implementation and research accessibility, requiring innovative solutions for digital humanities infrastructure:

**Data Access and Infrastructure Limitations:**
- Remote storage on Aliyun Object Storage Service (OSS) with significant latency issues for international researchers, necessitating migration to globally accessible AWS S3 infrastructure
- Absence of dedicated database management system optimized for large-scale image serving and metadata queries
- Requirements for implementing efficient data retrieval mechanisms supporting both programmatic access and web-based research interfaces

**Linguistic and Metadata Complexity:**
- Systematic inconsistencies between Traditional and Simplified Chinese character representations requiring comprehensive standardization protocols
- Complex multilingual metadata structure demanding detailed field-by-field analysis and normalization procedures
- Absence of standardized English translations limiting research accessibility for international scholars specializing in Chinese history but lacking advanced Chinese language proficiency

**Data Quality and Completeness Issues:**
- Substantial portion of total dataset (61.4%) lacks comprehensive captioning, representing significant opportunity for future optical character recognition (OCR) and manual cataloging initiatives
- Presence of redundant or inconsistent metadata fields requiring systematic optimization and quality assurance protocols
- Need for implementing standardized vocabulary controls and authority files for product categories, brand names, and geographic locations

**Preservation and Sustainability Concerns:**
- Long-term digital preservation requirements for ensuring continued scholarly access to these unique primary sources
- Development of sustainable funding models for ongoing maintenance of technical infrastructure and metadata enhancement projects
- Creation of interoperable data formats supporting integration with other digital humanities projects and institutional repositories

# 2. Data Processing and Standardization Methodology

## 2.1 Data Acquisition and Initial Processing

The data processing pipeline for the Chinese Commercial Advertisement Archive involved multiple stages of acquisition, validation, and standardization to transform raw archival materials into a research-ready dataset. The initial dataset was stored on Aliyun Object Storage Service (OSS) in China, requiring systematic migration to AWS S3 infrastructure for improved international accessibility and research collaboration.

### Primary Data Sources and Validation

The processing began with a comprehensive audit of 108,244 advertisement images distributed across five major newspaper collections. Each advertisement entry comprised multiple file components requiring individual validation: primary cropped advertisement images (image.jpg), optimized thumbnail previews (image_thumbnail.jpg), and complete newspaper page contexts (image_page.jpg). The validation process employed Python's PIL (Python Imaging Library) to verify image integrity and prevent corrupted files from entering the research dataset.

### Metadata Extraction and Normalization

The original metadata structure contained nested JSON objects with complex multilingual field hierarchies requiring systematic flattening and standardization. Key transformations included extracting embedded metadata from the 'zh-Hans' collection structure, converting Aliyun OSS URLs to standardized AWS S3 paths, and creating publisher mappings using standardized abbreviation systems.

**Example: Metadata Structure Transformation**

The complex nested architecture of the original metadata required comprehensive flattening to enable efficient research queries:

*Before (Nested JSON Structure):*
```json
{
  "metadata": {
    "zh-Hans": {
      "collection_moreinfos": {
        "dc_subject_brand": "清快丸",
        "dc_subject_product": "Pharmaceutical products[藥品]",
        "chao_company_name": "高橋盛大堂藥房[Sei-K Wai-Gan]",
        "dc_contributor_publisher": "Hankow Times[汉口中西报]"
      }
    }
  }
}
```

*After (Flattened Structure):*
```json
{
  "dc_subject_brand": "清快丸",
  "dc_subject_product": "Pharmaceutical products[藥品]",
  "chao_company_name": "高橋盛大堂藥房[Sei-K Wai-Gan]",
  "publisher": "Press of Hankow Times [汉口中西报社]"
}
```

### Publisher Standardization and Dating Systems

Inconsistent publisher naming conventions required systematic standardization to enable cross-collection analysis:

*Before (Inconsistent Naming):*
- `"dc_contributor_publisher": "Hankow Times[汉口中西报]"`
- `"dc_contributor_publisher": "[Missing label]`
- `"chao_contributor_printer": "Press of Hankow Times[汉口中西报社]"`

*After (Standardized with Abbreviation System):*
- `"publisher": "Press of Hankow Times [汉口中西报社]"`


### Image Processing and Optimization

Thumbnail images underwent systematic processing to optimize storage and improve research interface performance. Original thumbnails were converted to grayscale, resized to 75% of original dimensions, and encoded as base64 strings for direct embedding in research databases. This approach eliminated the need for separate image serving infrastructure while maintaining sufficient visual quality for preliminary content analysis.

**Example: Image Processing Transformation**

*Before (Original Thumbnail Requirements):*
- Full-color JPEG thumbnail files
- Original dimensions maintained
- Separate file serving infrastructure required
- Additional HTTP requests for image loading

*After (Optimized for Database Integration):*
- Converted to grayscale for for storage efficiency
- Base64 encoded for direct database retrieval
```
thumbnail_base64: "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQ..."
```

## 2.2 Linguistic Standardization and Translation Processes

### Character Set Normalization

A critical challenge involved standardizing Chinese character representations across the multilingual dataset. The archive contained inconsistent usage of Simplified and Traditional Chinese characters, requiring systematic conversion using OpenCC (Open Chinese Convert) libraries. All Chinese text fields were standardized to Traditional Chinese characters to maintain historical authenticity and consistency with early twentieth-century publishing practices.

**Example: Character Set Standardization**

The normalization process required careful attention to historical authenticity while ensuring systematic consistency:

*Before (Mixed Inconsistent Simplified/Traditional Characters):*
```
dc_subject_product: "Pharmaceutical products[药品]"  // Simplified: 药品
dc_subject_product: "Tobacco products[菸草製品]"
```

*After (Standardized to Traditional Chinese):*
```
dc_subject_product: "Pharmaceutical products[藥品]"  // Traditional: 藥品
dc_subject_product: "Tobacco products[煙草製品]"
```

### Field-Specific Standardization Protocols

Systematic normalization was applied to product categories, brand names, and geographic locations to eliminate variant spellings and inconsistent terminology. Product categories underwent consolidation to enable meaningful analysis across the collection.

Company nationality fields required similar standardization to remove punctuation inconsistencies:

*Before (Inconsistent Punctuation):*
```
chao_company_nation: "Japan[日本]"
chao_company_nation: "U.S.A."
chao_company_nation: "U.S.A"
```

*After (Standardized Format):*
```
chao_company_nation: "Japan[日本]"
chao_company_nation: "U.S.A.[美国]"
```

### Bilingual Translation Methodology

For enhancing international research accessibility, a comprehensive translation process was implemented for uncaptioned materials using advanced language models. The translation protocol employed a specialized scholarly prompt designed to ensure accuracy and maintain historical context.

**Translation Prompt Framework:**
```
Invoking Claude 3.0 Haiku model with prompt: 

    You are a scholar translator. You are given a Chinese text and you need to translate it into English rigourously.
    The image is a advertisement. You need to transform it into both Chinese and English and make sure the translation is accurate and professional.

    <dc_title_ch> Exact Title in Chinese characers in Tranditional Chinese (Not Simplified)</dc_title_ch>
    <dc_title_en> English Translation of Chinese Title</dc_title_en>
    Example Chinese format: 懷中良藥 個人常備之良劑清快丸

    <fulltext_ch> Exact Full Text Chinese characers in Tranditional Chinese (Not Simplified)</fulltext_ch>
    <fulltext_en> English Translation of Chinese Full Text </fulltext_en>
    Example Chinese format: 清快丸之藥清胃鎮痙於為主眼以最新最良之藥為配劑者故對社會有十二分之一責任也 清快丸之藥
    平常一二粒於口中含味即芳香馥鬱立刻精神爽快 故名清快丸誠不誣也 凡一切社會於夫優美之令孃賢德之夫人奉公之紳士活潑之青年強健之軍人敏腕之事物家熱心之藝術家豔麗之名妓嘗祈注意可懷中者也
    大包美術每匣兩角半 中包一角 小包五分 躉批另議
    總經理處 上海法大馬陸路中市一百號 日信洋行藥品部 
    副經理處 漢口龍王廟河街 泰信洋行
    不論上海漢口於中國十八行省各處出名藥廠均可收發代售

    Start with <dc_title_ch> and end with </fulltext_en>.
```

**Example: Translation Process Implementation**

*Chinese Source Text:*
```
懷中良藥 個人常備之良劑清快丸
清快丸之藥清胃鎮痙於為主眼以最新最良之藥為配劑者故對社會有十二分之一責任也
```

*Translation Prompt Application Results:*
```xml
<dc_title_ch>清快丸,"懷中良藥"</dc_title_ch>
<dc_title_en>Qingkuai Pill, "Pocket Remedy"</dc_title_en>
<fulltext_ch>懷中良藥 個人常備之良劑清快丸...</fulltext_ch>
<fulltext_en>Pocket Remedy - A Reliable Tonic for Personal Use: Qingkuai Pill
The Qingkuai Pill's main ingredients are to cleanse the stomach and relieve spasms...</fulltext_en>
```

### Translation Quality Control

The translation process utilized Anthropic's Claude 3.0 Haiku model for cost-effective processing while maintaining scholarly translation standards. The structured prompt format ensured consistent output formatting and enabled systematic quality review of translated materials. Each translation underwent validation for historical terminology accuracy and contextual appropriateness for early twentieth-century commercial language.

### Temporal and Geographic Data Processing

Date fields were standardized to ISO format (YYYY-MM-DD) with comprehensive error handling for incomplete or ambiguous historical dates. Geographic location data was normalized to contemporary historical place names while preserving original Chinese designations. Publication citation numbers were systematically extracted from image filenames using regular expression patterns to reconstruct bibliographic sequences.

### Text Separation by Language for Language-Specific Retrieval from Database

Full-text descriptions underwent preprocessing to separate Chinese and English content in two distinct fields, enabling efficient language-specific retrieval from the MongoDB database. This separation facilitated targeted queries for researchers focusing on either Chinese or English content without requiring complex parsing of mixed-language fields.

The comprehensive data processing pipeline transformed a complex, inconsistent archival collection into a standardized research dataset that maintains historical authenticity while enabling modern scholarly analysis and international accessibility. The systematic approach to normalization, translation, and quality control ensures that researchers can conduct reliable comparative studies across the entire collection while preserving the unique characteristics of early twentieth-century Chinese commercial culture.

### 3.2 Automated Text Transcription Experiments

**Large Language Model Evaluation Framework:**
Systematic testing revealed significant variations in transcription accuracy across different AI models when processing early twentieth-century Chinese advertisements. The evaluation framework employed six distinct models representing current state-of-the-art capabilities: Anthropic's Claude 3.7 Sonnet, Claude Sonnet 4, Claude Opus 4, Claude 3.5 Sonnet variants, and Meta's Llama 4 Maverick. Each model was evaluated using identical test images to ensure comparative validity.

**Standardized Transcription Prompt:**
```
You are a translation scholar. You are given a Chinese image of advertisement appeared in 1900s newspaper and you need to translate it into English rigorously. You need to transform it into both Chinese and English and make sure the translation is accurate and professional.

<dc_title_ch> Exact Title in Chinese characters in Traditional Chinese (Not Simplified)</dc_title_ch>
<dc_title_en> English Translation of Chinese Title</dc_title_en>
<fulltext_ch> Exact Full Text Chinese characters in Traditional Chinese (Not Simplified)</fulltext_ch>
<fulltext_en> English Translation of Chinese Full Text</fulltext_en>

Start with <dc_title_ch> and end with </fulltext_en>. Do not include any other text or explanation.
```

**Comparative Model Performance Analysis:**
Testing across representative advertisement samples demonstrated substantial differences in transcription quality and consistency. Anthropic's Claude 3.7 Sonnet and Claude Sonnet 4 models provided the most coherent interpretations of historical commercial content, successfully identifying company names, product categories, and basic advertisement structures. However, even the highest-performing models exhibited significant character-level inaccuracies when attempting verbatim transcription of historical Chinese text.

**Critical Limitations in Text Recognition:**
Comprehensive evaluation revealed fundamental challenges in automated transcription of historical Chinese advertisements. All tested models struggled with precise character recognition due to historical typeface variations, print quality degradation, and period-specific commercial terminology. Meta's Llama models demonstrated particular instability, frequently generating entirely fictional content including anachronistic company names and product descriptions that bore no relationship to the actual advertisement content.

### 3.3 OCR Technology Assessment and Alternative Approaches

**Traditional OCR Limitations:**
Evaluation of conventional Optical Character Recognition (OCR) technologies, including Tesseract with specialized Chinese language models (chi_tra_vert.traineddata and chi_tra), yielded completely unsuccessful results for the historical advertisement materials. Testing with multiple pre-trained models designed for vertical and horizontal Chinese text processing returned empty outputs across all tested images, demonstrating fundamental incompatibility with early twentieth-century commercial printing styles.

**Technical Challenges in Historical Text Recognition:**
The systematic failure of traditional OCR approaches highlighted critical barriers in processing historical Chinese commercial materials: significant variations in typeface design across different newspapers and time periods, specialized commercial vocabulary and naming conventions not present in contemporary training datasets, complex visual layouts integrating text with graphic elements and product illustrations, and substantial image quality degradation affecting character clarity and recognition algorithms optimized for modern digital text.

### 3.4 Strategic Pivot to Image Description and Categorization

**Recognition of Technical Constraints:**
Following extensive testing that demonstrated consistent failures in verbatim transcription across all available AI models, the project strategically shifted from text-focused extraction to comprehensive image description and categorical analysis. This approach proved more technically feasible while still generating valuable metadata for scholarly research applications.

**Enhanced Description Generation Framework:**
The refined methodology employed a specialized prompt structure designed to generate consistent, research-quality descriptions of advertisement visual elements and systematic product categorization:

```
Given a Chinese image of advertisement appeared in 1900s newspaper and return the description of the visual elements in the image, return empty string if there is no visual element but pure text.

<image_description_ch> Exact Title of this advertisement visual elements in Chinese characters in Chinese. If there is not visual element, return empty string.</image_description_ch>
<image_description_en> Exact English translation of image image_description_ch. If there is not visual element, return empty string.</image_description_en>

<image_category> Category of the image. Pick one from ['橡膠輪胎及橡膠管', '傢俱及其它製成品', '菸草製品', '鐘錶及其部件', '煙草製品', '原油及提煉油', '樂器', '保險和養老金服務', '穀物研磨品', '日化用品', '光學儀器', '食品', '家用設備', '糖果', '飲品', '機械車', '乳製品', '紡織品', '玻璃製品', '化工產品', '化肥及殺蟲劑', '原料耗材', '藥品', '體育用品', '其它運輸工具及其配件', '廣播電視通訊設備及部件', '日用品', '辦公設備及其部件', '發動機及其配件', '織物', '布料皮革製品機器及其配件', '音響設備', '耗材', '蓄電池']</image_category>

Start with <image_description_ch> and end with </image_category>. Do not include any other text or explanation.
```

**Asynchronous Processing Implementation:**
The production system employed sophisticated asynchronous processing architecture to manage large-scale image analysis efficiently. The implementation utilized batch processing with configurable concurrency limits, comprehensive error handling and retry mechanisms, and progress tracking across thousands of images. This approach enabled processing of the complete Shen Bao uncaptioned collection (2,924 images) and substantial portions of other newspaper archives (63,544 images) within a reasonable timeframe while maintaining searchable metadata integrity.

**Product Classification and Taxonomy Integration:**
The automated categorization system successfully classified advertisements into 34 distinct product categories aligned with the existing metadata taxonomy. This classification enabled systematic analysis of commercial patterns across temporal and geographic dimensions. The system demonstrated particular effectiveness in identifying pharmaceutical advertisements (藥品), which constituted the largest single category, tobacco products (煙草製品), and various categories of imported consumer goods.



The automated description and categorization process provided a scalable solution for enhancing the accessibility of historical advertisement materials while acknowledging the limitations of current AI-assisted text processing technologies. The system's ability to generate consistent, structured metadata enabled researchers to conduct meaningful analyses of commercial trends and product representations across the collection without relying on verbatim text extraction.

**Example: Automated Image Description and Categorization Output**
```xml
<image_description_ch>中藥丸藥瓶，上面有裝飾圖案</image_description_ch>
<image_description_en>A traditional Chinese medicine bottle with decorative patterns</image_description_en>
<image_category>藥品</image_category>
```
```xml
<image_description_ch>漁夫背著一條大魚站立的形象，以及一瓶史考特乳劑藥品包裝</image_description_ch>
<image_description_en>A fisherman standing with a large fish on his back, and a bottle of Scott's Emulsion medicine packaging</image_description_en>
<image_category>藥品</image_category>
```

The automated captioning initiative demonstrated both the potential and current limitations of AI-assisted processing for historical Chinese materials, establishing a scalable methodology for enhancing archival accessibility while providing realistic assessments of technological capabilities for historical text processing applications.


## 4. Database Architecture and Visualization Infrastructure

## 4.1 MongoDB as the Main Database for Historical Advertisement Research

The Chinese Commercial Advertisement Archive's implementation of MongoDB as its primary database solution represents a strategic choice that addresses the unique challenges inherent in managing large-scale historical multimedia collections. Unlike traditional relational databases that impose rigid schema constraints, MongoDB's document-based architecture provides the flexibility essential for accommodating the heterogeneous nature of historical advertisement data, where fields may be incomplete, multilingual, or variable in structure across different time periods and publishers.

### Document Structure and Multilingual Data Representation

The archive's data structure encompasses a complex array of metadata fields including Dublin Core elements (dc_title_ch, dc_title_en, dc_description_fulltext_ch, dc_description_fulltext_en), bibliographic information (dc_citation_volumenumber, dc_citation_issuenumber), commercial metadata (chao_company_name, chao_productagency, dc_subject_brand), and technical storage references and visual contents (s3_url_img, thumbnail_base64). This multifaceted data model would require extensive normalization and complex join operations in a relational system, potentially compromising query performance and complicating data retrieval for researchers seeking to explore cross-temporal advertising patterns or brand evolution.

**Example: Document Structure Flexibility**

Consider how MongoDB accommodates the varying completeness of historical records:

*Complete Entry (1907 Pharmaceutical Advertisement):*
```json
{
  "_id": "683424d62c3ea95f4d373b1a",
  "publisher": "Press of Hankow Times [汉口中西报社]",
  "dc_date_issued": {"$date": {"$numberLong": "-1956787200000"}},
  "dc_citation_volumenumber": 1907,
  "dc_citation_issuenumber": "589",
  "dc_title_en": "Qingkuai Pill, \"Pocket Remedy\"",
  "dc_title_ch": "清快丸,\"懷中良藥\"",
  "dc_subject_brand": "清快丸",
  "dc_subject_product": "Pharmaceutical products[藥品]",
  "dc_description_fulltext_en": "Pocket Remedy - A Reliable Tonic...",
  "dc_description_fulltext_ch": "懷中良藥 個人常備之良劑清快丸...",
  "chao_company_name": "高橋盛大堂藥房[Sei-K Wai-Gan]",
  "chao_company_nation": "Japan[日本]",
  "thumbnail_base64": "/9j/4AAQSkZJRgABAQAAAQABAAD..."
}
```

*Incomplete Entry (Missing Translation):*
```json
{
  "_id": "683424d62c3ea95f4d373b1c",
  "publisher": "Press of Hankow Times [汉口中西报社]",
  "dc_date_issued": {"$date": {"$numberLong": "-1893456000000"}},
  "dc_citation_volumenumber": 1910,
  "dc_title_ch": "德國西藥房",
  "dc_subject_product": "Pharmaceutical products[藥品]",
  "chao_company_nation": "Germany[德國]",
  // Note: Missing English translation fields, but document remains valid
  "processing_status": "TRANSLATION_PENDING"
}
```

In a relational database, the incomplete entry would either require NULL values across multiple tables or force artificial data creation. MongoDB's flexible schema allows researchers to access available data immediately while flagging entries for future enhancement.

MongoDB's native support for nested documents and arrays proves particularly valuable when handling the multilingual aspects of the collection. Historical Chinese advertisements often contain mixed-script content, combining traditional Chinese characters, modern Chinese text, and Western languages within single advertisements.

### Strategic Index Design for Historical Research Patterns

The database indexing strategy reflects careful consideration of anticipated research patterns within the digital humanities community. The creation of indexes on dc_date_issued, dc_citation_volumenumber, dc_citation_issuenumber, and dc_subject_product directly supports the most common scholarly inquiries into historical advertising materials. Temporal indexing enables efficient chronological analysis, allowing researchers to examine advertising trends across decades, identify the emergence of new product categories, or analyze the evolution of marketing strategies during specific historical periods such as the Republican era or the early Communist period.

The unique index on s3_url_img serves dual purposes: ensuring data integrity while optimizing image retrieval operations. Given the substantial size of the image collection (198.28 GB), efficient access to specific visual materials is essential for both computational analysis and traditional art historical examination. This indexing approach supports rapid retrieval while preventing duplicate image entries that could skew quantitative analyses of advertising prevalence or brand representation.

The inclusion of dc_subject_product indexing recognizes the particular importance of commodity studies within historical advertisement research. Scholars investigating the history of consumption, the introduction of foreign products to Chinese markets, or the evolution of domestic industries require efficient access to product-categorized materials. This indexing strategy enables complex queries that might examine, for example, the changing representation of pharmaceutical products between different publishers or the emergence of luxury goods advertising during periods of economic transformation.


**Example: Temporal Research Queries**

*Chronological Analysis Query:*
```javascript
// Efficient temporal querying enabled by dc_date_issued index
db.advertisements.find({
  "dc_date_issued": {
    "$gte": ISODate("1905-01-01"),
    "$lte": ISODate("1915-12-31")
  },
  "dc_subject_product": "Pharmaceutical products[藥品]"
}).sort({"dc_date_issued": 1})

// Results reveal emergence patterns of pharmaceutical advertising
```

*Publisher Evolution Analysis:*
```javascript
// Cross-publisher product category analysis
db.advertisements.aggregate([
  {
    "$match": {
      "dc_citation_volumenumber": {"$gte": 1905, "$lte": 1915}
    }
  },
  {
    "$group": {
      "_id": {
        "publisher": "$publisher",
        "product": "$dc_subject_product",
        "year": "$dc_citation_volumenumber"
      },
      "count": {"$sum": 1}
    }
  }
])

// Reveals: Publisher-specific advertising trends in pharmaceutical products during the early twentieth century
```

The unique index on s3_url_img serves dual purposes: ensuring data integrity while optimizing image retrieval operations. Given the substantial size of the image collection (198.28 GB), efficient access to specific visual materials is essential for both computational analysis and traditional art historical examination.

### Atlas Search Configuration and Multilingual Considerations

The implementation of MongoDB Atlas Search with Chinese language analysis represents a sophisticated approach to the challenges of historical Chinese text retrieval. The configuration utilizing the "lucene.chinese" analyzer addresses the particular complexities of historical Chinese texts, which may employ variant character forms, traditional orthography, or historical terminology that differs significantly from contemporary usage.

The strategic selection of stored source fields (publisher, titles in both languages, descriptions, image descriptions, company information, geographic data, and product classifications) optimizes search performance while maintaining comprehensive access to research-relevant metadata. This configuration acknowledges that digital humanities researchers typically require rapid access to bibliographic and commercial metadata rather than complete document reconstruction for preliminary exploration and filtering.

**Configuration: Atlas Search Query for Multilingual Metadata**
```
{
  "analyzer": "lucene.chinese",
  "searchAnalyzer": "lucene.chinese",
  "mappings": {
    "dynamic": true
  },
  "storedSource": {
    "include": [
      "publisher",
      "dc_title",
      "dc_description_fulltext",
      "chao_company_name",
      "chao_company_nation",
      "chao_productagency",
      "dc_publishing_location",
      "dc_subject_brand",
      "dc_subject_product"
    ]
  }
}
```

The bilingual indexing approach, incorporating both Chinese and English metadata fields, recognizes the international nature of the research community studying Chinese commercial history. Western scholars may initiate searches using English terms while requiring access to Chinese-language primary source materials, necessitating seamless cross-linguistic discovery capabilities.

### Multimodal Embeddings and the Significance of Visual Representation

The Chinese Commercial Advertisement Archive (CCAA) incorporates a TensorBoard Embedding Projector to support exploratory analysis of high-dimensional representations of historical advertisements. This interactive visualization tool enables researchers to navigate, cluster, and interpret image embeddings generated from the archive’s visual and textual features.

---

### Overview of Embedding Projection

The embedding projector visualizes precomputed vectors derived from the archived advertisements using deep learning models. These vectors encode semantic and stylistic patterns captured from advertisement images, including layout, typography, and iconography, and optionally integrate textual metadata such as product categories or publication dates.

Researchers can explore this latent space to uncover:

* **Visual affinities across product types**
* **Temporal clusters indicating design evolution**
* **Cross-publication similarities in advertising style**
* **Outlier analysis highlighting unique or innovative advertisements**

---

### Interactive Interface Features

The TensorBoard interface provides intuitive controls for manipulating and filtering the embedding space:

* **Label By**: Assigns label text to each data point. Common choices include `Publisher`, `Product`, or `Date`.
* **Color By**: Applies color mapping based on metadata (e.g., date range, category) to aid in visual clustering.
* **Edit By / Tag Selection**: Allows users to create custom tags or organize subsets of advertisements for further analysis.
* **Spherize Data**: Normalizes the vector distribution for optimal UMAP/PCA/T-SNE projection.

Learn more about the Dimension Reduction techniques: [UMAP](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html).

---

### Dimensionality Reduction: UMAP Configuration

The default projection is computed using **UMAP (Uniform Manifold Approximation and Projection)** with configurable parameters:

* **Dimension**: Select between **2D** or **3D** space for visual rendering.
* **Neighbors**: Adjusts local neighborhood size; higher values reveal broader structure, lower values emphasize local clustering.
* **Sampling**: For performance, the interface automatically samples down to 5,000 points if the dataset is large.

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/spinning.gif" alt="PCA Spinning Preview" width="600">
</p>

---

### Metadata-Driven Filtering and Exploration

Users can navigate the embedding space using metadata controls:

* Filter by **Publisher**, **Product Category**, or **Publication Date**
* Explore bilingual metadata (English/Chinese) for cross-lingual comparison
* Hover or click on individual points to retrieve image thumbnails and corresponding metadata

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/navigation.gif" alt="Interactive Metadata Filtering" width="600">
</p>

---

### Analytical Potential

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
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/umap.gif" alt="Cluster Exploration" width="600">
</p>

---

### Use Cases

This embedded tool supports a variety of scholarly workflows:

* **Media historians** tracing visual style shifts by decade or product class
* **Design researchers** identifying typographic or compositional conventions
* **Digital humanists** conducting exploratory clustering or similarity search
* **Educators** creating visual narratives from selected advertisement clusters

## 5. Cloud Native Infrastructure and Scalability

The **Chinese Commercial Advertisement Archive (CCAA)** is built on a cloud-native, modular infrastructure optimized for scalability, reliability, and international accessibility. This design enables robust, low-latency interaction with over 100,000 historical advertisement records while ensuring cost-efficiency and resilience.

<p align="center">
  <img src="https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/report/ccaa_architecture.png" alt="CCAA Architecture Diagram" width="800">
</p>

---

### 5.1 Key Components and Responsibilities

**1. Users**
End users access the archive through a web interface or RESTful API endpoints. The system supports both technical and non-technical users, including historians, linguists, designers, and data scientists.

**2. Streamlit Interface**
A lightweight Python-based application built using [Streamlit](https://streamlit.io/), providing an interactive graphical interface. It enables:

* Faceted search by year, publisher, and product category
* Metadata preview and image visualization
* Download/export capabilities
  The application is designed for easy re-deployment across cloud platforms and is open-sourced under a Creative Commons license.

**3. GitHub**
The application source code, configuration, and deployment instructions are publicly maintained via GitHub. This promotes transparency, collaboration, and reproducibility within the digital humanities community.

---

### 5.2 AWS Cloud Services Integration

**4. Amazon API Gateway**
Serves as the secure entry point for all metadata and image retrieval requests. It enables:

* Access control and throttling
* Stateless RESTful communication
* Decoupling of frontend and backend layers

**5. AWS Lambda**
Implements serverless, event-driven logic for on-demand metadata filtering, presigned image URL generation, and efficient API responses. Benefits include:

* Auto-scaling under load
* Reduced operational overhead
* Stateless compute layer

**6. AWS S3 (Simple Storage Service)**
All advertisement images (cropped and thumbnails) are stored in a dedicated Amazon S3 bucket. Features include:

* Durable, globally accessible image storage
* Efficient distribution via presigned URLs
* Optimized delivery for different image resolutions

**7. MongoDB Atlas**
A fully managed cloud database hosting structured metadata for the archive (e.g., title, year, publisher, product, OCR results). It supports:

* Rich queries with text indexing and filtering
* Seamless horizontal scaling
* Integration with Python-based backend services

---

### 5.3 Separation of Concerns and Performance Optimization

This architecture reflects a clear **separation of concerns** between:

* **Metadata retrieval** (MongoDB Atlas)
* **Image serving** (AWS S3)
* **Application logic** (Lambda functions)
* **User interface** (Streamlit)

Such separation ensures that queries for metadata do not overload image storage or processing pipelines, and vice versa. This architecture is particularly advantageous for researchers in bandwidth-constrained environments, as metadata previews can be browsed without loading high-resolution images.

---

### 5.4 Scalability and Global Accessibility

* The serverless architecture (Lambda + API Gateway) enables **elastic scalability**, automatically adjusting to increased demand (e.g., during workshops or data crawls).
* Geographic distribution of AWS services supports **low-latency access** for users across regions.
* Future enhancements may include integration with CloudFront (CDN) for even faster global image access.


## 6. Conclusion: Implications for Digital Humanities Infrastructure

The technical infrastructure developed for the CCAA demonstrates the necessity of moving beyond traditional text-based approaches in digital humanities projects that engage with visual historical materials. The combination of flexible document storage, multilingual search capabilities, and computational visual analysis creates a research environment that supports both traditional scholarly methodologies and emerging computational approaches.

The scalability of this infrastructure proves essential given the archive's substantial size and the likelihood of future expansion. Historical newspaper digitization projects continue to uncover additional advertisement materials, and the database architecture must accommodate growth while maintaining query performance. The MongoDB approach provides horizontal scaling capabilities that ensure continued research accessibility as the collection expands.

The integration of cloud storage (AWS S3) with database metadata creates a distributed architecture that separates concerns between image storage and analytical access, enabling efficient resource utilization while maintaining data integrity. The capability of s3 presigned URLs for image retrieval allows researchers to access images directly without requiring large downloads, and enhance security by controlling access to image files through temporary URLs.

The success of this infrastructure suggests broader implications for digital humanities projects working with large-scale multimedia historical collections. The methodological framework demonstrated here—combining flexible document databases, multimodal computational analysis, and interactive visualization—provides a template for similar projects in other historical and cultural domains. As digital humanities continues to grapple with increasingly complex and voluminous source materials, the approaches developed for the CCAA offer valuable precedents for creating research infrastructure that serves both computational and traditional scholarly methodologies.

The archive's technical achievements ultimately serve broader scholarly goals: enabling new forms of historical inquiry that combine quantitative analysis with qualitative interpretation, supporting collaborative research across linguistic and disciplinary boundaries, and preserving important cultural materials in formats that ensure long-term accessibility for future scholarship. The intersection of historical content with advanced computational infrastructure creates possibilities for understanding Chinese commercial culture and advertising history that extend far beyond what either traditional archival methods or computational analysis could achieve independently.