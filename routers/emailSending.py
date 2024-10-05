from fastapi import FastAPI,status,HTTPException,Depends,APIRouter
from schemas import GettingValues
from utils import sendEmail
router = APIRouter(tags=["Email"])


@router.get("/try", status_code=status.HTTP_200_OK)
async def test():
    return "Hello World"


@router.get("/SendEmail", status_code=status.HTTP_201_CREATED)
async def send_Email(payload: GettingValues = Depends(GettingValues)):
    data = [float(i) for i in payload.values.split(",")]
    ph_value:float = data[0]
    waterLevel:float = data[1]
    ldrValue: float = data[2]
    humid: float = data[3]
    temperature: float = data[4]

    if ph_value < 6 or ph_value > 7:
        
        sendEmail(["vj.pablo03@gmail.com", "victorbernabe87@gmail.com"], "Alert! Problem with Water", 
                  f"Ph Sensor Value:{ph_value}.The Water Quality is dirty. Please change it now!")
    if temperature > 40:
        sendEmail(["vj.pablo03@gmail.com", "victorbernabe87@gmail.com"], "The temperature is not normal", 
                  f"Make sure the temperature is complementary for the chicks")
   
    if humid < 55:
        humText = f"Temperatue Value:{temperature}. The humidity is not normal. Make sure the humidity is complementary for the chick"
        sendEmail(["vj.pablo03@gmail.com", "victorbernabe87@gmail.com"], "The temperature is not normal", 
                  humText)
    if waterLevel == 0:
        waterText = "The water level is low. Please Refill it."
        sendEmail(["vj.pablo03@gmail.com", "victorbernabe87@gmail.com"], "No more water!", 
                  waterText)
    if ldrValue < 11:
        foodText = "There are no food for the chicken. Please Kindly refill it"
        sendEmail(["vj.pablo03@gmail.com", "victorbernabe87@gmail.com"], "Alert! No Food for the chicken", foodText)

    return "Done"
