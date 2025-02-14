CREATE TABLE IF NOT EXISTS holdings_staging (
    business_date DATE,
    portfolio_id VARCHAR(20),
    security_id VARCHAR(20),
    exchange VARCHAR(20),
    quantity NUMERIC,
    market_value NUMERIC,
    currency VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS portfolio_stats_staging (
    business_date DATE,
    portfolio_id VARCHAR(20),
    nav NUMERIC,
    daily_pnl NUMERIC,
    ytd_return NUMERIC,
    sharpe_ratio NUMERIC,
    volatility NUMERIC,
    var_95 NUMERIC
);

CREATE TABLE IF NOT EXISTS holdings (
    business_date DATE,
    portfolio_id VARCHAR(20),
    security_id VARCHAR(20),
    exchange VARCHAR(20),
    quantity NUMERIC,
    market_value NUMERIC,
    currency VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS portfolio_stats (
    business_date DATE,
    portfolio_id VARCHAR(20),
    nav NUMERIC,
    daily_pnl NUMERIC,
    ytd_return NUMERIC,
    sharpe_ratio NUMERIC,
    volatility NUMERIC,
    var_95 NUMERIC
);