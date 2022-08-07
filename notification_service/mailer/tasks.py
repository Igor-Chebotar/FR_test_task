from rest_framework import status
import requests

from secret_data import TOKEN
from .models import Client, Message, Distribution
from notification_service.celery import app
from datetime import datetime



@app.task
def distribution_send_function(data):
    d_tag = data['tag']
    d_operator_code = data['operator_code']
    d_msg_text = str(data['msg_text'])
    d_id = data['id']
    start_time = data['datetime_start']
    finish_time = data['datetime_finish']
    distribution = Distribution.objects.filter(id=d_id).first()
    right_clients = Client.objects.filter(operator_code=d_operator_code).filter(tag=d_tag[0])
    for client in right_clients:
        if not (start_time <= str(datetime.now()) < finish_time):
            break
        if len(Message.objects.filter(distribution_id=distribution).filter(client_id=client)) != 0:
            continue
        c_id = client.id
        number = int(str(client.phone_number)[1::])
        now_dt = datetime.now()
        msg = Message(datetime=now_dt, distribution_id=distribution, client_id=client, sent=False)
        msg.save()
        m_id = msg.id
        url = f"https://probe.fbrq.cloud/v1/send/{m_id}"
        message_data = {'id': m_id,
                        'phone': number,
                        'text': d_msg_text}
        header_params = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + TOKEN,
            'Content-Type': 'application/json'
        }
        response = requests.post(url,
                                 data=message_data,
                                 headers=header_params)
        if response.status_code == status.HTTP_200_OK:
            msg.sent = True

        msg.save()


@app.task
def distribution_check():
    distributions = Distribution.objects.all()
    for el in distributions:
        data = {
            'datetime_start': el.datetime_start,
            'msg_text': el.msg_text,
            'operator_code': el.operator_code,
            'tag': el.tag,
            'datetime_finish': el.datetime_finish
        }
        distribution_send_function.delay(data)

