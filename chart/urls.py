from django.urls import path
from .views import manager_chart, client_chart, get_messages, send_message, select_participant, start_conversation, conversation_messages

app_name = 'chart'
urlpatterns = [
    path('manager/chart/', manager_chart, name='manager-chart'),
    path('client/chart', client_chart, name='client-chart'),
    path('select-participant/', select_participant, name='select-participant'),
    path('start-conversation/<int:participant_id>/', start_conversation, name='start-conversation'),
    path('api/messages/<int:conversation_id>/', get_messages, name='get-messages'),
    path('api/messages/send/<int:conversation_id', send_message, name='send-messages'),
    path('conversation/<int:conversation_id>/', conversation_messages, name='conversation-messages'),  # New URL pattern
]
