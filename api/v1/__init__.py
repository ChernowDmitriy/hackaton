from fastapi import APIRouter

from . import (
    auth,
    user,
    predict_event
)

router = APIRouter()

router.include_router(auth.router)
router.include_router(user.router)
router.include_router(predict_event.router)
