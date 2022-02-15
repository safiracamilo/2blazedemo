import time

from behave import given, when, then

@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site Blazemo')
    time.sleep(2)


@when(u'clico em home')
def step_impl(context):

    print('Passo 2 - Clicou no home')

@when(u'clico em Register')
def step_impl(context):
    print('Passo 3 - clicou no Register')



@then(u'vejo o formulario de cadastro')
def step_impl(context):
    print('Passo 4 - Vejo formulario de cadastro')



@when(u'preencho "<nome>" "<empresa>" "<email>" "<senha>"')
def step_impl(context):
    print('Passo 5 - Preencho nome empresa email senha')



@when(u'clico no botao Register')
def step_impl(context):
    print('Passo 6 - Clico no botao register')



@then(u'exibe a confirmacao do cadastro')
def step_impl(context):
    print('Passo 7 - Exibe confirmacao de cadastro')

