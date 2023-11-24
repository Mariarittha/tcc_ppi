from django import forms
from .models import Produtos, hospede, filomenas, estadia

class ProdutosForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome do Produto",
        })
    )
    preco = forms.FloatField(
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Preço",
        })
    )
    imagem = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
        })
    )
    descricao_produto = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Descrição do Produto",
        })
    )

    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'imagem', 'descricao_produto']


class HospedeForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome do Hóspede",
        })
    )
    profissao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Profissão",
        })
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
        })
    )
    idade = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Idade",
        })
    )
    imagem_perfil = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
        }),
        required=False,
    )

    class Meta:
        model = hospede
        fields = ['nome', 'profissao', 'email', 'idade', 'imagem_perfil']


class FilomenasForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome",
        })
    )
    idade = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Idade",
        })
    )
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Descrição",
        })
    )
    imagem_filo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
        }),
        required=False,
    )

    class Meta:
        model = filomenas
        fields = ['nome', 'idade', 'descricao', 'imagem_filo']


class EstadiaForm(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
        }),
        required=False,
    )
    duracao = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Duração",
        })
    )
    nome_estadia = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome da Estadia",
        })
    )
    descricao_estadia = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Descrição da Estadia",
        })
    )
    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Localização",
        })
    )
    valor = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Valor",
        })
    )
    programacao = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Programação",
        })
    )

    class Meta:
        model = estadia
        fields = ['imagem', 'duracao', 'nome_estadia', 'descricao_estadia', 'localizacao', 'valor', 'programacao']
