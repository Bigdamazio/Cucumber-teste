from behave import given, when, then

@given('insiro o numero um "{num1}"')
def step_insiro_o_numero_um(context, num1):
    context.num1 = int(num1)

@given('insiro o numero dois "{num2}"')
def step_insiro_o_numero_dois(context, num2):
    context.num2 = int(num2)

@when('clico no botão soma')
def step_clico_no_botao_soma(context):
    context.resultado = context.num1 + context.num2

@then('O resultado deve ser "{resultado}"')
def step_o_resultado_deve_ser(context, resultado):
    assert context.resultado == int(resultado)