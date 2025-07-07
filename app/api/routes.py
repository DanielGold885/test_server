from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.db.session import SessionLocal
from app.logger import logger

router = APIRouter()


# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/health")
def health_check():
    logger.info("GET /health called")
    return {"status": "ok"}


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"POST /users called for ID: {user.id}")

    existing = db.query(User).filter(User.id == user.id).first()
    if existing:
        logger.warning(f"User already exists: {user.id}")
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        id=user.id,
        name=user.name,
        phone=user.phone,
        address=user.address
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"User created successfully: {user.id}")
    return {
        "id": new_user.id,
        "name": new_user.name,
        "phone": new_user.phone,
        "address": new_user.address
    }


@router.get("/users/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    logger.info(f"GET /users/{user_id} called")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"User not found: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")

    logger.info(f"User fetched: {user.id}")
    return {
        "id": user.id,
        "name": user.name,
        "phone": user.phone,
        "address": user.address
    }


@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    logger.info("GET /users called")
    users = db.query(User).all()
    user_ids = [user.id for user in users]
    logger.info(f"Returning {len(user_ids)} user(s)")
    return user_ids
