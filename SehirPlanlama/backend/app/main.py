from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import nufus, saglik, konut, ulasim

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nufus.router , prefix="/nufus" , tags=["Nüfus Dağılımı"])
app.include_router(saglik.router, prefix="/saglik", tags=["Sağlık Hizmetleri"])
app.include_router(konut.router , prefix="/konut" , tags=["Konut Orani"])
app.include_router(ulasim.router, prefix="/ulasim", tags=["Ulaşım"])
