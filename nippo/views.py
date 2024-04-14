from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (ListView 
                                  ,DetailView 
                                  ,FormView
                                 )
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import NippoModel
from .forms  import NippoFormClass, NippoModelForm
from django.urls import reverse, reverse_lazy,path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .filters import  NippoModelFilter
from accounts.models import Profile



def okayamaagrifoods(request): #クラス作成
    return render(request,"nippo/okayama-agrifoods.html")    
    
# forms.py からフォーム定義をimport
from .forms import ContactForm

# submitイベントの挙動を定義
class okayamaagrifoodscontact(FormView):
    # 表示させる html を指定
    template_name = 'nippo/okayama-agrifoodscontact.html'
    # form.py で定義したクラス名を指定
    form_class = ContactForm
    # 遷移後のurlを引数で指定
    success_url = reverse_lazy('okayama-agrifoodscontactresult')

    # メールを送信
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

def okayamaagrifoodscontactresult(request): #クラス作成
    return render(request,"nippo/okayama-agrifoodscontactresult.html")  