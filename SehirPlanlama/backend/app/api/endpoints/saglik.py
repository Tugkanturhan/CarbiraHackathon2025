
from fastapi import APIRouter, HTTPException
from database.crud import crud     # import yolu senin proje adlarına göre değişebilir

router = APIRouter()
SECTION = "saglik"             # data.json içindeki anahtar

@router.get("/")
def get_nufus():
    return crud.get_section(SECTION)

@router.post("/")
def update_nufus(data: dict):
    return crud.update_section(SECTION, data)

@router.post("/add")
def add_nufus_item(item: dict):
    return crud.add_item(SECTION, item)

@router.put("/{index}")
def update_nufus_item(index: int, new_item: dict):
    try:
        return crud.update_item(SECTION, index, new_item)
    except IndexError:
        raise HTTPException(status_code=404, detail="İndeks bulunamadı")

@router.delete("/{index}")
def delete_nufus_item(index: int):
    try:
        return crud.delete_item(SECTION, index)
    except IndexError:
        raise HTTPException(status_code=404, detail="İndeks bulunamadı")
