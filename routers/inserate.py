from fastapi import APIRouter, Query

from scrapers.inserate import get_inserate_klaz
from utils.browser import PlaywrightManager

router = APIRouter()


@router.get("/inserate")
async def get_inserate(query: str = Query(None),
                       location: str = Query(None),
                       radius: int = Query(None),
                       min_price: int = Query(None),
                       max_price: int = Query(None),
                       page_count: int = Query(1, ge=1, le=20),
                       category: str = Query(None),
                       min_rooms: int = Query(None),
                       max_rooms: int = Query(None),
                       min_size: int = Query(None),
                       max_size: int = Query(None),
                       status: str = Query(None, regex="^(active|sold|reserved|deleted)$")):
    browser_manager = PlaywrightManager()
    await browser_manager.start()
    try:
        results = await get_inserate_klaz(browser_manager, query, location, radius, min_price, max_price, page_count, category, min_rooms, max_rooms, min_size, max_size)
        if status:
            results = [result for result in results if result.get("status") == status]
        return {"success": True, "data": results}
    finally:
        await browser_manager.close()
