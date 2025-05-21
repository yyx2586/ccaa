import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from io import BytesIO


import streamlit as st
import pandas as pd
import requests
import base64
import datetime
from io import BytesIO
from PIL import Image

# --- Settings
API_URL = "https://9pphdnzmo8.execute-api.us-east-1.amazonaws.com/Prod"
VIEWER_API = "https://9pphdnzmo8.execute-api.us-east-1.amazonaws.com/Prod"
RESULTS_PER_PAGE = 10

st.set_page_config(
    page_title="Positions Press - Chinese Commercial Advertisement Archive",
    layout="wide",
    page_icon="📰",
)

# Header
t1, t2 = st.columns((0.1, 1))
t1.image("images/index.png", width=100)
t2.title("Chinese Commercial Advertisement Archive")
t2.markdown(
    "**Project:** Ephemera Project | **Source:** Positions.Press | **Contact:** positionspress@gmail.com"
)


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("./ccaa_final.csv")  # Or .xlsx with pd.read_excel
    df["dc_date_issued"] = pd.to_datetime(df["dc_date_issued"], errors="coerce")
    return df


df = load_data()

# st.set_page_config(page_title="📚 Catalog Table", layout="wide")

# --- State for full-size image modal
if "modal_image" not in st.session_state:
    st.session_state.modal_image = None
if "modal_title" not in st.session_state:
    st.session_state.modal_title = None

with st.container():
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    query = col1.text_input("Search", "")
    start_date = col2.date_input(
        "Start Date",
        datetime.date(1907, 3, 9),
        min_value=datetime.date(1901, 1, 1),
        max_value=datetime.date(1938, 12, 31),
    )

    end_date = col3.date_input(
        "End Date",
        datetime.date(1938, 12, 31),
        min_value=datetime.date(1901, 1, 1),
        max_value=datetime.date(1938, 12, 31),
    )
    page = col4.number_input("Page", min_value=1, value=1, step=1)


def parse_mongo_date(obj):
    try:
        date = datetime.datetime.utcfromtimestamp(
            int(obj["$date"]["$numberLong"]) / 1000
        )
        return date.strftime("%Y-%m-%d")
    except:
        return ""


def limit_words(text, limit=20):
    if not text:
        return ""
    import re

    segments = re.findall(r"[\u4e00-\u9fa5]|[^\s\u4e00-\u9fa5]+", str(text))
    return "".join(segments[:limit]) + ("..." if len(segments) > limit else "")


# --- Fetch Catalog Page
params = {
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "page": page,
}
if query:
    params["query"] = query

with st.spinner("Loading catalog..."):
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        catalog = response.json()
        results = catalog.get("results", [])
        total_count = catalog.get("total_count", len(results))
        total_pages = catalog.get("total_pages", 1)

        st.write(
            f"📄 Showing page {page} of {total_pages} — Total results: {total_count}"
        )

        if not results:
            st.warning("No records found.")
        else:
            # --- HTML Table with Embedded Base64 Images
            html_rows = []
            html_rows.append(
                """
            <table style="width:100%; border-collapse: collapse;">
            <thead>
            <tr style="background-color: #f2f2f2;">
            <th style="padding: 8px; border: 1px solid #ccc;">Thumbnail</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Title</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Brand</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Product</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Company</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Date</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Agency</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Publisher</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Location</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Text Preview</th>
            </tr>
            </thead>
            <tbody>
            """
            )

            for i, item in enumerate(results):
                title = item.get("dc_title", "")
                brand = item.get("dc_subject_brand", "")
                product = item.get("dc_subject_product", "")
                company = item.get("chao_company_name", "")
                agency = limit_words(item.get("chao_productagency", ""), 15)
                publisher = item.get("dc_contributor_publisher", "")
                location = item.get("dc_publishing_location", "")
                full_text = limit_words(item.get("dc_description_fulltext", ""), 20)
                issued = parse_mongo_date(item.get("dc_date_issued", {}))
                thumb_b64 = item.get("thumbnail_base64", "")
                s3_url = item.get("s3_url_img", "")

                if thumb_b64 and s3_url:
                    full_img_url = f"{VIEWER_API}?s3_url={s3_url}"
                    img_tag = f"""
                        <a href="{full_img_url}" target="_blank">
                            <img src="data:image/jpeg;base64,{thumb_b64}" style="height:80px;" title="Click to view full image"/>
                        </a>
                    """
                else:
                    img_tag = "N/A"

                html_rows.append(
                    f"""
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">{img_tag}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{title}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{brand}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{product}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{company}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{issued}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{agency}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{publisher}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{location}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{full_text}</td>
            </tr>
            """
                )

            html_rows.append("</tbody></table>")
            st.markdown("".join(html_rows), unsafe_allow_html=True)
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Plotting
st.subheader("📊 Advertisement Statistics")

# Plot by year
if df["dc_date_issued"].notnull().any():
    df["year"] = df["dc_date_issued"].dt.year
    fig1 = px.histogram(df, x="year", title="Number of Advertisements per Year")
    st.plotly_chart(fig1, use_container_width=True)

# Brand frequency
top_brands = df["dc_subject_brand"].value_counts().nlargest(30)
fig2 = px.bar(
    top_brands,
    x=top_brands.index,
    y=top_brands.values,
    labels={"x": "Brand", "y": "Count"},
    title="Top 30 Brands",
)
st.plotly_chart(fig2, use_container_width=True)

# Top product categories
top_products = df["dc_subject_product"].value_counts().nlargest(15)
fig3 = px.bar(
    top_products,
    x=top_products.index,
    y=top_products.values,
    labels={"x": "Product Category", "y": "Count"},
    title="Top 15 Product Categories",
)
st.plotly_chart(fig3, use_container_width=True)

# Company nations
nation_counts = df["chao_company_nation"].value_counts().nlargest(10)
fig4 = px.pie(
    names=nation_counts.index,
    values=nation_counts.values,
    title="Top Company Nations",
    hole=0.4,
)
st.plotly_chart(fig4, use_container_width=True)

# Publisher trends over years
if "year" not in df.columns:
    df["year"] = df["dc_date_issued"].dt.year

pub_years = df.groupby(["year", "publisher"]).size().reset_index(name="count")
fig5 = px.line(
    pub_years,
    x="year",
    y="count",
    color="publisher",
    title="Publisher Activity Over Time",
    labels={"count": "Ad Count", "year": "Year"},
)
st.plotly_chart(fig5, use_container_width=True)

# Ad count per issue page (grouped by issue number and page number)
page_stats = (
    df.groupby(["dc_citation_issuenumber", "dc_citation_pagenumber"])
    .size()
    .reset_index(name="count")
)
fig6 = px.box(
    page_stats,
    x="dc_citation_pagenumber",
    y="count",
    title="Distribution of Ads per Page Number",
    labels={"dc_citation_pagenumber": "Page", "count": "Ad Count"},
)
st.plotly_chart(fig6, use_container_width=True)

fig7 = px.treemap(
    df.dropna(subset=["dc_subject_product", "dc_subject_brand"]),
    path=["dc_subject_product", "dc_subject_brand"],
    title="Treemap of Brands within Product Categories",
)
st.plotly_chart(fig7, use_container_width=True)

fig8 = px.sunburst(
    df.dropna(subset=["chao_company_nation", "dc_subject_product", "dc_subject_brand"]),
    path=["chao_company_nation", "dc_subject_product", "dc_subject_brand"],
    title="Sunburst of Brands by Nation and Product Type",
)
st.plotly_chart(fig8, use_container_width=True)

heat_df = df.copy()
heat_df["year"] = heat_df["dc_date_issued"].dt.year
heat_data = (
    heat_df.groupby(["year", "dc_subject_product"])
    .size()
    .reset_index(name="count")
    .pivot(index="dc_subject_product", columns="year", values="count")
    .fillna(0)
)

fig9 = px.imshow(
    heat_data,
    aspect="auto",
    title="Heatmap of Ads by Product Type and Year",
    labels={"x": "Year", "y": "Product Type", "color": "Ad Count"},
)
st.plotly_chart(fig9, use_container_width=True)

polar_df = (
    df.groupby("dc_language_iso")["dc_type_genre"]
    .value_counts()
    .unstack(fill_value=0)
    .reset_index()
)

# Footer
with st.expander("About this project"):
    st.markdown(
        """
        **About this project**  
        This dashboard is part of the *Positions Press* initiative and is shared under the  
        [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
        Content is made publicly accessible to support scholarly research and engagement.
        """
    )
