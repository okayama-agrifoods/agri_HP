from django import forms
from .models import NippoModel
from bootstrap_datepicker_plus.widgets import DatePickerInput
#from bootstrap_datepicker_plus import DatePickerInput
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
# Django設定をimport
from django.conf import settings


class NippoModelForm(forms.ModelForm):
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )

    class Meta:          
        model = NippoModel
        exclude = ["user"]


        #fields = "__all__"

    def __init__(self, user=None,*args, **kwargs):
        for key, field in self.base_fields.items():
            if key != "public":
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs["class"] = "form-check-input"
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        nippo_obj = super().save(commit=False)
        if self.user:
            nippo_obj.user = self.user
        if commit:
            nippo_obj.save()
        return nippo_obj
        
class NippoFormClass(forms.Form):
    title = forms.CharField(label="タイトル", widget=forms.TextInput(attrs={'placeholder':'タイトル...'}))
    content = forms.CharField(label="内容",widget=forms.Textarea(attrs={'placeholder':'内容...'}))

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)



class ContactForm(forms.Form):
    # フォーム項目として"お名前"を定義
    name = forms.CharField(
        label='名前(必須)',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "例）テスト太郎",
        }),
    )
    # フォーム項目として"お名前"を定義
    kana = forms.CharField(
        label='フリガナ(必須)（※全角カタカナでご入力ください。）',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "例）テストタロウ",
        }),
    )
    # フォーム項目として"会社名"を定義
    org_name = forms.CharField(
        label='組織名称(必須)（※個人様は「個人」とご入力ください。）',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "例）岡山アグリフーズ",

        }),
    )

    # フォーム項目として"電話番号"を定義
    phone = forms.CharField(
        label='電話番号（必須）',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "例）080-1234-5678",
        }),
    )

    # フォーム項目として"メールアドレス"を定義
    mail = forms.EmailField(
        label='メールアドレス（必須）',
        #label = "",
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "例）info@example.com",
        }),
    )
    # フォーム項目として"お問い合わせ内容"を定義
    inq2 = forms.CharField(
        label='お問い合わせ内容（必須）',
        #label = "",
        max_length=1025,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容をご入力ください。",
        }),
    )
    # メールを送信する
    def send_email(self):
        subject = '岡山アグリフーズへの問い合わせ'
        name = self.cleaned_data['name']
        email = self.cleaned_data['mail']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        # 受信者リストを指定
        recipient_list = [settings.EMAIL_HOST_USER]

        msg = "\n 名前："            + self.cleaned_data['name']  + \
              "\n \n フリガナ："     + self.cleaned_data['kana']  + \
              "\n \n 組織名称："           + self.cleaned_data['org_name'] + \
              "\n \n 電話番号："         + self.cleaned_data['phone'] + \
              "\n \n メールアドレス："   + self.cleaned_data['mail']  + \
              "\n \n お問い合わせ内容："   + self.cleaned_data['inq2']
        try:
            send_mail(subject, msg, from_email, recipient_list)
            
        except BadHeaderError:
           
            return HttpResponse("無効なヘッダが検出されました。")
        
