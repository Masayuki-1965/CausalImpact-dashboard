import pandas as pd
from datetime import date, timedelta

def get_period_defaults(session_state, dataset):
    period_defaults = session_state.get('period_defaults', {})
    pre_start = period_defaults.get('pre_start', dataset['ymd'].min().date())
    pre_end = period_defaults.get('pre_end', dataset['ymd'].max().date())
    post_start = period_defaults.get('post_start', dataset['ymd'].min().date())
    post_end = period_defaults.get('post_end', dataset['ymd'].max().date())
    return pre_start, pre_end, post_start, post_end

def validate_periods(pre_end_date, post_start_date):
    """
    介入前期間の終了日と介入期間の開始日の整合性をチェック
    """
    if pre_end_date is not None and post_start_date is not None and post_start_date <= pre_end_date:
        return False, f"⚠ 分析期間の設定エラー：介入期間の開始日（{post_start_date}）は、介入前期間の終了日（{pre_end_date}）より後の日付を指定してください。"
    return True, ""

def calc_period_days(pre_start_date, pre_end_date, post_start_date, post_end_date):
    """
    期間の日数を計算（エラー時はNone返却）
    """
    try:
        pre_days = (pre_end_date - pre_start_date).days + 1
        post_days = (post_end_date - post_start_date).days + 1
        return pre_days, post_days
    except Exception:
        return None, None

def build_analysis_params(alpha, seasonality, seasonality_type, custom_period, prior_level_sd, standardize, niter):
    seasonality_period = None
    if seasonality:
        if seasonality_type == "週次 (7日)":
            seasonality_period = 7
        elif seasonality_type == "旬次 (10日)":
            seasonality_period = 10
        elif seasonality_type == "月次 (30日)":
            seasonality_period = 30
        elif seasonality_type == "四半期 (90日)":
            seasonality_period = 90
        elif seasonality_type == "年次 (365日)":
            seasonality_period = 365
        else:  # カスタム
            seasonality_period = custom_period if custom_period is not None else 7
    return {
        'alpha': alpha,
        'seasonality': seasonality,
        'seasonality_period': seasonality_period,
        'prior_level_sd': prior_level_sd,
        'standardize': standardize,
        'niter': niter
    } 