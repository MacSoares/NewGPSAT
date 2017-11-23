from django import forms

from .models import Evaluation


class PostForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = (
            'nome',
            'idade',
            'sexo',
            'peso',
            'altura',
            'causaAmputacao',
            'tempoAmputacao',
            'tipoAmputacao',
            'sintomas',
            'medicacoes',
            'tratamentoFisioterapeuticoAnterior',
            'historicoPregresso',
            'condicaoDaPele',
            'temperaturaAlterada',
            'alteracaoDeUnhaEPelos',
            'alteracaoDeCorDaPele',
            'sentibilidadeNaPele',
            'condicaoDaPele',
            'pulsosNaPele',
            'deformidades',
            'trofismo',
            'enfaixamento',
            'amplitudeDeMovimentoFlexao',
        )
