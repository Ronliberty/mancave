from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from user.models import CustomUser
from .serializers import MessageSerializer

@login_required
def manager_chart(request):
    conversation = Conversation.objects.filter(participants=request.user)
    return render(request, 'chart/manager_chart.html', {'conversation': conversation})

@login_required
def client_chart(request):
    conversation = Conversation.objects.filter(participants=request.user)
    return render(request, 'chart/client_chart.html', {'conversation':conversation})


@login_required
def select_participant(request):
    if request.user.is_manager():
        # Managers can select any user
        participants = CustomUser.objects.exclude(id=request.user.id)
    elif request.user.is_client():
        # Clients can only select managers
        participants = CustomUser.objects.filter(role='manager')
    else:
        return JsonResponse({'error': 'Unauthorized access'})

    return render(request, 'chart/select_participant.html', {'participants': participants})


def start_conversation(request, participant_id):
    participant = get_object_or_404(CustomUser, id=participant_id)

    # Clients can only start conversations with managers
    if request.user.is_client() and not participant.is_manager():
        return JsonResponse({'error': 'Clients can only start conversations with managers'}, status=403)

    # Check if conversation already exists
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=participant).first()
    if not conversation:
        # Create new conversation if none exists
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, participant)

    # Redirect to the conversation messages view
    return redirect('chart:conversation-messages', conversation_id=conversation.id)

@login_required
def conversation_messages(request, conversation_id):
    # Get the conversation based on the conversation_id
    conversation = get_object_or_404(Conversation, id=conversation_id)
    # Get messages related to this conversation
    messages = Message.objects.filter(conversation=conversation)  # Assuming you have a Message model

    # Render the messages in a template
    return render(request, 'chart/conversation_messages.html', {
        'conversation': conversation,
        'messages': messages,
    })
@api_view(['GET'])
def get_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse({'messages':serializer.data})

@api_view(['POST'])
def send_message(request, conversation_id):
    content = request.POST.get('content')  # Use request.POST to get form data in a standard Django view
    if content:
        message = Message.objects.create(content=content, sender=request.user, conversation_id=conversation_id)
        serializer = MessageSerializer(message)  # Fixed variable name from 'serializers' to 'serializer'
        return JsonResponse({'message': serializer.data})
    else:
        return JsonResponse({'success': False, 'error': 'No content provided'})






