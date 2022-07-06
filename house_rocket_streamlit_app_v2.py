import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

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
# =========================================================================================================== #

def dashboard_func(data):

    st.write('Mostrando Overview Geral')
    st.markdown("***")

    #Big numbers
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Número total de imóveis", value=len(data['id'].unique()))
    col2.metric(label="Preço médio dos imóveis", value=data['price'].mean())
    col3.metric(label="Quantidade de casas com vista para água", value=len(data[data['waterfront']==1]))

    st.markdown("***")


    # Histograms
    st.title("Histogramas - Preço e Ano de Construção")
    fig, ax = plt.subplots()
    plt.subplot(1, 2, 1)
    sns.histplot(data=data, x="price", kde=True)

    plt.subplot(1, 2, 2)
    sns.histplot(data=data, x="yr_built", kde=True)

    st.pyplot(fig)

    st.markdown("***")

    # ============== Average per Year ================ #

    st.title('Average Price per Year')

    df = data[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    fig = px.line(df, x='yr_built', y='price')

    st.plotly_chart(fig, use_container_width=True)

    # ============== Average per Day ================ #

    st.markdown("***")

    st.title('Average Price per Day')

    data['date'] = pd.to_datetime(data['date'])
    df = data[['date', 'price']].groupby('date').mean().reset_index()

    fig = px.line(df, x='date', y='price')

    st.plotly_chart(fig, use_container_width=True)


    return None


def mapa_fuc(data):
    # ============== Título do mapa ============== #
    st.write("***")
    st.title('Localização dos imóveis')

    f_price_min = int(data['price'].min())
    f_price_max = int(data['price'].max())
    f_price_avg = int(data['price'].mean())

    f_price_slider = st.slider('Selecione o preço máximo dos imóveis que deseja visualizar: ',
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
    fig.update_layout(height=700, width=1000, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)


    return None



def overview_geral_func(data):



    st.sidebar.title('Informações comerciais')

    f_attributes = st.sidebar.multiselect('Selecione as colunas', data.columns)

    f_zipcode = st.sidebar.multiselect(
        'Zipcode',
        data['zipcode'].unique())

    f_id = st.sidebar.multiselect(
        'Id do imóvel',
        data['id'].unique())


    # ============== Writing features ================== #
    st.write("***")

    st.title('Overview dos dados')
    if (f_id != []) & (f_attributes != []):
        data_overview = data.loc[data['id'].isin(f_id), f_attributes]

    elif (f_id == []) & (f_attributes != []):
        data_overview = data.loc[:, f_attributes]

    elif (f_id != []) & (f_attributes == []):
        data_overview = data.loc[data['id'].isin(f_id), :]

    else:
        data_overview = data.copy()

    st.dataframe(data_overview)

    # ========================= Zipcode ===================== #
    st.write("***")

    st.title('Imóveis por zipcode e atributos selecionado')
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
    st.write("***")

    st.title('Métricas Estatísticas')
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
## HEADER ##
    st.title('House Rocket Dashboard')

    st.markdown('Análise dos imóveis')

# =========================================================================================================== #
    data = transformation(data)

    page = st.sidebar.selectbox('Selecione a visão que deseja: ',
                        ('Overview Geral', 'Mapa', 'Extração Geral'))
    st.title(page)

    if page == 'Overview Geral':
        dashboard_func(data)

    elif page == 'Mapa':
        mapa_fuc(data)

    else:
        overview_geral_func(data)