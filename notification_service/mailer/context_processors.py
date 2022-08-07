from .models import Message


def get_messages(request):
    param_distribution_id = int(str(request.get_full_path()).split('/')[-2])
    right_messages = Message.objects.filter(distribution_id=int(param_distribution_id))
    #right_messages = Message.objects.all()
    return {
       'messages': right_messages,
     }
