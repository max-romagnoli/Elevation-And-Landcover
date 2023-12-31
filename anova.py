import pandas as pd
from scipy.stats import f_oneway

HEATHLANDS = 700
PEATLANDS = 600
GRASSLAND = 500

data = pd.read_csv(r'C:\path\to\data')

print("Number of missing values for HEATHLANDS:", data['ELEVATION'][data['LANDCOVER_ID'] == HEATHLANDS].isnull().sum())
print("Number of missing values for PEATLANDS:", data['ELEVATION'][data['LANDCOVER_ID'] == PEATLANDS].isnull().sum())
print("Number of missing values for GRASSLAND:", data['ELEVATION'][data['LANDCOVER_ID'] == GRASSLAND].isnull().sum())


data['ELEVATION'] = data.groupby('LANDCOVER_ID')['ELEVATION'].transform(lambda x: x.fillna(x.mean()))

result_anova = f_oneway(data['ELEVATION'][data['LANDCOVER_ID'] == HEATHLANDS],
                        data['ELEVATION'][data['LANDCOVER_ID'] == PEATLANDS],
                        data['ELEVATION'][data['LANDCOVER_ID'] == GRASSLAND])

print("ANOVA F-statistic:", result_anova.statistic)
print("ANOVA p-value:", result_anova.pvalue)

alpha = 0.05
if result_anova.pvalue < alpha:
    print("Reject the null hypothesis. There are significant differences in mean elevation.")
else:
    print("Fail to reject the null hypothesis. No significant differences in mean elevation.")