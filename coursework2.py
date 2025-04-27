import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. load data
df = pd.read_csv('Results_21Mar2022.csv')

# 2. sort by age
age_list = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
df_age = df[df['age_group'].isin(age_list)]
df_age['age_group'] = pd.Categorical(df_age['age_group'], categories=age_list, ordered=True)

# ===================== violin =====================
fig1, axes1 = plt.subplots(nrows=2, ncols=3, figsize=(18, 12), sharey=True)
for i, age in enumerate(age_list):
    row, col = i // 3, i % 3
    ax = axes1[row, col]
    age_data = df_age[df_age['age_group'] == age]

    sns.violinplot(
        data=age_data,
        x='diet_group',
        y='mean_ghgs',
        hue='sex',
        palette={'male': '#ADD8E6', 'female': 'pink'},
        inner='quartile',
        split=True,
        ax=ax
    )
    ax.set_title(f"Age {age} (Violin Plot)")
    ax.set_xlabel("Diet Group")
    ax.set_ylabel("Mean GHG (kg)" if col == 0 else "")
    ax.tick_params(axis='x', rotation=45)
    ax.get_legend().remove()

# add legends
handles, labels = axes1[0, 0].get_legend_handles_labels()
fig1.legend(handles, labels, title='Sex', loc='upper right', bbox_to_anchor=(1.1, 0.9))
fig1.suptitle("GHG Emissions by Age/Diet/Sex (Violin Plots)", fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('GHG_Emissions_Violin.png', bbox_inches='tight', dpi=300)
plt.close()

# ===================== box =====================
fig2, axes2 = plt.subplots(nrows=2, ncols=3, figsize=(18, 12), sharey=True)
for i, age in enumerate(age_list):
    row, col = i // 3, i % 3
    ax = axes2[row, col]
    age_data = df_age[df_age['age_group'] == age]

    sns.boxplot(
        data=age_data,
        x='diet_group',
        y='mean_watuse',
        hue='sex',
        palette={'male': '#ADD8E6', 'female': 'pink'},
        ax=ax
    )
    ax.set_title(f"Age {age} (Box Plot)")
    ax.set_xlabel("Diet Group")
    ax.set_ylabel("Mean Water Use in cubic meters" if col == 0 else "")
    ax.tick_params(axis='x', rotation=45)
    ax.get_legend().remove()

# add legends
handles, labels = axes2[0, 0].get_legend_handles_labels()
fig2.legend(handles, labels, title='Sex', loc='upper right', bbox_to_anchor=(1.1, 0.9))
fig2.suptitle("Water Use by Age/Diet/Sex (Box Plots)", fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('WaterUse_Box.png', bbox_inches='tight', dpi=300)
plt.close()