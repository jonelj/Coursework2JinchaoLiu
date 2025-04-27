import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. load data
df = pd.read_csv('Results_21Mar2022.csv')

# 2. order by age group
age_list = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
df_age = df[df['age_group'].isin(age_list)]
df_age['age_group'] = pd.Categorical(df_age['age_group'], categories=age_list, ordered=True)

# 3. create 2 views for displaying
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12), sharey=True)

# 4. dipict the third pics by violin ploting
for i, age in enumerate(age_list[:3]):
    ax = axes[0, i]
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
    ax.set_ylabel("Mean GHG Emissions (kg)" if i == 0 else "")
    ax.tick_params(axis='x', rotation=45)
    ax.get_legend().remove()

# 5. dipict last few pics by box ploting
for i, age in enumerate(age_list[3:]):
    ax = axes[1, i]  # 第二行
    age_data = df_age[df_age['age_group'] == age]

    sns.boxplot(
        data=age_data,
        x='diet_group',
        y='mean_ghgs',
        hue='sex',
        palette={'male': '#ADD8E6', 'female': 'pink'},
        ax=ax
    )
    ax.set_title(f"Age {age} (Box Plot)")
    ax.set_xlabel("Diet Group")
    ax.set_ylabel("Mean GHG Emissions (kg)" if i == 0 else "")
    ax.tick_params(axis='x', rotation=45)
    ax.get_legend().remove()

# 6. add the legends
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, title='Sex', loc='upper right', bbox_to_anchor=(1.1, 0.9))

# 7. the title
fig.suptitle(
    "Comparative Analysis of GHG Emissions: Disaggregated by Gender, Sex, Age\n"
    "Comparative Analysis of GHG Emissions: Disaggregated by Gender, Sex, Age",
    fontsize=16,
    y=1.02
)

plt.tight_layout()
plt.savefig('GHG_Emissions.png')
plt.show()
