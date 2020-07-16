from NetLab.celery import app
import time
import datetime

@app.task(bind=True)
def debug_task(self):
    print(self.request)
    # print('Request: {0!r}'.format(self.request))


@app.task(name="wait_5_seconds", bind=True)
def work_for_5_seconds(self):
    print(datetime.datetime.now().time())
    time.sleep(5)
    print(datetime.datetime.now().time())
