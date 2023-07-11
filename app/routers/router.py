from fastapi import APIRouter
from app.controller.buzzword_controller import BuzzwordControllerInstance


buzzwordRouter = APIRouter(prefix='/buzzword')



@buzzwordRouter.get('')
def getBuzzword(idx: int):
    return BuzzwordControllerInstance.getRecentBuzzword(idx)


@buzzwordRouter.post('')
def updateBuzzword():
    return BuzzwordControllerInstance.updateRecentBuzzword()