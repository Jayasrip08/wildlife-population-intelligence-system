"""
Initialize database with demo users for testing.
Run this ONCE to set up the database.
"""
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from sqlalchemy.orm import Session
import database, models, auth, schemas

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Demo users with hashed passwords
DEMO_USERS = [
    {
        "username": "admin",
        "email": "admin@wildlife-intel.org",
        "password": "root",
        "role": "admin"
    },
    {
        "username": "researcher",
        "email": "researcher@wildlife-intel.org",
        "password": "root",
        "role": "researcher"
    },
    {
        "username": "officer",
        "email": "officer@wildlife-intel.org",
        "password": "root",
        "role": "conservation_officer"
    },
    {
        "username": "forest",
        "email": "forest@wildlife-intel.org",
        "password": "root",
        "role": "forest_department"
    }
]

def init_database():
    db = database.SessionLocal()
    try:
        for user_data in DEMO_USERS:
            # Check if user already exists
            existing = db.query(models.User).filter(
                models.User.username == user_data["username"]
            ).first()
            
            if not existing:
                # Create new user with hashed password
                hashed_pwd = auth.get_password_hash(user_data["password"])
                new_user = models.User(
                    username=user_data["username"],
                    email=user_data["email"],
                    hashed_password=hashed_pwd,
                    role=user_data["role"]
                )
                db.add(new_user)
                print(f"✅ Created user: {user_data['username']} ({user_data['role']})")
            else:
                print(f"⚠️  User already exists: {user_data['username']}")
        
        db.commit()
        print("\n✅ Database initialization complete!")
        print("\nYou can now login with:")
        for user in DEMO_USERS:
            print(f"  • {user['username']} / {user['password']} ({user['role']})")
            
    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
