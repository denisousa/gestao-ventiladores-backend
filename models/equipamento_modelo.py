from config.db import db


class Equipamento(db.Document):
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO

    numero_ordem_servico = db.StringField(required=True, unique=True)

    foto_equipamento_chegada = db.StringField(
        unique=True)  # verificar se tem um tipo especifico para links, faz sentido ser único ?
    tipo = db.StringField(required=True)
    unidade_de_origem = db.StringField(required=True)
    numero_do_patrimonio = db.IntField(required=True,
                                       unique=True)  # verificar se é único mesmo, pois pelo o historico, pode existir varias vezes esse mesmo campo
    numero_de_serie = db.StringField(required=True,
                                     unique=True)  # verificar se é único mesmo, pois pelo o historico, pode existir varias vezes esse mesmo campo
    instituicao_de_origem = db.StringField(required=True)
    responsavel_contato_da_instituicao_de_origem = db.StringField(required=True)  # compo telefone é texto ou int ?
    estado_de_conservacao = db.StringField(required=True)
    marca = db.StringField(required=True)
    modelo = db.StringField(required=True)
    acessorios = db.StringField(required=True)
    foto_apos_limpeza = db.StringField(required=True)
    observacao = db.StringField()
    responsavel_pelo_preenchimento = db.StringField(
        unique=True)  # verificar se tem um tipo especifico para links, faz sentido ser único ?

    # FORMULARIO DE DIAGNOSTICO CLINICO
    acoes_avaliacao = db.ListField(db.DictField(), required=True)
    informar_os_resultados_do_teste = db.StringField()

    # FORMULARIO DE DIAGNOSTICO TECNICO

    defeito_observado = db.StringField()
    acoes_necessarias = db.StringField()
