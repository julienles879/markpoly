from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import JsonResponse


import random
from .models import *
from .forms import PlayerForm


class RandomNumberView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        random_number = random.randint(1, 6)
        return JsonResponse({'random_number': random_number})
    
class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = PlayerForm()
        players = Player.objects.all()[:6]
        show_add_button = len(players) < 6
        show_delete_all_button = len(players) >= 2

        topics = Topic.objects.all()

        selected_topic_id = request.GET.get('selected_topic')

        questions_for_topic = None
        marks_for_topic = None
        marks_for_topics = {} 

        if selected_topic_id:
            selected_topic = Topic.objects.get(pk=selected_topic_id)
            questions_for_topic = Question.objects.filter(mark__topic=selected_topic)
            marks_for_topic = Mark.objects.filter(topic=selected_topic)
            marks_for_topics = {selected_topic.id: marks_for_topic}

        return render(request, self.template_name, {
            'form': form,
            'players': players,
            'show_add_button': show_add_button,
            'show_delete_all_button': show_delete_all_button,
            'topics': topics,
            'selected_topic_id': selected_topic_id,
            'questions_for_topic': questions_for_topic,
            'marks_for_topic': marks_for_topic,
            'marks_for_topics': marks_for_topics,
            
        })

    def post(self, request, *args, **kwargs):
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        if 'delete_all_players' in request.POST:
            Player.objects.all().delete()
            return redirect('index')

        player_id = request.POST.get('delete_player')
        if player_id:
            Player.objects.filter(pk=player_id).delete()
            return redirect('index')

        return redirect('index')


class RulesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'rules.html')

class TopicDetailView(View):
    template_name = 'topic_detail.html'

    def get(self, request, *args, **kwargs):
        topic_id = kwargs.get('topic_id')
        
        if topic_id:
            topic = Topic.objects.get(pk=topic_id)
            marks = Mark.objects.filter(topic=topic)
            questions = Question.objects.filter(mark__topic=topic)

            # Organize data for rendering
            marks_with_questions = []
            for mark in marks:
                # Filter questions for the current mark
                mark_questions = questions.filter(mark=mark)
                marks_with_questions.append({'mark': mark, 'questions': mark_questions})

            return render(request, self.template_name, {
                'topic': topic,
                'marks_with_questions': marks_with_questions,
            })

        # Handle the case where no topic_id is provided
        # You may want to customize this based on your application's requirements
        return render(request, 'error.html', {'error_message': 'Topic not found'})