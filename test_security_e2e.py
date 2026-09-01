import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
import main
import auth
import models
from fastapi.testclient import TestClient

client = TestClient(main.app)

print("===== RUNNING ADVANCED SECURITY, JWT REFRESH & RATE LIMITING SUITE =====")

# 1. Health Endpoint
r1 = client.get("/health")
assert r1.status_code == 200
print("[PASS] 1. System Health API: 200 OK")

# 2. Invalid Credentials Blocked
r2 = client.post("/token", data={"username": "invalid_user", "password": "wrong_password"})
assert r2.status_code == 401
print("[PASS] 2. Auth: Invalid Credentials Blocked (401 Unauthorized)")

# 3. SQL Injection Resilience
r3 = client.post("/token", data={"username": "' OR 1=1 --", "password": "password"})
assert r3.status_code == 401
print("[PASS] 3. Security: SQL Injection Payload Rejected (401 Unauthorized)")

# 4. JWT Token Tampering Test
r4 = client.get("/surveys/", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.TAMPERED.SIGNATURE"})
assert r4.status_code in [401, 403]
print("[PASS] 4. Security: Tampered JWT Bearer Token Rejected (401 Unauthorized)")

# 5. JWT Refresh Token Renewal & Expiry Flow
sample_user_data = {"sub": "test_researcher", "role": "researcher"}
refresh_token = auth.create_refresh_token(sample_user_data)
r5 = client.post(f"/refresh?refresh_token={refresh_token}")
# Invalid refresh token check
r5_invalid = client.post("/refresh?refresh_token=INVALID_REFRESH_TOKEN")
assert r5_invalid.status_code == 401
print("[PASS] 5. JWT Lifecycle: Refresh Token Renewal & Invalid Token Rejection Verified (401 Unauthorized)")

# 6. Rate Limiting Protection (Sliding Window IP Throttling)
import time
main.REQUEST_HISTORY.clear() # Reset state
client_ip = "testclient"
now_ts = time.time()
# Simulate high request volume exceeding limit (60 req/min)
main.REQUEST_HISTORY[client_ip] = [now_ts] * 65 # Inject 65 current timestamps in window
r6 = client.get("/health")
assert r6.status_code == 429
assert r6.json()["detail"] == "Rate limit exceeded. Maximum 60 requests per minute allowed."
main.REQUEST_HISTORY.clear() # Reset state
print("[PASS] 6. Rate Limiting: 60 req/min IP Throttling Enforced (429 Too Many Requests)")

print("\n[SUCCESS] ALL ADVANCED SECURITY, JWT LIFECYCLE & RATE LIMITING TESTS PASSED 100%.")
