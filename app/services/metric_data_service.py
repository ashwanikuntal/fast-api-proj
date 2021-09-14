import logging
from app.models import SessionLocal
from app.models.metric import Metric
from typing import Optional
from traceback import print_exc


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('metric_data_service_api_log')

class MetricDataService:

    def getAllMetricsData(self, start_date: Optional[str] = None, end_date: Optional[str] = None):
        db_session = SessionLocal()
        
        try:
            if start_date is not None and end_date is not None:
                query_result = db_session.query(Metric) \
                    .filter(Metric.created_time > start_date) \
                    .filter(Metric.created_time < end_date) \
                    .order_by(Metric.id.asc()).all()
            elif start_date is not None and end_date is None:
                query_result = db_session.query(Metric) \
                    .filter(Metric.created_time > start_date) \
                    .order_by(Metric.id.asc()).all()
            elif end_date is not None and start_date is None:
                query_result = db_session.query(Metric) \
                    .filter(Metric.created_time < end_date) \
                    .order_by(Metric.id.asc()).all()
            else:
                query_result = db_session.query(Metric) \
                    .order_by(Metric.id.asc()).all()
        
        except Exception as e:
            print_exc()
            logger.debug(f'Error in fetching metric data - {str(e)}')
            raise
        finally:
            db_session.close()

        return query_result


    def postMetricsData(self, payload):
        db_session = SessionLocal()
        
        try:
            metrics_data = payload['metric']

            for metric in metrics_data:
                metric_data = Metric()
                metric_data.created_time = metric.get('created_time')
                metric_data.voltage = metric.get('voltage')
                metric_data.current = metric.get('current')
                db_session.add(metric_data)

            db_session.flush()
            db_session.commit()
        except Exception as e:
            print_exc()
            logger.debug(f'Error in adding metric data to the table - {str(e)}')
            raise
        finally:
            db_session.close()
