import logging
from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Optional
import json

from app.services.metric_data_service import MetricDataService
from app.schemas.metric_schema import MetricsData

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('metric_route_api_log')

router = APIRouter(
    tags=["Metric Data API"]
)

@router.get('/metrics', response_model=MetricsData, status_code=status.HTTP_200_OK)
def getMetricsData(start: Optional[str] = None, end: Optional[str] = None):
    try:
        dataservice = MetricDataService()
        data = dataservice.getAllMetricsData(start, end)
        return JSONResponse(jsonable_encoder(data))
    except Exception as e:
        logger.debug(f'Error in fetching metric data - {str(e)}')
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": f'Error in fetching metric dara - {str(e)}'})


@router.post('/addMetrics', status_code=status.HTTP_201_CREATED)
def postMetricsData(metric: MetricsData):
    try:
        payload = json.loads(metric.json())
        dataservice = MetricDataService()
        dataservice.postMetricsData(payload)
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content={"message": 'SUCCESS'})
    except Exception as e:
        logger.debug(f'Error in adding metric data - {str(e)}')
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": f'Error in adding metric dara - {str(e)}'})