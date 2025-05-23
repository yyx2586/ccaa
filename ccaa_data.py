import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from io import BytesIO
import streamlit.components.v1 as components
import html
import streamlit as st
import pandas as pd
import requests
import base64
import datetime
from io import BytesIO
from PIL import Image
from plotly.graph_objects import Sankey

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
        max_value=datetime.date(1940, 12, 31),
    )

    end_date = col3.date_input(
        "End Date",
        datetime.date(1938, 12, 31),
        min_value=datetime.date(1901, 1, 1),
        max_value=datetime.date(1940, 12, 31),
    )

    page = col4.number_input("Page", min_value=1, value=1, step=1)

    publisher = st.selectbox(
        "Select Publisher (optional)",
        options=[
            "",
            "Ta Kung Pao [大公报]",
            "Press of Hankow Times [汉口中西报社]",
            "Press of Sheng-ching Shih-pao [盛京时报社]",
            "Press of Yuet Wa Po [越华报社]",
        ],
        index=0,
        help="Filter by specific newspaper publisher",
    )


def parse_mongo_date(obj):
    try:
        date = datetime.datetime.fromtimestamp(
            int(obj["$date"]["$numberLong"]) / 1000, tz=datetime.timezone.utc
        )
        return date.strftime("%Y-%m-%d")
    except:
        return ""


def limit_words(text, limit=100):
    if not text:
        return ""
    import re

    segments = re.findall(r"[\u4e00-\u9fa5]+", str(text))
    return "".join(segments[:limit]) + ("..." if len(segments) > limit else "")


# --- Fetch Catalog Page
params = {
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "page": page,
    "publisher": publisher,
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
            <th style="padding: 8px; border: 1px solid #ccc;">Publisher</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Date</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Title</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Nation</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Company</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Brand</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Product</th>
            <th style="padding: 8px; border: 1px solid #ccc;">Text Preview</th>
            </tr>
            </thead>
            <tbody>
            """
            )

            # ["publisher", "dc_date_issued", "dc_citation_issuenumber", "dc_title", "dc_subject_brand", "dc_subject_product", "dc_description_fulltext"]

            for i, item in enumerate(results):
                publisher = item.get("publisher", "").replace("\n", " ")
                issued = parse_mongo_date(item.get("dc_date_issued", {})).replace(
                    "\n", " "
                )
                issued_vol = parse_mongo_date(
                    item.get("dc_citation_issuenumber", {})
                ).replace("\n", " ")
                title = item.get("dc_title", "").replace("\n", " ")
                brand = item.get("dc_subject_brand", "").replace("\n", " ")
                product = item.get("dc_subject_product", "").replace("\n", " ")
                full_text = item.get("dc_description_fulltext", "").replace("\n", " ")
                nation = item.get("chao_company_nation", "").replace("\n", " ")
                company = item.get("chao_company_name", "").replace("\n", " ")
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
            <td style="padding: 8px; border: 1px solid #ccc;">{publisher}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{issued}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{title}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{nation}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{company}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{brand}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">{product}</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
            <details>
            <summary style="cursor:pointer;">{full_text[:100]}[click_to_expand]</summary>
            {full_text}
            </details>
            </td>
            </tr>
            """
                )

            html_rows.append("</tbody></table>")
            st.markdown("".join(html_rows), unsafe_allow_html=True)
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


# Universe
st.subheader("🌐 Advertisement Embedding Universe")
st.markdown(
    """
    This section visualizes the advertisement embedding universe using TensorBoard Projector.

    The embeddings are generated using a model trained on the advertisement data.
    
    [TensorBoard Projector](https://projector.tensorflow.org/?config=https://ccaa-public-us-east-1-504133794192.s3.us-east-1.amazonaws.com/tensorboard_config_sprite.json).
    """
)

# Plotting
st.subheader("📊 Advertisement Statistics Analysis")
# --- Prepare data ---
if df["dc_date_issued"].notnull().any():
    df["year"] = pd.to_datetime(df["dc_date_issued"], errors="coerce").dt.year
    fig1 = px.histogram(df, x="year", title="Number of Advertisements per Year")

top_brands = df["dc_subject_brand"].value_counts().nlargest(30)
fig2 = px.bar(
    x=top_brands.index,
    y=top_brands.values,
    labels={"x": "Brand", "y": "Count"},
    title="Top 30 Brands",
)

top_products = df["dc_subject_product"].value_counts().nlargest(15)
truncated_labels = [
    label[:20] + "…" if len(str(label)) > 20 else label for label in top_products.index
]
fig3 = px.bar(
    x=truncated_labels,
    y=top_products.values,
    labels={"x": "Product Category", "y": "Count"},
    title="Top 15 Product Categories",
)

# --- Display all in one row ---
col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    st.plotly_chart(fig3, use_container_width=True)


# Get top 20 entries
nation_counts = df["chao_company_nation"].value_counts().nlargest(20)
brand_counts = df["dc_subject_brand"].value_counts().nlargest(20)
company_names = df["chao_company_name"].value_counts().nlargest(20)

# Create three pie charts
fig4 = px.pie(
    names=nation_counts.index,
    values=nation_counts.values,
    title="Top Company Nations",
    hole=0.4,
)
fig41 = px.pie(
    names=brand_counts.index,
    values=brand_counts.values,
    title="Top Brands",
    hole=0.4,
)
fig42 = px.pie(
    names=company_names.index,
    values=company_names.values,
    title="Top Company Names",
    hole=0.4,
)

# Display them side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig4, use_container_width=True)
with col2:
    st.plotly_chart(fig41, use_container_width=True)
with col3:
    st.plotly_chart(fig42, use_container_width=True)

import plotly.graph_objects as go

# Ensure 'year' column exists
if "year" not in df.columns:
    df["year"] = pd.to_datetime(df["dc_date_issued"], errors="coerce").dt.year

# --- Line Chart: Publisher Activity Over Time ---
pub_years = df.groupby(["year", "publisher"]).size().reset_index(name="count")
fig5 = px.line(
    pub_years,
    x="year",
    y="count",
    color="publisher",
    title="Publisher Activity Over Time",
    labels={"count": "Ad Count", "year": "Year"},
)

# --- Sankey Chart: Nation → Brand → Product ---
df_sankey = df.dropna(
    subset=["chao_company_nation", "dc_subject_brand", "dc_subject_product"]
)

top_brands = df["dc_subject_brand"].value_counts().nlargest(20).index
df_sankey = df_sankey[df_sankey["dc_subject_brand"].isin(top_brands)]

sources = df_sankey["chao_company_nation"]
brands = df_sankey["dc_subject_brand"]
products = df_sankey["dc_subject_product"]

all_labels = pd.concat([sources, brands, products]).astype(str).unique().tolist()


def map_labels(series):
    return series.map(lambda x: all_labels.index(str(x)))


source_labels = map_labels(sources._append(brands))
target_labels = map_labels(brands._append(products))

fig6 = go.Figure(
    go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=all_labels,
            color="lightblue",
        ),
        link=dict(
            source=source_labels,
            target=target_labels,
            value=[1] * len(source_labels),
            color="rgba(173,216,230,0.4)",
        ),
    )
)

fig6.update_layout(
    title_text="Flow: Nation → Brand → Product",
    font=dict(size=12),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=20, r=20, t=50, b=20),
)

# --- Display side by side ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig5, use_container_width=True)
with col2:
    st.plotly_chart(fig6, use_container_width=True)


top_publishers = df["publisher"].value_counts().nlargest(10).index
top_brands = df["dc_subject_brand"].value_counts().nlargest(30).index

heat_df = df[
    df["publisher"].isin(top_publishers) & df["dc_subject_brand"].isin(top_brands)
]
pivot = heat_df.pivot_table(
    index="publisher", columns="dc_subject_brand", aggfunc="size", fill_value=0
)

fig_heat = px.imshow(
    pivot,
    labels=dict(x="Brand", y="Publisher", color="Count"),
    title="Top Publishers vs. Top Brands",
    text_auto=True,
)
st.plotly_chart(fig_heat, use_container_width=True)


fig7 = px.treemap(
    df.dropna(subset=["dc_subject_product", "dc_subject_brand"]),
    path=["dc_subject_product", "dc_subject_brand"],
    title="Treemap of Brands within Product Categories",
)
st.plotly_chart(fig7, use_container_width=True)
# --- Sunburst Chart ---
fig8 = px.sunburst(
    df.dropna(subset=["chao_company_nation", "dc_subject_product", "dc_subject_brand"]),
    path=["chao_company_nation", "dc_subject_product", "dc_subject_brand"],
    title="Sunburst of Brands by Nation and Product Type",
)

# --- Heatmap Data Preparation ---
heat_df = df.copy()
heat_df["year"] = pd.to_datetime(heat_df["dc_date_issued"], errors="coerce").dt.year
heat_df["dc_subject_product"] = heat_df["dc_subject_product"].astype(str).str[:50]
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

# --- Layout with st.columns ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig8, use_container_width=True)
with col2:
    st.plotly_chart(fig9, use_container_width=True)

# Footer
st.markdown(
    """
    **About this project**  
    This dashboard is part of the *Positions Press* initiative and is shared under the  
    [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
    Content is made publicly accessible to support scholarly research and engagement.
    """
)
