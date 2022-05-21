# maxhof905

# gather se in the p.s. post scriptum corpus

import pandas as pd


# %%
# get 'se'
df = pd.read_csv('gathered_se_data/PS/postcriptum_se.txt')
df2 = df[df.word.str.contains('\\bse\\b', regex=True, na=False) & df.lemma.str.contains('\\bse\\b', regex=True, na=False)]
df2.to_csv('postcriptum_se_clean.txt', index=False)

# %%
# get stats
pt_total = df2[df2.lang == 'portuguese']
pt_P00CN000 = df2[(df2.lang == 'portuguese') & (df2.pos == str('P00CN000'))]
pt_VMIP3S0_P00CN000 = df2[(df2.lang == 'portuguese') & (df2.pos == str('VMIP3S0+P00CN000'))]
pt_VMN0000_P00CN000= df2[(df2.lang == 'portuguese') & (df2.pos == 'VMN0000+P00CN000')]
pt_PP0CN000 = df2[(df2.lang == 'portuguese') & (df2.pos == str('PP0CN000'))]
pt_PP3CN000 = df2[(df2.lang == 'portuguese') & (df2.pos == str('PP3CN000'))]
pt_PP3CNA00 = df2[(df2.lang == 'portuguese') & (df2.pos == str('PP3CNA00'))]
pt_PP3 = df2[(df2.lang == 'portuguese') & (df2.pos == str('PP3'))]
pt_CS = df2[(df2.lang == 'portuguese') & (df2.pos == str('CS'))]
pt_CSI = df2[(df2.lang == 'portuguese') & (df2.pos == str('CSI'))]

sp_total = df2[df2.lang == 'spanish']
sp_P00CN000 = df2[(df2.lang == 'spanish') & (df2.pos == str('P00CN000'))]
sp_VMIP3S0_P00CN000 = df2[(df2.lang == 'spanish') & (df2.pos == str('VMIP3S0+P00CN000'))]
sp_VMN0000_P00CN000= df2[(df2.lang == 'spanish') & (df2.pos == 'VMN0000+P00CN000')]
sp_PP0CN000 = df2[(df2.lang == 'spanish') & (df2.pos == str('PP0CN000'))]
sp_PP3CN000 = df2[(df2.lang == 'spanish') & (df2.pos == str('PP3CN000'))]
sp_PP3CNA00 = df2[(df2.lang == 'spanish') & (df2.pos == str('PP3CNA00'))]
sp_PP3 = df2[(df2.lang == 'spanish') & (df2.pos == str('PP3'))]
sp_CS = df2[(df2.lang == 'spanish') & (df2.pos == str('CS'))]
sp_CSI = df2[(df2.lang == 'spanish') & (df2.pos == str('CSI'))]

df_stats = pd.DataFrame({'spanish': [len(sp_P00CN000), len(sp_VMIP3S0_P00CN000), len(sp_VMN0000_P00CN000),
                                     len(sp_PP0CN000), len(sp_PP3CN000), len(sp_PP3CNA00), len(sp_PP3), len(sp_CS), len(sp_CSI), len(sp_total)],
                         'portuguese': [len(pt_P00CN000), len(pt_VMIP3S0_P00CN000), len(pt_VMN0000_P00CN000),
                                     len(pt_PP0CN000), len(pt_PP3CN000), len(pt_PP3CNA00), len(pt_PP3), len(pt_CS), len(pt_CSI), len(pt_total)],
                         'tags': ['P00CN000', 'VMIP3S0_P00CN000', 'VMN0000_P00CN000', 'PP0CN000', 'PP3CN000', 'PP3CNA00', 'PP3', 'CS', 'CSI', 'total']}).set_index('tags')



with open('gathered_se_data/PS/postscriptum_stats.txt', 'a') as outfile:
    outfile.write(df_stats.to_string())
