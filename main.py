# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.475486Z","iopub.execute_input":"2022-12-11T20:26:23.476460Z","iopub.status.idle":"2022-12-11T20:26:23.482205Z","shell.execute_reply.started":"2022-12-11T20:26:23.476412Z","shell.execute_reply":"2022-12-11T20:26:23.481336Z"}}
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import streamlit as st

sns.set_theme()
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# %% [markdown]
st.markdown("""Let's consider our dataset ->""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.489830Z","iopub.execute_input":"2022-12-11T20:26:23.490509Z","iopub.status.idle":"2022-12-11T20:26:23.553275Z","shell.execute_reply.started":"2022-12-11T20:26:23.490470Z","shell.execute_reply":"2022-12-11T20:26:23.551554Z"}}
df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# %% [markdown]
st.markdown("""Great! Now 'df' variable takes the value of our dataset. Let's get print it out""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.695077Z","iopub.execute_input":"2022-12-11T20:26:23.695507Z","iopub.status.idle":"2022-12-11T20:26:23.736102Z","shell.execute_reply.started":"2022-12-11T20:26:23.695470Z","shell.execute_reply":"2022-12-11T20:26:23.734637Z"}}
st.markdown("""df""")

# %% [markdown]
st.markdown("""Let's find out the number of rows and columns, respectively**""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.737949Z","iopub.execute_input":"2022-12-11T20:26:23.738330Z","iopub.status.idle":"2022-12-11T20:26:23.745369Z","shell.execute_reply.started":"2022-12-11T20:26:23.738296Z","shell.execute_reply":"2022-12-11T20:26:23.744310Z"}}
st.markdown("""rows, columns""")
df.shape()

# %% [markdown]
st.markdown("""Using the info() command we can get more detailed information about each column""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.765115Z","iopub.execute_input":"2022-12-11T20:26:23.765800Z","iopub.status.idle":"2022-12-11T20:26:23.786317Z","shell.execute_reply.started":"2022-12-11T20:26:23.765760Z","shell.execute_reply":"2022-12-11T20:26:23.785014Z"}}
df.info()

# %% [markdown]
st.markdown("""Using describe command we will generate descriptive statistics**""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:23.979537Z","iopub.execute_input":"2022-12-11T20:26:23.980040Z","iopub.status.idle":"2022-12-11T20:26:24.034087Z","shell.execute_reply.started":"2022-12-11T20:26:23.979999Z","shell.execute_reply":"2022-12-11T20:26:24.033097Z"}}
df.describe()

# %% [markdown]
st.markdown("""Сommand isnull().sum() will help us refine how accurate our data is by displaying the total number of missing parameters""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:24.141170Z","iopub.execute_input":"2022-12-11T20:26:24.141986Z","iopub.status.idle":"2022-12-11T20:26:24.158985Z","shell.execute_reply.started":"2022-12-11T20:26:24.141947Z","shell.execute_reply":"2022-12-11T20:26:24.157692Z"}}
df.isnull().sum()

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:24.542610Z","iopub.execute_input":"2022-12-11T20:26:24.543280Z","iopub.status.idle":"2022-12-11T20:26:24.568711Z","shell.execute_reply.started":"2022-12-11T20:26:24.543225Z","shell.execute_reply":"2022-12-11T20:26:24.567341Z"}}
df.corr()

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:24.603698Z","iopub.execute_input":"2022-12-11T20:26:24.604960Z","iopub.status.idle":"2022-12-11T20:26:25.395482Z","shell.execute_reply.started":"2022-12-11T20:26:24.604913Z","shell.execute_reply":"2022-12-11T20:26:25.394301Z"}}
fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
sns.heatmap(df.corr(), vmax=.8, square=True, annot=True)
plt.title('Confusion Matrix', fontsize=15);

# %% [markdown]
st.markdown("""Let's check how many times it occurs each year since 2010""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:25.397637Z","iopub.execute_input":"2022-12-11T20:26:25.398008Z","iopub.status.idle":"2022-12-11T20:26:25.416704Z","shell.execute_reply.started":"2022-12-11T20:26:25.397973Z","shell.execute_reply":"2022-12-11T20:26:25.415337Z"}}
st.markdown("""'2010 -', len(df[df['Year_of_Release'] == 2010])""")
st.markdown("""'2011 -', len(df[df['Year_of_Release'] == 2011])""")
st.markdown("""'2012 -', len(df[df['Year_of_Release'] == 2012])""")
st.markdown("""'2013 -', len(df[df['Year_of_Release'] == 2013])""")
st.markdown("""'2014 -', len(df[df['Year_of_Release'] == 2014])""")
st.markdown("""'2015 -', len(df[df['Year_of_Release'] == 2015])""")
st.markdown("""'2016 -', len(df[df['Year_of_Release'] == 2016])""")
st.markdown("""'2017 -', len(df[df['Year_of_Release'] == 2017])""")
st.markdown("""'2018 -', len(df[df['Year_of_Release'] == 2018])""")
st.markdown("""'2019 -', len(df[df['Year_of_Release'] == 2019])""")
st.markdown("""'2020 -', len(df[df['Year_of_Release'] == 2020])""")

# %% [markdown]
st.title("DS CLeanup")

# %% [markdown]
st.markdown("""Based on the fact that during the initial study of the dataset, we identified a huge number of missing values in the parameters: *'Critic_Score','Critic_Count','User_Score', 'User_Count', 'Developer', 'Rating'""")
#
st.markdown("""Let's delete them in order to prevent inaccuracy of the data.""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:25.418837Z","iopub.execute_input":"2022-12-11T20:26:25.419310Z","iopub.status.idle":"2022-12-11T20:26:25.447616Z","shell.execute_reply.started":"2022-12-11T20:26:25.419244Z","shell.execute_reply":"2022-12-11T20:26:25.446459Z"}}
df.drop(df[['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']], axis=1, inplace=True)
df.head(5)

# %% [markdown]
st.markdown("""It is also worth noting that the data for 2017-2020 is almost empty. let's remove them.""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:33:57.478562Z","iopub.execute_input":"2022-12-11T20:33:57.479043Z","iopub.status.idle":"2022-12-11T20:33:57.524962Z","shell.execute_reply.started":"2022-12-11T20:33:57.479008Z","shell.execute_reply":"2022-12-11T20:33:57.523778Z"}}
df = df[df.Year_of_Release != 2017]
df = df[df.Year_of_Release != 2018]
df = df[df.Year_of_Release != 2019]
df = df[df.Year_of_Release != 2020]
st.markdown("""df""")

# %% [markdown]
st.title("DS Transformation")

# %% [markdown]
st.markdown("""Let's add each country's sales ratio""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:25.897222Z","iopub.execute_input":"2022-12-11T20:26:25.897852Z","iopub.status.idle":"2022-12-11T20:26:25.935075Z","shell.execute_reply.started":"2022-12-11T20:26:25.897810Z","shell.execute_reply":"2022-12-11T20:26:25.933850Z"}}
df = df.assign(NA_Sales_ratio=df.NA_Sales / df.Global_Sales)
df = df.assign(EU_Sales_ratio=df.EU_Sales / df.Global_Sales)
df = df.assign(JP_Sales_ratio=df.JP_Sales / df.Global_Sales)
df = df.assign(Other_Sales_ratio=df.Other_Sales / df.Global_Sales)

df.head(5)

# %% [markdown]
st.title("DS Vizualisation")

# %% [markdown]
st.markdown("""After all changes, we have significantly changed our dataset. Let's take a look at it""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:26.160163Z","iopub.execute_input":"2022-12-11T20:26:26.161522Z","iopub.status.idle":"2022-12-11T20:26:26.187861Z","shell.execute_reply.started":"2022-12-11T20:26:26.161477Z","shell.execute_reply":"2022-12-11T20:26:26.186568Z"}}
df.head(10)

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:26.190270Z","iopub.execute_input":"2022-12-11T20:26:26.190774Z","iopub.status.idle":"2022-12-11T20:26:27.117492Z","shell.execute_reply.started":"2022-12-11T20:26:26.190711Z","shell.execute_reply":"2022-12-11T20:26:27.116513Z"}}
fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
sns.heatmap(df.corr(), vmax=.8, square=True, annot=True)
plt.title('Confusion Matrix', fontsize=15);
st.plotly_chart(fig)

# %% [markdown]
st.markdown("""Let's take a closer look at our dataset by visualizing it using a few simple graphs""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:27.119338Z","iopub.execute_input":"2022-12-11T20:26:27.119727Z","iopub.status.idle":"2022-12-11T20:26:27.139059Z","shell.execute_reply.started":"2022-12-11T20:26:27.119692Z","shell.execute_reply":"2022-12-11T20:26:27.137526Z"}}
sum_counts = df['Platform'].value_counts()[:10]
fig = go.Figure()
pull = [0] * len(sum_counts)
pull[sum_counts.tolist().index(sum_counts.max())] = 0.2
fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, pull=pull, hole=0.9))

fig.update_layout(
    annotations=[dict(text='Top 10 Publishers', x=0.5, y=0.5, font_size=20, showarrow=False)])
fig.show()
st.plotly_chart(fig)

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:27.140352Z","iopub.execute_input":"2022-12-11T20:26:27.140782Z","iopub.status.idle":"2022-12-11T20:26:27.272454Z","shell.execute_reply.started":"2022-12-11T20:26:27.140744Z","shell.execute_reply":"2022-12-11T20:26:27.271319Z"}}
fig = px.histogram(data_frame=df,
                   x="Genre",
                   color_discrete_sequence=px.colors.sequential.Plasma,
                   template="plotly_white",
                   title="Company Size")

fig.update_layout(yaxis_title="Amount of Companies",
                  xaxis_title="Company Size",
                  xaxis={"categoryorder": "total descending"})
st.plotly_chart(fig)

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:27.274817Z","iopub.execute_input":"2022-12-11T20:26:27.275192Z","iopub.status.idle":"2022-12-11T20:26:27.667547Z","shell.execute_reply.started":"2022-12-11T20:26:27.275159Z","shell.execute_reply":"2022-12-11T20:26:27.666062Z"}}
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df["Year_of_Release"],
             color="blue",
             kde=True,
             bins=25)
plt.title("Games Published Anually", fontsize=15, y=1)
ax.set_xlabel("Year", fontsize=15);
ax.set_ylabel("Count", fontsize=15);
st.plotly_chart(fig)

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:27.669237Z","iopub.execute_input":"2022-12-11T20:26:27.670535Z","iopub.status.idle":"2022-12-11T20:26:27.904548Z","shell.execute_reply.started":"2022-12-11T20:26:27.670488Z","shell.execute_reply":"2022-12-11T20:26:27.903314Z"}}
years = set(df['Year_of_Release'])
fund_by_year = {}
for year in sorted(years):
    fund_by_year[year] = df[df['Year_of_Release'] == year]['Global_Sales'].sum()
fig = px.line(x=fund_by_year.keys(),
              y=fund_by_year.values(),
              labels={'x': 'Year', 'y': 'Total Sales in millions of Units'},
              color_discrete_sequence=["Blue"])
fig.show()
st.plotly_chart(fig)
# %% [markdown]
st.markdown("""There significant differences in sales of games on the same platform in different countries?""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:27.906181Z","iopub.execute_input":"2022-12-11T20:26:27.907417Z","iopub.status.idle":"2022-12-11T20:26:28.319837Z","shell.execute_reply.started":"2022-12-11T20:26:27.907370Z","shell.execute_reply":"2022-12-11T20:26:28.318557Z"}}
toplam_platform_NA_EU_JP = df.groupby(['Platform'])[["NA_Sales", "EU_Sales", "JP_Sales"]].sum().reset_index()
a = toplam_platform_NA_EU_JP[["NA_Sales", "EU_Sales", "JP_Sales"]] / toplam_platform_NA_EU_JP[["NA_Sales", "EU_Sales", "JP_Sales"]].sum()

plat_sum = df[["Platform"]]
plat_sum = plat_sum.groupby(["Platform"]).size().reset_index()

deneme = pd.concat([a, plat_sum["Platform"]], axis=1)

plt.figure(figsize=(20, 10))
line = sns.lineplot(data=deneme,
                    x="Platform",
                    y="NA_Sales",
                    marker="o",
                    label="NA_Sales")

line = sns.lineplot(data=deneme,
                    x="Platform",
                    y="EU_Sales",
                    marker="o",
                    label="EU_Sales")

line = sns.lineplot(data=deneme,
                    x="Platform",
                    y="JP_Sales",
                    marker="o",
                    label="JP_Sales")

line.set(xticks=deneme.Platform.values)
line.set(ylabel="Percent of Sales")
plt.show()
st.plotly_chart(fig)

# %% [markdown]
st.markdown("""By paying attention to the given graph, we can say with confidence that the demand for different platforms varies depending on the country.""")

# %% [markdown]
st.markdown("""Let's form another hypothesis. Does Role-playing sells best in Japan?""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:28.321571Z","iopub.execute_input":"2022-12-11T20:26:28.322039Z","iopub.status.idle":"2022-12-11T20:26:28.638312Z","shell.execute_reply.started":"2022-12-11T20:26:28.322001Z","shell.execute_reply":"2022-12-11T20:26:28.637208Z"}}
toplam_genre_NA_EU_JP = df.groupby(['Genre'])[["NA_Sales", "EU_Sales", "JP_Sales"]].sum().reset_index()
toplam_genre = toplam_genre_NA_EU_JP[["NA_Sales", "EU_Sales", "JP_Sales"]] / toplam_genre_NA_EU_JP[["NA_Sales", "EU_Sales", "JP_Sales"]].sum()

genre_sum = df[["Genre"]]
genre_sum = genre_sum.groupby(["Genre"]).size().reset_index()

genre_sales = pd.concat([toplam_genre,
                         genre_sum["Genre"]],
                        axis=1)

plt.figure(figsize=(20, 10))
line = sns.lineplot(data=genre_sales,
                    x="Genre",
                    y="NA_Sales",
                    marker="o",
                    label="NA_Sales")

line = sns.lineplot(data=genre_sales,
                    x="Genre",
                    y="EU_Sales",
                    marker="o",
                    label="EU_Sales")

line = sns.lineplot(data=genre_sales,
                    x="Genre",
                    y="JP_Sales",
                    marker="o",
                    label="JP_Sales")

line.set(xticks=genre_sales.Genre.values)
line.set(ylabel="Percent of Sales")
plt.show()
st.plotly_chart(fig)

# %% [markdown]
st.markdown("""Visualizing the data, we can clearly see that role-playing is the dominant category in japan""")

st.markdown("""Action is the most popular genre in Japan?""")

# %% [code] {"execution":{"iopub.status.busy":"2022-12-11T20:26:28.640004Z","iopub.execute_input":"2022-12-11T20:26:28.641222Z","iopub.status.idle":"2022-12-11T20:26:29.016560Z","shell.execute_reply.started":"2022-12-11T20:26:28.641170Z","shell.execute_reply":"2022-12-11T20:26:29.015378Z"}}
data_8 = df.loc[:, ['Year_of_Release', 'Genre']]

dummy_genre = pd.get_dummies(data_8['Genre'])

data_8 = pd.concat([data_8,
                    dummy_genre],
                   axis=1)

data_8 = data_8.groupby('Year_of_Release').sum()

colors = [plt.cm.Spectral(i) for i in np.linspace(0, 1, 12)]

plot_8 = data_8.plot.line(figsize=(19, 8),
                          color=colors,
                          linewidth=2,
                          fontsize=20)

plot_8.set_ylabel('Number of game released',
                  fontsize=15)

plot_8.set_xlabel('Year',
                  fontsize=15)

plot_8.set_title("Games Released between 1980-2016 by genres",
                 fontsize=20)
st.plotly_chart(fig)

st.markdown("""looking at the graph, we can say with confidence, yes""")
