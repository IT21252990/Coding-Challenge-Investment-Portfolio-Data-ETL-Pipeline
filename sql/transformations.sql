INSERT INTO holdings
SELECT * FROM holdings_staging;

INSERT INTO portfolio_stats
SELECT * FROM portfolio_stats_staging;

CREATE VIEW portfolio_holdings_view AS
SELECT 
    h.business_date, 
    h.portfolio_id,
    h.security_id,
    h.exchange,
    h.quantity,
    h.market_value,
    h.currency,
    p.nav,
    p.daily_pnl,
    p.ytd_return,
    p.sharpe_ratio,
    p.volatility,
    p.var_95
FROM holdings h
JOIN portfolio_stats p ON h.business_date = p.business_date AND h.portfolio_id = p.portfolio_id

-- SELECT *  FROM holdings_staging
-- SELECT *  FROM portfolio_stats_staging
-- SELECT *  FROM holdings
-- SELECT *  FROM portfolio_stats

-- SELECT * FROM portfolio_holdings_view WHERE portfolio_id = 'PORT001';
