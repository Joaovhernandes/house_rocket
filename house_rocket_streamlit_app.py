import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

pd.set_option('display.float_format', lambda x: '%.2f' % x)


# ============================ layout size =========================== #
st.set_page_config(layout='wide')
# =========================================================================================================== #


# ============================ Functions =========================== #
@st.cache(allow_output_mutation=True)
def get_data(url):
    data = pd.read_csv(url)

    return data


def transformation(data):
    # =========== Transforming data ===================== #
    data['date'] = data['date'].apply(lambda x: pd.to_datetime(x))

    data['bathrooms'] = data['bathrooms'].apply(lambda x: int(x))

    data['floors'] = data['floors'].apply(lambda x: int(x))

    data['yr_built'] = data['yr_built'].apply(lambda x: pd.to_datetime(x, format='%Y'))

    # ============ converting sqft to m2 ============= #
    data['m2_living'] = (data['sqft_living'] * 0.09290304)

    data['m2_lot'] = (data['sqft_lot'] * 0.09290304)

    data['sqft_above'] = (data['sqft_above'] * 0.09290304)

    data['sqft_basement'] = (data['sqft_basement'] * 0.09290304)

    data['m2_living15'] = (data['sqft_living15'] * 0.09290304)

    data['m2_lot15'] = (data['sqft_lot15'] * 0.09290304)

    data['price_buy'] = (data['price'] * 0.90)

    data['price_sell'] = (data['price'] * 1.1)
    # ================= house level ==================== #
    data['level'] = 'NA'

    for i in range(len(data)):
        if data.loc[i, 'price'] <= 321950:
            data.loc[i, 'level'] = 0

        elif (data.loc[i, 'price'] > 321950) & (data.loc[i, 'price'] <= 450000):
            data.loc[i, 'level'] = 1

        elif (data.loc[i, 'price'] > 450000) & (data.loc[i, 'price'] <= 645000):
            data.loc[i, 'level'] = 2

        else:
            data.loc[i, 'level'] = 3

    data['price_m2'] = data['price'] / data['m2_lot']

    # ================== drop bedrooms == 33 ================ #
    data = data.drop(data[data['bedrooms'] == 33].index)

    return data



def house_information(data):
    st.title('House Rocket Company')

    st.markdown('Welcome to House Rocket Data Analysis')

    st.title('House Information')
    f_id_ = st.sidebar.multiselect('Insert id', data['id'].unique())

    data_id = data[['id', 'bedrooms', 'bathrooms', 'm2_lot', 'price_m2', 'price', 'price_buy', 'price_sell']]

    if f_id_ != []:
        data_id = data_id.loc[data_id['id'].isin(f_id_), :]
    else:
        data_id = data_id.copy()

    st.write(f_id_)
    st.dataframe(data_id)

    return None


def houses_map (data):
    st.title('House Rocket Map')
    is_check = st.checkbox('Display Map')

    f_price_min = int(data['price'].min())
    f_price_max = int(data['price'].max())
    f_price_avg = int(data['price'].mean())

    if is_check:
        f_price_slider = st.slider('Price Range',
                                   f_price_min,
                                   f_price_max,
                                   f_price_avg
                                   )


        houses = data[data['price'] < f_price_slider][['id', 'lat', 'long', 'price']]
        # st.dataframe(houses)

        fig = px.scatter_mapbox(
            houses,
            lat='lat',
            lon='long',
            color='price',
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10
        )

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(height=600, margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)


    return None

def commercial_attributes(data):
    # ============== Average per Year ================ #

    st.title('Average Price per Year')

    df = data[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    fig = px.line(df, x='yr_built', y='price')

    st.plotly_chart(fig, use_container_width=True)

    # ============== Average per Day ================ #
    st.title('Average Price per Day')

    data['date'] = pd.to_datetime(data['date'])
    df = data[['date', 'price']].groupby('date').mean().reset_index()

    fig = px.line(df, x='date', y='price')

    st.plotly_chart(fig, use_container_width=True)

    return None


def data_overview(data):

    st.sidebar.title('Commercial Information')

    f_attributes = st.sidebar.multiselect('Enter columns', data.columns)

    f_zipcode = st.sidebar.multiselect(
        'Enter zipcode',
        data['zipcode'].unique())

    # ============== Writing features ================== #
    st.write(f_attributes)
    st.write(f_zipcode)

    st.title('Data overview')
    if (f_zipcode != []) & (f_attributes != []):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

    elif (f_zipcode == []) & (f_attributes != []):
        data = data.loc[:, f_attributes]

    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), :]

    else:
        data = data.copy()

    st.dataframe(data)

    # ========================= Relevants metrics ===================== #
    st.title('Relevant Metrics')
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    average = pd.DataFrame(num_attributes.apply(np.mean))
    median = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))

    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    df1 = pd.concat([max_, min_, average, median, std], axis=1).reset_index()
    df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

    st.dataframe(df1)

    return None



if __name__ == "__main__":

# =========================================================================================================== #
    url = 'kc_house_data.csv'
    data = get_data(url)

# =========================================================================================================== #
    data = transformation(data)
    house_information(data)
    houses_map (data)
    commercial_attributes(data)
    data_overview(data)

# =========================================================================================================== #

# =========================================================================================================== #




















