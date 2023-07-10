from fastapi import APIRouter
from app.controller.buzzword_controller import BuzzwordControllerInstance


mainRouter = APIRouter()


@mainRouter.get('/')
def hello():
    return "hi!"


@mainRouter.get('/buzzword', tags=['idx'])
def getBuzzword():
    return BuzzwordControllerInstance.getRecentBuzzword()


@mainRouter.post('/buzzword')
def updateBuzzword():
    return BuzzwordControllerInstance.updateRecentBuzzword()