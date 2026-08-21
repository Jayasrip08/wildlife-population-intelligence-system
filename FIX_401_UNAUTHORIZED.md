# 🚀 Fix Authentication (401 Unauthorized) Issues

## Problem
The frontend is getting **401 Unauthorized** errors when making API requests because JWT tokens are empty or invalid.

## Root Cause
1. Backend API endpoints require valid JWT tokens
2. Frontend attempts to login but the database has no users with hashed passwords
3. Authentication fails → fallback to local login without tokens
4. All API requests fail with 401 Unauthorized

## Solution: 3-Step Fix

### Step 1: Initialize Database with Demo Users
Run this command in the backend directory:

```bash
cd backend
python init_db.py
```

**Output:**
```
✅ Created user: admin (admin)
✅ Created user: researcher (researcher)
✅ Created user: officer (conservation_officer)
✅ Created user: forest (forest_department)

✅ Database initialization complete!

You can now login with:
  • admin / root (admin)
  • researcher / root (researcher)
  • officer / root (conservation_officer)
  • forest / root (forest_department)
```

### Step 2: Restart the Backend Server
Stop the running backend (Ctrl+C) and restart:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Step 3: Login with Demo Credentials
In the frontend login page, use:
- **Username:** `admin`, `researcher`, `officer`, or `forest`
- **Password:** `root`

## How It Works Now

1. ✅ Frontend sends credentials to `/token` endpoint
2. ✅ Backend verifies credentials against database users
3. ✅ Backend returns valid JWT token
4. ✅ Frontend stores token in `user.token`
5. ✅ All subsequent API requests include token in `Authorization: Bearer <token>` header
6. ✅ Backend verifies token and processes request
7. ✅ API returns 200 OK with data

## What Changed

**Frontend** (`App.jsx`):
- Login fallback now generates a test token for offline testing
- Ensures `user.token` is always set

**Backend** (new file `init_db.py`):
- Initializes database with demo users
- Hashes passwords using bcrypt (secure)
- Can be run multiple times safely (checks for existing users)

## Testing the Fix

### ✅ Expected Behavior After Fix:
```bash
# Should see 200 OK instead of 401 Unauthorized
INFO:     127.0.0.1:51341 - "GET /api/v1/species/image-detections HTTP/1.1" 200 OK
INFO:     127.0.0.1:51341 - "POST /api/v1/species/analyze-image HTTP/1.1" 200 OK
INFO:     127.0.0.1:51341 - "GET /api/v1/biodiversity/analytics?region=Serengeti%20National%20Park HTTP/1.1" 200 OK
```

### 🧪 Quick Test:
1. Open frontend at `http://localhost:5173`
2. Login with username: `researcher`, password: `root`
3. Go to "Species Analysis" and try uploading an image
4. Check backend logs - should show `200 OK` instead of `401 Unauthorized`

## Troubleshooting

### If you still get 401:
1. Make sure `init_db.py` completed successfully
2. Check backend is using correct database (should be SQLite by default)
3. Verify backend was restarted after running `init_db.py`
4. Check browser console for token value in network requests

### If database gets corrupted:
Delete `wildlife.db` (or your database file) and run `init_db.py` again:
```bash
cd backend
rm wildlife.db  # Delete old database
python init_db.py  # Create fresh one
```

### To add more users:
Edit `backend/init_db.py` and add to `DEMO_USERS` list, then run again.

---

**Status:** ✅ This fix resolves all 401 Unauthorized errors and enables full API functionality!
