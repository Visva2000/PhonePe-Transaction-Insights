import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page config
st.set_page_config(page_title="PhonePe Insights Dashboard", layout="wide")
st.title("📊 PhonePe Insights Dashboard")

# Use Case Dropdown
use_case = st.selectbox(
    "Select a Use Case",
    ("Use Case 1.0: Transaction Growth",
     "Use Case 1.1: QuarterGrowthStateWise",
     "Use Case 1.2: Top Performing States",
     "Use Case 1.3: Top Performing Districts",
     "Usecase 2: Top Device Brand By Total Registered Users",
     "Usecase 3.1: Total Insurance Transactions Per state",
     "Usecase 3.2: Low Insurance States",
     "Usecase 5.1: Maximum registered User statewise",
     "Usecase 5.2: State With High User But Low Engagement",
     "Use Case 5.3: Brandwise User Engagement Statewise Comparison",
     "Use Case 6.1: Average Insurance Amount Per Policy",
     "Usecase 6.2: Insurance Product Diversity Per State",
     "Use Case 9: Underperforming States (Users vs Insurance)",
     "India Map TransactionCount Per State"
     )
)

# -------- Use Case 1.0 --------
if use_case == "Use Case 1.0: Transaction Growth":
    st.header("Top States Transaction Growth")
    df1 = pd.read_csv("TopSatesTransactionGrowth_UC1.csv")
    

    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    sns.barplot(data=df1, x='State', y='total_transaction_Count', palette='viridis', ax=axes[0], ci=None)
    axes[0].set_title("Transaction Count by State")
    axes[0].tick_params(axis='x', rotation=45)

    sns.barplot(data=df1, x='State', y='total_transaction_Amount', palette='magma', ax=axes[1], ci=None)
    axes[1].set_title("Transaction Amount by State")
    axes[1].tick_params(axis='x', rotation=45)

    st.pyplot(fig)
    st.dataframe(df1)
    
# -------- Use Case 1.1 --------
elif use_case == "Use Case 1.1: QuarterGrowthStateWise":
    # st.header("QuarterGrowthStateWise")
    QuarterGrowth = pd.read_csv("QuarterGrowth_UC1.csv") 

    QuarterGrowth['Quarter_Label'] = QuarterGrowth['Year'].astype(str) + "-Q" + QuarterGrowth['Quarter'].astype(str)

    st.title("📈 State-wise Quarterly Transaction % Growth")

    selected_state = st.selectbox("Select a State", QuarterGrowth['State'].unique())

    state_data = QuarterGrowth[QuarterGrowth['State'] == selected_state].copy()

    fig, ax = plt.subplots(figsize=(16, 6))

    import plotly.express as px
    fig = px.line(
        x=state_data['Quarter_Label'],
        y=state_data['percentage_growth'],
        markers=True,
        labels={'x': 'Quarter_Label', 'y': 'Percentage Growth (%)'},
        title=f"{selected_state} - Quarterly Transaction % Growth"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(state_data)
    
# -------- Use Case 1.2 --------
elif use_case == "Use Case 1.2: Top Performing States":
    # st.header("Top Performing States")
    TopPerformingStates = pd.read_csv("TopPerformingStates_UC1.csv")  # or use your in-memory df

    st.title("Top Performing States Transactions")

    # Dropdown for selecting state
    selected_state = st.selectbox("Total Transaction Details",("Total Transaction Count per State","Total Transaction Amount per State"))

    if selected_state == "Total Transaction Count per State":
        
        fig, ax = plt.subplots(figsize=(16, 6))
        sns.barplot(data=TopPerformingStates, x='State', y='total_transaction_count',hue='State', ci=None, ax=ax)
        ax.set_title("Top Performing States Transaction Count")
        ax.set_xlabel("State")
        ax.set_ylabel("Total Transaction Count")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        st.dataframe(TopPerformingStates[["State","total_transaction_count"]])

    elif selected_state == "Total Transaction Amount per State":
        
        fig, ax = plt.subplots(figsize=(16, 6))
        sns.barplot(data=TopPerformingStates, x='State', y='total_transaction_amount',hue='State', ci=None, ax=ax)
        ax.set_title("Top Performing States Transaction Amount")
        ax.set_xlabel("State")
        ax.set_ylabel("Total Transaction Amount")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        st.dataframe(TopPerformingStates[["State","total_transaction_amount"]])


# -------- Use Case 1.3 --------
elif use_case == "Use Case 1.3: Top Performing Districts":

    TopPerformingDistricts = pd.read_csv("TopPerformingDistricts_UC1.csv")  # or use your in-memory df
    
    TopPerformingDistricts['State_District'] = TopPerformingDistricts['State'].astype(str) + "-" + TopPerformingDistricts['District'].astype(str)


    st.title("Top Performing Districts Transactions")

    # Dropdown for selecting district
    selected_district = st.selectbox("Total Transaction Details",("Total Transaction Count per District","Total Transaction Amount per District"))

    if selected_district == "Total Transaction Count per District":
        
        fig, ax = plt.subplots(figsize=(16, 6))
        sns.barplot(data=TopPerformingDistricts, x='State_District', y='total_transaction_count',hue='State_District', ci=None, ax=ax)
        ax.set_title("Top Performing Districts Transaction Count")
        ax.set_xlabel("State - District")
        ax.set_ylabel("Total Transaction Count")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        st.dataframe(TopPerformingDistricts[["State_District","total_transaction_count"]])

    elif selected_district == "Total Transaction Amount per District":
        fig, ax = plt.subplots(figsize=(16, 6))
        sns.barplot(data=TopPerformingDistricts, x='State_District', y='total_transaction_amount',hue='State_District', ci=None, ax=ax)
        ax.set_title("Top Performing Districts Transaction Amount")
        ax.set_xlabel("State - District")
        ax.set_ylabel("Total Transaction Amount")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        st.dataframe(TopPerformingDistricts[["State_District","total_transaction_amount"]])

# -------- Use Case 2 --------
elif use_case == "Usecase 2: Top Device Brand By Total Registered Users":
    st.header("Top Device Brand By Total Registered Users")
    df2 = pd.read_csv("TopDeviceBrandsByTotalRegisteredUser_UC2.csv")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
    data=df2, 
    x='State', 
    y='total_registered_user',
    palette='viridis',
    hue='Brand',
    ci=None
    )

    plt.title("Registered Users by Device Brand and State", fontsize=14)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Registered Users", fontsize=12)
    plt.legend(title='Device Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
    st.pyplot(fig)
    st.dataframe(df2)
    
# -------- Use Case 3 --------
elif use_case=="Usecase 3.1: Total Insurance Transactions Per state":
    st.header("Total Insurance Transactions Per state")
    df3=pd.read_csv("TotalInsuranceTransactionsPerState_UC3.csv")
    
    fig=plt.figure(figsize=(12,6))
    sns.barplot(
        data=df3,
        x='total_insurance_count',
        y='total_insurance_amount',
        hue='State',
        ci=None,
        palette='viridis'
    )
    
    plt.title("Total Insurance Transactions Per State", fontsize=14)
    plt.xlabel("Insurance Count",fontsize=12)
    plt.ylabel("Insurance Amount", fontsize=12)
    plt.legend(title='State',loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=5,frameon=True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.dataframe(df3)

# -------- Use Case 3 --------
elif use_case=="Usecase 3.2: Low Insurance States":
    st.header("Low Insurance States")
    df3=pd.read_csv("LowInsuranceStates_UC3.csv")
    
    fig=plt.figure(figsize=(16,8))
    sns.barplot(
        data=df3,
        x='total_users',
        y='total_insurance_transactions',
        hue='State',
        ci=None
    )
    
    plt.title("Insurance Trend", fontsize=14)
    plt.xlabel("Total Users", fontsize=12)
    plt.ylabel("Total Insurance Transactions", fontsize=12)
    plt.legend(title='State', bbox_to_anchor=(1.05, 1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.dataframe(df3)
    
#-------Use Case 5--------

elif use_case == "Usecase 5.1: Maximum registered User statewise":
    st.header("Maximum registered User statewise")
    df5 = pd.read_csv("MaximumRegisteredUserStateWise_UC5.csv")
    plot_type = st.selectbox("Select a plot", ("Bar Plot", "Line Plot"))
    if plot_type == "Bar Plot":
        fig= plt.figure(figsize=(16, 8))
        sns.barplot(
            data=df5,
            x='State', 
            y='total_registered_users', 
            hue='State',
            ci=None
        )

        plt.title("Highest Number of Registered Users per State State", fontsize=14)
        plt.xlabel("State", fontsize=12)
        plt.ylabel("Total Registered Users", fontsize=12)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()
        st.pyplot(fig)
        st.dataframe(df5)
    else:
        fig = px.line(
            df5,
            x='State',
            y='total_registered_users',
            markers=True,
            labels={'x': 'State', 'y': 'Total Registered Users'},
            title="Highest Number of Registered Users per State"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df5)

elif use_case == "Usecase 5.2: State With High User But Low Engagement":
    st.header("State With High User But Low Engagement")
    df5 = pd.read_csv("StateWithHighUserButLowEngagement_UC5.csv")
    
    fig = px.line(
        x=df5['total_users'],
        y=df5['avg_engagement_percentage'],
        markers=True,
        labels={'x': 'Total Registered Users', 'y': 'Average Engagement Percentage'},
        title=f"State-wise User Base vs Engagement %"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df5)
    
# -------- Use Case 5.3 --------
elif use_case == "Use Case 5.3: Brandwise User Engagement Statewise Comparison":
    st.header("Brandwise User Engagement Statewise Comparison")
    
    df5 = pd.read_csv("BrandWiseUserEngagementStateWise_UC5.csv")

    selected_state = st.selectbox("Select a State", df5['State'].unique())

    # Filter data for selected state
    state_data = df5[df5['State'] == selected_state].copy()

    fig, ax = plt.subplots(figsize=(16, 6))
    
 
    fig = px.line(
        x=state_data['Brand'],
        y=state_data['avg_engagement_percentage'],
        markers=True,
        labels={'x': 'Brand', 'y': 'Average Engagement Percentage'},
        title=f"{selected_state} - Brandwise User Engagement"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(state_data)
    
# -------- Use Case 6 --------
elif use_case == "Use Case 6.1: Average Insurance Amount Per Policy":
    st.header("Average Insurance Amount Per Policy")
    
    df6 = pd.read_csv("AvgAmountPerPolicy_UC6.csv")

    fig = plt.figure(figsize=(18, 8))
    sns.barplot(
        data=df6,
        x='State',
        y='avg_amount_per_policy',
        hue='State',
        ci=None
    )

    plt.title("Average Insurance Amount Per Policy by State", fontsize=14)
    plt.xlabel("State", fontsize=11)
    plt.ylabel("avg_amount_per_policy", fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()
    st.pyplot(fig)
    st.dataframe(df6)
    
#-------Use Case 6.2--------

elif use_case == "Usecase 6.2: Insurance Product Diversity Per State":
    st.header("Insurance Product Diversity Per State")
    df6 = pd.read_csv("ProductDiversity_UC6.csv")
    plot_type = st.selectbox("Select a plot", ("Bar Plot", "Line Plot"))
    if plot_type == "Bar Plot":
        fig=plt.figure(figsize=(18, 8))
        sns.barplot(
            data=df6,
            x='State',
            y='unique_insurance_products',
            hue='State',
            ci=None
        )

        plt.title("Unique Insurance Products", fontsize=14)
        plt.xlabel("State", fontsize=11)
        plt.ylabel("unique_insurance_products", fontsize=12)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()
        st.pyplot(fig)
        st.dataframe(df6)
    else:
        fig = px.line(
            df6,
            x='State',
            y='unique_insurance_products',
            markers=True,
            labels={'x': 'State', 'y': 'unique_insurance_products'},
            title="Unique Insurance Products"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df6)
        
# -------- Use Case 9 --------
elif use_case == "Use Case 9: Underperforming States (Users vs Insurance)":
    st.header("Underperforming States")
    
    df9 = pd.read_csv("UnderPerformingState_UC9.csv")

    fig = plt.figure(figsize=(18, 8))
    sns.barplot(
        data=df9,
        x='total_users',
        y='total_insurance_transactions',
        hue='State',
        ci=None
    )

    plt.title("UnderPerforming State (User vs Insurance)", fontsize=14)
    plt.xlabel("Total Users", fontsize=11)
    plt.ylabel("Total Insurance Transactions", fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.dataframe(df9)
    
# -------- India Map --------
elif use_case == "India Map TransactionCount Per State":
       
    
    df_map = pd.read_csv("TopPerformingStates_UC1_Completed.csv")

    # Title
    st.header("Transaction Count Per State")

    # Load the India GeoJSON URL
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

    # Create Choropleth map
    fig = px.choropleth(
        df_map,
        geojson=geojson_url,
        featureidkey="properties.ST_NM",
        locations="State",
        color="total_transaction_count",
        color_continuous_scale="Reds",
        title="Total Transactions by State"
    )

    fig.update_geos(fitbounds="locations", visible=False)

    # Show map in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Optional: Display Data
    st.dataframe(df_map)