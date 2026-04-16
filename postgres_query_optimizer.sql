CREATE INDEX idx_vehicle_time ON telemetry(vehicle_id, timestamp DESC);

EXPLAIN ANALYZE
SELECT * FROM telemetry
WHERE vehicle_id = 'VH001'
ORDER BY timestamp DESC LIMIT 100;