from fastapi import APIRouter

from . import (
    auth,
    user,
    major_repairs,
    predict_events
)

router = APIRouter()

router.include_router(auth.router)
router.include_router(user.router)
router.include_router(major_repairs.router)
router.include_router(predict_events.router)
