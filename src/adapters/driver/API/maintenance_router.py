from fastapi import APIRouter, HTTPException
from loguru import logger

from migration.seed import seed_db

router = APIRouter(
    prefix="/maintenance",
    tags=["maintenance"],
)


@router.post("/seed_db", include_in_schema=False)
async def seed_db_api() -> bool:
    try:
        seed_db()
        return True
    except (ValueError, AttributeError) as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
