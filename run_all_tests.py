import sys
import os
import subprocess

print("==========================================================================")
print("     WILDLIFE POPULATION INTELLIGENCE SYSTEM - ALL VERIFICATION TESTS")
print("==========================================================================")

print("\n--- 1. RUNNING BIOMETRIC RE-ID TRUE POSITIVE & TRUE NEGATIVE SUITE ---")
res1 = subprocess.run([sys.executable, "test_reid_discrimination.py"], capture_output=True, text=True)
print(res1.stdout)
if res1.returncode != 0:
    print(res1.stderr)
    sys.exit(1)

print("\n--- 2. RUNNING DEEP SECURITY, JWT LIFECYCLE & RATE LIMITING SUITE ---")
res2 = subprocess.run([sys.executable, "test_security_e2e.py"], capture_output=True, text=True)
print(res2.stdout)
if res2.returncode != 0:
    print(res2.stderr)
    sys.exit(1)

print("\n--- 3. RUNNING GBIF LIVE API & CORE SYSTEM METRICS SUITE ---")
res3 = subprocess.run([sys.executable, "test_suite.py"], capture_output=True, text=True)
print(res3.stdout)
if res3.returncode != 0:
    print(res3.stderr)
    sys.exit(1)

print("\n==========================================================================")
print("  ALL 3 TEST SUITES PASSED 100%! SYSTEM FULLY VERIFIED & PRODUCTION READY.")
print("==========================================================================")
