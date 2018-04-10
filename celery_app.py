from celery import Celery
import os

if not os.environ["LOCAL"]:
    from config import ProductionConfig as config
else:
    from config import ProductionConfig as config

app = Celery(
    'LMNFlask',
    broker=config.BROKER_URL,
    backend=config.BROKER_URL,
    includes="tasks"
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
