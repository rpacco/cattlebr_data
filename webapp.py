import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import plotly.graph_objects as go
import json

# Load data
# converting numeric types
cattle_raw = pd.read_csv("data/cattle_raw_data.csv", index_col="D3C", parse_dates=True)

# Brazil cattle population
df_brazil = cattle_raw.query("D1N == 'Brasil'")["V"]

# Set page size
st.set_page_config(page_title="Cattle livestock analysis", layout="wide")
st.title("Brazilian cattle livestock timeseries :ox:")
st.subheader("Country timeseries vs. Amazon forest mesoregions timeseries")

# list of amazon states (abbreviations)
amazon = ["AC", "AM", "AP", "MA", "MT", "PA", "RO", "RR", "TO"]
# querying from raw data only mesoregions within amazon states
amazon_df = cattle_raw[cattle_raw['D1N'].apply(lambda x: any(elem in x for elem in amazon))].copy()

# Region selection
regions = amazon_df.query("D1N != 'Brasil'")["D1N"].unique().tolist()
user_select = st.selectbox("Select a region/mesoregion to compare with Brazil time series:", regions)
df_region = cattle_raw.query(f"D1N == '{user_select}'")["V"]
region_id = cattle_raw.query(f"D1N == '{user_select}'")["D1C"].unique()[0]
region_abv = cattle_raw.query(f"D1N == '{user_select}'")["D1N"].unique()[0].split(" ")[-1]

# Create slider for year selection
min_year = df_region.index.min().year
max_year = df_region.index.max().year
selected_year = st.slider(
    "Select a year:",
    min_value=min_year,
    max_value=max_year,
    value=min_year
)

# Filter data
filtered_df_brazil = df_brazil[df_brazil.index.year <= selected_year]
filtered_df_region = df_region[df_region.index.year <= selected_year]

sns.set_style("darkgrid")
# Create Brazil plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
sns.lineplot(x=filtered_df_brazil.index, y=filtered_df_brazil, ax=ax1, linewidth=4)
ax1.set_xlabel("Year")
ax1.set_ylabel("Cattle pop.")
ax1.set_title("Cattle pop. in Brazil")
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}M'.format(y/1e6)))

# Create region plot
fig2, ax2 = plt.subplots(figsize=(12, 8))
sns.lineplot(x=filtered_df_region.index, y=filtered_df_region, ax=ax2, linewidth=4)
ax2.set_xlabel("Year")
ax2.set_ylabel("Cattle population")
ax2.set_title(f"Cattle population in {user_select}")
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}M'.format(y/1e6)))


# Display plots in Streamlit app
col1, col2 = st.columns(2)
with col1:
    st.header("Cattle pop. in Brazil")
    st.pyplot(fig1)

with col2:
    st.header(f"Cattle pop. in {user_select}")
    st.pyplot(fig2)

## deforestation plot
st.header(f"{user_select} deforestation over the years")
# calculatin def rates
with open(f'data/amazon_def.csv') as f:
    amazon_def = pd.read_csv(f, index_col="date", parse_dates=True)
current_def = amazon_def[region_abv].loc[f"{selected_year}"][0]
cum_def = amazon_def[region_abv].loc[f"{min_year}":f"{selected_year}"].sum()
# Creating map figure
with open(f'data/geojson/{region_id}.json', 'r') as f:
    json_data = json.load(f)
    coordinates_list = json_data["features"][0]["geometry"]["coordinates"][0]

if len(coordinates_list) > 1:
    # Use the existing value of coordinates_list
    geojson_data = coordinates_list
else:
    # Update coordinates_list to the first coordinate in the nested list
    coordinates_list = json_data["features"][0]["geometry"]["coordinates"][0][0]
    geojson_data = coordinates_list

#creating hover text
hovertext = f'''
<span style="font-size: 16px">Mesoregion selected: {user_select}</span> <br> 
<span style="font-size: 16px">Mesoregion located in state: {region_abv}</span> <br> 
<span style="font-size: 16px">Deforestation at {region_abv} in {selected_year}: {current_def} km²</span> <br>
<span style="font-size: 16px">Cumulated deforestation at {region_abv} since {min_year}: {cum_def} km²</span>
'''
trace = go.Scattermapbox(
    lon=[coord[0] for coord in geojson_data],
    lat=[coord[1] for coord in geojson_data],
    mode='lines',
    line=dict(width=1, color='blue'),
    fill='toself',
    text = hovertext,
    hoverinfo= "text"
)

fig = go.Figure(trace)

fig.update_layout(
    mapbox=dict(
        style='carto-positron',
        zoom=3,
        center=dict(lon=-55, lat=-10)
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    width=800
)

# Display map
st.plotly_chart(fig)