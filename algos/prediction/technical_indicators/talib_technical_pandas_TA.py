# https://github.com/twopirllc/pandas-ta
import numpy as np
import pandas as pd
import pandas_ta as ta

from Utils import UtilsL


def get_all_pandas_TA_tecnical(df_ta, cos_cols=None):
    # https://github.com/twopirllc/pandas-ta#available-metrics

    ### Cycles (1)
    # Even Better Sinewave: ebsw
    if cos_cols is None or "cycl_EBSW_40_10" in cos_cols:
        df_ta.ta.ebsw(prefix="cycl", cumulative=True, append=True)

    ### Momentum (41)
    # Awesome Oscillator: ao
    if cos_cols is None or "mtum_AO_5_34" in cos_cols:
        df_ta.ta.ao(prefix="mtum", cumulative=True, append=True)
    # Bias: bias
    if cos_cols is None or "mtum_BIAS_SMA_26" in cos_cols:
        df_ta.ta.bias(prefix="mtum", cumulative=True, append=True)
    # BRAR: brar
    if cos_cols is None or "mtum_AR_26" or "mtum_BR_26" in cos_cols:
        df_ta.ta.brar(prefix="mtum", cumulative=True, append=True)
    # Chande Forecast Oscillator: cfo
    if cos_cols is None or "mtum_CFO_9" in cos_cols:
        df_ta.ta.cfo(prefix="mtum", cumulative=True, append=True)
    # Center of Gravity: cg
    if cos_cols is None or "mtum_CG_10" in cos_cols:
        df_ta.ta.cg(prefix="mtum", cumulative=True, append=True)
    # Correlation Trend Indicator: cti
    if cos_cols is None or "mtum_CTI_12" in cos_cols:
        df_ta.ta.cti(prefix="mtum", cumulative=True, append=True)
    # Directional Movement: dm
    if cos_cols is None or "mtum_DMP_14" or "mtum_DMN_14" in cos_cols:
        df_ta.ta.dm(prefix="mtum", cumulative=True, append=True)
    # Efficiency Ratio: er
    if cos_cols is None or "mtum_ER_10" in cos_cols:
        df_ta.ta.er(prefix="mtum", cumulative=True, append=True)
    # Elder Ray Index: eri
    if cos_cols is None or "mtum_BULLP_13" or "mtum_BEARP_13" in cos_cols:
        df_ta.ta.eri(prefix="mtum", cumulative=True, append=True)
    # Fisher Transform: fisher
    if cos_cols is None or "mtum_FISHERT_9_1" or "mtum_FISHERTs_9_1" in cos_cols:
        df_ta.ta.fisher(prefix="mtum", cumulative=True, append=True)
    # Inertia: inertia
    if cos_cols is None or "mtum_INERTIA_20_14" in cos_cols:
        df_ta.ta.inertia(prefix="mtum", cumulative=True, append=True)
    # KDJ: kdj
    if cos_cols is None or "mtum_K_9_3" in cos_cols or "mtum_D_9_3" in cos_cols or "mtum_J_9_3" in cos_cols:
        df_ta.ta.kdj(prefix="mtum", cumulative=True, append=True)
    # Pretty Good Oscillator: pgo
    if cos_cols is None or "mtum_PGO_14" in cos_cols:
        df_ta.ta.pgo(prefix="mtum", cumulative=True, append=True)
    # Psychological Line: psl
    if cos_cols is None or "mtum_PSL_12" in cos_cols:
        df_ta.ta.psl(prefix="mtum", cumulative=True, append=True)
    # Percentage Volume Oscillator: pvo
    if cos_cols is None or "mtum_PVO_12_26_9" in cos_cols or "mtum_PVOh_12_26_9" in cos_cols or "mtum_PVOs_12_26_9" in cos_cols:
        df_ta.ta.pvo(prefix="mtum", cumulative=True, append=True)
    # Quantitative Qualitative Estimation: qqe
    if cos_cols is None or "mtum_QQE_14_5_4236_RSIMA" in cos_cols or "mtum_QQEl_14_5_4236" in cos_cols or "mtum_QQEs_14_5_4236" in cos_cols:
        df_ta.ta.qqe(prefix="mtum", cumulative=True, append=True)
    # Relative Strength Xtra: rsx
    if cos_cols is None or "mtum_RSX_14" in cos_cols:
        df_ta.ta.rsx(prefix="mtum", cumulative=True, append=True)
    # Schaff Trend Cycle: stc
    if cos_cols is None or "mtum_STC_10_12_26_05" in cos_cols or "mtum_STCmacd_10_12_26_05" in cos_cols or "mtum_STCstoch_10_12_26_05" in cos_cols:
        df_ta.ta.stc(prefix="mtum", cumulative=True, append=True)
    # SMI Ergodic smi
    if cos_cols is None or "mtum_SMI_5_20_5" in cos_cols or "mtum_SMIs_5_20_5" in cos_cols or "mtum_SMIo_5_20_5" in cos_cols:
        df_ta.ta.smi(prefix="mtum", cumulative=True, append=True)
    # TD Sequential: td_seq No me gusta el resultado , se usara otro en   TD Sequential ichimucu.py
    # df.ta.td_seq(prefix="mtum", cumulative=True, append=True)

    ### Overlap (33)
    # Arnaud Legoux Moving Average: alma
    if cos_cols is None or "olap_ALMA_10_60_085" in cos_cols:
        df_ta.ta.alma(prefix="olap", cumulative=True, append=True)
    # Holt-Winter Moving Average: hwma
    if cos_cols is None or "olap_HWMA_02_01_01" in cos_cols:
        df_ta.ta.hwma(prefix="olap", cumulative=True, append=True)
    # Jurik Moving Average: jma
    if cos_cols is None or "olap_JMA_7_0" in cos_cols:
        df_ta.ta.jma(prefix="olap", cumulative=True, append=True)
    # McGinley Dynamic: mcgd
    if cos_cols is None or "olap_MCGD_10" in cos_cols:
        pd.options.mode.chained_assignment = None
        df_ta.ta.mcgd(prefix="olap", cumulative=True, append=True)
        pd.options.mode.chained_assignment = 'warn'
    # Pascal's Weighted Moving Average: pwma
    if cos_cols is None or "olap_PWMA_10" in cos_cols:
        df_ta.ta.pwma(prefix="olap", cumulative=True, append=True)
    # Sine Weighted Moving Average: sinwma
    if cos_cols is None or "olap_SINWMA_14" in cos_cols:
        df_ta.ta.sinwma(prefix="olap", cumulative=True, append=True)
    # Ehler's Super Smoother Filter: ssf
    if cos_cols is None or "olap_SSF_10_2" in cos_cols:
        df_ta.ta.ssf(prefix="olap", cumulative=True, append=True)
    # Symmetric Weighted Moving Average: swma
    if cos_cols is None or "olap_SWMA_10" in cos_cols:
        df_ta.ta.swma(prefix="olap", cumulative=True, append=True)
    # Volume Weighted Average Price: vwap
    if cos_cols is None or "olap_VMAP" in cos_cols:
        df_ta = __calculation_volume_weighted_avg_price(df_ta, "olap_VMAP")
    #No funciona {AttributeError}'RangeIndex' object has no attribute 'to_period'  df_ta.ta.vwap(prefix="olap", cumulative=True, append=True, anchor = "D")
    # Volume Weighted Moving Average: vwma
    if cos_cols is None or "olap_VWMA_10" in cos_cols:
        df_ta.ta.vwma(prefix="olap", cumulative=True, append=True)

    ### Performance (3)
    # Draw Down: drawdown   It does not exist
    # df_ta.ta.drawdown(prefix="perf", cumulative=True, append=True)
    # Log Return: log_return
    if cos_cols is None or "perf_CUMLOGRET_1" in cos_cols:
        df_ta.ta.log_return(prefix="perf", cumulative=True, append=True)
    # Percent Return: percent_return
    if cos_cols is None or "perf_CUMPCTRET_1" in cos_cols:
        df_ta.ta.percent_return(prefix="perf", cumulative=True, append=True)
    if cos_cols is None or "perf_z_30_1" in cos_cols:
        df_ta["perf_z_30_1"] = df_ta.ta.cdl_z(prefix="ta")["ta_close_Z_30_1"]
    if cos_cols is None or "perf_ha" in cos_cols:
        df_ta["perf_ha"] = df_ta.ta.ha(prefix="ta")["ta_HA_close"]

    ### Statistics (11)
    # Entropy: entropy
    if cos_cols is None or "sti_ENTP_10" in cos_cols:
        df_ta.ta.entropy(prefix="sti", cumulative=True, append=True)
    # Kurtosis: kurtosis
    if cos_cols is None or "sti_KURT_30" in cos_cols:
        df_ta.ta.kurtosis(prefix="sti", cumulative=True, append=True)
    # Think or Swim Standard Deviation All: tos_stdevall
    if cos_cols is None or "sti_TOS_STDEVALL_LR" in cos_cols or "sti_TOS_STDEVALL_L_1" in cos_cols or "sti_TOS_STDEVALL_U_1" in cos_cols or "sti_TOS_STDEVALL_L_2" in cos_cols or "sti_TOS_STDEVALL_U_2" in cos_cols or "sti_TOS_STDEVALL_L_3" in cos_cols or "sti_TOS_STDEVALL_U_3" in cos_cols:
        df_ta.ta.tos_stdevall(prefix="sti", cumulative=True, append=True)
    # Z Score: zscore
    if cos_cols is None or "sti_ZS_30" in cos_cols:
        df_ta.ta.zscore(prefix="sti", cumulative=True, append=True)

    ### Trend (18)
    # Formally: linear_decay
    if cos_cols is None or "tend_LDECAY_5" in cos_cols:
        df_ta.ta.decay(prefix="tend", cumulative=True, append=True)
    # Parabolic Stop and Reverse: psar
    if cos_cols is None or "tend_PSARl_002_02" in cos_cols or "tend_PSARs_002_02" in cos_cols or "tend_PSARaf_002_02" in cos_cols or "tend_PSARr_002_02" in cos_cols:
        df_ta.ta.psar(prefix="tend", cumulative=True, append=True)


    # Trend Signals: tsignals
    if cos_cols is None or "tend_tsignals" in cos_cols:
        df_ta.ta.tsignals(prefix="tend", cumulative=True, append=True)
    # Vertical Horizontal Filter: vhf
    if cos_cols is None or "tend_VHF_28" in cos_cols:
        df_ta.ta.vhf(prefix="tend", cumulative=True, append=True)
    # Cross Signals: xsignals
    if cos_cols is None or "tend_signals" in cos_cols:
        df_ta.ta.xsignals(prefix="tend", cumulative=True, append=True)

    ### Volatility (14)
    # Holt-Winter Channel: hwc
    if cos_cols is None or "vola_HWM" in cos_cols or "vola_HWU" in cos_cols or "vola_HWL" in cos_cols:
        df_ta.ta.hwc(prefix="vola", cumulative=True, append=True)
    # Keltner Channel: kc
    if cos_cols is None or "vola_KCLe_20_2" or "vola_KCBe_20_2" in cos_cols or "vola_KCUe_20_2" in cos_cols:
        df_ta.ta.kc(prefix="vola", cumulative=True, append=True)
    # Relative Volatility Index: rvi
    if cos_cols is None or "vola_RVI_14" in cos_cols:
        df_ta.ta.rvi(prefix="vola", cumulative=True, append=True)
    # Elder's Thermometer: thermo
    if cos_cols is None or "vola_THERMO_20_2_05" in cos_cols or "vola_THERMOma_20_2_05" in cos_cols or "vola_THERMOl_20_2_05" in cos_cols or "vola_THERMOs_20_2_05" in cos_cols:
        df_ta.ta.thermo(prefix="vola", cumulative=True, append=True)
    # True Range: true_range
    if cos_cols is None or "vola_TRUERANGE_1" in cos_cols:
        df_ta.ta.true_range(prefix="vola", cumulative=True, append=True)
    # Ulcer Index: ui
    if cos_cols is None or "vola_UI_14" in cos_cols:
        df_ta.ta.ui(prefix="vola", cumulative=True, append=True)

    ### Volume (15)
    # Elder's Force Index: efi
    if cos_cols is None or "volu_EFI_13" in cos_cols:
        df_ta.ta.efi(prefix="volu", cumulative=True, append=True)
    # Klinger Volume Oscillator: kvo tarda muchas filas en dar datos
    # df.ta.kvo(prefix="volu", cumulative=True, append=True)
    # Negative Volume Index: nvi
    if cos_cols is None or "volu_NVI_1" in cos_cols:
        df_ta.ta.nvi(prefix="volu", cumulative=True, append=True)
    # Positive Volume Index: pvi
    if cos_cols is None or "volu_PVI_1" in cos_cols:
        df_ta.ta.pvi(prefix="volu", cumulative=True, append=True)
    # Price-Volume: pvol
    if cos_cols is None or "volu_PVOL" in cos_cols:
        df_ta.ta.pvol(prefix="volu", cumulative=True, append=True)
    # Price Volume Rank: pvr
    if cos_cols is None or "volu_PVR" in cos_cols:
        df_ta.ta.pvr(prefix="volu", cumulative=True, append=True)
    # Price Volume Trend: pvt
    if cos_cols is None or "volu_PVT" in cos_cols:
        df_ta.ta.pvt(prefix="volu", cumulative=True, append=True)
    # Volume Profile: vp solo da una fila
    # df.ta.vp(prefix="volu", cumulative=True, append=True)
    # result = ta.cagr(df.close)
    df_ta = df_ta.drop(columns=['mtum_QQE_14_5_4.236'], errors='ignore')
    for l in ['mtum_QQEl_14_5_4.236', 'mtum_QQEs_14_5_4.236', 'tend_PSARl_0.02_0.2', 'tend_PSARs_0.02_0.2']:
        if l in df_ta.columns:
            df_ta[l] = df_ta[l].replace(np.nan, 0)

    df_ta = UtilsL.replace_bat_chars_in_columns_name(df_ta, "")

    return df_ta


#Calculation of Volume Weighted Average Price
def __calculation_volume_weighted_avg_price(df, nom_col):
    df[nom_col] = np.cumsum(df['Volume'] * (df['High'] + df['Low']) / 2) / np.cumsum(df['Volume'])
    return df