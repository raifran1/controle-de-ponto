from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Register
from django.views.generic import ListView


# Create your views here.
def tela_inicial(request):
    template_name = 'controle_de_ponto/tela_inicial.html'

    return render(request, template_name, {})


def cadastro_entrada(request):
    template_name = 'controle_de_ponto/cadastro_entrada.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                registro = Register.objects.get(rfid=form.cleaned_data['rfid'], horario_saida=None)
                messages.error(request, 'O funcionário já iniciou o expediente!')
            except:
                form.save()
                messages.success(request, 'Entrada registrada com sucesso!')

            return redirect('controle_de_ponto:tela_inicial')
        else:
            print(form.errors)

    form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def cadastro_saida(request):
    template_name = 'controle_de_ponto/cadastro_saida.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            try:
                registro = Register.objects.get(rfid=form.cleaned_data['rfid'], horario_saida=None)
                registro.horario_saida = form.cleaned_data['horario_saida']
                registro.servico = form.cleaned_data['servico']
                registro.save()
                messages.success(request, 'Saída cadastrada com sucesso!')
            except:
                messages.error(request, 'O funcionário não iniciou o expediente!')

            return redirect('controle_de_ponto:tela_inicial')
        else:
            print(form.errors)

    form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)


class listar_registros(ListView):
    model = Register
    paginate_by = 20
    page_kwarg = 'page'

    context_object_name = 'registros'
    template_name = 'controle_de_ponto/listar_registros.html'

    link_search = str()

    def get(self, request, *args, **kwargs):
        rfid = self.request.GET.get('rfid')

        search = {}

        # filtros para pesquisa
        if rfid:
            search['rfid'] = rfid
            self.link_search += '&rfid=' + rfid

        if request.GET:
            self.queryset = self.model.registros.search(search)

        return super(listar_registros, self).get(self, request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(listar_registros, self).get_context_data(
            count=self.model.objects.all().count(),
            link_search=self.link_search,
        )
